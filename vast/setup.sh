#!/usr/bin/env bash
# Runs ON the vast.ai instance (deploy.sh calls it). Safe to run more than once.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== GPU"
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv

PY=${PY:-python3}
echo "== Python: $($PY --version)"

# Keep the image's torch if it supports this GPU; otherwise install a CUDA 12.8 build.
if ! $PY - <<'EOF'
import sys, torch
ok = torch.cuda.is_available()
if ok:
    cap = torch.cuda.get_device_capability(0)
    arch = f"sm_{cap[0]}{cap[1]}"
    ok = arch in torch.cuda.get_arch_list()
    print(f"torch {torch.__version__} | device {torch.cuda.get_device_name(0)} | {arch} supported: {ok}")
sys.exit(0 if ok else 1)
EOF
then
    echo "== installing torch for CUDA 12.8"
    $PY -m pip install -q --upgrade torch torchvision --index-url https://download.pytorch.org/whl/cu128
fi

echo "== python packages"
$PY -m pip install -q numpy pyyaml matplotlib

command -v tmux >/dev/null || { apt-get update -qq && apt-get install -y -qq tmux >/dev/null; }

echo "== datasets (downloaded once, shared by all jobs)"
$PY - <<'EOF'
from torchvision import datasets
root = "data/datasets"
datasets.MNIST(root, train=True, download=True); datasets.MNIST(root, train=False, download=True)
datasets.FashionMNIST(root, train=True, download=True); datasets.FashionMNIST(root, train=False, download=True)
datasets.CIFAR10(root, train=True, download=True); datasets.CIFAR10(root, train=False, download=True)
print("datasets ready")
EOF

echo "== plan"
$PY run_v2.py --plan all --dry-run | tail -8
echo
echo "setup done. Next: bash vast/benchmark.sh   (about 5 minutes)"
