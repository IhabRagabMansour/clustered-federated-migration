"""
Replot a completed configuration folder without rerunning training.

Examples
--------
    python replot_results.py --config-folder grid_results/dataset_CIFAR10_model_CNN_clusters_2_clientsPerCluster_3_seed_42

    python replot_results.py --config-folder ... --title-prefix "CIFAR-10 CNN" --ylabel "Accuracy (%)"
"""

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def read_csv(path: Path) -> List[dict]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def int_key_dict(raw: Dict) -> Dict[int, List[float]]:
    return {int(k): v for k, v in raw.items()}


def load_runs(config_folder: Path) -> Dict[Tuple[str, str], dict]:
    manifest_path = config_folder / "run_manifest.csv"
    if not manifest_path.exists():
        raise FileNotFoundError(f"No run_manifest.csv in {config_folder}")

    runs = {}
    for row in read_csv(manifest_path):
        if row.get("status") != "ok":
            continue
        run_dir = Path(row["run_dir"])
        metrics = load_json(run_dir / "metrics.json")
        analysis = load_json(run_dir / "analysis.json")
        metrics["cluster_test_acc"] = int_key_dict(metrics["cluster_test_acc"])
        metrics["global_test_acc"] = int_key_dict(metrics["global_test_acc"])
        analysis["between_cluster_variance"] = analysis.get("between_cluster_variance", [])
        runs[(row["submode"], row["case"])] = {
            "metrics": metrics,
            "analysis": analysis,
            "run_dir": str(run_dir),
        }
    return runs


def migration_rounds(metrics: dict) -> List[int]:
    return sorted({int(m["round"]) for m in metrics.get("migrations", [])})


def affected_clusters(metrics: dict) -> List[int]:
    affected = set()
    for migration in metrics.get("migrations", []):
        affected.add(int(migration["src"]))
        affected.add(int(migration["dst"]))
    return sorted(affected)


def draw_migration_lines(ax, rounds: List[int]) -> None:
    for idx, migration_round in enumerate(rounds):
        ax.axvline(
            migration_round,
            color="red",
            linestyle="--",
            alpha=0.6,
            label="migration" if idx == 0 else None,
        )


def plot_case_series(rounds: List[int], series_a: List[float], series_b: List[float],
                     migration_rounds_: List[int], title: str, xlabel: str,
                     ylabel: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    ax.plot(rounds, series_a, linewidth=2.2, color="#d62728", label="Case A (isolated)")
    ax.plot(rounds, series_b, linewidth=2.2, color="#1f77b4", label="Case B (sharing)")
    draw_migration_lines(ax, migration_rounds_)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def plot_variance(rounds: List[int], var_a: List[float], var_b: List[float],
                  migration_rounds_: List[int], title: str, xlabel: str,
                  ylabel: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    n = min(len(rounds), len(var_a), len(var_b))
    plt.figure(figsize=(11, 6))
    ax = plt.gca()
    ax.plot(rounds[:n], var_a[:n], linewidth=2.2, color="#d62728", label="Case A (isolated)")
    ax.plot(rounds[:n], var_b[:n], linewidth=2.2, color="#1f77b4", label="Case B (sharing)")
    draw_migration_lines(ax, migration_rounds_)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def replot(config_folder: Path, args) -> None:
    runs = load_runs(config_folder)
    output_dir = Path(args.output_dir) if args.output_dir else config_folder / "replots"
    for submode in sorted({key[0] for key in runs}):
        pair_a = runs.get((submode, "caseA"))
        pair_b = runs.get((submode, "caseB"))
        if not pair_a or not pair_b:
            continue
        metrics_a = pair_a["metrics"]
        metrics_b = pair_b["metrics"]
        rounds = metrics_a["rounds"]
        mrounds = migration_rounds(metrics_a)
        clusters = args.clusters if args.clusters else affected_clusters(metrics_a)
        title_prefix = args.title_prefix or config_folder.name

        for cluster in clusters:
            plot_case_series(
                rounds,
                metrics_a["cluster_test_acc"][int(cluster)],
                metrics_b["cluster_test_acc"][int(cluster)],
                mrounds,
                f"{title_prefix} | {submode} | Cluster {cluster} Test",
                args.xlabel,
                args.ylabel,
                output_dir / f"replot_{submode}_cluster{cluster}_clusterTest.png",
            )
            plot_case_series(
                rounds,
                metrics_a["global_test_acc"][int(cluster)],
                metrics_b["global_test_acc"][int(cluster)],
                mrounds,
                f"{title_prefix} | {submode} | Cluster {cluster} Global Test",
                args.xlabel,
                args.global_ylabel,
                output_dir / f"replot_{submode}_cluster{cluster}_globalTest.png",
            )
        plot_variance(
            rounds,
            pair_a["analysis"]["between_cluster_variance"],
            pair_b["analysis"]["between_cluster_variance"],
            mrounds,
            f"{title_prefix} | {submode} | Between-Cluster Variance",
            args.xlabel,
            args.variance_ylabel,
            output_dir / f"replot_{submode}_between_variance.png",
        )
    print(f"Replots saved to: {output_dir}")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-folder", required=True)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--title-prefix", default=None)
    parser.add_argument("--xlabel", default="Communication Round")
    parser.add_argument("--ylabel", default="Cluster Test Accuracy (%)")
    parser.add_argument("--global-ylabel", default="Global Test Accuracy (%)")
    parser.add_argument("--variance-ylabel", default="Between-Cluster Accuracy Variance")
    parser.add_argument("--clusters", nargs="+", type=int, default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    replot(Path(args.config_folder), args)


if __name__ == "__main__":
    main()
