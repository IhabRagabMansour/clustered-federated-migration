"""
Create publication-ready plots for the completed CIFAR-10 ResNet grid.

The current ResNet results are complete for K=2 only. These plots therefore
focus on the 2-cluster setting and report the destination cluster, matching
the main CNN result plots.

Outputs:
    figures/results/resnet_cifar10_k2_destination_drop_summary.{pdf,svg,png,pgf}
    figures/results/resnet_cifar10_k2_destination_client_trend.{pdf,svg,png,pgf}
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt
import numpy as np


CASE_LABELS = {
    "caseA": "Isolated",
    "caseB": "Knowledge sharing",
}
CASE_COLORS = {
    "caseA": "#6f7f92",
    "caseB": "#bd7d24",
}
SUBMODE_LABELS = {
    "membership_only": "Membership-only",
    "data_changes": "Data-changing",
}


def load_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["dataset"] != "CIFAR-10" or row["model"] != "ResNet":
                continue
            if int(row["num_clusters"]) != 2:
                continue
            row = dict(row)
            row["num_clusters"] = int(row["num_clusters"])
            row["clients_per_cluster"] = int(row["clients_per_cluster"])
            row["seed"] = int(row["seed"])
            row["cluster"] = int(row["cluster"])
            row["value"] = float(row["value"])
            row["role"] = "source" if row["cluster"] == 0 else "destination"
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


def save_all(fig, out_dir: Path, stem: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ["pdf", "svg", "png", "pgf"]:
        fig.savefig(out_dir / f"{stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_drop_summary(rows: list[dict], out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(4.0, 3.2))
    submodes = ["membership_only", "data_changes"]
    x = np.arange(len(submodes))
    width = 0.34

    for offset, case in [(-width / 2, "caseA"), (width / 2, "caseB")]:
        means, stds = [], []
        for submode in submodes:
            vals = values(
                rows,
                role="destination",
                submode=submode,
                case=case,
                metric="clusterTest_maxDrop",
            )
            m, s = mean_std(vals)
            means.append(m)
            stds.append(s)

        ax.bar(
            x + offset,
            means,
            width,
            yerr=stds,
            label=CASE_LABELS[case],
            color=CASE_COLORS[case],
            edgecolor="#4e5b6a" if case == "caseA" else "#8c5a14",
            linewidth=0.8,
            capsize=3,
        )

    ax.set_title("CIFAR-10 ResNet, K=2", pad=6)
    ax.set_xticks(x)
    ax.set_xticklabels([SUBMODE_LABELS[s] for s in submodes])
    ax.set_ylabel("Maximum accuracy drop (percentage points)")
    ax.grid(axis="y", alpha=0.9)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    ax.set_ylim(0, 90)
    fig.tight_layout()
    save_all(fig, out_dir, "resnet_cifar10_k2_destination_drop_summary")


def plot_client_trend(rows: list[dict], out_dir: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2), sharey=False)

    for ax, submode in zip(axes, ["data_changes", "membership_only"]):
        for case in ["caseA", "caseB"]:
            xs, ys, errs = [], [], []
            for clients_per_cluster in range(3, 11):
                vals = values(
                    rows,
                    role="destination",
                    clients_per_cluster=clients_per_cluster,
                    submode=submode,
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
                linewidth=1.6,
                markersize=4,
                capsize=3,
                label=CASE_LABELS[case],
                color=CASE_COLORS[case],
            )

        ax.set_title(SUBMODE_LABELS[submode], pad=6)
        ax.set_xlabel("Clients per cluster")
        ax.set_xticks(range(3, 11))
        ax.grid(axis="y", alpha=0.9)
        ax.set_axisbelow(True)

    axes[0].set_ylabel("Destination max drop (percentage points)")
    axes[0].legend(frameon=False, loc="upper right")
    fig.tight_layout(w_pad=1.7)
    save_all(fig, out_dir, "resnet_cifar10_k2_destination_client_trend")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="grid_results", help="Grid result folder")
    parser.add_argument("--out", default="figures/results", help="Output folder")
    args = parser.parse_args()

    rows_path = Path(args.root) / "all_results.csv"
    if not rows_path.exists():
        raise FileNotFoundError(
            f"Missing {rows_path}. Run aggregate_grid_results.py first."
        )

    apply_style()
    rows = load_rows(rows_path)
    if not rows:
        raise RuntimeError("No completed CIFAR-10 ResNet K=2 rows found.")

    out_dir = Path(args.out)
    plot_drop_summary(rows, out_dir)
    plot_client_trend(rows, out_dir)
    print(f"Wrote ResNet CIFAR-10 plots to: {out_dir}")


if __name__ == "__main__":
    main()
