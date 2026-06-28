# Clustered Federated Learning with Client Migration

This project studies how client migration affects clustered federated learning
and whether inter-cluster model sharing reduces the accuracy disruption in the
destination cluster.

- **Isolated:** each cluster aggregates only its own clients using per-cluster FedAvg.
- **Knowledge sharing:** cluster-level models are periodically mixed across clusters.

In the knowledge-sharing setting, the shared model is computed as:

```text
new_model_i = beta * own_model_i + (1 - beta) * mean(other_cluster_models)
```

For example, `beta = 0.9` means `90%` own cluster model and `10%` information
from the other cluster models.

## Recommended Entry Point

Use `run_experiments.py` as the main launcher. It is a small wrapper around the
existing experiment scripts, so the original runners remain the source of truth.

Before running experiments, activate the environment:

```powershell
conda activate gossip
```

Preview what will run without starting training:

```powershell
python run_experiments.py --dry-run
```

Run the configured experiments:

```powershell
python run_experiments.py
```

Regenerate plots from existing results only:

```powershell
python run_experiments.py --plots-only
```

## Editable Configuration

The main settings are near the top of `run_experiments.py`:

```python
EXPERIMENTS_TO_RUN = ["main_grid", "migrant_sweep", "sharing_sweep"]
RUN_TRAINING = True
RUN_PLOTS = True
RESUME = True

DATASETS = ["CIFAR-10"]
MODELS = ["CNN"]
SEEDS = [42, 43, 44]

CLUSTERS = [2]
CLIENTS_PER_CLUSTER = [10]
MIGRANTS = [5]
SHARING_SWEEP_MIGRANTS = 5
SHARING_PERCENTAGES = [5, 10, 20, 30, 40, 50]
```

Change these values to run different datasets, models, cluster counts, migrant
counts, or sharing percentages.

## Launcher Options

```powershell
python run_experiments.py --dry-run
```

Print all commands without executing them.

```powershell
python run_experiments.py --only sharing_sweep
```

Run only one experiment family. Valid values are:

```text
main_grid
migrant_sweep
sharing_sweep
plots_only
```

```powershell
python run_experiments.py --plots-only
```

Skip training and regenerate plots from existing results.

```powershell
python run_experiments.py --no-plots
```

Run training but skip plot generation.

```powershell
python run_experiments.py --only migrant_sweep --limit 1 --no-plots
```

Run only the first configuration of a selected training script. This is useful
as a smoke test.

```powershell
python run_experiments.py --verbose-rounds
```

Print per-round training output.

## Windows Helper Scripts

Two helper scripts are provided so the launcher can be run directly from the
project root.

PowerShell:

```powershell
.\run_experiments.ps1 --dry-run
.\run_experiments.ps1 --plots-only
.\run_experiments.ps1 --only sharing_sweep
```

If PowerShell blocks script execution, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_experiments.ps1 --dry-run
```

Command Prompt:

```cmd
run_experiments.bat --dry-run
run_experiments.bat --plots-only
run_experiments.bat --only sharing_sweep
```

The helper scripts pass all arguments directly to `run_experiments.py`.

## Experiment Families

### Main Grid

Runs the main clustered FL configurations through:

```text
run_grid.py
aggregate_grid_results.py
scripts/create_results_plots.py
scripts/create_instability_plots.py
scripts/create_resnet_cifar10_plots.py
```

Results are stored in:

```text
grid_results
figures/results
```

### Migrant-Count Sweep

Fixes the setup and varies the number of migrated clients. This produces a plot
of migrated clients versus maximum accuracy drop.

Underlying scripts:

```text
run_migrant_sweep.py
scripts/create_migrant_sweep_plots.py
```

Results are stored in:

```text
migrant_sweep_results
figures/results
```

### Sharing-Percentage Sweep

Fixes the migration setting and varies the knowledge-sharing percentage. This
produces a plot of information sharing percentage versus maximum accuracy drop.

Underlying scripts:

```text
run_sharing_sweep.py
scripts/create_sharing_sweep_plots.py
```

Results are stored in:

```text
sharing_sweep_results
figures/results
```

## Plot Outputs

Paper plots are exported to:

```text
figures/results
```

Each plot is saved as:

```text
.pgf
.pdf
.svg
.png
```

Use `.pgf` in LaTeX for publication-quality figures.

## Manual Single Run

For a single config-driven experiment, you can still run:

```powershell
python main.py
```

This uses `config.yaml` directly.

## Project Structure

```text
data/          loading and clustered partitioning
models/        CNN and ResNet model creation
clustering/    cluster manager
federated/     client training, FedAvg, trainer loop
migration/     migration scheduler
metrics/       disruption and variance metrics
logs/          metrics logging
plots/         per-run plotting helpers
scripts/       paper-figure generation scripts
```
