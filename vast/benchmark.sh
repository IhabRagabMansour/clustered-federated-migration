#!/usr/bin/env bash
# Runs ON the instance. Times one full 60-round job per dataset, alone and with
# 4 in parallel, so you can pick --workers and check the cost estimate.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-python3}
rm -rf results_bench results_bench_par

echo "== 1 worker (3 jobs: CIFAR-10, F-MNIST, MNIST)"
T0=$(date +%s); $PY run_v2.py --benchmark --workers 1 | tail -5; T1=$(date +%s)
echo "sequential: $((T1-T0)) s"

echo "== 4 workers (2 CIFAR-10 + 2 F-MNIST jobs at once)"
T0=$(date +%s)
$PY run_v2.py --plan main --filter K2_M10_ s42 data_changes keep_weights \
    --workers 4 --out results_bench_par --limit 4 | tail -6
T1=$(date +%s)
echo "parallel (4 jobs): $((T1-T0)) s"
echo
echo "Rule of thumb: if 4 parallel jobs take < 2x the time of one CIFAR job, use --workers 4."
rm -rf results_bench_par
