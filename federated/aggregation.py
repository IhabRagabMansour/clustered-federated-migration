"""
Aggregation:
  - fedavg: intra-cluster weighted averaging (by #samples)
  - inter_cluster_mix: Case B sharing  model_i <- beta*own + (1-beta)*mean(others)
"""

from collections import OrderedDict
from typing import Dict, List

import torch


def _is_float(t: torch.Tensor) -> bool:
    return t.dtype.is_floating_point


def fedavg(state_dicts: List[Dict[str, torch.Tensor]],
           num_samples: List[int]) -> "OrderedDict[str, torch.Tensor]":
    """Weighted average of state dicts. Non-float buffers copied from the first."""
    if not state_dicts:
        raise ValueError("fedavg: no state dicts provided")
    total = float(sum(num_samples)) or 1.0
    first = state_dicts[0]
    agg = OrderedDict()
    for k, v in first.items():
        agg[k] = torch.zeros_like(v) if _is_float(v) else v.clone()
    for sd, n in zip(state_dicts, num_samples):
        w = n / total
        for k in agg:
            if _is_float(agg[k]):
                agg[k] += w * sd[k]
    return agg


def inter_cluster_mix(cluster_models: Dict[int, Dict[str, torch.Tensor]],
                      beta: float) -> Dict[int, "OrderedDict[str, torch.Tensor]"]:
    """
    For each cluster i:  mixed_i = beta * own_i + (1 - beta) * mean_{j != i} own_j
    Only float tensors are mixed; integer buffers are kept from the own model.
    """
    ids = list(cluster_models.keys())
    mixed: Dict[int, OrderedDict] = {}
    for i in ids:
        own = cluster_models[i]
        others = [cluster_models[j] for j in ids if j != i]
        out = OrderedDict()
        for k, v in own.items():
            if _is_float(v):
                if others:
                    others_mean = torch.stack([o[k].float() for o in others], 0).mean(0)
                    out[k] = beta * v.float() + (1.0 - beta) * others_mean
                else:
                    out[k] = v.clone()
            else:
                out[k] = v.clone()
        mixed[i] = out
    return mixed
