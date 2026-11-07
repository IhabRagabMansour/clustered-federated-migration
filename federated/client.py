"""
Federated client (GPU-resident tensor data path).

Each client holds a LongTensor of indices into the shared, device-resident
(X, y) training tensors. Batches are pure GPU slices.
"""

import copy
from typing import Dict

import torch
import torch.nn as nn
import torch.optim as optim

from data.fast_data import iterate_batches


class Client:
    def __init__(self, client_id: int, X, y, idx, cluster_id: int,
                 batch_size: int, lr: float, optimizer_name: str, device: str,
                 momentum: float = 0.9, weight_decay: float = 1e-4):
        self.client_id = client_id
        self.X = X                          # shared device tensor (all train samples)
        self.y = y
        self.idx = idx                      # LongTensor on device (this client's rows)
        self.cluster_id = cluster_id        # mutable: changes on migration
        self.home_cluster_id = cluster_id
        self.batch_size = batch_size
        self.lr = lr
        self.optimizer_name = optimizer_name
        self.device = device
        self.momentum = momentum
        self.weight_decay = weight_decay

        self.model = None
        self.optimizer = None

    @property
    def num_samples(self) -> int:
        return int(self.idx.numel())

    def set_indices(self, idx):
        """Replace this client's training rows (used by data_changes migration)."""
        self.idx = idx

    def set_model(self, model: nn.Module):
        self.model = copy.deepcopy(model).to(self.device)
        self._init_optimizer()

    def _init_optimizer(self):
        if self.optimizer_name.upper() == "SGD":
            self.optimizer = optim.SGD(self.model.parameters(), lr=self.lr,
                                       momentum=self.momentum, weight_decay=self.weight_decay)
        else:
            self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr,
                                        weight_decay=self.weight_decay)

    def get_weights(self) -> Dict[str, torch.Tensor]:
        return copy.deepcopy(self.model.state_dict())

    def load_weights(self, state_dict: Dict[str, torch.Tensor]):
        self.model.load_state_dict(state_dict)
        self._init_optimizer()

    def train_local(self, epochs: int) -> Dict[str, float]:
        self.model.train()
        criterion = nn.CrossEntropyLoss()
        # Accumulate on-device; sync to host once at the end (avoids per-batch stalls)
        loss_sum = torch.zeros((), device=self.device)
        correct = torch.zeros((), device=self.device)
        total = 0
        for _ in range(epochs):
            for xb, yb in iterate_batches(self.X, self.y, self.idx, self.batch_size,
                                          shuffle=True, drop_last=False):
                self.optimizer.zero_grad(set_to_none=True)
                out = self.model(xb)
                loss = criterion(out, yb)
                loss.backward()
                self.optimizer.step()
                loss_sum += loss.detach() * xb.size(0)
                correct += (out.detach().argmax(1) == yb).sum()
                total += xb.size(0)
        if total == 0:
            return {"loss": 0.0, "accuracy": 0.0}
        return {"loss": loss_sum.item() / total, "accuracy": 100.0 * correct.item() / total}


@torch.no_grad()
def evaluate_fast(model: nn.Module, X, y, idx, batch_size: int) -> tuple:
    model.eval()
    criterion = nn.CrossEntropyLoss()
    device = X.device
    loss_sum = torch.zeros((), device=device)
    correct = torch.zeros((), device=device)
    total = 0
    for xb, yb in iterate_batches(X, y, idx, batch_size, shuffle=False):
        out = model(xb)
        loss_sum += criterion(out, yb) * xb.size(0)
        correct += (out.argmax(1) == yb).sum()
        total += xb.size(0)
    if total == 0:
        return 0.0, 0.0
    return loss_sum.item() / total, 100.0 * correct.item() / total


@torch.no_grad()
def per_class_accuracy(model: nn.Module, X, y, idx, batch_size: int, num_classes: int):
    """Accuracy (%) of `model` per class on the rows `idx`; LongTensor-safe, on device."""
    model.eval()
    correct = torch.zeros(num_classes, device=X.device)
    count = torch.zeros(num_classes, device=X.device)
    for xb, yb in iterate_batches(X, y, idx, batch_size, shuffle=False):
        hit = (model(xb).argmax(1) == yb).float()
        correct.index_add_(0, yb, hit)
        count.index_add_(0, yb, torch.ones_like(hit))
    return 100.0 * correct / count.clamp(min=1)
