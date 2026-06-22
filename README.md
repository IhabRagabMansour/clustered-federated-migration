# Clustered Federated Learning with Client Migration

Tests how a client **migrating between clusters while keeping its weights** disturbs
the receiving cluster's accuracy, and whether **inter-cluster weight sharing** reduces
that disruption.

- **Case A (isolated):** each cluster aggregates only its own members (per-cluster FedAvg).
- **Case B (sharing):** every `N` rounds, `cluster_i ← β·own + (1−β)·mean(others)`.

Clusters are formed by data distribution (each cluster owns a contiguous group of
classes). Accuracy is measured per cluster on its **own class-restricted test set**
and on the **global test set**. Variance is quantified by rolling std and a
before/after-migration window (mean drop, std change, recovery time), plus the L2
**weight shift** of the receiving cluster.

## Run

```bash
python main.py          # everything is driven by config.yaml
```

Switch cases in `config.yaml`:
- `clustered.sharing.enabled: false` → Case A
- `clustered.sharing.enabled: true`  → Case B (set `beta`, `interval`)

Migration is configured under `clustered.migration.schedule`
(`{round, clients, src, dst}`), with `behavior_change: membership_only | data_changes`.

## Outputs
`logs/results/<name>_<timestamp>/`: `metrics.csv`, `metrics.json`, `analysis.json`,
`config.json`. Plots in `plots/results/`: per-cluster accuracy (with migration marker),
rolling std, between-cluster variance.

## Structure
`data/` (loading + clustered partition) · `models/` · `clustering/` (cluster manager) ·
`federated/` (client, aggregation, trainer) · `migration/` · `metrics/` (distance, variance) ·
`logs/` · `plots/`
