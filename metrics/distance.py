"""
Weight-shift metrics: total and per-layer L2 distance between two state dicts.
Ported/adapted from partial-layer-aggregation/distance_metrics.
"""

from typing import Dict

import torch


def l2_distance(sd_a: Dict[str, torch.Tensor], sd_b: Dict[str, torch.Tensor]) -> float:
    total = 0.0
    for k, v in sd_a.items():
        if v.dtype.is_floating_point and k in sd_b:
            total += (v - sd_b[k]).norm(p=2).item()
    return total


def per_layer_distance(sd_a: Dict[str, torch.Tensor],
                       sd_b: Dict[str, torch.Tensor]) -> Dict[str, float]:
    return {k: (v - sd_b[k]).norm(p=2).item()
            for k, v in sd_a.items()
            if v.dtype.is_floating_point and k in sd_b}
