#!/usr/bin/env bash
# Runs on YOUR PC (Git Bash). Copies the code to the instance and runs setup.
# Usage: bash vast/deploy.sh HOST PORT      (from vast's "ssh -p PORT root@HOST")
# The .env file (GitHub token), datasets, old results and the paper are NOT uploaded.
set -euo pipefail
HOST=${1:?HOST}; PORT=${2:?PORT}
cd "$(dirname "$0")/.."
printf 'HOST=%s\nPORT=%s\n' "$HOST" "$PORT" > vast/instance.env

SSH="ssh -p $PORT -o StrictHostKeyChecking=accept-new root@$HOST"
echo "== uploading code to $HOST:$PORT"
tar czf - \
    --exclude=.git --exclude=.env --exclude='*.env' --exclude=__pycache__ \
    --exclude=data/datasets --exclude=grid_results --exclude=migrant_sweep_results \
    --exclude=sharing_sweep_results --exclude=results_v2 --exclude=results_bench \
    --exclude=Ehab_FLTA26 --exclude=analysis_review --exclude=logs/results \
    --exclude=plots/results --exclude=figures --exclude=tmp --exclude='*.log' \
    . | $SSH "mkdir -p ~/cfm && tar xzf - -C ~/cfm"

echo "== running setup on the instance"
$SSH "cd ~/cfm && bash vast/setup.sh"
