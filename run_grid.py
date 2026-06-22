"""
Run a resumable experiment grid for clustered FL migration.

Examples
--------
Dry-run the full grid:
    python run_grid.py --dry-run

Run a small smoke subset:
    python run_grid.py --datasets MNIST --models CNN --clusters 2 --clients-per-cluster 3 --seeds 42

Resume a long run:
    python run_grid.py --resume
"""

import argparse
import copy
import csv
import json
import os
from itertools import product
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from config_loader import config
from main import build_and_run
from plots.plot import plot_between_variance_comparison, plot_case_comparison


DATASET_ALIASES = {
    "mnist": "MNIST",
    "m": "MNIST",
    "f-mnist": "F-MNIST",
    "fmnist": "F-MNIST",
    "fashion-mnist": "F-MNIST",
    "fashion": "F-MNIST",
    "cifar": "CIFAR-10",
    "cifar10": "CIFAR-10",
    "cifar-10": "CIFAR-10",
}
MODEL_ALIASES = {
    "cnn": "CNN",
    "resnet": "ResNet",
    "resnet18": "ResNet",
}
SUBMODES = ["membership_only", "data_changes"]
CASES = [("caseA", False), ("caseB", True)]


def normalize_dataset(name: str) -> str:
    key = name.strip().lower()
    if key not in DATASET_ALIASES:
        raise argparse.ArgumentTypeError(f"Unknown dataset '{name}'")
    return DATASET_ALIASES[key]


def normalize_model(name: str) -> str:
    key = name.strip().lower()
    if key not in MODEL_ALIASES:
        raise argparse.ArgumentTypeError(f"Unknown model '{name}'")
    return MODEL_ALIASES[key]


def safe_name(value: str) -> str:
    return value.replace("-", "").replace(" ", "").replace("_", "")


def config_name(dataset: str, model: str, clusters: int,
                clients_per_cluster: int, seed: int) -> str:
    return (
        f"dataset_{safe_name(dataset)}"
        f"_model_{safe_name(model)}"
        f"_clusters_{clusters}"
        f"_clientsPerCluster_{clients_per_cluster}"
        f"_seed_{seed}"
    )


def migration_schedule(num_clusters: int, clients_per_cluster: int,
                       migration_round: int, requested_migrants: int) -> Tuple[List[dict], int]:
    if num_clusters < 2:
        raise ValueError("Migration needs at least two clusters")
    if clients_per_cluster < 2:
        raise ValueError("Migration needs at least two clients in the source cluster")
    num_migrants = min(requested_migrants, clients_per_cluster - 1)
    clients = list(range(num_migrants))
    return ([{
        "round": int(migration_round),
        "clients": clients,
        "src": 0,
        "dst": int(num_clusters - 1),
    }], num_migrants)


def impact_lookup(analysis: dict, cluster: int, key: str) -> dict:
    for item in analysis.get(key, []):
        if int(item["cluster"]) == int(cluster):
            return item
    return {}


def summary_rows(meta: dict, results: Dict[Tuple[str, str], dict]) -> List[dict]:
    rows = []
    for submode in SUBMODES:
        res_a = results[(submode, "caseA")]
        res_b = results[(submode, "caseB")]
        affected = res_a["affected_clusters"]
        for cluster in affected:
            sa = impact_lookup(res_a["analysis"], cluster, "migration_impact")
            sb = impact_lookup(res_b["analysis"], cluster, "migration_impact")
            ga = impact_lookup(res_a["analysis"], cluster, "migration_impact_global")
            gb = impact_lookup(res_b["analysis"], cluster, "migration_impact_global")
            metric_pairs = [
                ("clusterTest_before", sa.get("before_mean"), sb.get("before_mean")),
                ("clusterTest_maxDrop", sa.get("max_drop"), sb.get("max_drop")),
                ("clusterTest_afterMean", sa.get("after_mean"), sb.get("after_mean")),
                ("clusterTest_afterStd", sa.get("after_std"), sb.get("after_std")),
                ("clusterTest_recovery", sa.get("recovery_time"), sb.get("recovery_time")),
                ("globalTest_before", ga.get("before_mean"), gb.get("before_mean")),
                ("globalTest_maxDrop", ga.get("max_drop"), gb.get("max_drop")),
                ("globalTest_afterMean", ga.get("after_mean"), gb.get("after_mean")),
                ("globalTest_afterStd", ga.get("after_std"), gb.get("after_std")),
            ]
            for metric, case_a, case_b in metric_pairs:
                row = dict(meta)
                row.update({
                    "submode": submode,
                    "cluster": cluster,
                    "metric": metric,
                    "caseA": case_a,
                    "caseB": case_b,
                })
                rows.append(row)
    return rows


def case_value_rows(meta: dict, results: Dict[Tuple[str, str], dict]) -> List[dict]:
    rows = []
    for (submode, case_name), result in results.items():
        for source_key, prefix in [
            ("migration_impact", "clusterTest"),
            ("migration_impact_global", "globalTest"),
        ]:
            for stats in result["analysis"].get(source_key, []):
                for metric_key, metric_name in [
                    ("before_mean", "before"),
                    ("max_drop", "maxDrop"),
                    ("after_mean", "afterMean"),
                    ("after_std", "afterStd"),
                    ("recovery_time", "recovery"),
                ]:
                    row = dict(meta)
                    row.update({
                        "submode": submode,
                        "case": case_name,
                        "sharing_enabled": case_name == "caseB",
                        "cluster": int(stats["cluster"]),
                        "metric": f"{prefix}_{metric_name}",
                        "value": stats.get(metric_key),
                        "run_dir": result["run_dir"],
                    })
                    rows.append(row)
    return rows


def write_csv(path: Path, rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def append_csv(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def write_markdown_summary(path: Path, rows: List[dict], meta: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Configuration Summary\n\n")
        for key in [
            "dataset", "model", "num_clusters", "clients_per_cluster",
            "total_clients", "seed", "migration_round", "num_migrants",
        ]:
            f.write(f"- **{key}**: {meta[key]}\n")
        f.write("\n")
        f.write("| submode | cluster | metric | Case A | Case B |\n")
        f.write("|---|---:|---|---:|---:|\n")
        for row in rows:
            f.write(
                f"| {row['submode']} | {row['cluster']} | {row['metric']} | "
                f"{format_value(row['caseA'])} | {format_value(row['caseB'])} |\n"
            )


def format_value(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def make_plots(config_dir: Path, meta: dict, results: Dict[Tuple[str, str], dict]) -> None:
    plot_dir = config_dir / "plots"
    for submode in SUBMODES:
        res_a = results[(submode, "caseA")]
        res_b = results[(submode, "caseB")]
        rounds = res_a["history"]["rounds"]
        migration_rounds = res_a["migration_rounds"]
        for cluster in res_a["affected_clusters"]:
            title_base = (
                f"{meta['dataset']} {meta['model']} | clusters={meta['num_clusters']} "
                f"clients/group={meta['clients_per_cluster']} seed={meta['seed']} | {submode}"
            )
            plot_case_comparison(
                rounds,
                res_a["history"]["cluster_test_acc"][cluster],
                res_b["history"]["cluster_test_acc"][cluster],
                migration_rounds,
                cluster,
                f"{title_base} | Cluster {cluster} Test Accuracy",
                str(plot_dir),
                f"compare_{submode}_cluster{cluster}_clusterTest.png",
            )
            plot_case_comparison(
                rounds,
                res_a["history"]["global_test_acc"][cluster],
                res_b["history"]["global_test_acc"][cluster],
                migration_rounds,
                cluster,
                f"{title_base} | Cluster {cluster} Global Test Accuracy",
                str(plot_dir),
                f"compare_{submode}_cluster{cluster}_globalTest.png",
            )
        plot_between_variance_comparison(
            rounds,
            res_a["analysis"]["between_cluster_variance"],
            res_b["analysis"]["between_cluster_variance"],
            migration_rounds,
            f"{meta['dataset']} {meta['model']} | {submode} | Between-Cluster Variance",
            str(plot_dir),
            f"compare_{submode}_between_variance.png",
        )


def apply_config(meta: dict, schedule: List[dict], config_dir: Path,
                 submode: str, case_name: str, sharing_enabled: bool,
                 verbose_rounds: bool) -> None:
    total_clients = meta["total_clients"]
    config._config["data"]["dataset"] = meta["dataset"]
    config._config["model"]["architecture"] = meta["model"]
    config._config["clustered"]["num_clusters"] = meta["num_clusters"]
    config._config["clustered"]["total_clients"] = total_clients
    config._config["clustered"]["migration"]["schedule"] = copy.deepcopy(schedule)
    config._config["clustered"]["migration"]["behavior_change"] = submode
    config._config["clustered"]["sharing"]["enabled"] = bool(sharing_enabled)
    config._config["experiment"]["seed"] = meta["seed"]
    config._config["experiment"]["name"] = f"{case_name}_{submode}"
    config._config["logging"]["save_path"] = str(config_dir / "runs")
    config._config["logging"]["verbose"] = bool(verbose_rounds)
    config._config["plotting"]["save_path"] = str(config_dir / "plots")


def run_one_configuration(meta: dict, config_dir: Path, schedule: List[dict],
                          args) -> None:
    config_dir.mkdir(parents=True, exist_ok=True)
    complete_marker = config_dir / "COMPLETE.json"
    if args.resume and complete_marker.exists():
        print(f"[skip] {config_dir.name}")
        return

    with (config_dir / "grid_config.json").open("w", encoding="utf-8") as f:
        json.dump({"meta": meta, "migration_schedule": schedule}, f, indent=2)

    results: Dict[Tuple[str, str], dict] = {}
    manifest_rows = []
    for submode in SUBMODES:
        for case_name, sharing_enabled in CASES:
            print(f"[run] {config_dir.name} | {submode} | {case_name}")
            apply_config(meta, schedule, config_dir, submode, case_name,
                         sharing_enabled, args.verbose_rounds)
            try:
                result = build_and_run(
                    sharing_enabled=sharing_enabled,
                    experiment_name=f"{case_name}_{submode}",
                    do_plots=False,
                )
                results[(submode, case_name)] = result
                row = {
                    **meta,
                    "submode": submode,
                    "case": case_name,
                    "status": "ok",
                    "run_dir": result["run_dir"],
                    "error": "",
                }
            except Exception as exc:
                row = {
                    **meta,
                    "submode": submode,
                    "case": case_name,
                    "status": "failed",
                    "run_dir": "",
                    "error": repr(exc),
                }
                append_csv(Path(args.output_root) / "failed_runs.csv", row)
                append_csv(Path(args.output_root) / "run_manifest.csv", row)
                write_csv(config_dir / "run_manifest.csv", manifest_rows + [row])
                raise
            manifest_rows.append(row)
            append_csv(Path(args.output_root) / "run_manifest.csv", row)

    write_csv(config_dir / "run_manifest.csv", manifest_rows)
    rows = summary_rows(meta, results)
    value_rows = case_value_rows(meta, results)
    write_csv(config_dir / "summary.csv", rows)
    write_csv(config_dir / "case_values.csv", value_rows)
    write_markdown_summary(config_dir / "summary.md", rows, meta)
    make_plots(config_dir, meta, results)

    with complete_marker.open("w", encoding="utf-8") as f:
        json.dump({"status": "complete", "meta": meta}, f, indent=2)


def build_grid(args) -> Iterable[Tuple[dict, List[dict], Path]]:
    output_root = Path(args.output_root)
    for dataset, model, clusters, clients_per_cluster, seed in product(
        args.datasets, args.models, args.clusters, args.clients_per_cluster, args.seeds
    ):
        total_clients = int(clusters) * int(clients_per_cluster)
        schedule, num_migrants = migration_schedule(
            int(clusters),
            int(clients_per_cluster),
            args.migration_round,
            args.migrants,
        )
        meta = {
            "dataset": dataset,
            "model": model,
            "num_clusters": int(clusters),
            "clients_per_cluster": int(clients_per_cluster),
            "total_clients": total_clients,
            "seed": int(seed),
            "migration_round": int(args.migration_round),
            "num_migrants": int(num_migrants),
            "beta": config.clustered.sharing.beta,
            "share_interval": config.clustered.sharing.interval,
            "global_rounds": config.training.global_rounds,
            "local_epochs": config.training.local_epochs,
        }
        yield meta, schedule, output_root / config_name(
            dataset, model, int(clusters), int(clients_per_cluster), int(seed)
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="grid_results")
    parser.add_argument("--datasets", nargs="+", type=normalize_dataset,
                        default=["CIFAR-10", "MNIST", "F-MNIST"])
    parser.add_argument("--models", nargs="+", type=normalize_model,
                        default=["CNN", "ResNet"])
    parser.add_argument("--clusters", nargs="+", type=int, default=[2, 10])
    parser.add_argument("--clients-per-cluster", nargs="+", type=int,
                        default=list(range(3, 11)))
    parser.add_argument("--seeds", nargs="+", type=int, default=[42, 43, 44])
    parser.add_argument("--migration-round", type=int, default=40)
    parser.add_argument("--migrants", type=int, default=3)
    parser.add_argument("--resume", action="store_true",
                        help="Skip configuration folders with COMPLETE.json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None,
                        help="Run only the first N configurations")
    parser.add_argument("--verbose-rounds", action="store_true",
                        help="Print every round during training")
    return parser.parse_args()


def main():
    args = parse_args()
    grid = list(build_grid(args))
    if args.limit is not None:
        grid = grid[:args.limit]
    atomic_runs = len(grid) * len(SUBMODES) * len(CASES)
    print(f"Configurations: {len(grid)} | atomic runs: {atomic_runs}")
    for meta, schedule, config_dir in grid:
        if args.dry_run:
            print(f"[dry-run] {config_dir.name} | schedule={schedule}")
            continue
        try:
            run_one_configuration(meta, config_dir, schedule, args)
        except Exception as exc:
            print(f"[failed] {config_dir.name}: {exc!r}")
            if args.limit == 1:
                raise


if __name__ == "__main__":
    main()
