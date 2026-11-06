#!/usr/bin/env bash
# Runs ON the instance. Starts (or resumes) all jobs inside tmux so an SSH drop
# does not stop them. Usage: bash vast/start.sh [workers] [extra run_v2 args...]
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-python3}
WORKERS=${1:-4}; shift || true
mkdir -p results_v2
if tmux has-session -t runs 2>/dev/null; then
    echo "tmux session 'runs' already exists: attach with  tmux attach -t runs"
    exit 0
fi
tmux new-session -d -s runs \
    "$PY run_v2.py --plan all --workers $WORKERS --resume $* 2>&1 | tee -a results_v2/launcher.log; \
     $PY run_v2.py --collect | tee -a results_v2/launcher.log"
echo "started. progress: tail -f results_v2/launcher.log   (or: tmux attach -t runs, detach with Ctrl-b d)"
