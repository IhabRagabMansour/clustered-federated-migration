"""
ClusterManager: owns clients, per-cluster models, and device-resident test
tensors with per-cluster + global index sets. Provides membership queries and
evaluation helpers (GPU-resident).
"""

import copy
from collections import OrderedDict
from typing import Dict, List

import torch

from federated.client import Client, evaluate_fast, per_class_accuracy


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
        self.num_classes = int(y_test.max().item()) + 1

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

    def client_losses_per_cluster(self) -> Dict[int, List[float]]:
        """Loss of every cluster model on every client's CURRENT local data
        (what a client can compute privately to pick its cluster)."""
        out = {c.client_id: [0.0] * self.num_clusters for c in self.clients}
        for k in range(self.num_clusters):
            self._eval_model.load_state_dict(self.cluster_models[k])
            for c in self.clients:
                loss, _ = evaluate_fast(self._eval_model, c.X, c.y, c.idx, self.eval_batch_size)
                out[c.client_id][k] = loss
        return out

    def client_accuracies(self) -> Dict[int, float]:
        """Accuracy each client gets from its current cluster model, on held-out
        test data matching the client's CURRENT class mix: sum_c w_c * acc_c,
        with w_c the class proportions of the client's local data."""
        per_cluster = {}
        for k in range(self.num_clusters):
            self._eval_model.load_state_dict(self.cluster_models[k])
            per_cluster[k] = per_class_accuracy(self._eval_model, self.X_test, self.y_test,
                                                self.global_test_idx, self.eval_batch_size,
                                                self.num_classes)
        out = {}
        for c in self.clients:
            w = torch.bincount(c.y[c.idx], minlength=self.num_classes).float()
            w = w / w.sum().clamp(min=1)
            out[c.client_id] = float((w * per_cluster[c.cluster_id]).sum().item())
        return out
