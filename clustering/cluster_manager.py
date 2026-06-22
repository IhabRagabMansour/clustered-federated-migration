"""
ClusterManager: owns clients, per-cluster models, and device-resident test
tensors with per-cluster + global index sets. Provides membership queries and
evaluation helpers (GPU-resident).
"""

import copy
from collections import OrderedDict
from typing import Dict, List

from federated.client import Client, evaluate_fast


class ClusterManager:
    def __init__(self, clients: List[Client], num_clusters: int,
                 X_test, y_test, cluster_test_idx: Dict[int, "Tensor"], global_test_idx,
                 init_model, device: str, eval_batch_size: int = 1024):
        self.clients = clients
        self.clients_by_id: Dict[int, Client] = {c.client_id: c for c in clients}
        self.num_clusters = num_clusters
        self.X_test = X_test
        self.y_test = y_test
        self.cluster_test_idx = cluster_test_idx     # cluster_id -> LongTensor
        self.global_test_idx = global_test_idx       # LongTensor (all test rows)
        self.device = device
        self.eval_batch_size = eval_batch_size

        init_state = copy.deepcopy(init_model.state_dict())
        self.cluster_models: Dict[int, OrderedDict] = {
            c: copy.deepcopy(init_state) for c in range(num_clusters)
        }
        self._eval_model = copy.deepcopy(init_model).to(device)

    def members(self, cluster_id: int) -> List[Client]:
        return [c for c in self.clients if c.cluster_id == cluster_id]

    def cluster_sizes(self) -> Dict[int, int]:
        sizes = {c: 0 for c in range(self.num_clusters)}
        for c in self.clients:
            sizes[c.cluster_id] += 1
        return sizes

    def evaluate_both(self, cluster_id: int, do_cluster: bool, do_global: bool):
        """Load the cluster model once; return (cluster_acc | None, global_acc | None)."""
        self._eval_model.load_state_dict(self.cluster_models[cluster_id])
        cluster_acc = global_acc = None
        if do_cluster:
            _, cluster_acc = evaluate_fast(self._eval_model, self.X_test, self.y_test,
                                           self.cluster_test_idx[cluster_id], self.eval_batch_size)
        if do_global:
            _, global_acc = evaluate_fast(self._eval_model, self.X_test, self.y_test,
                                          self.global_test_idx, self.eval_batch_size)
        return cluster_acc, global_acc
