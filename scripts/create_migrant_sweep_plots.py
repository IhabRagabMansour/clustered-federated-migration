"""
Plot destination-cluster accuracy drop versus number of migrated clients.

The script reads completed outputs from run_migrant_sweep.py and writes a
publication-ready plot in vector formats, including PGF.

Default output:
    figures/results/migrant_sweep_data_changes_k2_cnn.{pdf,svg,png,pgf}
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from run_grid import normalize_dataset, normalize_model


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


def load_rows(root: Path) -> list[dict]:
    rows = []
    for path in root.glob("**/case_values.csv"):
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if not row:
                    continue
                if row.get("metric") != "clusterTest_maxDrop":
                    continue
                row = dict(row)
                row["num_clusters"] = int(row["num_clusters"])
                row["clients_per_cluster"] = int(row["clients_per_cluster"])
                row["num_migrants"] = int(row["num_migrants"])
                row["seed"] = int(row["seed"])
                row["cluster"] = int(row["cluster"])
                row["value"] = float(row["value"])
                row["role"] = (
                    "destination"
                    if row["cluster"] == row["num_clusters"] - 1
                    else "source"
                    if row["cluster"] == 0
                    else "other"
                )
                rows.append(row)
    return rows


def filtered_values(rows: list[dict], **filters) -> list[float]:
    vals = []
    for row in rows:
        if all(row.get(k) == v for k, v in filters.items()):
            vals.append(row["value"])
    return vals


def mean_std(vals: list[float]) -> tuple[float, float]:
    if not vals:
        return float("nan"), float("nan")
    if len(vals) == 1:
        return vals[0], 0.0
    return mean(vals), stdev(vals)


def save_all(fig, out_dir: Path, stem: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ["pdf", "svg", "png", "pgf"]:
        fig.savefig(out_dir / f"{stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_sweep(
    rows: list[dict],
    datasets: list[str],
    model: str,
    clusters: int,
    clients_per_cluster: int,
    submode: str,
    out_dir: Path,
    stem: str,
) -> None:
    if not rows:
        raise RuntimeError("No migrant sweep rows found. Run run_migrant_sweep.py first.")

    fig_width = 3.6 * len(datasets)
    fig, axes = plt.subplots(
        1,
        len(datasets),
        figsize=(fig_width, 3.2),
        sharey=True,
        squeeze=False,
    )
    axes = axes[0]

    for ax, dataset in zip(axes, datasets):
        for case in ["caseA", "caseB"]:
            xs, ys, errs = [], [], []
            for num_migrants in range(1, clients_per_cluster + 1):
                vals = filtered_values(
                    rows,
                    dataset=dataset,
                    model=model,
                    num_clusters=clusters,
                    clients_per_cluster=clients_per_cluster,
                    num_migrants=num_migrants,
                    role="destination",
                    submode=submode,
                    case=case,
                )
                if not vals:
                    continue
                m, s = mean_std(vals)
                xs.append(num_migrants)
                ys.append(m)
                errs.append(s)

            if xs:
                ax.errorbar(
                    xs,
                    ys,
                    yerr=errs,
                    marker="o",
                    linewidth=1.7,
                    markersize=4,
                    capsize=3,
                    label=CASE_LABELS[case],
                    color=CASE_COLORS[case],
                )

        ax.set_title(DATASET_LABELS.get(dataset, dataset), pad=6)
        ax.set_xlabel("Migrated clients")
        ax.set_xticks(range(1, clients_per_cluster + 1))
        ax.grid(axis="y", alpha=0.9)
        ax.set_axisbelow(True)

    axes[0].set_ylabel("Maximum accuracy drop (percentage points)")
    axes[0].legend(frameon=False, loc="upper left")
    fig.suptitle(
        f"{model}, K={clusters}, {clients_per_cluster} clients/cluster, {submode.replace('_', '-')}",
        y=1.04,
    )
    fig.tight_layout(w_pad=1.6)
    save_all(fig, out_dir, stem)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="migrant_sweep_results")
    parser.add_argument("--out", default="figures/results")
    parser.add_argument("--datasets", nargs="+", type=normalize_dataset, default=["CIFAR-10"])
    parser.add_argument("--model", type=normalize_model, default="CNN")
    parser.add_argument("--clusters", type=int, default=2)
    parser.add_argument("--clients-per-cluster", type=int, default=10)
    parser.add_argument("--submode", choices=["membership_only", "data_changes"], default="data_changes")
    parser.add_argument("--stem", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    stem = args.stem
    if stem is None:
        stem = (
            f"migrant_sweep_{args.submode}_k{args.clusters}_"
            f"{args.model.lower()}_{len(args.datasets)}datasets"
        )

    apply_style()
    rows = load_rows(Path(args.root))
    plot_sweep(
        rows,
        args.datasets,
        args.model,
        args.clusters,
        args.clients_per_cluster,
        args.submode,
        Path(args.out),
        stem,
    )
    print(f"Wrote migrant sweep plot to: {args.out}")


if __name__ == "__main__":
    main()
