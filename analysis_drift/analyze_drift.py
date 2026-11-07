"""
Analysis of the gradual-drift plan (results_drift/summary_drift.csv).

Run from the project folder:
    python run_v2.py --plan drift --collect
    python analysis_drift/analyze_drift.py [results_drift]

All accuracies are averaged over rounds >= drift start (30) unless named *_last10.
  src_after / dst_after         cluster-test accuracy of source / destination cluster
  mig_client_after              accuracy the drifting clients get on test data that
                                matches their CURRENT class mix (their "service")
  srcres_/dstres_client_after   same for the residents of each cluster
  *_ex                          minus the matched no-drift control (same M, case, seed)
  mig_gap                       mig_client_after - dstres_client_after (0 = drifting
                                clients served as well as the destination's residents)
"""

import glob
import json
import os
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
RES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "results_drift")
OUT = sys.argv[2] if len(sys.argv) > 2 else HERE

MATCH = ["clients_per_cluster", "case", "seed"]
CLUSTER_COLS = ["src_after", "dst_after", "src_min_after", "dst_min_after",
                "srcres_client_after", "dstres_client_after"]


def sem(x):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    return x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else np.nan


def load():
    d = pd.read_csv(os.path.join(RES, "summary_drift.csv"))
    ctrl = d[d.submode == "control"][MATCH + CLUSTER_COLS].rename(
        columns={c: f"ctrl_{c}" for c in CLUSTER_COLS})
    t = d[d.submode == "drift"].merge(ctrl, on=MATCH, how="left", validate="many_to_one")
    for c in CLUSTER_COLS:
        t[f"{c}_ex"] = t[c] - t[f"ctrl_{c}"]
    t["mig_gap"] = t["mig_client_after"] - t["dstres_client_after"]
    t["arm"] = np.where(t.policy == "never", "never",
                        t.policy + "/" + t.handover.str.replace("_weights", "").str.replace(
                            "adopt_destination", "adopt"))
    return d, t


def main():
    d, t = load()
    md = ["# Gradual-drift tables\n", __doc__]

    cols = ["mig_client_after", "mig_client_min_after", "mig_gap",
            "src_after_ex", "dst_after_ex", "dst_min_after_ex", "srcres_client_after_ex",
            "mean_move_round", "mean_move_p", "n_drifting_moved", "false_switches"]
    g = t.groupby(["clients_per_cluster", "drift_duration", "arm", "case"])
    tab = g[cols].mean().round(2)
    tab["mig_se"] = g["mig_client_after"].apply(sem).round(2)
    tab["n"] = g.size()
    tab.to_csv(os.path.join(OUT, "drift_table.csv"))
    md += ["\n## All arms (mean over seeds)\n", tab.to_markdown(), ""]

    # Case B - Case A, paired by M, D, arm, seed
    if set(t.case) >= {"caseA", "caseB"}:
        vals = ["mig_client_after", "dst_after_ex", "src_after_ex", "mean_move_round"]
        p = t.pivot_table(index=["clients_per_cluster", "drift_duration", "arm", "seed"],
                          columns="case", values=vals)
        diff = pd.DataFrame({f"{v}_B-A": p[(v, "caseB")] - p[(v, "caseA")] for v in vals})
        tab2 = diff.groupby(level=[0, 1, 2]).mean().round(2)
        tab2.to_csv(os.path.join(OUT, "drift_caseB_minus_caseA.csv"))
        md += ["\n## Case B minus Case A (paired by seed)\n", tab2.to_markdown(), ""]

    with open(os.path.join(OUT, "drift_tables.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    fig_service(t)
    fig_trajectories(M=int(t.clients_per_cluster.max()))
    print("wrote", OUT)


def fig_service(t):
    Ms = sorted(t.clients_per_cluster.unique())
    fig, axes = plt.subplots(len(Ms), 2, figsize=(11, 3.8 * len(Ms)), sharey=True, squeeze=False)
    arms = ["never", "fixed/keep", "fixed/adopt", "detected/keep", "detected/adopt"]
    for i, M in enumerate(Ms):
        for j, case in enumerate(["caseA", "caseB"]):
            ax = axes[i][j]
            for arm in arms:
                x = t[(t.clients_per_cluster == M) & (t.case == case) & (t.arm == arm)]
                if x.empty:
                    continue
                g = x.groupby("drift_duration")["mig_client_after"].agg(["mean", sem])
                ax.errorbar(g.index, g["mean"], yerr=g["sem"], marker="o", capsize=3, label=arm)
            ax.set_title(f"M={M}, {case}")
            ax.set_xlabel("drift duration D (rounds)")
            ax.set_ylabel("drifting clients' accuracy\n(rounds >= 30)")
    axes[0][0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fd1_drifting_client_accuracy.png"), dpi=150)
    plt.close(fig)


def fig_trajectories(M=10, D=10, case="caseA", seed=42):
    """Per-round accuracy of one drifting client, source and destination cluster."""
    arms = [("never", "none"), ("fixed", "keep_weights"), ("detected", "keep_weights"),
            ("detected", "adopt_destination")]
    fig, axes = plt.subplots(1, len(arms), figsize=(4.2 * len(arms), 3.6), sharey=True)
    found = False
    for ax, (pol, h) in zip(axes, arms):
        pat = os.path.join(RES, f"CIFAR10_CNN_K2_M{M}_q3_r30_drift_D{D}_{pol}_{h}_{case}_*s{seed}",
                           "run_*", "metrics.json")
        f = glob.glob(pat)
        if not f:
            continue
        found = True
        m = json.load(open(f[0]))
        r = m["rounds"]
        ax.plot(r, m["cluster_test_acc"]["0"], label="src cluster", lw=1)
        ax.plot(r, m["cluster_test_acc"]["1"], label="dst cluster", lw=1)
        ax.plot(r, m["client_acc"]["0"], label="drifting client 0", lw=1.6, color="k")
        moves = [x["round"] for x in m["migrations"] if x.get("client") == 0]
        for mv in moves:
            ax.axvline(mv, color="k", ls=":", lw=0.8)
        ax.axvspan(30, 30 + max(D, 1) - 1, color="grey", alpha=0.12)
        ax.set_title(f"{pol} / {h.split('_')[0]}")
        ax.set_xlabel("round")
    if found:
        axes[0].set_ylabel("accuracy (%)")
        axes[0].legend(fontsize=7)
        fig.suptitle(f"M={M}, D={D}, {case}, seed {seed} (grey = drift period, dotted = move)")
        fig.tight_layout()
        fig.savefig(os.path.join(OUT, "fd2_example_trajectories.png"), dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
