"""
Professor-friendly launcher for clustered FL migration experiments.

Edit the configuration block near the top of this file, then run:

    python run_experiments.py

Useful command-line overrides:

    python run_experiments.py --dry-run
    python run_experiments.py --only sharing_sweep
    python run_experiments.py --plots-only
    python run_experiments.py --no-plots
    python run_experiments.py --only migrant_sweep --limit 1 --no-plots

This file is intentionally a thin wrapper around the existing experiment
scripts. The existing runners remain the source of truth for training,
aggregation, and plotting behavior.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence


# ============================================================================
# Editable experiment configuration
# ============================================================================

# Choose any subset of: "main_grid", "migrant_sweep", "sharing_sweep".
EXPERIMENTS_TO_RUN = ["main_grid", "migrant_sweep", "sharing_sweep"]

RUN_TRAINING = True
RUN_PLOTS = True
RESUME = True

DATASETS = ["CIFAR-10"]
MODELS = ["CNN"]
SEEDS = [42, 43, 44]

CLUSTERS = [2]
CLIENTS_PER_CLUSTER = [10]

# Used by main_grid and migrant_sweep. For the full migrant-count sweep, set:
# MIGRANTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MIGRANTS = [5]

# Used by sharing_sweep. This is the fixed number of migrated clients.
SHARING_SWEEP_MIGRANTS = 5
SHARING_PERCENTAGES = [5, 10, 20, 30, 40, 50]

SUBMODES = ["data_changes"]
MIGRATION_ROUND = 40

GRID_RESULTS_ROOT = "grid_results"
MIGRANT_SWEEP_ROOT = "migrant_sweep_results"
SHARING_SWEEP_ROOT = "sharing_sweep_results"
FIGURES_OUT = "figures/results"

# Plot settings. The current paper plots use CNN, K=2, CIFAR-10 for the sweeps.
PLOT_MODEL = "CNN"
PLOT_DATASETS = ["CIFAR-10"]
PLOT_CLUSTER = 2
PLOT_CLIENTS_PER_CLUSTER = 10
PLOT_MIGRANTS = 5
PLOT_SUBMODE = "data_changes"

MIGRANT_SWEEP_PLOT_STEM = "migrant_sweep_data_changes_k2_cnn_cifar10"
SHARING_SWEEP_PLOT_STEM = "sharing_sweep_data_changes_k2_cnn_cifar10"
INSTABILITY_PLOT_STEM = "instability_data_changing_k2_cnn"

# The ResNet plot is generated from completed CIFAR-10 ResNet rows in grid_results.
RUN_RESNET_CIFAR10_PLOT = True


# ============================================================================
# Launcher implementation
# ============================================================================

ROOT = Path(__file__).resolve().parent
VALID_EXPERIMENTS = ["main_grid", "migrant_sweep", "sharing_sweep", "plots_only"]


def as_strings(values: Iterable[object]) -> list[str]:
    return [str(v) for v in values]


def script(path: str) -> list[str]:
    return [sys.executable, str(ROOT / path)]


def command_to_string(cmd: Sequence[str]) -> str:
    return subprocess.list2cmdline([str(part) for part in cmd])


def run_command(cmd: Sequence[str], dry_run: bool) -> None:
    cmd = [str(part) for part in cmd]
    print("\n$ " + command_to_string(cmd), flush=True)
    if dry_run:
        return
    subprocess.run(cmd, cwd=ROOT, check=True)


def with_common_training_flags(cmd: list[str], args: argparse.Namespace) -> list[str]:
    if RESUME:
        cmd.append("--resume")
    if args.limit is not None:
        cmd.extend(["--limit", str(args.limit)])
    if args.verbose_rounds:
        cmd.append("--verbose-rounds")
    return cmd


def main_grid_training_command(args: argparse.Namespace) -> list[str]:
    cmd = script("run_grid.py")
    cmd.extend(["--output-root", GRID_RESULTS_ROOT])
    cmd.extend(["--datasets", *DATASETS])
    cmd.extend(["--models", *MODELS])
    cmd.extend(["--clusters", *as_strings(CLUSTERS)])
    cmd.extend(["--clients-per-cluster", *as_strings(CLIENTS_PER_CLUSTER)])
    cmd.extend(["--seeds", *as_strings(SEEDS)])
    cmd.extend(["--migration-round", str(MIGRATION_ROUND)])
    cmd.extend(["--migrants", str(MIGRANTS[0])])
    return with_common_training_flags(cmd, args)


def migrant_sweep_training_commands(args: argparse.Namespace) -> list[list[str]]:
    commands = []
    for cluster in CLUSTERS:
        for clients_per_cluster in CLIENTS_PER_CLUSTER:
            cmd = script("run_migrant_sweep.py")
            cmd.extend(["--output-root", MIGRANT_SWEEP_ROOT])
            cmd.extend(["--datasets", *DATASETS])
            cmd.extend(["--models", *MODELS])
            cmd.extend(["--clusters", str(cluster)])
            cmd.extend(["--clients-per-cluster", str(clients_per_cluster)])
            cmd.extend(["--migrants", *as_strings(MIGRANTS)])
            cmd.extend(["--seeds", *as_strings(SEEDS)])
            cmd.extend(["--submodes", *SUBMODES])
            cmd.extend(["--migration-round", str(MIGRATION_ROUND)])
            commands.append(with_common_training_flags(cmd, args))
    return commands


def sharing_sweep_training_commands(args: argparse.Namespace) -> list[list[str]]:
    commands = []
    for cluster in CLUSTERS:
        for clients_per_cluster in CLIENTS_PER_CLUSTER:
            cmd = script("run_sharing_sweep.py")
            cmd.extend(["--output-root", SHARING_SWEEP_ROOT])
            cmd.extend(["--datasets", *DATASETS])
            cmd.extend(["--models", *MODELS])
            cmd.extend(["--clusters", str(cluster)])
            cmd.extend(["--clients-per-cluster", str(clients_per_cluster)])
            cmd.extend(["--migrants", str(SHARING_SWEEP_MIGRANTS)])
            cmd.extend(["--sharing-percents", *as_strings(SHARING_PERCENTAGES)])
            cmd.extend(["--seeds", *as_strings(SEEDS)])
            cmd.extend(["--submodes", *SUBMODES])
            cmd.extend(["--migration-round", str(MIGRATION_ROUND)])
            commands.append(with_common_training_flags(cmd, args))
    return commands


def main_grid_plot_commands() -> list[list[str]]:
    commands = [
        [*script("aggregate_grid_results.py"), "--root", GRID_RESULTS_ROOT],
        [
            *script("scripts/create_results_plots.py"),
            "--root",
            GRID_RESULTS_ROOT,
            "--model",
            PLOT_MODEL,
            "--out",
            FIGURES_OUT,
        ],
        [
            *script("scripts/create_instability_plots.py"),
            "--root",
            GRID_RESULTS_ROOT,
            "--out",
            FIGURES_OUT,
            "--model",
            PLOT_MODEL,
            "--clusters",
            str(PLOT_CLUSTER),
            "--submode",
            PLOT_SUBMODE,
            "--stem",
            INSTABILITY_PLOT_STEM,
        ],
    ]
    if RUN_RESNET_CIFAR10_PLOT:
        commands.append(
            [
                *script("scripts/create_resnet_cifar10_plots.py"),
                "--root",
                GRID_RESULTS_ROOT,
                "--out",
                FIGURES_OUT,
            ]
        )
    return commands


def migrant_sweep_plot_command() -> list[str]:
    return [
        *script("scripts/create_migrant_sweep_plots.py"),
        "--root",
        MIGRANT_SWEEP_ROOT,
        "--out",
        FIGURES_OUT,
        "--datasets",
        *PLOT_DATASETS,
        "--model",
        PLOT_MODEL,
        "--clusters",
        str(PLOT_CLUSTER),
        "--clients-per-cluster",
        str(PLOT_CLIENTS_PER_CLUSTER),
        "--submode",
        PLOT_SUBMODE,
        "--stem",
        MIGRANT_SWEEP_PLOT_STEM,
    ]


def sharing_sweep_plot_command() -> list[str]:
    return [
        *script("scripts/create_sharing_sweep_plots.py"),
        "--root",
        SHARING_SWEEP_ROOT,
        "--out",
        FIGURES_OUT,
        "--datasets",
        *PLOT_DATASETS,
        "--model",
        PLOT_MODEL,
        "--clusters",
        str(PLOT_CLUSTER),
        "--clients-per-cluster",
        str(PLOT_CLIENTS_PER_CLUSTER),
        "--migrants",
        str(PLOT_MIGRANTS),
        "--submode",
        PLOT_SUBMODE,
        "--stem",
        SHARING_SWEEP_PLOT_STEM,
    ]


def selected_experiments(args: argparse.Namespace) -> list[str]:
    experiments = args.only if args.only else list(EXPERIMENTS_TO_RUN)
    if "plots_only" in experiments and len(experiments) == 1:
        return ["main_grid", "migrant_sweep", "sharing_sweep"]
    return [exp for exp in experiments if exp != "plots_only"]


def plots_only_mode(args: argparse.Namespace) -> bool:
    return bool(args.plots_only or (args.only and "plots_only" in args.only))


def training_enabled(args: argparse.Namespace) -> bool:
    if plots_only_mode(args):
        return False
    return RUN_TRAINING


def plots_enabled(args: argparse.Namespace) -> bool:
    if args.no_plots:
        return False
    if plots_only_mode(args):
        return True
    return RUN_PLOTS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        nargs="+",
        choices=VALID_EXPERIMENTS,
        help="Run only selected experiment families.",
    )
    parser.add_argument(
        "--plots-only",
        action="store_true",
        help="Regenerate plots from existing results without running training.",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Run training but skip plot generation.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print commands without executing them.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Pass --limit to selected training runners.",
    )
    parser.add_argument(
        "--verbose-rounds",
        action="store_true",
        help="Pass --verbose-rounds to selected training runners.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if plots_only_mode(args) and args.no_plots:
        raise SystemExit("plots-only mode and --no-plots cannot be used together.")

    experiments = selected_experiments(args)
    do_training = training_enabled(args)
    do_plots = plots_enabled(args)

    print("Selected experiments:", ", ".join(experiments))
    print(f"Training: {'on' if do_training else 'off'} | Plots: {'on' if do_plots else 'off'}")
    if args.dry_run:
        print("Dry run: commands will be printed but not executed.")

    if do_training:
        if "main_grid" in experiments:
            run_command(main_grid_training_command(args), args.dry_run)
        if "migrant_sweep" in experiments:
            for cmd in migrant_sweep_training_commands(args):
                run_command(cmd, args.dry_run)
        if "sharing_sweep" in experiments:
            for cmd in sharing_sweep_training_commands(args):
                run_command(cmd, args.dry_run)

    if do_plots:
        plot_experiments = experiments
        if plots_only_mode(args) and args.only and set(args.only) == {"plots_only"}:
            plot_experiments = ["main_grid", "migrant_sweep", "sharing_sweep"]

        if "main_grid" in plot_experiments:
            for cmd in main_grid_plot_commands():
                run_command(cmd, args.dry_run)
        if "migrant_sweep" in plot_experiments:
            run_command(migrant_sweep_plot_command(), args.dry_run)
        if "sharing_sweep" in plot_experiments:
            run_command(sharing_sweep_plot_command(), args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
