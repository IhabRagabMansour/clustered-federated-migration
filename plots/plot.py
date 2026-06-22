"""
Plots: per-cluster accuracy vs round with migration markers, rolling std,
and between-cluster variance.
"""

import os
from typing import Dict, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _migration_lines(ax, migration_rounds):
    for i, mr in enumerate(migration_rounds):
        ax.axvline(x=mr, color="red", linestyle="--", alpha=0.6,
                   label="migration" if i == 0 else None)


def plot_cluster_accuracy(rounds, cluster_test_acc: Dict[int, List[float]],
                          migration_rounds, title, save_path, fname):
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    for c, series in cluster_test_acc.items():
        ax.plot(rounds, series, linewidth=2, label=f"Cluster {c}")
    _migration_lines(ax, migration_rounds)
    ax.set_xlabel("Communication Round")
    ax.set_ylabel("Cluster Test Accuracy (%)")
    ax.set_title(title)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)
    _save(save_path, fname)


def plot_rolling_std(rounds, rolling_std: Dict[int, List[float]],
                     migration_rounds, title, save_path, fname):
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    for c, series in rolling_std.items():
        ax.plot(rounds, series, linewidth=2, label=f"Cluster {c}")
    _migration_lines(ax, migration_rounds)
    ax.set_xlabel("Communication Round")
    ax.set_ylabel("Rolling Std of Cluster Accuracy")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)
    _save(save_path, fname)


def plot_between_cluster_variance(rounds, variance: List[float],
                                  migration_rounds, title, save_path, fname):
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    n = min(len(rounds), len(variance))
    ax.plot(rounds[:n], variance[:n], linewidth=2, color="purple")
    _migration_lines(ax, migration_rounds)
    ax.set_xlabel("Communication Round")
    ax.set_ylabel("Between-Cluster Accuracy Variance")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    _save(save_path, fname)


def plot_case_comparison(rounds, series_a: List[float], series_b: List[float],
                         migration_rounds, cluster_id, title, save_path, fname):
    """Overlay one cluster's accuracy for Case A vs Case B."""
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    ax.plot(rounds, series_a, linewidth=2.2, color="#d62728",
            label=f"Case A (isolated) - cluster {cluster_id}")
    ax.plot(rounds, series_b, linewidth=2.2, color="#1f77b4",
            label=f"Case B (sharing) - cluster {cluster_id}")
    _migration_lines(ax, migration_rounds)
    ax.set_xlabel("Communication Round")
    ax.set_ylabel("Cluster Test Accuracy (%)")
    ax.set_title(title)
    ax.legend(loc="lower right", fontsize=10)
    ax.grid(True, alpha=0.3)
    _save(save_path, fname)


def plot_between_variance_comparison(rounds, var_a: List[float], var_b: List[float],
                                     migration_rounds, title, save_path, fname):
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    n = min(len(rounds), len(var_a), len(var_b))
    ax.plot(rounds[:n], var_a[:n], linewidth=2.2, color="#d62728", label="Case A (isolated)")
    ax.plot(rounds[:n], var_b[:n], linewidth=2.2, color="#1f77b4", label="Case B (sharing)")
    _migration_lines(ax, migration_rounds)
    ax.set_xlabel("Communication Round")
    ax.set_ylabel("Between-Cluster Accuracy Variance")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.3)
    _save(save_path, fname)


def _save(save_path, fname):
    os.makedirs(save_path, exist_ok=True)
    path = os.path.join(save_path, fname)
    plt.tight_layout()
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Plot saved: {path}")
