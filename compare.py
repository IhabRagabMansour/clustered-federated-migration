"""
Run Case A (isolated) and Case B (sharing) with the SAME seed, for BOTH
behaviour-change sub-modes (membership_only and data_changes). For each sub-mode
produce overlay figures for affected clusters + a summary table (markdown + CSV)
of migration impact on cluster-test AND global-test accuracy.

Run:  python compare.py
"""

import csv
import os
from datetime import datetime

from config_loader import config
from main import build_and_run
from plots.plot import plot_case_comparison, plot_between_variance_comparison

SUBMODES = ["membership_only", "data_changes"]


def _impact_lookup(analysis, cluster, key="migration_impact"):
    for s in analysis[key]:
        if s["cluster"] == cluster:
            return s
    return None


def run_submode(sub: str, out_root: str):
    config._config["clustered"]["migration"]["behavior_change"] = sub
    print("\n" + "#" * 70)
    print(f"# SUB-MODE: {sub}")
    print("#" * 70)

    res_a = build_and_run(sharing_enabled=False, experiment_name=f"caseA_{sub}", do_plots=False)
    res_b = build_and_run(sharing_enabled=True, experiment_name=f"caseB_{sub}", do_plots=False)

    rounds = res_a["history"]["rounds"]
    mrounds = res_a["migration_rounds"]
    affected = res_a["affected_clusters"]
    plot_dir = config.plotting.save_path

    for c in affected:
        plot_case_comparison(
            rounds, res_a["history"]["cluster_test_acc"][c], res_b["history"]["cluster_test_acc"][c],
            mrounds, c, f"[{sub}] Cluster {c} Test Accuracy - Case A vs B",
            plot_dir, f"compare_{sub}_cluster{c}_clusterTest.png")
        plot_case_comparison(
            rounds, res_a["history"]["global_test_acc"][c], res_b["history"]["global_test_acc"][c],
            mrounds, c, f"[{sub}] Cluster {c} GLOBAL Test Accuracy - Case A vs B",
            plot_dir, f"compare_{sub}_cluster{c}_globalTest.png")

    plot_between_variance_comparison(
        rounds, res_a["analysis"]["between_cluster_variance"], res_b["analysis"]["between_cluster_variance"],
        mrounds, f"[{sub}] Between-Cluster Variance - Case A vs B",
        plot_dir, f"compare_{sub}_between_variance.png")

    # Summary rows
    header = ["submode", "cluster", "metric", "Case A (isolated)", "Case B (sharing)"]
    rows = []
    for c in affected:
        sa = _impact_lookup(res_a["analysis"], c)
        sb = _impact_lookup(res_b["analysis"], c)
        ga = _impact_lookup(res_a["analysis"], c, "migration_impact_global")
        gb = _impact_lookup(res_b["analysis"], c, "migration_impact_global")
        if sa is None or sb is None:
            continue
        rows.append([sub, c, "clusterTest_before", f"{sa['before_mean']:.2f}", f"{sb['before_mean']:.2f}"])
        rows.append([sub, c, "clusterTest_maxDrop", f"{sa['max_drop']:.2f}", f"{sb['max_drop']:.2f}"])
        rows.append([sub, c, "clusterTest_afterStd", f"{sa['after_std']:.2f}", f"{sb['after_std']:.2f}"])
        rows.append([sub, c, "clusterTest_recovery", f"{sa['recovery_time']}", f"{sb['recovery_time']}"])
        if ga and gb:
            rows.append([sub, c, "globalTest_before", f"{ga['before_mean']:.2f}", f"{gb['before_mean']:.2f}"])
            rows.append([sub, c, "globalTest_maxDrop", f"{ga['max_drop']:.2f}", f"{gb['max_drop']:.2f}"])
            rows.append([sub, c, "globalTest_afterStd", f"{ga['after_std']:.2f}", f"{gb['after_std']:.2f}"])
    return header, rows


def main():
    print("=" * 70)
    print("COMPARISON: Case A vs Case B, both sub-modes")
    print("=" * 70)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(config.logging.save_path, f"comparison_{ts}")
    os.makedirs(out_dir, exist_ok=True)

    all_rows, header = [], None
    for sub in SUBMODES:
        header, rows = run_submode(sub, out_dir)
        all_rows.extend(rows)

    # CSV
    with open(os.path.join(out_dir, "comparison_summary.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(all_rows)
    # Markdown
    with open(os.path.join(out_dir, "comparison_summary.md"), "w") as f:
        f.write("# Case A vs Case B - Migration Impact (both sub-modes)\n\n")
        f.write(f"Dataset: {config.data.dataset} | clusters: {config.clustered.num_clusters} | "
                f"clients: {config.clustered.total_clients} | rounds: {config.training.global_rounds} | "
                f"beta: {config.clustered.sharing.beta} | interval: {config.clustered.sharing.interval}\n\n")
        f.write(f"Migration(s): {config.to_dict()['clustered']['migration']['schedule']}\n\n")
        f.write("| " + " | ".join(header) + " |\n")
        f.write("|" + "|".join(["---"] * len(header)) + "|\n")
        for r in all_rows:
            f.write("| " + " | ".join(str(x) for x in r) + " |\n")

    print("\n" + "=" * 70)
    print("SUMMARY (migration impact)")
    print("=" * 70)
    print(f"{'submode':>16} {'cl':>3} {'metric':>22} {'Case A':>12} {'Case B':>12}")
    for r in all_rows:
        print(f"{r[0]:>16} {r[1]:>3} {r[2]:>22} {r[3]:>12} {r[4]:>12}")
    print(f"\nSaved: {out_dir}")
    print(f"Figures: {config.plotting.save_path} (compare_*.png)")


if __name__ == "__main__":
    main()
