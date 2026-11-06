"""
Variance / disruption metrics for per-cluster accuracy trajectories.

  - rolling_std: windowed std of a per-cluster accuracy series
  - before_after_stats: compares a window before vs after a migration round
    (mean, std, max drop, recovery time)
"""

from typing import Dict, List

import numpy as np


def rolling_std(values: List[float], window: int) -> List[float]:
    out = []
    for i in range(len(values)):
        lo = max(0, i - window + 1)
        out.append(float(np.std(values[lo:i + 1])))
    return out


def before_after_stats(rounds: List[int], values: List[float],
                       migration_round: int, window: int,
                       recovery_eps: float = 1.0) -> Dict[str, float]:
    """
    Quantify the disruption around `migration_round`.
    Before window: [R-window, R-1]; after window: [R, R+window-1].
    Recovery time: if the after-window minimum falls below `recovery_eps`
    of the pre-migration mean, the first round at/after that minimum where
    accuracy returns within the threshold. Returns 0 if no threshold-crossing
    disruption is observed, and -1 if recovery never happens.
    """
    r = np.asarray(rounds)
    v = np.asarray(values, dtype=float)

    before_mask = (r >= migration_round - window) & (r < migration_round)
    after_mask = (r >= migration_round) & (r < migration_round + window)
    before = v[before_mask]
    after = v[after_mask]

    before_mean = float(before.mean()) if before.size else float("nan")
    after_vals = v[r >= migration_round]
    after_rounds = r[r >= migration_round]

    max_drop = float(before_mean - after.min()) if (after.size and before.size) else float("nan")

    recovery_time = -1
    if before.size and after.size:
        threshold = before_mean - recovery_eps
        min_idx = int(after.argmin())
        min_val = float(after[min_idx])
        if min_val >= threshold:
            recovery_time = 0
        else:
            min_round = int(r[after_mask][min_idx])
            for rr, vv in zip(after_rounds, after_vals):
                if rr >= min_round and vv >= threshold:
                    recovery_time = int(rr) - migration_round
                    break

    # Censoring / relapse diagnostics. `recovery_time` keeps the legacy encoding
    # (-1 = never recovered); averages must exclude -1 and report the
    # never-recovered fraction separately (see `recovered`).
    recovered = recovery_time >= 0
    relapsed = False
    rounds_below_after_recovery = 0
    if recovered and recovery_time > 0 and before.size:
        threshold = before_mean - recovery_eps
        rec_round = migration_round + recovery_time
        later = after_vals[after_rounds > rec_round]
        rounds_below_after_recovery = int((later < threshold).sum())
        relapsed = rounds_below_after_recovery > 0
    rounds_below_total = 0
    if before.size:
        rounds_below_total = int((after_vals < before_mean - recovery_eps).sum())
    final_mean = float(v[-window:].mean()) if v.size >= window else float("nan")

    return {
        "migration_round": migration_round,
        "recovered": bool(recovered),
        "relapsed": bool(relapsed),
        "rounds_below_after_recovery": rounds_below_after_recovery,
        "rounds_below_threshold": rounds_below_total,
        "final_mean": final_mean,
        "final_minus_before": (final_mean - before_mean) if before.size else float("nan"),
        "before_mean": before_mean,
        "after_mean": float(after.mean()) if after.size else float("nan"),
        "before_std": float(before.std()) if before.size else float("nan"),
        "after_std": float(after.std()) if after.size else float("nan"),
        "max_drop": max_drop,
        "recovery_time": recovery_time,
    }


def between_cluster_variance(per_cluster_values: Dict[int, List[float]]) -> List[float]:
    """Per-round variance across clusters (homogenisation measure)."""
    series = list(per_cluster_values.values())
    if not series:
        return []
    length = min(len(s) for s in series)
    return [float(np.var([s[i] for s in series])) for i in range(length)]
