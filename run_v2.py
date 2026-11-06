"""
Corrected experiment runner (v2): one process per atomic run, parallel workers,
and resume that can never reuse a different experiment.

What changed relative to run_grid.py / the sweep scripts
--------------------------------------------------------
* Every run folder name contains every setting that defines the run (dataset,
  model, K, M, migrants, migration round, sub-mode, handover, case, beta,
  interval, rounds, seed). The full job spec is also hashed; --resume skips a
  folder only when COMPLETE.json carries the same hash.
* Handover baseline: each migrating run exists with handover=keep_weights and
  handover=adopt_destination.
* No-migration controls (sub-mode "control") use the same partition and the
  same nominal schedule for analysis, but nobody migrates.
* data_changes migrants receive held-back, disjoint data (reserve_for_migrants),
  never residents' examples.
* K=10 (one class per cluster) is replaced by K=5 (two classes per cluster).
* Pre-mix accuracy, recovery/relapse fields and arrival distances are logged
  by the core code (see trainer.py / logger.py / variance.py).

Usage
-----
    python run_v2.py --plan all --dry-run            # list the jobs
    python run_v2.py --plan all --workers 4 --resume # run everything
    python run_v2.py --plan main --filter CIFAR10 --workers 3 --resume
    python run_v2.py --plan all --shard 0/2 ...      # split across 2 GPUs/machines
    python run_v2.py --benchmark                      # time one job per dataset
    python run_v2.py --collect                        # build results_v2/summary_long.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent
DEFAULT_OUT = ROOT / "results_v2"
CODE_VERSION = "v2.0"

DATASETS = ["CIFAR-10", "F-MNIST", "MNIST"]   # CIFAR first: longest jobs start early
CLUSTERS = [2, 5]
CLIENTS_PER_CLUSTER = list(range(3, 11))
SEEDS = [42, 43, 44]
SUBMODES = ["membership_only", "data_changes"]
HANDOVERS = ["keep_weights", "adopt_destination"]
CASES = [("caseA", False), ("caseB", True)]
DEFAULT_BETA = 0.9
DEFAULT_INTERVAL = 5
DEFAULT_MIGRATION_ROUND = 40
ROUNDS = 60


@dataclass(frozen=True)
class Job:
    plan: str
    dataset: str
    model: str
    num_clusters: int
    clients_per_cluster: int
    num_migrants: int
    migration_round: int
    submode: str            # membership_only | data_changes | control
    handover: str           # keep_weights | adopt_destination | none (control)
    case: str               # caseA | caseB
    beta: float
    interval: int
    rounds: int
    seed: int

    @property
    def sharing(self) -> bool:
        return self.case == "caseB"

    @property
    def is_control(self) -> bool:
        return self.submode == "control"

    @property
    def key(self) -> str:
        ds = self.dataset.replace("-", "")
        b = f"{self.beta:g}".replace(".", "p")
        return (f"{ds}_{self.model}_K{self.num_clusters}_M{self.clients_per_cluster}"
                f"_q{self.num_migrants}_r{self.migration_round}_{self.submode}"
                f"_{self.handover}_{self.case}_b{b}_i{self.interval}"
                f"_R{self.rounds}_s{self.seed}")

    def spec(self) -> dict:
        d = asdict(self)
        d["code_version"] = CODE_VERSION
        d["reserve_for_migrants"] = True
        return d

    @property
    def hash(self) -> str:
        ident = {k: v for k, v in self.spec().items() if k != "plan"}  # plan is only a label
        blob = json.dumps(ident, sort_keys=True).encode()
        return hashlib.sha256(blob).hexdigest()[:16]

    def schedule(self) -> List[dict]:
        return [{"round": self.migration_round, "clients": list(range(self.num_migrants)),
                 "src": 0, "dst": self.num_clusters - 1}]


def _migrating_and_control(plan, dataset, K, M, q, seed, mround=DEFAULT_MIGRATION_ROUND,
                           beta=DEFAULT_BETA, cases=CASES, submodes=SUBMODES,
                           handovers=HANDOVERS, controls=True) -> List[Job]:
    jobs = []
    for case, _ in cases:
        for sub in submodes:
            for h in handovers:
                jobs.append(Job(plan, dataset, "CNN", K, M, q, mround, sub, h, case,
                                beta, DEFAULT_INTERVAL, ROUNDS, seed))
        if controls:
            jobs.append(Job(plan, dataset, "CNN", K, M, q, mround, "control", "none", case,
                            beta, DEFAULT_INTERVAL, ROUNDS, seed))
    return jobs


def plan_main() -> List[Job]:
    jobs = []
    for ds in DATASETS:
        for K in CLUSTERS:
            for M in CLIENTS_PER_CLUSTER:
                q = min(3, M - 1)
                for s in SEEDS:
                    jobs += _migrating_and_control("main", ds, K, M, q, s)
    return jobs


def plan_sweeps() -> List[Job]:
    """CIFAR-10 CNN, K=2, M=10 sweeps (data_changes, keep_weights) + timing check."""
    jobs = []
    ds, K, M = "CIFAR-10", 2, 10
    for s in SEEDS:
        # migrant-count sweep, both cases, with a matched control per q
        for q in range(1, M):
            jobs += _migrating_and_control("migrant_sweep", ds, K, M, q, s,
                                           submodes=["data_changes"],
                                           handovers=["keep_weights"])
        # sharing-percentage sweep (Case B only; Case A comes from q=5 above)
        for pct in [5, 10, 20, 30, 40, 50]:
            beta = round(1.0 - pct / 100.0, 4)
            jobs += _migrating_and_control("sharing_sweep", ds, K, M, 5, s, beta=beta,
                                           cases=[("caseB", True)],
                                           submodes=["data_changes"],
                                           handovers=["keep_weights"])
        # timing check: migrate at round 42 (not a mixing round)
        jobs += _migrating_and_control("timing", ds, K, M, 3, s, mround=42,
                                       handovers=["keep_weights"])
    return jobs


def build_jobs(plan: str) -> List[Job]:
    if plan == "main":
        jobs = plan_main()
    elif plan == "sweeps":
        jobs = plan_sweeps()
    else:
        jobs = plan_main() + plan_sweeps()
    # Dedupe on run identity (the plan label is not part of the identity).
    seen, out = set(), []
    for j in jobs:
        if j.key not in seen:
            seen.add(j.key)
            out.append(j)
    return out


# --------------------------------------------------------------------------- #
# single job (runs in its own process so the global config never leaks)
# --------------------------------------------------------------------------- #
def run_single(job: Job, out_root: Path) -> None:
    from config_loader import config
    from main import build_and_run

    job_dir = out_root / job.key
    job_dir.mkdir(parents=True, exist_ok=True)
    (job_dir / "job.json").write_text(json.dumps({**job.spec(), "hash": job.hash}, indent=2))

    c = config._config
    c["data"]["dataset"] = job.dataset
    c["data"]["data_path"] = str(ROOT / "data" / "datasets")
    c["model"]["architecture"] = job.model
    c["training"]["global_rounds"] = job.rounds
    c["clustered"]["num_clusters"] = job.num_clusters
    c["clustered"]["total_clients"] = job.num_clusters * job.clients_per_cluster
    c["clustered"]["sharing"]["enabled"] = job.sharing
    c["clustered"]["sharing"]["beta"] = job.beta
    c["clustered"]["sharing"]["interval"] = job.interval
    mig = c["clustered"]["migration"]
    mig["schedule"] = job.schedule()
    mig["behavior_change"] = "membership_only" if job.is_control else job.submode
    mig["handover"] = "keep_weights" if job.is_control else job.handover
    mig["reserve_for_migrants"] = True
    mig["control"] = job.is_control
    c["experiment"]["seed"] = job.seed
    c["experiment"]["name"] = "run"
    c["logging"]["save_path"] = str(job_dir)
    c["logging"]["verbose"] = False
    c["plotting"]["enabled"] = False

    t0 = time.time()
    res = build_and_run(sharing_enabled=job.sharing, experiment_name="run", do_plots=False)
    elapsed = time.time() - t0
    (job_dir / "COMPLETE.json").write_text(json.dumps({
        "hash": job.hash, "key": job.key, "run_dir": str(Path(res["run_dir"]).relative_to(job_dir)),
        "seconds": round(elapsed, 1), "finished": datetime.now().isoformat(timespec="seconds"),
    }, indent=2))


def is_complete(job: Job, out_root: Path) -> bool:
    marker = out_root / job.key / "COMPLETE.json"
    if not marker.exists():
        return False
    try:
        return json.loads(marker.read_text()).get("hash") == job.hash
    except Exception:
        return False


def clear_partial(job: Job, out_root: Path) -> None:
    """Move an incomplete/mismatched folder aside (never delete results)."""
    d = out_root / job.key
    if d.exists():
        stale = out_root / "_stale" / f"{job.key}_{datetime.now():%Y%m%d_%H%M%S}"
        stale.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(d), str(stale))


# --------------------------------------------------------------------------- #
# parallel launcher
# --------------------------------------------------------------------------- #
def launch(jobs: List[Job], out_root: Path, workers: int, resume: bool) -> int:
    out_root.mkdir(parents=True, exist_ok=True)
    todo = []
    for j in jobs:
        if resume and is_complete(j, out_root):
            continue
        clear_partial(j, out_root)
        todo.append(j)
    print(f"jobs: {len(jobs)} | already complete: {len(jobs) - len(todo)} | to run: {len(todo)}"
          f" | workers: {workers}", flush=True)
    if not todo:
        return 0

    running: Dict[subprocess.Popen, tuple] = {}
    queue = list(todo)
    done = failed = 0
    t_start = time.time()
    fail_log = out_root / "failed_jobs.txt"
    env = dict(os.environ, PYTHONUNBUFFERED="1")
    while queue or running:
        while queue and len(running) < workers:
            j = queue.pop(0)
            (out_root / j.key).mkdir(parents=True, exist_ok=True)
            log = open(out_root / j.key / "stdout.log", "w")
            p = subprocess.Popen(
                [sys.executable, str(ROOT / "run_v2.py"), "--run-key", j.key,
                 "--plan", "all", "--out", str(out_root), "--rounds", str(j.rounds)],
                cwd=str(ROOT), stdout=log, stderr=subprocess.STDOUT, env=env)
            running[p] = (j, log, time.time())
        time.sleep(1.0)
        for p in [p for p in running if p.poll() is not None]:
            j, log, t0 = running.pop(p)
            log.close()
            ok = p.returncode == 0 and is_complete(j, out_root)
            if ok:
                done += 1
            else:
                failed += 1
                with open(fail_log, "a") as f:
                    f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\t{j.key}\trc={p.returncode}\n")
            finished = done + failed
            rate = (time.time() - t_start) / finished
            eta_h = rate * (len(todo) - finished) / 3600
            print(f"[{finished}/{len(todo)}] {'ok  ' if ok else 'FAIL'} {j.key} "
                  f"({time.time() - t0:.0f}s) | eta {eta_h:.2f} h", flush=True)
    print(f"finished: {done} ok, {failed} failed ({(time.time() - t_start) / 3600:.2f} h)")
    if failed:
        print(f"see {fail_log} and each job's stdout.log; rerun with --resume to retry")
    return 1 if failed else 0


# --------------------------------------------------------------------------- #
# collect results into one tidy CSV
# --------------------------------------------------------------------------- #
STAT_FIELDS = ["before_mean", "after_mean", "before_std", "after_std", "max_drop",
               "recovery_time", "recovered", "relapsed", "rounds_below_after_recovery",
               "rounds_below_threshold", "final_mean", "final_minus_before"]


def collect(out_root: Path) -> None:
    rows = []
    for marker in sorted(out_root.glob("*/COMPLETE.json")):
        job_dir = marker.parent
        spec = json.loads((job_dir / "job.json").read_text())
        run_dir = job_dir / json.loads(marker.read_text())["run_dir"]
        analysis = json.loads((run_dir / "analysis.json").read_text())
        metrics = json.loads((run_dir / "metrics.json").read_text())
        dst = spec["num_clusters"] - 1
        arrival = [m.get("arrival_l2_to_dst") for m in metrics.get("migrations", [])]
        for family in ["migration_impact", "migration_impact_premix", "migration_impact_global"]:
            for st in analysis.get(family, []):
                c = int(st["cluster"])
                row = {k: spec[k] for k in spec if k not in ("code_version",)}
                row.update({"key": job_dir.name, "family": family, "cluster": c,
                            "role": "dst" if c == dst else ("src" if c == 0 else "other"),
                            "mean_arrival_l2": (sum(arrival) / len(arrival)) if arrival else ""})
                for f in STAT_FIELDS:
                    row[f] = st.get(f)
                rows.append(row)
    if not rows:
        print("no complete jobs found")
        return
    path = out_root / "summary_long.csv"
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows from {len({r['key'] for r in rows})} jobs)")


# --------------------------------------------------------------------------- #
def parse_args():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", choices=["main", "sweeps", "all"], default="all")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--filter", nargs="+", default=None,
                    help="keep jobs whose key contains ALL of these substrings")
    ap.add_argument("--shard", default=None, help="i/n: run every n-th job starting at i")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--rounds", type=int, default=None, help="override rounds (smoke tests only)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--benchmark", action="store_true",
                    help="run one data_changes caseB job per dataset into results_bench/")
    ap.add_argument("--collect", action="store_true")
    ap.add_argument("--run-key", default=None, help=argparse.SUPPRESS)
    return ap.parse_args()


def main():
    global ROUNDS
    args = parse_args()
    if args.rounds:
        ROUNDS = args.rounds
    out_root = Path(args.out)
    if args.collect:
        collect(out_root)
        return

    jobs = build_jobs(args.plan)
    if args.run_key:
        match = [j for j in jobs if j.key == args.run_key]
        if not match:
            sys.exit(f"unknown job key {args.run_key}")
        run_single(match[0], out_root)
        return

    if args.benchmark:
        out_root = ROOT / "results_bench"
        jobs = [j for j in jobs if j.plan == "main" and j.num_clusters == 2
                and j.clients_per_cluster == 10 and j.seed == 42 and j.case == "caseB"
                and j.submode == "data_changes" and j.handover == "keep_weights"]
    if args.filter:
        jobs = [j for j in jobs if all(f in j.key for f in args.filter)]
    if args.shard:
        i, n = map(int, args.shard.split("/"))
        jobs = jobs[i::n]
    if args.limit:
        jobs = jobs[:args.limit]

    if args.dry_run:
        by_plan: Dict[str, int] = {}
        for j in jobs:
            by_plan[f"{j.plan}/{j.dataset}"] = by_plan.get(f"{j.plan}/{j.dataset}", 0) + 1
        for j in jobs[:10]:
            print(j.key)
        if len(jobs) > 10:
            print(f"... ({len(jobs) - 10} more)")
        for k, v in sorted(by_plan.items()):
            print(f"  {k}: {v}")
        print(f"total jobs: {len(jobs)}")
        return

    sys.exit(launch(jobs, out_root, max(1, args.workers), args.resume))


if __name__ == "__main__":
    main()
