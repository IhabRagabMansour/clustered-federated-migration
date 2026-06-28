"""
Plot maximum accuracy drop versus inter-cluster sharing percentage.

The script reads completed outputs from run_sharing_sweep.py. The isolated
setting is shown as a no-sharing baseline, while knowledge sharing is plotted
across the requested sharing percentages.

Default output:
    figures/results/sharing_sweep_data_changes_k2_cnn_cifar10.{pdf,svg,png,pgf}
"""

from __future__ import annotations

import argparse
import csv
import sys
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
CASE_A_COLOR = "#6f7f92"
CASE_B_COLOR = "#bd7d24"


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
                row["sharing_percent"] = float(row["sharing_percent"])
                row["beta"] = float(row["beta"])
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
    num_migrants: int,
    submode: str,
    out_dir: Path,
    stem: str,
) -> None:
    if not rows:
        raise RuntimeError("No sharing sweep rows found. Run run_sharing_sweep.py first.")

    fig_width = 3.8 * len(datasets)
    fig, axes = plt.subplots(
        1,
        len(datasets),
        figsize=(fig_width, 3.2),
        sharey=True,
        squeeze=False,
    )
    axes = axes[0]

    for ax, dataset in zip(axes, datasets):
        case_a_vals = filtered_values(
            rows,
            dataset=dataset,
            model=model,
            num_clusters=clusters,
            clients_per_cluster=clients_per_cluster,
            num_migrants=num_migrants,
            role="destination",
            submode=submode,
            case="caseA",
        )
        baseline_mean, baseline_std = mean_std(case_a_vals)

        percentages = sorted(
            {
                row["sharing_percent"]
                for row in rows
                if row["dataset"] == dataset
                and row["model"] == model
                and row["num_clusters"] == clusters
                and row["clients_per_cluster"] == clients_per_cluster
                and row["num_migrants"] == num_migrants
                and row["role"] == "destination"
                and row["submode"] == submode
                and row["case"] == "caseB"
            }
        )

        xs, ys, errs = [], [], []
        for pct in percentages:
            vals = filtered_values(
                rows,
                dataset=dataset,
                model=model,
                num_clusters=clusters,
                clients_per_cluster=clients_per_cluster,
                num_migrants=num_migrants,
                role="destination",
                submode=submode,
                case="caseB",
                sharing_percent=pct,
            )
            if not vals:
                continue
            m, s = mean_std(vals)
            xs.append(pct)
            ys.append(m)
            errs.append(s)

        if xs:
            ax.errorbar(
                xs,
                ys,
                yerr=errs,
                marker="o",
                linewidth=1.8,
                markersize=4,
                capsize=3,
                label="Knowledge sharing",
                color=CASE_B_COLOR,
            )

        if case_a_vals:
            x_min = 0
            x_max = max(xs) if xs else 50
            ax.hlines(
                baseline_mean,
                x_min,
                x_max,
                colors=CASE_A_COLOR,
                linestyles="--",
                linewidth=1.7,
                label="Isolated",
            )
            ax.fill_between(
                [x_min, x_max],
                [baseline_mean - baseline_std, baseline_mean - baseline_std],
                [baseline_mean + baseline_std, baseline_mean + baseline_std],
                color=CASE_A_COLOR,
                alpha=0.12,
                linewidth=0,
            )

        ax.set_title(DATASET_LABELS.get(dataset, dataset), pad=6)
        ax.set_xlabel("Information sharing (%)")
        ax.set_xlim(left=0)
        if xs:
            ax.set_xticks([0] + xs)
        ax.grid(axis="y", alpha=0.9)
        ax.set_axisbelow(True)

    axes[0].set_ylabel("Maximum accuracy drop (percentage points)")
    axes[0].legend(frameon=False, loc="upper right")
    fig.suptitle(
        f"{model}, K={clusters}, {clients_per_cluster} clients/cluster, "
        f"{num_migrants} migrated clients",
        y=1.04,
    )
    fig.tight_layout(w_pad=1.6)
    save_all(fig, out_dir, stem)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="sharing_sweep_results")
    parser.add_argument("--out", default="figures/results")
    parser.add_argument("--datasets", nargs="+", type=normalize_dataset, default=["CIFAR-10"])
    parser.add_argument("--model", type=normalize_model, default="CNN")
    parser.add_argument("--clusters", type=int, default=2)
    parser.add_argument("--clients-per-cluster", type=int, default=10)
    parser.add_argument("--migrants", type=int, default=5)
    parser.add_argument("--submode", choices=["membership_only", "data_changes"], default="data_changes")
    parser.add_argument("--stem", default="sharing_sweep_data_changes_k2_cnn_cifar10")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    apply_style()
    rows = load_rows(Path(args.root))
    plot_sweep(
        rows,
        args.datasets,
        args.model,
        args.clusters,
        args.clients_per_cluster,
        args.migrants,
        args.submode,
        Path(args.out),
        args.stem,
    )
    print(f"Wrote sharing sweep plot to: {args.out}")


if __name__ == "__main__":
    main()
