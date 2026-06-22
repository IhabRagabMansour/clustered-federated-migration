"""
GPU-resident in-memory data path.

The whole dataset is transformed once and held as tensors on the device, so
each training/eval batch is a pure GPU slice (no per-round CPU transforms or
DataLoader overhead). This keeps the tiny CNNs GPU-bound.

Note: for CIFAR-10 this freezes the train-time augmentation (it is applied once
during materialisation). Fine for these experiments; revisit if augmentation
randomness matters.
"""

import torch
from torch.utils.data import DataLoader


def materialize(dataset, device: str, batch: int = 4096):
    """Transform the entire dataset once into (X, y) tensors on `device`."""
    loader = DataLoader(dataset, batch_size=batch, shuffle=False, num_workers=0)
    xs, ys = [], []
    for x, y in loader:
        xs.append(x)
        ys.append(y)
    X = torch.cat(xs).to(device)
    y = torch.cat(ys).to(device)
    return X, y


def iterate_batches(X, y, idx, batch_size: int, shuffle: bool, drop_last: bool = False):
    """Yield (xb, yb) GPU slices for the rows in `idx` (a LongTensor on device)."""
    n = int(idx.numel())
    if shuffle:
        order = torch.randperm(n, device=idx.device)
    else:
        order = torch.arange(n, device=idx.device)
    sel = idx[order]
    end = n - (n % batch_size) if (drop_last and n >= batch_size) else n
    for i in range(0, end, batch_size):
        b = sel[i:i + batch_size]
        yield X[b], y[b]
