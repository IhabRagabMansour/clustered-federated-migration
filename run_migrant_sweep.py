"""
Run a migration-size sweep for clustered FL migration.

This experiment fixes the number of clusters and clients per cluster, then
varies how many clients migrate from the source cluster to the destination
cluster. It is intended for plots such as:

    x-axis: number of migrated clients
    y-axis: destination-cluster maximum accuracy drop

Examples
--------
Dry-run the default CIFAR-10 CNN sweep:
    python run_migrant_sweep.py --dry-run

Run CIFAR-10 CNN, K=2, 10 clients/cluster, 1..10 migrants, 3 seeds:
    python run_migrant_sweep.py --datasets CIFAR-10 --models CNN --resume

Run all three CNN datasets:
    python run_migrant_sweep.py --datasets MNIST F-MNIST CIFAR-10 --models CNN --resume
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
from itertools import product
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from config_loader import config
from main import build_and_run
from run_grid import normalize_dataset, normalize_model, safe_name


CASES = [("caseA", False), ("caseB", True)]
SUBMODE_CHOICES = ["membership_only", "data_changes"]


def config_name(
    dataset: str,
    model: str,
    clusters: int,
    clients_per_cluster: int,
    num_migrants: int,
    seed: int,
) -> str:
    return (
        f"dataset_{safe_name(dataset)}"
        f"_model_{safe_name(model)}"
        f"_clusters_{clusters}"
        f"_clientsPerCluster_{clients_per_cluster}"
        f"_migrants_{num_migrants}"
        f"_seed_{seed}"
    )


def migration_schedule(
    num_clusters: int,
    clients_per_cluster: int,
    migration_round: int,
    num_migrants: int,
) -> List[dict]:
    if num_clusters < 2:
        raise ValueError("Migration needs at least two clusters")
    if clients_per_cluster < 1:
        raise ValueError("clients_per_cluster must be positive")
    if num_migrants < 1 or num_migrants > clients_per_cluster:
        raise ValueError(
            f"num_migrants must be in [1, {clients_per_cluster}], got {num_migrants}"
        )

    return [
        {
            "round": int(migration_round),
            "clients": list(range(int(num_migrants))),
            "src": 0,
            "dst": int(num_clusters - 1),
        }
    ]


def impact_lookup(analysis: dict, cluster: int, key: str) -> dict:
    for item in analysis.get(key, []):
        if int(item["cluster"]) == int(cluster):
            return item
    return {}


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


def format_value(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def summary_rows(
    meta: dict,
    results: Dict[Tuple[str, str], dict],
    submodes: List[str],
) -> List[dict]:
    rows = []
    for submode in submodes:
        res_a = results[(submode, "caseA")]
        res_b = results[(submode, "caseB")]
        affected = res_a["affected_clusters"]
        for cluster_id in affected:
            sa = impact_lookup(res_a["analysis"], cluster_id, "migration_impact")
            sb = impact_lookup(res_b["analysis"], cluster_id, "migration_impact")
            ga = impact_lookup(res_a["analysis"], cluster_id, "migration_impact_global")
            gb = impact_lookup(res_b["analysis"], cluster_id, "migration_impact_global")
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
                row.update(
                    {
                        "submode": submode,
                        "cluster": cluster_id,
                        "metric": metric,
                        "caseA": case_a,
                        "caseB": case_b,
                    }
                )
                rows.append(row)
    return rows


def case_value_rows(
    meta: dict,
    results: Dict[Tuple[str, str], dict],
) -> List[dict]:
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
                    row.update(
                        {
                            "submode": submode,
                            "case": case_name,
                            "sharing_enabled": case_name == "caseB",
                            "cluster": int(stats["cluster"]),
                            "metric": f"{prefix}_{metric_name}",
                            "value": stats.get(metric_key),
                            "run_dir": result["run_dir"],
                        }
                    )
                    rows.append(row)
    return rows


def write_markdown_summary(path: Path, rows: List[dict], meta: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Migrant-Count Sweep Configuration Summary\n\n")
        for key in [
            "dataset",
            "model",
            "num_clusters",
            "clients_per_cluster",
            "total_clients",
            "seed",
            "migration_round",
            "num_migrants",
        ]:
            f.write(f"- **{key}**: {meta[key]}\n")
        if int(meta["num_migrants"]) == int(meta["clients_per_cluster"]):
            f.write("\n")
            f.write(
                "Note: this configuration migrates all clients from the source "
                "cluster, leaving the source cluster empty after migration.\n"
            )
        f.write("\n")
        f.write("| submode | cluster | metric | Case A | Case B |\n")
        f.write("|---|---:|---|---:|---:|\n")
        for row in rows:
            f.write(
                f"| {row['submode']} | {row['cluster']} | {row['metric']} | "
                f"{format_value(row['caseA'])} | {format_value(row['caseB'])} |\n"
            )


def apply_config(
    meta: dict,
    schedule: List[dict],
    config_dir: Path,
    submode: str,
    case_name: str,
    sharing_enabled: bool,
    verbose_rounds: bool,
) -> None:
    config._config["data"]["dataset"] = meta["dataset"]
    config._config["model"]["architecture"] = meta["model"]
    config._config["clustered"]["num_clusters"] = meta["num_clusters"]
    config._config["clustered"]["total_clients"] = meta["total_clients"]
    config._config["clustered"]["migration"]["schedule"] = copy.deepcopy(schedule)
    config._config["clustered"]["migration"]["behavior_change"] = submode
    config._config["clustered"]["sharing"]["enabled"] = bool(sharing_enabled)
    config._config["experiment"]["seed"] = meta["seed"]
    config._config["experiment"]["name"] = f"{case_name}_{submode}"
    config._config["logging"]["save_path"] = str(config_dir / "runs")
    config._config["logging"]["verbose"] = bool(verbose_rounds)
    config._config["plotting"]["save_path"] = str(config_dir / "plots")


def run_one_configuration(meta: dict, config_dir: Path, schedule: List[dict], args) -> None:
    config_dir.mkdir(parents=True, exist_ok=True)
    complete_marker = config_dir / "COMPLETE.json"
    if args.resume and complete_marker.exists():
        print(f"[skip] {config_dir.name}")
        return

    with (config_dir / "sweep_config.json").open("w", encoding="utf-8") as f:
        json.dump({"meta": meta, "migration_schedule": schedule}, f, indent=2)

    results: Dict[Tuple[str, str], dict] = {}
    manifest_rows = []
    for submode in args.submodes:
        for case_name, sharing_enabled in CASES:
            print(f"[run] {config_dir.name} | {submode} | {case_name}")
            apply_config(
                meta,
                schedule,
                config_dir,
                submode,
                case_name,
                sharing_enabled,
                args.verbose_rounds,
            )
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
    rows = summary_rows(meta, results, args.submodes)
    value_rows = case_value_rows(meta, results)
    write_csv(config_dir / "summary.csv", rows)
    write_csv(config_dir / "case_values.csv", value_rows)
    write_markdown_summary(config_dir / "summary.md", rows, meta)

    with complete_marker.open("w", encoding="utf-8") as f:
        json.dump({"status": "complete", "meta": meta}, f, indent=2)


def build_grid(args) -> Iterable[Tuple[dict, List[dict], Path]]:
    output_root = Path(args.output_root)
    for dataset, model, num_migrants, seed in product(
        args.datasets, args.models, args.migrants, args.seeds
    ):
        total_clients = int(args.clusters) * int(args.clients_per_cluster)
        schedule = migration_schedule(
            int(args.clusters),
            int(args.clients_per_cluster),
            int(args.migration_round),
            int(num_migrants),
        )
        meta = {
            "dataset": dataset,
            "model": model,
            "num_clusters": int(args.clusters),
            "clients_per_cluster": int(args.clients_per_cluster),
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
            dataset,
            model,
            int(args.clusters),
            int(args.clients_per_cluster),
            int(num_migrants),
            int(seed),
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="migrant_sweep_results")
    parser.add_argument("--datasets", nargs="+", type=normalize_dataset, default=["CIFAR-10"])
    parser.add_argument("--models", nargs="+", type=normalize_model, default=["CNN"])
    parser.add_argument("--clusters", type=int, default=2)
    parser.add_argument("--clients-per-cluster", type=int, default=10)
    parser.add_argument("--migrants", nargs="+", type=int, default=list(range(1, 11)))
    parser.add_argument("--seeds", nargs="+", type=int, default=[42, 43, 44])
    parser.add_argument("--submodes", nargs="+", choices=SUBMODE_CHOICES, default=["data_changes"])
    parser.add_argument("--migration-round", type=int, default=40)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--verbose-rounds", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    grid = list(build_grid(args))
    if args.limit is not None:
        grid = grid[: args.limit]
    atomic_runs = len(grid) * len(args.submodes) * len(CASES)
    print(f"Configurations: {len(grid)} | atomic runs: {atomic_runs}")
    if any(m == args.clients_per_cluster for m in args.migrants):
        print(
            "[note] The largest migrant count moves every source-cluster client. "
            "The source cluster is empty after migration in that setting."
        )

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
