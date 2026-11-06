#!/usr/bin/env bash
# Runs on YOUR PC. Shortcuts for the instance saved by deploy.sh.
#   bash vast/remote.sh benchmark     # time jobs on the 5090
#   bash vast/remote.sh start [N]     # start/resume all jobs with N workers (default 4)
#   bash vast/remote.sh status        # progress + GPU use
#   bash vast/remote.sh fetch         # download results_v2/ into this folder
#   bash vast/remote.sh ssh           # open a shell on the instance
set -euo pipefail
cd "$(dirname "$0")/.."
source vast/instance.env
SSH="ssh -p $PORT root@$HOST"
case "${1:-status}" in
  benchmark) $SSH "cd ~/cfm && bash vast/benchmark.sh" ;;
  start)     $SSH "cd ~/cfm && bash vast/start.sh ${2:-4}" ;;
  status)    $SSH "cd ~/cfm && tail -n 5 results_v2/launcher.log 2>/dev/null; \
                   echo; echo complete: \$(ls results_v2/*/COMPLETE.json 2>/dev/null | wc -l) / 1584; \
                   nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader" ;;
  fetch)     mkdir -p results_v2
             $SSH "cd ~/cfm && python3 run_v2.py --collect >/dev/null; tar czf - results_v2" | tar xzf -
             echo "results in $(pwd)/results_v2 ($(ls results_v2/*/COMPLETE.json | wc -l) complete jobs)" ;;
  ssh)       $SSH ;;
  *) echo "unknown command: $1"; exit 1 ;;
esac
