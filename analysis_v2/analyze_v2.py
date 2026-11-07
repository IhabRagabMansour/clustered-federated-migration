"""
Analysis of results_v2/summary_long.csv (v2 run, 1584 CNN jobs).

Run from the project folder:  python analysis_v2/analyze_v2.py
Writes tables (CSV + one markdown file) and figures into analysis_v2/.

Definitions (10-round windows around the migration round R):
  dip      = before_mean - after_mean   (mean accuracy lost in rounds R..R+9; >0 = worse)
  max_drop = before_mean - min(after)   (worst single round)
  below    = rounds in R..59 more than 1 point under before_mean
  final    = mean(last 10 rounds) - before_mean
  excess_X = X(migration run) - X(matched no-migration control), matched on
             dataset, K, M, q, migration round, case, beta, seed, cluster role.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "results_v2", "summary_long.csv")
OUT = HERE

MATCH = ["plan", "dataset", "num_clusters", "clients_per_cluster", "num_migrants",
         "migration_round", "case", "beta", "seed", "family", "role"]
METRICS = ["dip", "max_drop", "rounds_below_threshold", "final_minus_before"]


def load():
    d = pd.read_csv(SRC)
    d["dip"] = d["before_mean"] - d["after_mean"]
    d["sharing"] = np.where(d["case"] == "caseA", 0.0, 1 - d["beta"]).round(2)
    ctrl = d[d.submode == "control"][MATCH + METRICS + ["after_std"]]
    ctrl = ctrl.rename(columns={m: f"ctrl_{m}" for m in METRICS + ["after_std"]})
    t = d[d.submode != "control"].merge(ctrl, on=MATCH, how="left", validate="many_to_one")
    assert t["ctrl_dip"].notna().all(), "some runs have no matched control"
    for m in METRICS + ["after_std"]:
        t[f"ex_{m}"] = t[m] - t[f"ctrl_{m}"]
    return d, t


def sem(x):
    x = np.asarray(x, float)
    return x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else np.nan


def agg(df, by, cols):
    g = df.groupby(by)
    out = g[cols].mean()
    for c in cols:
        out[c + "_se"] = g[c].apply(sem)
    out["n"] = g.size()
    if "recovered" in df:
        out["never_recovered_%"] = 100 * (1 - g["recovered"].mean())
    return out.round(3)


def main():
    d, t = load()
    md = []

    def section(title, frame, note=""):
        md.append(f"\n## {title}\n")
        if note:
            md.append(note + "\n")
        md.append(frame.to_markdown())
        md.append("")

    main_ = t[t.plan == "main"]
    cols = ["dip", "ex_dip", "max_drop", "ex_max_drop", "rounds_below_threshold",
            "ex_rounds_below_threshold", "ex_final_minus_before", "ex_after_std"]

    # 1. Headline: destination cluster, cluster-test acc (post-mix), per dataset/K/submode/handover/case
    dst = main_[(main_.role == "dst") & (main_.family == "migration_impact")]
    tab1 = agg(dst, ["dataset", "num_clusters", "submode", "handover", "case"], cols)
    tab1.to_csv(os.path.join(OUT, "t1_dst_main.csv"))
    section("1. Destination cluster, main grid (mean over M=3..10 and 3 seeds)",
            tab1[["dip", "ex_dip", "ex_dip_se", "ex_max_drop", "ex_rounds_below_threshold",
                  "ex_final_minus_before", "never_recovered_%", "n"]])

    # 1b. source cluster
    src = main_[(main_.role == "src") & (main_.family == "migration_impact")]
    tab1b = agg(src, ["dataset", "num_clusters", "submode", "handover", "case"], cols)
    tab1b.to_csv(os.path.join(OUT, "t1b_src_main.csv"))
    section("1b. Source cluster, main grid",
            tab1b[["ex_dip", "ex_dip_se", "ex_max_drop", "ex_final_minus_before", "n"]])

    # 2. Paired Case B - Case A on control-adjusted dip (dst, post-mix and pre-mix)
    rows = []
    for fam in ["migration_impact", "migration_impact_premix", "migration_impact_global"]:
        x = main_[(main_.role == "dst") & (main_.family == fam)]
        key = ["dataset", "num_clusters", "clients_per_cluster", "seed", "submode", "handover"]
        p = x.pivot_table(index=key, columns="case", values="ex_dip")
        p["diff"] = p["caseB"] - p["caseA"]
        g = p.reset_index().groupby(["dataset", "num_clusters", "submode", "handover"])
        r = pd.DataFrame({"A_ex_dip": g["caseA"].mean(), "B_ex_dip": g["caseB"].mean(),
                          "B_minus_A": g["diff"].mean(), "se": g["diff"].apply(sem),
                          "B_better_%": g["diff"].apply(lambda s: 100 * (s < 0).mean()),
                          "n": g.size()})
        r["family"] = fam
        rows.append(r.reset_index())
    tab2 = pd.concat(rows).set_index(["family", "dataset", "num_clusters", "submode", "handover"]).round(3)
    tab2.to_csv(os.path.join(OUT, "t2_caseB_minus_caseA.csv"))
    section("2. Case B minus Case A, control-adjusted dip of the destination (paired by M, seed)",
            tab2, "Negative B_minus_A = sharing reduces the migration dip. "
                  "migration_impact = after mixing (as in v1); _premix = before mixing; _global = global test set.")

    # 3. Handover: keep_weights - adopt_destination
    x = dst.pivot_table(index=["dataset", "num_clusters", "clients_per_cluster", "seed", "submode", "case"],
                        columns="handover", values="ex_dip")
    x["keep_minus_adopt"] = x["keep_weights"] - x["adopt_destination"]
    g = x.reset_index().groupby(["dataset", "num_clusters", "submode", "case"])
    tab3 = pd.DataFrame({"keep": g["keep_weights"].mean(), "adopt": g["adopt_destination"].mean(),
                         "keep_minus_adopt": g["keep_minus_adopt"].mean(),
                         "se": g["keep_minus_adopt"].apply(sem), "n": g.size()}).round(3)
    tab3.to_csv(os.path.join(OUT, "t3_handover.csv"))
    section("3. Handover: control-adjusted dst dip, keep_weights vs adopt_destination", tab3,
            "Positive keep_minus_adopt = injecting the migrant's own weights costs extra accuracy.")

    # 4. Controls: how much do clusters move without migration? (pre vs post mix)
    c = d[(d.plan == "main") & (d.submode == "control")]
    tab4 = c.groupby(["dataset", "num_clusters", "case", "family", "role"])[
        ["before_mean", "dip", "max_drop", "after_std"]].mean().round(3)
    tab4.to_csv(os.path.join(OUT, "t4_controls.csv"))
    section("4. No-migration controls (what the window statistics show with nobody moving)", tab4)

    # 5. Dependence on M (CIFAR-10, data_changes keep_weights, dst)
    x = dst[(dst.submode == "data_changes") & (dst.handover == "keep_weights")]
    tab5 = x.pivot_table(index=["dataset", "num_clusters", "clients_per_cluster"], columns="case",
                         values="ex_dip").round(3)
    tab5.to_csv(os.path.join(OUT, "t5_by_M.csv"))
    section("5. Control-adjusted dst dip by cluster size M (data_changes, keep_weights)", tab5)

    # 6. Migrant sweep (CIFAR-10, K=2, M=10, data_changes keep_weights); q=3 from main grid
    ms = t[((t.plan == "migrant_sweep") |
            ((t.plan == "main") & (t.dataset == "CIFAR-10") & (t.num_clusters == 2) &
             (t.clients_per_cluster == 10) & (t.submode == "data_changes") &
             (t.handover == "keep_weights"))) & (t.family == "migration_impact")]
    tab6 = ms.pivot_table(index="num_migrants", columns=["role", "case"], values="ex_dip").round(3)
    tab6.to_csv(os.path.join(OUT, "t6_migrant_sweep.csv"))
    section("6. Migrant sweep: control-adjusted dip vs number of migrants q (CIFAR-10, K=2, M=10)", tab6)

    # 7. Sharing sweep (q=5); 0% and 10% from the migrant sweep at q=5
    ss = t[((t.plan == "sharing_sweep") | ((t.plan == "migrant_sweep") & (t.num_migrants == 5)))]
    tab7 = ss.pivot_table(index="sharing", columns=["family", "role"], values="ex_dip").round(3)
    raw7 = ss[ss.family == "migration_impact"].pivot_table(
        index="sharing", columns="role", values=["before_mean", "dip", "ctrl_dip"]).round(3)
    tab7.to_csv(os.path.join(OUT, "t7_sharing_sweep.csv"))
    section("7. Sharing sweep: control-adjusted dip vs sharing 1-beta (CIFAR-10, K=2, M=10, q=5)", tab7)
    section("7b. Sharing sweep, raw values (before-mean, raw dip, control dip)", raw7)

    # 8. Timing: migration at round 42 (off the mixing grid) vs round 40
    tm = t[((t.plan == "timing") |
            ((t.plan == "main") & (t.dataset == "CIFAR-10") & (t.num_clusters == 2) &
             (t.clients_per_cluster == 10) & (t.handover == "keep_weights"))) &
           (t.role == "dst")]
    tab8 = tm.pivot_table(index=["submode", "family", "migration_round"], columns="case",
                          values=["ex_dip", "ex_max_drop"]).round(3)
    tab8.to_csv(os.path.join(OUT, "t8_timing.csv"))
    section("8. Timing: migration at round 40 (= mixing round) vs 42 (CIFAR-10, K=2, M=10, keep_weights, dst)", tab8)

    # 9. Global test accuracy level (all main runs), last 10 rounds
    gl = d[(d.plan == "main") & (d.family == "migration_impact_global") & (d.role == "dst")]
    tab9 = gl.groupby(["dataset", "num_clusters", "case"])[["final_mean"]].mean().round(2)
    tab9.to_csv(os.path.join(OUT, "t9_global_level.csv"))
    section("9. Global test accuracy, mean of last 10 rounds", tab9)

    with open(os.path.join(OUT, "tables.md"), "w", encoding="utf-8") as f:
        f.write("# v2 analysis tables\n" + __doc__ + "\n".join(md))

    figures(d, t, dst)
    print("wrote", OUT)


def figures(d, t, dst):
    # F1: control-adjusted dst dip, A vs B, per dataset/K/submode (keep_weights)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, sub in zip(axes, ["membership_only", "data_changes"]):
        x = dst[(dst.submode == sub)]
        g = x.groupby(["dataset", "num_clusters", "handover", "case"])["ex_dip"].agg(["mean", sem]).reset_index()
        labels = sorted({(r.dataset, r.num_clusters) for r in g.itertuples()})
        xs = np.arange(len(labels))
        w = 0.2
        for i, (h, cse) in enumerate([("keep_weights", "caseA"), ("keep_weights", "caseB"),
                                      ("adopt_destination", "caseA"), ("adopt_destination", "caseB")]):
            vals = [g[(g.dataset == a) & (g.num_clusters == k) & (g.handover == h) & (g.case == cse)]
                    for a, k in labels]
            m = [v["mean"].iloc[0] for v in vals]
            e = [v["sem"].iloc[0] for v in vals]
            ax.bar(xs + (i - 1.5) * w, m, w, yerr=e, capsize=2,
                   label=f"{'keep' if h == 'keep_weights' else 'adopt'} / {'A' if cse == 'caseA' else 'B'}",
                   hatch="" if h == "keep_weights" else "//",
                   color="#4C72B0" if cse == "caseA" else "#DD8452")
        ax.set_xticks(xs)
        ax.set_xticklabels([f"{a}\nK={k}" for a, k in labels], fontsize=8)
        ax.axhline(0, color="k", lw=0.6)
        ax.set_title(sub)
        ax.set_ylabel("dst dip minus control dip (acc. points)")
    axes[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "f1_dst_excess_dip.png"), dpi=150)
    plt.close(fig)

    # F2: sharing sweep
    ss = t[((t.plan == "sharing_sweep") | ((t.plan == "migrant_sweep") & (t.num_migrants == 5))) &
           (t.role == "dst")]
    fig, ax = plt.subplots(figsize=(5.5, 4))
    for fam, lab in [("migration_impact", "post-mix"), ("migration_impact_premix", "pre-mix"),
                     ("migration_impact_global", "global test")]:
        g = ss[ss.family == fam].groupby("sharing")["ex_dip"].agg(["mean", sem])
        ax.errorbar(g.index * 100, g["mean"], yerr=g["sem"], marker="o", capsize=3, label=lab)
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xlabel("sharing 1-beta (%)")
    ax.set_ylabel("dst dip minus control dip")
    ax.set_title("Sharing sweep (CIFAR-10, K=2, M=10, q=5)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "f2_sharing_sweep.png"), dpi=150)
    plt.close(fig)

    # F3: migrant sweep
    ms = t[((t.plan == "migrant_sweep") |
            ((t.plan == "main") & (t.dataset == "CIFAR-10") & (t.num_clusters == 2) &
             (t.clients_per_cluster == 10) & (t.submode == "data_changes") &
             (t.handover == "keep_weights"))) & (t.family == "migration_impact")]
    fig, ax = plt.subplots(figsize=(5.5, 4))
    for role in ["dst", "src"]:
        for cse in ["caseA", "caseB"]:
            g = ms[(ms.role == role) & (ms.case == cse)].groupby("num_migrants")["ex_dip"].agg(["mean", sem])
            ax.errorbar(g.index, g["mean"], yerr=g["sem"], marker="o" if role == "dst" else "s",
                        ls="-" if cse == "caseA" else "--", capsize=3, label=f"{role} {cse}")
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xlabel("migrants q (of M=10)")
    ax.set_ylabel("dip minus control dip")
    ax.set_title("Migrant sweep (CIFAR-10, K=2, M=10)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "f3_migrant_sweep.png"), dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
