"""
Run an inter-cluster sharing-percentage sweep for clustered FL migration.

The experiment fixes the migration setting and varies the percentage of model
information mixed from other clusters in Case B. In the implementation:

    mixed_model = beta * own_model + (1 - beta) * mean(other_cluster_models)

so:

    sharing_percent = 100 * (1 - beta)

The default setting follows the supervisor-requested sweep:
    - K = 2
    - 10 clients per cluster
    - 5 migrated clients
    - data-changing migration
    - CIFAR-10 CNN

Examples
--------
Dry-run:
    python run_sharing_sweep.py --dry-run

Run CIFAR-10 CNN with three seeds:
    python run_sharing_sweep.py --datasets CIFAR-10 --models CNN --resume
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


SUBMODE_CHOICES = ["membership_only", "data_changes"]


def percent_name(value: float) -> str:
    text = f"{value:g}".replace(".", "p").replace("-", "m")
    return text


def config_name(
    dataset: str,
    model: str,
    clusters: int,
    clients_per_cluster: int,
    num_migrants: int,
    case_name: str,
    sharing_percent: float,
    seed: int,
) -> str:
    return (
        f"dataset_{safe_name(dataset)}"
        f"_model_{safe_name(model)}"
        f"_clusters_{clusters}"
        f"_clientsPerCluster_{clients_per_cluster}"
        f"_migrants_{num_migrants}"
        f"_{case_name}"
        f"_sharePct_{percent_name(sharing_percent)}"
        f"_seed_{seed}"
    )


def beta_from_percent(sharing_percent: float) -> float:
    if sharing_percent < 0 or sharing_percent > 100:
        raise ValueError(f"sharing_percent must be in [0, 100], got {sharing_percent}")
    return 1.0 - (float(sharing_percent) / 100.0)


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


def append_csv(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def write_csv(path: Path, rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def apply_config(
    meta: dict,
    schedule: List[dict],
    config_dir: Path,
    submode: str,
    case_name: str,
    sharing_enabled: bool,
    beta: float,
    verbose_rounds: bool,
) -> None:
    config._config["data"]["dataset"] = meta["dataset"]
    config._config["model"]["architecture"] = meta["model"]
    config._config["clustered"]["num_clusters"] = meta["num_clusters"]
    config._config["clustered"]["total_clients"] = meta["total_clients"]
    config._config["clustered"]["migration"]["schedule"] = copy.deepcopy(schedule)
    config._config["clustered"]["migration"]["behavior_change"] = submode
    config._config["clustered"]["sharing"]["enabled"] = bool(sharing_enabled)
    config._config["clustered"]["sharing"]["beta"] = float(beta)
    config._config["experiment"]["seed"] = meta["seed"]
    config._config["experiment"]["name"] = f"{case_name}_{submode}"
    config._config["logging"]["save_path"] = str(config_dir / "runs")
    config._config["logging"]["verbose"] = bool(verbose_rounds)
    config._config["plotting"]["save_path"] = str(config_dir / "plots")


def impact_lookup(analysis: dict, cluster: int, key: str) -> dict:
    for item in analysis.get(key, []):
        if int(item["cluster"]) == int(cluster):
            return item
    return {}


def case_value_rows(meta: dict, result: dict, submode: str, case_name: str) -> List[dict]:
    rows = []
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


def summary_rows(meta: dict, result: dict, submode: str, case_name: str) -> List[dict]:
    rows = []
    for cluster_id in result["affected_clusters"]:
        sa = impact_lookup(result["analysis"], cluster_id, "migration_impact")
        ga = impact_lookup(result["analysis"], cluster_id, "migration_impact_global")
        metric_pairs = [
            ("clusterTest_before", sa.get("before_mean")),
            ("clusterTest_maxDrop", sa.get("max_drop")),
            ("clusterTest_afterMean", sa.get("after_mean")),
            ("clusterTest_afterStd", sa.get("after_std")),
            ("clusterTest_recovery", sa.get("recovery_time")),
            ("globalTest_before", ga.get("before_mean")),
            ("globalTest_maxDrop", ga.get("max_drop")),
            ("globalTest_afterMean", ga.get("after_mean")),
            ("globalTest_afterStd", ga.get("after_std")),
        ]
        for metric, value in metric_pairs:
            row = dict(meta)
            row.update(
                {
                    "submode": submode,
                    "case": case_name,
                    "cluster": cluster_id,
                    "metric": metric,
                    "value": value,
                }
            )
            rows.append(row)
    return rows


def run_one_atomic(meta: dict, schedule: List[dict], config_dir: Path, args) -> None:
    config_dir.mkdir(parents=True, exist_ok=True)
    complete_marker = config_dir / "COMPLETE.json"
    if args.resume and complete_marker.exists():
        print(f"[skip] {config_dir.name}")
        return

    with (config_dir / "sharing_sweep_config.json").open("w", encoding="utf-8") as f:
        json.dump({"meta": meta, "migration_schedule": schedule}, f, indent=2)

    manifest_rows = []
    all_value_rows = []
    all_summary_rows = []
    for submode in args.submodes:
        case_name = meta["case"]
        sharing_enabled = case_name == "caseB"
        print(f"[run] {config_dir.name} | {submode} | {case_name}")
        apply_config(
            meta,
            schedule,
            config_dir,
            submode,
            case_name,
            sharing_enabled,
            meta["beta"],
            args.verbose_rounds,
        )
        try:
            result = build_and_run(
                sharing_enabled=sharing_enabled,
                experiment_name=f"{case_name}_{submode}",
                do_plots=False,
            )
            row = {
                **meta,
                "submode": submode,
                "status": "ok",
                "run_dir": result["run_dir"],
                "error": "",
            }
        except Exception as exc:
            row = {
                **meta,
                "submode": submode,
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
        all_value_rows.extend(case_value_rows(meta, result, submode, case_name))
        all_summary_rows.extend(summary_rows(meta, result, submode, case_name))

    write_csv(config_dir / "run_manifest.csv", manifest_rows)
    write_csv(config_dir / "case_values.csv", all_value_rows)
    write_csv(config_dir / "summary.csv", all_summary_rows)
    with complete_marker.open("w", encoding="utf-8") as f:
        json.dump({"status": "complete", "meta": meta}, f, indent=2)


def build_grid(args) -> Iterable[Tuple[dict, List[dict], Path]]:
    output_root = Path(args.output_root)
    for dataset, model, seed in product(args.datasets, args.models, args.seeds):
        total_clients = int(args.clusters) * int(args.clients_per_cluster)
        schedule = migration_schedule(
            int(args.clusters),
            int(args.clients_per_cluster),
            int(args.migration_round),
            int(args.migrants),
        )

        if args.include_case_a:
            meta = {
                "dataset": dataset,
                "model": model,
                "num_clusters": int(args.clusters),
                "clients_per_cluster": int(args.clients_per_cluster),
                "total_clients": total_clients,
                "seed": int(seed),
                "migration_round": int(args.migration_round),
                "num_migrants": int(args.migrants),
                "sharing_percent": 0.0,
                "beta": 1.0,
                "share_interval": config.clustered.sharing.interval,
                "global_rounds": config.training.global_rounds,
                "local_epochs": config.training.local_epochs,
                "case": "caseA",
            }
            yield meta, schedule, output_root / config_name(
                dataset,
                model,
                int(args.clusters),
                int(args.clients_per_cluster),
                int(args.migrants),
                "caseA",
                0.0,
                int(seed),
            )

        for sharing_percent in args.sharing_percents:
            beta = beta_from_percent(float(sharing_percent))
            meta = {
                "dataset": dataset,
                "model": model,
                "num_clusters": int(args.clusters),
                "clients_per_cluster": int(args.clients_per_cluster),
                "total_clients": total_clients,
                "seed": int(seed),
                "migration_round": int(args.migration_round),
                "num_migrants": int(args.migrants),
                "sharing_percent": float(sharing_percent),
                "beta": beta,
                "share_interval": config.clustered.sharing.interval,
                "global_rounds": config.training.global_rounds,
                "local_epochs": config.training.local_epochs,
                "case": "caseB",
            }
            yield meta, schedule, output_root / config_name(
                dataset,
                model,
                int(args.clusters),
                int(args.clients_per_cluster),
                int(args.migrants),
                "caseB",
                float(sharing_percent),
                int(seed),
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="sharing_sweep_results")
    parser.add_argument("--datasets", nargs="+", type=normalize_dataset, default=["CIFAR-10"])
    parser.add_argument("--models", nargs="+", type=normalize_model, default=["CNN"])
    parser.add_argument("--clusters", type=int, default=2)
    parser.add_argument("--clients-per-cluster", type=int, default=10)
    parser.add_argument("--migrants", type=int, default=5)
    parser.add_argument(
        "--sharing-percents",
        nargs="+",
        type=float,
        default=[5, 10, 20, 30, 40, 50],
        help="Percentage mixed from other clusters in Case B.",
    )
    parser.add_argument("--seeds", nargs="+", type=int, default=[42, 43, 44])
    parser.add_argument("--submodes", nargs="+", choices=SUBMODE_CHOICES, default=["data_changes"])
    parser.add_argument("--migration-round", type=int, default=40)
    parser.add_argument("--include-case-a", action="store_true", default=True)
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
    atomic_runs = len(grid) * len(args.submodes)
    print(f"Configurations: {len(grid)} | atomic runs: {atomic_runs}")
    print(
        f"Fixed setting: K={args.clusters}, clients/cluster={args.clients_per_cluster}, "
        f"migrants={args.migrants}"
    )

    for meta, schedule, config_dir in grid:
        if args.dry_run:
            print(
                f"[dry-run] {config_dir.name} | case={meta['case']} "
                f"share={meta['sharing_percent']:g}% beta={meta['beta']:.3f} "
                f"schedule={schedule}"
            )
            continue
        try:
            run_one_atomic(meta, schedule, config_dir, args)
        except Exception as exc:
            print(f"[failed] {config_dir.name}: {exc!r}")
            if args.limit == 1:
                raise


if __name__ == "__main__":
    main()
