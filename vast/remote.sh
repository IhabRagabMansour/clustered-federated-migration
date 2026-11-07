#!/usr/bin/env bash
# Runs on YOUR PC. Shortcuts for the instance saved by deploy.sh.
#   bash vast/remote.sh benchmark     # time jobs on the 5090
#   bash vast/remote.sh start [N]     # start/resume all jobs with N workers (default 4)
#   bash vast/remote.sh status        # progress + GPU use
#   bash vast/remote.sh fetch         # download the results folder into this folder
#   bash vast/remote.sh ssh           # open a shell on the instance
# Prefix with PLAN=drift for the gradual-drift plan (results_drift/, 252 jobs).
set -euo pipefail
cd "$(dirname "$0")/.."
source vast/instance.env
SSH="ssh -p $PORT root@$HOST"
PLAN=${PLAN:-all}
OUT=results_v2; TOTAL=1584
[ "$PLAN" = drift ] && { OUT=results_drift; TOTAL=252; }
case "${1:-status}" in
  benchmark) $SSH "cd ~/cfm && bash vast/benchmark.sh" ;;
  start)     $SSH "cd ~/cfm && PLAN=$PLAN bash vast/start.sh ${2:-4}" ;;
  status)    $SSH "cd ~/cfm && tail -n 5 $OUT/launcher.log 2>/dev/null; \
                   echo; echo complete: \$(ls $OUT/*/COMPLETE.json 2>/dev/null | wc -l) / $TOTAL; \
                   nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader" ;;
  fetch)     mkdir -p $OUT
             $SSH "cd ~/cfm && python3 run_v2.py --plan $PLAN --collect >/dev/null; tar czf - $OUT" | tar xzf -
             echo "results in $(pwd)/$OUT ($(ls $OUT/*/COMPLETE.json | wc -l) complete jobs)" ;;
  ssh)       $SSH ;;
  *) echo "unknown command: $1"; exit 1 ;;
esac
