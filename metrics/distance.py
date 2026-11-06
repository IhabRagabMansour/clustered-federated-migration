"""
Weight-shift metrics: total and per-layer L2 distance between two state dicts.
Ported/adapted from partial-layer-aggregation/distance_metrics.
"""

import math
from typing import Dict

import torch


def l2_distance(sd_a: Dict[str, torch.Tensor], sd_b: Dict[str, torch.Tensor]) -> float:
    """True L2 norm of the difference over all float tensors (params + BN stats).

    Earlier versions summed per-layer norms, which is an upper bound on the true
    distance rather than the distance itself.
    """
    total_sq = 0.0
    for k, v in sd_a.items():
        if v.dtype.is_floating_point and k in sd_b:
            total_sq += float((v.float() - sd_b[k].float()).pow(2).sum().item())
    return math.sqrt(total_sq)


def per_layer_distance(sd_a: Dict[str, torch.Tensor],
                       sd_b: Dict[str, torch.Tensor]) -> Dict[str, float]:
    return {k: (v.float() - sd_b[k].float()).norm(p=2).item()
            for k, v in sd_a.items()
            if v.dtype.is_floating_point and k in sd_b}
