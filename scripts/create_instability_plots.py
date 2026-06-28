"""
Create per-round instability plots from experiment metrics.

The figure shows destination-cluster accuracy over communication rounds and
the corresponding standard deviation across completed runs. It is intended to
visualize post-migration instability more directly than the summary tables.

Default output:
    figures/results/instability_data_changing_k2_cnn.{pdf,svg,png,pgf}
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt
import numpy as np


DATASET_DIRS = {
    "MNIST": "MNIST",
    "F-MNIST": "FMNIST",
    "CIFAR-10": "CIFAR10",
}
DATASET_LABELS = {
    "MNIST": "MNIST",
    "F-MNIST": "Fashion-MNIST",
    "CIFAR-10": "CIFAR-10",
}
CASE_LABELS = {
    "caseA": "Isolated",
    "caseB": "Knowledge sharing",
}
CASE_COLORS = {
    "caseA": "#6f7f92",
    "caseB": "#bd7d24",
}


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.titlesize": 10,
            "axes.edgecolor": "#9aa5b5",
            "axes.linewidth": 0.8,
            "grid.color": "#d9dee7",
            "grid.linewidth": 0.7,
            "pgf.texsystem": "pdflatex",
            "pgf.rcfonts": False,
            "pgf.preamble": r"\usepackage{amsmath}",
        }
    )


def config_dirs(root: Path, dataset: str, model: str, clusters: int) -> list[Path]:
    dataset_slug = DATASET_DIRS[dataset]
    pattern = (
        f"dataset_{dataset_slug}_model_{model}_clusters_{clusters}"
        "_clientsPerCluster_*_seed_*"
    )
    return sorted(root.glob(pattern))


def latest_run(config_dir: Path, case: str, submode: str) -> Path | None:
    runs_dir = config_dir / "runs"
    if not runs_dir.exists():
        return None
    runs = sorted(runs_dir.glob(f"{case}_{submode}_*"))
    return runs[-1] if runs else None


def destination_cluster(config_dir: Path, default_clusters: int) -> int:
    grid_config = config_dir / "grid_config.json"
    if not grid_config.exists():
        return default_clusters - 1
    with grid_config.open(encoding="utf-8") as f:
        config = json.load(f)
    return int(config["meta"]["num_clusters"]) - 1


def collect_series(
    root: Path,
    dataset: str,
    model: str,
    clusters: int,
    submode: str,
) -> tuple[dict[str, dict[int, list[float]]], int]:
    series: dict[str, dict[int, list[float]]] = {
        "caseA": defaultdict(list),
        "caseB": defaultdict(list),
    }
    migration_round = 40

    for config_dir in config_dirs(root, dataset, model, clusters):
        dst = destination_cluster(config_dir, clusters)
        grid_config = config_dir / "grid_config.json"
        if grid_config.exists():
            with grid_config.open(encoding="utf-8") as f:
                config = json.load(f)
            migration_round = int(config["meta"].get("migration_round", migration_round))

        for case in ["caseA", "caseB"]:
            run_dir = latest_run(config_dir, case, submode)
            if run_dir is None:
                continue
            metrics_path = run_dir / "metrics.csv"
            if not metrics_path.exists():
                continue
            with metrics_path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if int(row["cluster"]) != dst:
                        continue
                    rnd = int(row["round"])
                    acc = float(row["cluster_test_acc"])
                    series[case][rnd].append(acc)

    return series, migration_round


def mean_std_by_round(series: dict[int, list[float]]) -> tuple[list[int], np.ndarray, np.ndarray]:
    rounds = sorted(series)
    means = []
    stds = []
    for rnd in rounds:
        vals = series[rnd]
        means.append(mean(vals))
        stds.append(stdev(vals) if len(vals) > 1 else 0.0)
    return rounds, np.array(means), np.array(stds)


def save_all(fig, out_dir: Path, stem: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ["pdf", "svg", "png", "pgf"]:
        fig.savefig(out_dir / f"{stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_instability(
    root: Path,
    out_dir: Path,
    model: str,
    clusters: int,
    submode: str,
    stem: str,
) -> None:
    datasets = ["MNIST", "F-MNIST", "CIFAR-10"]
    fig, axes = plt.subplots(
        2,
        3,
        figsize=(10.8, 5.4),
        sharex=True,
        gridspec_kw={"height_ratios": [2.0, 1.0]},
    )

    legend_handles = None
    for col, dataset in enumerate(datasets):
        series, migration_round = collect_series(root, dataset, model, clusters, submode)
        ax_acc = axes[0, col]
        ax_std = axes[1, col]

        for case in ["caseA", "caseB"]:
            rounds, means, stds = mean_std_by_round(series[case])
            if not rounds:
                continue
            ax_acc.plot(
                rounds,
                means,
                color=CASE_COLORS[case],
                linewidth=1.9,
                label=CASE_LABELS[case],
            )
            ax_acc.fill_between(
                rounds,
                means - stds,
                means + stds,
                color=CASE_COLORS[case],
                alpha=0.16,
                linewidth=0,
            )
            ax_std.plot(
                rounds,
                stds,
                color=CASE_COLORS[case],
                linewidth=1.8,
                label=CASE_LABELS[case],
            )

        for ax in [ax_acc, ax_std]:
            ax.axvline(migration_round, color="#333333", linestyle="--", linewidth=1.0)
            ax.grid(axis="y", alpha=0.9)
            ax.set_axisbelow(True)

        ax_acc.set_title(DATASET_LABELS[dataset], pad=6)
        ax_std.set_xlabel("Communication round")
        if col == 0:
            ax_acc.set_ylabel("Destination accuracy (%)")
            ax_std.set_ylabel("Std. across runs")
        if col == 2:
            handles, labels = ax_acc.get_legend_handles_labels()
            legend_handles = (handles, labels)

    if legend_handles:
        fig.legend(
            legend_handles[0],
            legend_handles[1],
            loc="upper center",
            bbox_to_anchor=(0.5, 1.02),
            ncol=2,
            frameon=False,
        )
    fig.suptitle(f"{model}, K={clusters}, data-changing migration", y=1.06)
    fig.tight_layout(w_pad=1.6, h_pad=1.0)
    save_all(fig, out_dir, stem)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="grid_results", help="Grid result folder")
    parser.add_argument("--out", default="figures/results", help="Output folder")
    parser.add_argument("--model", default="CNN", help="Model name")
    parser.add_argument("--clusters", type=int, default=2, help="Number of clusters")
    parser.add_argument("--submode", default="data_changes", help="Migration submode")
    parser.add_argument(
        "--stem",
        default="instability_data_changing_k2_cnn",
        help="Output filename stem",
    )
    args = parser.parse_args()

    apply_style()
    plot_instability(
        Path(args.root),
        Path(args.out),
        args.model,
        args.clusters,
        args.submode,
        args.stem,
    )
    print(f"Wrote instability plot to: {args.out}")


if __name__ == "__main__":
    main()
