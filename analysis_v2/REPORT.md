# v2 results: what the 1,584 runs show

Run: vast.ai RTX 5090, 9.6 h, 1,584 jobs, 0 failures, cost $6.86.
Data: `results_v2/` (branch `vast-fixes`). Tables: `tables.md` + `t*.csv`. Script: `analyze_v2.py`.

**How to read the numbers**
- **dip:** the mean cluster-test accuracy over rounds 30–39 minus the mean over rounds 40–49 (migration at round 40).
- **excess dip:** the dip of the migration run minus the dip of its matched no-migration control, with the same dataset, K, M, case, seed and cluster. All numbers below are excess dips in accuracy points. Positive means the migration cost accuracy.
- **Sample size:** each cell averages 24 runs (M=3..10 × 3 seeds).

**Why the controls matter.** Without migration, accuracy still rises by about 0.3–1 point in rounds 40–49. Raw dips therefore understate the damage of migration by that amount.

## 1. data_changes: the whole shock comes from the migrant's weights

Destination cluster, excess dip (Table 1/3):

| | keep_weights A | keep_weights B | adopt_destination A | adopt_destination B |
|---|---|---|---|---|
| CIFAR-10 K=2 | **2.44** | 0.33 | −0.56 | −0.65 |
| CIFAR-10 K=5 | **2.05** | 1.08 | −0.28 | 0.11 |
| F-MNIST K=2 | 1.20 | 0.47 | 0.02 | −0.06 |
| MNIST K=2 | 0.81 | 0.42 | −0.03 | −0.05 |
| F-MNIST / MNIST K=5 | ≤0.36 | ≤0.36 | ≈0 | ≈0 |

- **Adopting the destination model removes the shock completely.** The small negative values are a gain from the extra data the migrants bring. So the disruption is caused by the injected weights, not by the new data.
- **Worst single round:** in CIFAR-10 K=2 Case A, the worst post-migration round is on average **12 points** below the pre-migration level. Case B reduces this to 2.2.
- **Every run recovered** (0% never recovered). In data_changes, migration is a short, transient shock.

## 2. Case B (β=0.9) reduces the shock, and it is not a measurement artifact

Paired Case B minus Case A, data_changes + keep_weights (Table 2):
- **K=2, all three datasets:**
  - B has the smaller dip in **100% of the 24 pairs**;
  - CIFAR −2.1 ± 0.2, F-MNIST −0.7, MNIST −0.4.
- **CIFAR-10 K=5:** −1.0 ± 0.2 (B better in 87.5% of pairs).
- **F-MNIST / MNIST K=5:** no effect. The shock there is already near zero.
- **Pre-mix accuracy gives the same result** (CIFAR K=2: −2.07). This answers the v1 review's concern that the effect came from evaluating after mixing.
- **Migrating off the mixing round** (round 42 instead of 40) gives the same picture (A 1.06, B 0.38). The coincidence of migration and mixing rounds was not the cause.
- **Mechanism: the migrant arrives closer to the destination model.** Its L2 distance to the destination model at arrival is 30–55% lower in Case B:
  - CIFAR K=2: 6.7 → 4.2;
  - MNIST K=2: 4.1 → 1.8.

**Caveat: sharing has a constant cost.** In the no-migration controls, Case B clusters are 0.3–0.9 points less accurate before round 40 (CIFAR K=2: 87.2 vs 86.7; K=5: 91.1 vs 90.2).

Mean destination accuracy over the whole run, with migration:

| | Case A | Case B |
|---|---|---|
| CIFAR-10 K=2 | 84.05 | 83.98 |
| CIFAR-10 K=5 | 87.21 | 86.74 |

At β=0.9, sharing roughly trades a smaller migration shock for slightly lower accuracy the rest of the time. The paper should claim **robustness** (a smaller, shorter disruption), not higher accuracy.

**Sharing does not improve global-test accuracy** (CIFAR K=2: 45.5 A vs 45.9 B; K=5: 19.4 vs 19.2). The clusters stay specialists. Sharing works through parameter proximity, not through shared knowledge.

## 3. Source cluster

The source cluster loses its migrants' data:
- excess dip of about 2 points for CIFAR K=2 and 0.6 for K=5, near zero for MNIST;
- the same under both handovers, as expected;
- **sharing does not help the source cluster.**

## 4. Sweeps (CIFAR-10, K=2, M=10)

**Migrant count** (Table 6, f3):
- In Case A, the destination dip grows from about 0.2 (q=1–2) to about 4 (q≥6).
- Case B stays at 25–45% of Case A throughout.
- The source cluster collapses at q=9, where only one client is left: 10.6 points, the same in A and B.

**Sharing level** (q=5, Table 7, f2). Use the pre-mix values:

| sharing | 0% | 5% | 10% | 20% | 30% | 40% | 50% |
|---|---|---|---|---|---|---|---|
| excess dip (pre-mix) | 3.42 | 1.77 | 1.26 | 0.78 | 0.66 | 0.39 | 0.56 |
| baseline accuracy (dst, rounds 30–39) | 85.8 | 85.4 | 85.1 | 84.4 | 84.1 | 80.3 | 73.8 |

- Most of the protection comes from the first 5–10% of sharing. Above 30%, accuracy before migration drops sharply.
- At 40%, the post-mix numbers and the control are unstable (mixing collapse): the post-mix value of −2.7 is an artifact.
- **The best trade-off is 5–10% sharing.**

**Cluster size M** (Table 5): with q=3 fixed, Case A's dip shrinks as M grows (CIFAR K=2: 3.4 at M=3 → 1.2 at M=10), because migrants are a smaller share of the cluster. Case B stays small (0.1–0.9).

## 5. membership_only is a different phenomenon: a lasting oscillation

The destination "dip" is 12–33 points, but it is not a shock followed by recovery. Accuracy **alternates every round** for all 20 rounds after migration. An example from CIFAR K=2 M=10, after round 40:

> 63.8, 81.7, 50.2, 81.2, 73.9, 81.6, 70.8, 83.8 … 72.5, 87.2

The round-to-round change jumps from about 1 to **about 47 points** (CIFAR).

**What drives it:**
- The 3 migrants keep training on source classes that the destination's test set doesn't contain.
- The handover setting makes no difference, so the weights are not the cause.
- It is not stale optimizer state: the optimizer is reset after every `load_weights`.
- On MNIST it slowly dies out; on CIFAR-10 it doesn't within 20 rounds.

**Consequences:**
- Recovery time and the "recovered" flag are meaningless here: the flag fires on the high phase.
- Report amplitude and mean level instead, or define the destination test set to include the migrants' classes.
- Sharing does not help (MNIST/F-MNIST K=5 are 2–3 points worse with B).
- Global-test accuracy *rises*, because the destination cluster learns extra classes.

## 6. What to put in the paper

1. Use **data_changes** as the main result and report the **control-adjusted** dip.
2. Include **adopt_destination** as the baseline. It removes the shock, so frame keep_weights as the scenario studied (a client that cannot or does not reset).
3. **Claim:** β=0.9 sharing cuts the migration shock by 50–85% at K=2 (100% of paired runs) and by about 50% on CIFAR K=5.
   - It works through parameter proximity (lower arrival L2).
   - It costs about 0.5 points of baseline accuracy.
   - It gives no global-accuracy gain.
4. Present membership_only separately as a lasting oscillation, not a recoverable dip.
5. **Setup notes:**
   - clusters use 60–77% of their data (held back for migrants);
   - training is not converged at 60 rounds (controls still improve about 0.7 points per 10 rounds).
