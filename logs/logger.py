"""
Per-round, per-cluster logging. Writes metrics.csv (long format), metrics.json,
and a migration log. Computes before/after-migration variance stats at finalize.
"""

import csv
import json
import os
from datetime import datetime
from typing import Dict, List

from metrics.variance import rolling_std, before_after_stats, between_cluster_variance


class ClusterLogger:
    def __init__(self, experiment_name: str, save_path: str, num_clusters: int,
                 variance_window: int, config_dict: dict = None):
        self.num_clusters = num_clusters
        self.variance_window = variance_window
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.run_dir = os.path.join(save_path, f"{experiment_name}_{self.timestamp}")
        os.makedirs(self.run_dir, exist_ok=True)

        self.history = {
            "rounds": [],
            "cluster_test_acc": {c: [] for c in range(num_clusters)},
            "global_test_acc": {c: [] for c in range(num_clusters)},
            "train_acc": {c: [] for c in range(num_clusters)},
            "cluster_sizes": {c: [] for c in range(num_clusters)},
            "weight_shift": [],        # list of {round, {cluster: l2}}
            "migrations": [],          # flat list of executed migration records
        }

        if config_dict is not None:
            with open(os.path.join(self.run_dir, "config.json"), "w") as f:
                json.dump(config_dict, f, indent=2)

        # Keep the CSV handle open for the whole run (avoids per-round reopen,
        # which can hit transient Windows file locks from AV scanners).
        self.csv_path = os.path.join(self.run_dir, "metrics.csv")
        self._csv = open(self.csv_path, "w", newline="")
        self._writer = csv.writer(self._csv)
        self._writer.writerow(
            ["round", "cluster", "cluster_test_acc", "global_test_acc",
             "train_acc", "cluster_size"])
        self._csv.flush()
        print(f"Logger initialised: {self.run_dir}")

    def log_round(self, round_num, cluster_test_acc, global_test_acc, train_acc,
                  weight_shift, migrations, cluster_sizes):
        self.history["rounds"].append(round_num)
        for c in range(self.num_clusters):
            self.history["cluster_test_acc"][c].append(cluster_test_acc.get(c, float("nan")))
            self.history["global_test_acc"][c].append(global_test_acc.get(c, float("nan")))
            self.history["train_acc"][c].append(train_acc.get(c, float("nan")))
            self.history["cluster_sizes"][c].append(cluster_sizes.get(c, 0))
        if weight_shift:
            self.history["weight_shift"].append({"round": round_num, "shift": weight_shift})
        if migrations:
            self.history["migrations"].extend(migrations)

        for c in range(self.num_clusters):
            self._writer.writerow([round_num, c,
                                   cluster_test_acc.get(c, ""),
                                   global_test_acc.get(c, ""),
                                   train_acc.get(c, ""),
                                   cluster_sizes.get(c, 0)])
        self._csv.flush()

    def _compute_analysis(self) -> dict:
        rounds = self.history["rounds"]
        analysis = {"rolling_std": {}, "migration_impact": [],
                    "between_cluster_variance": between_cluster_variance(
                        self.history["cluster_test_acc"])}
        for c in range(self.num_clusters):
            series = self.history["cluster_test_acc"][c]
            analysis["rolling_std"][c] = rolling_std(series, self.variance_window)

        analysis["migration_impact_global"] = []
        migration_rounds = sorted({m["round"] for m in self.history["migrations"]})
        for mr in migration_rounds:
            affected = {m["dst"] for m in self.history["migrations"] if m["round"] == mr} | \
                       {m["src"] for m in self.history["migrations"] if m["round"] == mr}
            for c in affected:
                stats = before_after_stats(rounds, self.history["cluster_test_acc"][c],
                                           mr, self.variance_window)
                stats["cluster"] = c
                analysis["migration_impact"].append(stats)
                gstats = before_after_stats(rounds, self.history["global_test_acc"][c],
                                            mr, self.variance_window)
                gstats["cluster"] = c
                analysis["migration_impact_global"].append(gstats)
        return analysis

    def finalize(self) -> dict:
        try:
            self._csv.close()
        except Exception:
            pass
        analysis = self._compute_analysis()
        with open(os.path.join(self.run_dir, "metrics.json"), "w") as f:
            json.dump(self.history, f, indent=2)
        with open(os.path.join(self.run_dir, "analysis.json"), "w") as f:
            json.dump(analysis, f, indent=2)

        print("\n" + "=" * 60)
        print("Migration impact (cluster test accuracy)")
        print("=" * 60)
        for s in analysis["migration_impact"]:
            print(f"  Cluster {s['cluster']} @ round {s['migration_round']}: "
                  f"before_mean={s['before_mean']:.2f} after_min_drop={s['max_drop']:.2f} "
                  f"std {s['before_std']:.2f}->{s['after_std']:.2f} "
                  f"recovery={s['recovery_time']} rounds")
        print(f"\nResults saved to: {self.run_dir}")
        return analysis
