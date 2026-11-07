#!/usr/bin/env bash
# Runs ON the instance. Starts (or resumes) all jobs inside tmux so an SSH drop
# does not stop them. Usage: [PLAN=all|drift] bash vast/start.sh [workers] [extra run_v2 args...]
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-python3}
PLAN=${PLAN:-all}
OUT=results_v2; [ "$PLAN" = drift ] && OUT=results_drift
WORKERS=${1:-4}; shift || true
mkdir -p "$OUT"
if tmux has-session -t runs 2>/dev/null; then
    echo "tmux session 'runs' already exists: attach with  tmux attach -t runs"
    exit 0
fi
tmux new-session -d -s runs \
    "export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2; \
     $PY run_v2.py --plan $PLAN --workers $WORKERS --resume $* 2>&1 | tee -a $OUT/launcher.log; \
     $PY run_v2.py --plan $PLAN --collect | tee -a $OUT/launcher.log"
echo "started plan $PLAN. progress: tail -f $OUT/launcher.log   (or: tmux attach -t runs, detach with Ctrl-b d)"
