"""
Aggregate saved grid experiment results.

Reads every ``case_values.csv`` produced by ``run_grid.py`` and writes:

    grid_results/all_results.csv
    grid_results/grouped_summary.csv
    grid_results/grouped_summary.md

Example:
    python aggregate_grid_results.py --root grid_results
"""

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev
from typing import Dict, Iterable, List, Tuple


GROUP_KEYS = [
    "dataset",
    "model",
    "num_clusters",
    "clients_per_cluster",
    "total_clients",
    "submode",
    "cluster",
    "metric",
    "case",
]


def read_csv(path: Path) -> List[dict]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def parse_value(value: str):
    if value in ("", "None", None):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def collect_case_values(root: Path) -> List[dict]:
    rows: List[dict] = []
    for path in sorted(root.glob("dataset_*/case_values.csv")):
        for row in read_csv(path):
            row["config_dir"] = str(path.parent)
            rows.append(row)
    return rows


def numeric_summary(values: Iterable[float]) -> Dict[str, float]:
    nums = [float(v) for v in values if v is not None and not math.isnan(float(v))]
    if not nums:
        return {"n": 0, "mean": "", "std": "", "min": "", "max": ""}
    return {
        "n": len(nums),
        "mean": mean(nums),
        "std": stdev(nums) if len(nums) > 1 else 0.0,
        "min": min(nums),
        "max": max(nums),
    }


def grouped_summary(rows: List[dict]) -> List[dict]:
    grouped: Dict[Tuple[str, ...], List[float]] = defaultdict(list)
    seed_sets: Dict[Tuple[str, ...], set] = defaultdict(set)
    for row in rows:
        key = tuple(row.get(k, "") for k in GROUP_KEYS)
        grouped[key].append(parse_value(row.get("value")))
        seed_sets[key].add(row.get("seed", ""))

    out = []
    for key in sorted(grouped):
        stats = numeric_summary(grouped[key])
        row = {k: key[i] for i, k in enumerate(GROUP_KEYS)}
        row.update({
            "num_seeds": len(seed_sets[key]),
            "n": stats["n"],
            "mean": format_number(stats["mean"]),
            "std": format_number(stats["std"]),
            "min": format_number(stats["min"]),
            "max": format_number(stats["max"]),
        })
        out.append(row)
    return out


def comparison_summary(grouped_rows: List[dict]) -> List[dict]:
    base_keys = [
        "dataset",
        "model",
        "num_clusters",
        "clients_per_cluster",
        "total_clients",
        "submode",
        "cluster",
        "metric",
    ]
    grouped = defaultdict(dict)
    for row in grouped_rows:
        key = tuple(row[k] for k in base_keys)
        grouped[key][row["case"]] = row

    out = []
    for key in sorted(grouped):
        cases = grouped[key]
        row = {k: key[i] for i, k in enumerate(base_keys)}
        for case_name, label in [("caseA", "caseA"), ("caseB", "caseB")]:
            case_row = cases.get(case_name, {})
            row[f"{label}_mean"] = case_row.get("mean", "")
            row[f"{label}_std"] = case_row.get("std", "")
            row[f"{label}_n"] = case_row.get("n", "")
        out.append(row)
    return out


def format_number(value) -> str:
    if value == "" or value is None:
        return ""
    return f"{float(value):.6f}"


def write_markdown(path: Path, rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Grouped Grid Summary\n\n")
        f.write("| dataset | model | clusters | clients/group | submode | cluster | metric | Case A mean±std | Case B mean±std |\n")
        f.write("|---|---|---:|---:|---|---:|---|---:|---:|\n")
        for row in rows:
            case_a = format_mean_std(row.get("caseA_mean"), row.get("caseA_std"))
            case_b = format_mean_std(row.get("caseB_mean"), row.get("caseB_std"))
            f.write(
                f"| {row['dataset']} | {row['model']} | {row['num_clusters']} | "
                f"{row['clients_per_cluster']} | {row['submode']} | {row['cluster']} | "
                f"{row['metric']} | {case_a} | {case_b} |\n"
            )


def format_mean_std(avg, sd) -> str:
    if avg in ("", None):
        return ""
    return f"{float(avg):.3f} +/- {float(sd):.3f}"


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="grid_results")
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.root)
    rows = collect_case_values(root)
    write_csv(root / "all_results.csv", rows)
    grouped_rows = grouped_summary(rows)
    write_csv(root / "grouped_summary_long.csv", grouped_rows)
    comparison_rows = comparison_summary(grouped_rows)
    write_csv(root / "grouped_summary.csv", comparison_rows)
    write_markdown(root / "grouped_summary.md", comparison_rows)
    print(f"Collected seed-level rows: {len(rows)}")
    print(f"Wrote: {root / 'all_results.csv'}")
    print(f"Wrote: {root / 'grouped_summary.csv'}")


if __name__ == "__main__":
    main()
