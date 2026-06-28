"""
Create publication-ready result plots from grid_results/all_results.csv.

The plots focus on the destination cluster because it receives the migrated
clients. They use CNN results for MNIST, Fashion-MNIST, and CIFAR-10.

Outputs:
    figures/results/main_data_changing_drop.{pdf,svg,png,pgf}
    figures/results/membership_only_drop.{pdf,svg,png,pgf}
    figures/results/client_count_trend_data_changing.{pdf,svg,png,pgf}
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt
import numpy as np


DATASETS = ["MNIST", "F-MNIST", "CIFAR-10"]
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


def load_rows(path: Path, model: str) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["model"] != model:
                continue
            row = dict(row)
            row["num_clusters"] = int(row["num_clusters"])
            row["clients_per_cluster"] = int(row["clients_per_cluster"])
            row["seed"] = int(row["seed"])
            row["cluster"] = int(row["cluster"])
            row["value"] = float(row["value"])
            row["role"] = (
                "source"
                if row["cluster"] == 0
                else "destination"
                if row["cluster"] == row["num_clusters"] - 1
                else "other"
            )
            rows.append(row)
    return rows


def values(rows: list[dict], **filters) -> list[float]:
    out = []
    for row in rows:
        if all(row.get(k) == v for k, v in filters.items()):
            out.append(row["value"])
    return out


def mean_std(vals: list[float]) -> tuple[float, float]:
    if not vals:
        return float("nan"), float("nan")
    if len(vals) == 1:
        return vals[0], 0.0
    return mean(vals), stdev(vals)


def apply_style():
    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
            "figure.titlesize": 12,
            "axes.edgecolor": "#9aa5b5",
            "axes.linewidth": 0.9,
            "grid.color": "#d9dee7",
            "grid.linewidth": 0.8,
            "pgf.texsystem": "pdflatex",
            "pgf.rcfonts": False,
            "pgf.preamble": r"\usepackage{amsmath}",
        }
    )


def save_all(fig, out_dir: Path, stem: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ["pdf", "svg", "png", "pgf"]:
        fig.savefig(out_dir / f"{stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def bar_plot(ax, labels, means_a, stds_a, means_b, stds_b, ylabel=None, title=None):
    x = np.arange(len(labels))
    width = 0.34
    ax.bar(
        x - width / 2,
        means_a,
        width,
        yerr=stds_a,
        label=CASE_LABELS["caseA"],
        color=CASE_COLORS["caseA"],
        edgecolor="#4e5b6a",
        linewidth=0.9,
        capsize=3,
    )
    ax.bar(
        x + width / 2,
        means_b,
        width,
        yerr=stds_b,
        label=CASE_LABELS["caseB"],
        color=CASE_COLORS["caseB"],
        edgecolor="#8c5a14",
        linewidth=0.9,
        capsize=3,
    )
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title, pad=8)
    ax.grid(axis="y", alpha=0.9)
    ax.set_axisbelow(True)


def plot_main_data_changing(rows: list[dict], out_dir: Path):
    labels = [DATASET_LABELS[d] for d in DATASETS]
    means = defaultdict(list)
    stds = defaultdict(list)
    for dataset in DATASETS:
        for case in ["caseA", "caseB"]:
            vals = values(
                rows,
                dataset=dataset,
                role="destination",
                num_clusters=2,
                submode="data_changes",
                case=case,
                metric="clusterTest_maxDrop",
            )
            m, s = mean_std(vals)
            means[case].append(m)
            stds[case].append(s)

    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    bar_plot(
        ax,
        labels,
        means["caseA"],
        stds["caseA"],
        means["caseB"],
        stds["caseB"],
        ylabel="Maximum accuracy drop (percentage points)",
        title="Data-changing migration, K=2",
    )
    ax.legend(frameon=False, loc="upper left")
    ax.set_ylim(0, max(means["caseA"] + means["caseB"]) * 1.45)
    save_all(fig, out_dir, "main_data_changing_drop")


def plot_membership_only(rows: list[dict], out_dir: Path):
    labels = [DATASET_LABELS[d] for d in DATASETS]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), sharey=True)

    for ax, k in zip(axes, [2, 10]):
        means = defaultdict(list)
        stds = defaultdict(list)
        for dataset in DATASETS:
            for case in ["caseA", "caseB"]:
                vals = values(
                    rows,
                    dataset=dataset,
                    role="destination",
                    num_clusters=k,
                    submode="membership_only",
                    case=case,
                    metric="clusterTest_maxDrop",
                )
                m, s = mean_std(vals)
                means[case].append(m)
                stds[case].append(s)
        bar_plot(
            ax,
            labels,
            means["caseA"],
            stds["caseA"],
            means["caseB"],
            stds["caseB"],
            ylabel="Maximum accuracy drop (percentage points)" if k == 2 else None,
            title=f"Membership-only migration, K={k}",
        )
        ax.set_ylim(0, 110)

    axes[0].legend(frameon=False, loc="upper left")
    fig.tight_layout(w_pad=2.0)
    save_all(fig, out_dir, "membership_only_drop")


def plot_client_count_trend(rows: list[dict], out_dir: Path):
    fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0), sharex=True)

    for ax, dataset in zip(axes, DATASETS):
        for case in ["caseA", "caseB"]:
            xs, ys, errs = [], [], []
            for clients_per_cluster in range(3, 11):
                vals = values(
                    rows,
                    dataset=dataset,
                    role="destination",
                    num_clusters=2,
                    clients_per_cluster=clients_per_cluster,
                    submode="data_changes",
                    case=case,
                    metric="clusterTest_maxDrop",
                )
                if not vals:
                    continue
                m, s = mean_std(vals)
                xs.append(clients_per_cluster)
                ys.append(m)
                errs.append(s)
            ax.errorbar(
                xs,
                ys,
                yerr=errs,
                marker="o",
                linewidth=1.8,
                markersize=4.5,
                capsize=3,
                label=CASE_LABELS[case],
                color=CASE_COLORS[case],
            )

        ax.set_title(DATASET_LABELS[dataset], pad=8)
        ax.set_xlabel("Clients per cluster")
        ax.grid(axis="y", alpha=0.9)
        ax.set_axisbelow(True)
        ax.set_xticks(range(3, 11))

    axes[0].set_ylabel("Maximum accuracy drop (percentage points)")
    axes[0].legend(frameon=False, loc="upper right")
    fig.suptitle("Data-changing migration, K=2", y=1.03)
    fig.tight_layout(w_pad=2.0)
    save_all(fig, out_dir, "client_count_trend_data_changing")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="grid_results", help="Grid result folder")
    parser.add_argument("--model", default="CNN", help="Model to plot")
    parser.add_argument("--out", default="figures/results", help="Output folder")
    args = parser.parse_args()

    root = Path(args.root)
    rows_path = root / "all_results.csv"
    if not rows_path.exists():
        raise FileNotFoundError(
            f"Missing {rows_path}. Run aggregate_grid_results.py first."
        )

    apply_style()
    rows = load_rows(rows_path, args.model)
    out_dir = Path(args.out)

    plot_main_data_changing(rows, out_dir)
    plot_membership_only(rows, out_dir)
    plot_client_count_trend(rows, out_dir)
    print(f"Wrote plots to: {out_dir}")


if __name__ == "__main__":
    main()
