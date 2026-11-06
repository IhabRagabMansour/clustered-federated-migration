# Running the corrected experiments (v2) on vast.ai

All commands below run in **Git Bash on your PC**, from the project folder,
unless marked "on the instance".

## 1. Rent the instance (you, in the vast.ai web console)

- GPU: **1x RTX 5090**, on-demand (not interruptible), reliability >= 99%
- Template / image: a **PyTorch CUDA 12.8** image (torch >= 2.7). `setup.sh`
  installs a cu128 torch automatically if the image's torch can't drive the 5090.
- Disk: **40 GB**
- Launch, then copy the SSH command vast shows: `ssh -p PORT root@HOST`

## 2. Upload code + set up (about 5 minutes)

```bash
bash vast/deploy.sh HOST PORT
```

This uploads ~50 KB of code (no `.env`, no datasets, no old results, no paper),
installs packages, downloads MNIST / Fashion-MNIST / CIFAR-10 on the instance and
prints the job plan (1584 jobs).

## 3. Benchmark (about 5–10 minutes, ~$0.10)

```bash
bash vast/remote.sh benchmark
```

Check the seconds per job. Expected: CIFAR-10 CNN ~60–80 s, MNIST/F-MNIST ~30 s.

## 4. Start everything

```bash
bash vast/remote.sh start 4      # 4 parallel workers
```

Runs inside `tmux` on the instance, so closing your laptop or losing SSH is fine.
Re-running `start` after a crash/reboot resumes: finished jobs are skipped only
when their saved spec hash matches; half-finished folders are moved to
`results_v2/_stale/`, never reused.

## 5. Watch / download

```bash
bash vast/remote.sh status       # last log lines, jobs complete, GPU use
bash vast/remote.sh fetch        # copies results_v2/ here (safe to run any time)
```

## 6. When finished: fetch, then DESTROY the instance in the vast console
A stopped instance still bills for its disk.

## What each job is

Folder name = full identity, e.g.
`CIFAR10_CNN_K2_M10_q3_r40_data_changes_adopt_destination_caseB_b0p9_i5_R60_s42`

| part | meaning |
|---|---|
| K2 / K5 | clusters (K=10 replaced by K=5: two classes per cluster) |
| M10 | clients per cluster |
| q3 | migrants (min(3, M-1) in the main grid) |
| r40 | migration round (r42 = timing check off the mixing round) |
| membership_only / data_changes / control | sub-mode; control = nobody migrates |
| keep_weights / adopt_destination | handover baseline |
| caseA / caseB, b0p9, i5 | isolated vs sharing, beta, mixing interval |

Plans: main grid (3 datasets x K{2,5} x M3..10 x 3 seeds x [2 sub-modes x 2 handovers + control] x 2 cases = 1440),
CIFAR-10 sweeps (migrant count q=1..9 with matched controls, sharing 5–50 %, timing at round 42) = 144.

## Data hold-back (needed for disjoint migrant data)

Every cluster's class pool is split into M + q equal shards: M go to residents,
q are held back. data_changes migrants receive the destination's held-back
shards, so their new data never overlaps any resident's. Because every cluster
does this (in every sub-mode and in controls), all clients hold the same amount
of data and migrants carry the same FedAvg weight as residents. Cost: each
cluster trains on M/(M+q) of its data (60 % at M=3, 77 % at M=10). State this in
the paper's setup section; the old (v1) results used 100 %.

## Outputs per job

`run_*/metrics.csv` per round and cluster: `cluster_test_acc` (after mixing, as
before), `cluster_test_acc_premix` (before mixing), `global_test_acc`, `train_acc`.
`run_*/analysis.json`: before/after stats for cluster, pre-mix and global accuracy,
with `recovered`, `relapsed`, `rounds_below_threshold`, `final_mean`.
`run_*/metrics.json` → `migrations[]`: `data_source` (must be `reserved_disjoint`),
`arrival_l2_to_dst`, `handover`.

`python run_v2.py --collect` builds `results_v2/summary_long.csv` (one row per job x
cluster x metric family) for the analysis.

## Locally (no GPU rental)

```bash
python run_v2.py --plan all --dry-run
python run_v2.py --plan main --filter MNIST_CNN_K2_M3_ s42 --workers 2 --resume
```
