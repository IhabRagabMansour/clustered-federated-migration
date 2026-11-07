# Gradual-drift experiment: results

**Run:** 252 jobs on a vast.ai RTX 5090, 0 failures.

**Setup:**
- CIFAR-10 with a CNN, K=2 clusters: classes 0–4 and classes 5–9.
- 3 drifting clients in the source cluster, with M = 10 or 5 clients per cluster.
- q=3 reserved shards, 80 rounds.
- Drift starts at round 30 and lasts D ∈ {0, 5, 10, 20} rounds. During the drift, each drifting client's own shard is replaced step by step with a shard of destination classes.
- 3 seeds (42, 43, 44); Case A and Case B (β=0.9, every 5 rounds).

**Migration policies:**
- **never:** the client stays in its old cluster.
- **fixed:** the client moves when its drift is complete.
- **detected:** the client moves when the destination model has a lower loss on its current data for 2 rounds in a row. Checks start at round 10.

Each migration policy also has two handover options:
- **keep:** the client brings its own weights;
- **adopt:** the client takes the destination cluster's model.

The tables are in `drift_tables.md` and `drift_table.csv`. The figures are `fd1_*` and `fd2_*`.

## 1. Migration is necessary (never vs move)

| | drifting clients, rounds ≥ 30 | drifting clients, last 10 rounds | source cluster vs control, rounds ≥ 30 |
|---|---|---|---|
| never, M=10 | 37–44 % | about 42 % | −12 to −22 pts |
| never, M=5 | 48–57 % | about 60 % | −27 to −45 pts |
| fixed / detected | 72–89 % | 88.6 % (M=10), 89.6 % (M=5) | −0.5 to −5 pts |

- **Clients that never move stay badly served for the rest of the run.** Their old cluster's model cannot classify their new classes.
- **Clients that never move also damage their old cluster.** Their updates for the new classes pull the source model away from its own classes. The source cluster then oscillates every round between about 0 % and 75 %, the same pattern seen in v2's membership_only runs (`fd2_example_trajectories.png`).
  - The damage grows with the share of drifting clients: 3 of 10 costs about −15 pts, and 3 of 5 costs about −35 pts.
- **Moving the clients fixes both problems for good.**
  - In the last 10 rounds, the moved clients are served as well as the destination's own residents (gap 0 to 0.2 pts).
  - The source cluster returns to its no-drift control level, about 80 %.
  - This holds for every D, M, case and handover.

## 2. The drift period itself costs accuracy, and detection does not shorten it

- **Accuracy falls steadily while the client drifts.** The client stays in its old cluster during the drift, so its accuracy falls roughly in line with its old-class share. At M=10 and D=10 it goes from 75 % to about 15 % just before it moves.
  - The old cluster's model learns almost none of the new classes. At p=0.5 the client scores 38 %, which is about 0.5 × the model's 75 % on old classes.
- **The lowest point is about the same for every D ≥ 5.** The worst-round accuracy is 5–15 % at M=10 and 32–45 % at M=5.
  - Over rounds ≥ 30, the average falls with D only because the low period lasts longer: about 87 % at D=0, then 84 %, 80 % and 72–74 % at D=20 (M=10).
- **Loss-based detection triggers at the same time as the fixed rule.**
  - Detected moves happen at p ≈ 0.95–1.0, in round 31 for D=0, 34–35 for D=5, about 39 for D=10 and 48–49 for D=20.
  - There were no false switches in any of the 252 runs. The detector is safe, but it is not early.
  - **Likely reason:** cross-entropy is dominated by confident mistakes. The destination model is very confident and wrong on the client's remaining old-class samples, so its average loss stays higher until almost all of the old data is gone. Accuracy-based or soft (mixture) assignment would probably switch near p ≈ 0.5 instead.
  - **This is the most useful lever for future work:** an earlier or soft switch could recover most of the dip. That dip is the only lasting cost of gradual drift in these results.
- **detected/D=0 is slightly worse than fixed/D=0.** With D=0, detection needs 2 rounds of patience, so the fully drifted client trains in the wrong cluster for one extra round. This costs the source cluster about 4 pts more at M=5 (−5.4 vs −1.5).

## 3. keep vs adopt

The handover matters less under gradual drift than it did for v2's instant switch.

- **adopt is slightly better throughout.**
  - The destination cluster gains +0.3 to +0.6 pts over keep.
  - The drifting clients gain +0.1 to +0.7 pts.
- **The one case where keep clearly hurts is D=0 at M=5.**
  - The destination's worst round is −10 pts (Case A) and −2.4 pts (Case B) with fixed/keep, against +1.5 / +2.2 with adopt.
  - With D ≥ 5, keep's worst-round damage shrinks to between −3.5 and +1 pts.

## 4. Case A vs Case B

- **For clients that never move, Case B helps:** +4 to +5 pts for the drifting clients at M=10, and +1.6 to +4.5 at M=5. β-mixing gives the source model some knowledge of the other cluster's classes.
- **When clients do move, the differences are small** (|B−A| < 1.7 pts).
  - Case B gives slightly higher drifting-client accuracy at D=20.
  - Case B leaves a slightly larger source-cluster deficit at M=10: −0.4 to −1.2 pts with detected, −0.1 to −0.5 with fixed.
- **Case B also raises the worst-round accuracy for detected moves at D=0:** 72–77 % vs 49–51 % in Case A.

## 5. Take-aways for the thesis

1. Under gradual concept drift, cluster reassignment is essential. Without it, both the drifting clients and their old cluster lose a lot of accuracy, roughly in proportion to the share of clients that drift.
2. Once clients move, everything converges back to the no-drift level. Policy, handover and case affect only the transient.
3. The real cost is the time the client spends in the old cluster during the drift. Loss-based detection, as implemented here, does not shorten it. This motivates an earlier, accuracy-based or soft cluster assignment.
4. Adopting the destination model is a safe default. Keeping the client's own weights is only notably harmful for an abrupt switch (D=0) into a small cluster.
