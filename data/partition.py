"""
Class-based clustered data partitioning.

Clusters are defined by data distribution: each cluster owns a contiguous group
of classes. Clients within a cluster share that cluster's classes (within-cluster
IID, between-cluster non-IID), so each cluster model specialises on its classes.

Also provides per-cluster test loaders (test data restricted to a cluster's
classes) and a helper to resample a fresh subset for a given set of classes
(used by the `data_changes` migration sub-mode in later phases).
"""

from typing import List, Tuple, Dict

import numpy as np
import torch
from torch.utils.data import Dataset, Subset, DataLoader


def _extract_labels(dataset: Dataset) -> np.ndarray:
    if hasattr(dataset, "targets"):
        t = dataset.targets
        return t.numpy() if isinstance(t, torch.Tensor) else np.array(t)
    return np.array([y for _, y in dataset])


def assign_classes_to_clusters(num_classes: int, num_clusters: int) -> List[List[int]]:
    """Split classes into `num_clusters` contiguous, near-equal groups."""
    return [list(map(int, arr)) for arr in np.array_split(np.arange(num_classes), num_clusters)]


def clients_per_cluster(total_clients: int, num_clusters: int) -> List[int]:
    base, extra = divmod(total_clients, num_clusters)
    return [base + (1 if i < extra else 0) for i in range(num_clusters)]


class ClusteredPartitioner:
    """Builds client datasets, cluster test loaders, and resampling pools."""

    def __init__(self, train_dataset: Dataset, test_dataset: Dataset,
                 num_classes: int, num_clusters: int, total_clients: int, seed: int = 42):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.num_clusters = num_clusters
        self.seed = seed
        self.rng = np.random.default_rng(seed)

        self.cluster_classes = assign_classes_to_clusters(num_classes, num_clusters)
        self.counts = clients_per_cluster(total_clients, num_clusters)

        self._train_labels = _extract_labels(train_dataset)
        self._test_labels = _extract_labels(test_dataset)

        # Shuffled train indices per class (pool for resampling on data_changes)
        self._class_pool: Dict[int, np.ndarray] = {}
        for c in np.unique(self._train_labels):
            idx = np.where(self._train_labels == c)[0]
            self.rng.shuffle(idx)
            self._class_pool[int(c)] = idx

    def build_client_indices(self, reserve_slots: Dict[int, int] = None
                             ) -> Tuple[List[np.ndarray], List[int], List[List[int]]]:
        """Return (client_train_indices, client_cluster_id, client_classes).

        `reserve_slots` maps cluster -> number of extra client-sized shards to
        hold back from that cluster's pool. Held-back shards are never given to
        resident clients; `take_reserved` hands them to clients that migrate
        into the cluster under `data_changes`, so their new data is disjoint
        from every resident's data (no duplicated examples).
        """
        reserve_slots = reserve_slots or {}
        self.reserve: Dict[int, List[np.ndarray]] = {}
        client_indices, client_cluster, client_classes = [], [], []
        for cid, classes in enumerate(self.cluster_classes):
            n_clients = self.counts[cid]
            if n_clients == 0:
                continue
            n_reserve = int(reserve_slots.get(cid, 0))
            n_parts = n_clients + n_reserve
            per_part = [[] for _ in range(n_parts)]
            for cls in classes:
                pool = self._class_pool[cls]
                parts = np.array_split(pool, n_parts)
                for k in range(n_parts):
                    per_part[k].extend(parts[k].tolist())
            for k in range(n_clients):
                idx = np.array(per_part[k], dtype=np.int64)
                self.rng.shuffle(idx)
                client_indices.append(idx)
                client_cluster.append(cid)
                client_classes.append(list(classes))
            if n_reserve:
                shards = []
                for k in range(n_clients, n_parts):
                    idx = np.array(per_part[k], dtype=np.int64)
                    self.rng.shuffle(idx)
                    shards.append(idx)
                self.reserve[cid] = shards
        return client_indices, client_cluster, client_classes

    def take_reserved(self, cluster: int):
        """Pop one held-back shard for `cluster`, or None if none is left."""
        shards = getattr(self, "reserve", {}).get(cluster)
        if shards:
            return shards.pop(0)
        return None

    def cluster_test_index_lists(self) -> List[np.ndarray]:
        """Per-cluster test-set indices (restricted to that cluster's classes)."""
        return [np.where(np.isin(self._test_labels, classes))[0].astype(np.int64)
                for classes in self.cluster_classes]

    def global_test_indices(self) -> np.ndarray:
        return np.arange(len(self._test_labels), dtype=np.int64)

    def resample_indices(self, classes: List[int], approx_size: int) -> np.ndarray:
        """Draw fresh training indices from `classes` (used by data_changes migration)."""
        per_class = max(1, approx_size // len(classes))
        chosen = []
        for cls in classes:
            pool = self._class_pool[cls]
            pick = self.rng.choice(pool, size=min(per_class, len(pool)), replace=False)
            chosen.extend(pick.tolist())
        self.rng.shuffle(chosen)
        return np.array(chosen, dtype=np.int64)
