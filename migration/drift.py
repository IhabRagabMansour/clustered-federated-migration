"""
Gradual data drift with three re-clustering policies.

From `start_round`, each drifting client replaces a growing fraction p(r) of its
local data with data of the destination cluster's classes:

    p(r) = 1                                   if duration == 0 (instant swap)
    p(r) = min(1, (r - start_round + 1) / D)   otherwise, for r >= start_round

The client's dataset size never changes. The destination-class part comes from
a held-back shard of the destination cluster (disjoint from every resident), the
source-class part is the client's own original shard. Replacement is nested:
the samples added at p are still there at any larger p.

Policies (when does the drifting client change cluster?):
  never    : it stays in its source cluster for the whole run
  fixed    : it moves to the destination in the first round with p == 1
  detected : every round from `detect_from`, EVERY client computes its loss on its
             current local data under every cluster model and moves to the
             cluster with the lowest loss once that cluster has won `patience`
             consecutive checks (IFCA-style assignment with hysteresis).
             Residents may switch too; such switches are logged.

Each round: update_data(r) runs first, then migrations, then local training.
"""

from typing import Dict, List

import torch

POLICIES = ("never", "fixed", "detected")


class DriftController:
    def __init__(self, schedule: List[dict], start_round: int, duration: int, policy: str,
                 partitioner, patience: int = 2, detect_from: int = 10, verbose: bool = False):
        if policy not in POLICIES:
            raise ValueError(f"Unknown drift policy '{policy}', expected one of {POLICIES}")
        self.start = int(start_round)
        self.duration = int(duration)
        self.policy = policy
        self.partitioner = partitioner
        self.patience = int(patience)
        self.detect_from = int(detect_from)
        self.verbose = verbose

        # drifting client id -> (src, dst)
        self.targets: Dict[int, tuple] = {}
        for ev in schedule or []:
            for cid in ev["clients"]:
                self.targets[int(cid)] = (int(ev["src"]), int(ev["dst"]))
        self.own_idx: Dict[int, torch.Tensor] = {}
        self.new_idx: Dict[int, torch.Tensor] = {}
        self.p: Dict[int, float] = {cid: 0.0 for cid in self.targets}
        self._streak: Dict[int, tuple] = {}   # cid -> (candidate cluster, consecutive wins)
        self.detections: List[dict] = []     # every detected switch (drifting or not)

    # ------------------------------------------------------------------ #
    def p_at(self, r: int) -> float:
        if r < self.start:
            return 0.0
        if self.duration <= 0:
            return 1.0
        return min(1.0, (r - self.start + 1) / self.duration)

    @property
    def full_round(self) -> int:
        """First round with p == 1."""
        return self.start if self.duration <= 0 else self.start + self.duration - 1

    def update_data(self, r: int, clients_by_id) -> None:
        p = self.p_at(r)
        if p <= 0.0:
            return
        for cid, (src, dst) in self.targets.items():
            client = clients_by_id[cid]
            if cid not in self.own_idx:
                shard = self.partitioner.take_reserved(dst)
                if shard is None:
                    raise RuntimeError("drift needs reserve_for_migrants: true "
                                       "(no held-back shard left for the destination)")
                self.own_idx[cid] = client.idx
                self.new_idx[cid] = torch.as_tensor(shard, dtype=torch.long,
                                                    device=client.idx.device)
            own, new = self.own_idx[cid], self.new_idx[cid]
            n = int(own.numel())
            k = min(int(round(p * n)), int(new.numel()))
            client.set_indices(torch.cat([new[:k], own[k:]]))
            self.p[cid] = k / n

    # ------------------------------------------------------------------ #
    def _record(self, r, client, src, dst, trigger) -> dict:
        return {"round": r, "client": int(client.client_id), "src": int(src), "dst": int(dst),
                "behavior_change": "drift", "data_source": "drift_mixed",
                "num_samples": client.num_samples, "trigger": trigger,
                "drifting": int(client.client_id) in self.targets,
                "drift_p": round(self.p.get(int(client.client_id), 0.0), 4)}

    def step(self, r: int, manager) -> List[dict]:
        """Update data, then return the migrations executed this round."""
        self.update_data(r, manager.clients_by_id)
        out = []
        if self.policy == "fixed" and r == self.full_round:
            for cid, (src, dst) in self.targets.items():
                client = manager.clients_by_id[cid]
                if client.cluster_id != dst:
                    out.append(self._record(r, client, client.cluster_id, dst, "fixed"))
                    client.cluster_id = dst
        elif self.policy == "detected" and r >= self.detect_from:
            losses = manager.client_losses_per_cluster()      # {cid: [loss per cluster]}
            for client in manager.clients:
                cid = int(client.client_id)
                ls = losses[cid]
                best = min(range(len(ls)), key=lambda c: ls[c])
                if best == client.cluster_id:
                    self._streak.pop(cid, None)
                    continue
                cand, wins = self._streak.get(cid, (best, 0))
                wins = wins + 1 if cand == best else 1
                self._streak[cid] = (best, wins)
                if wins >= self.patience:
                    rec = self._record(r, client, client.cluster_id, best, "detected")
                    rec["loss_own"] = float(ls[client.cluster_id])
                    rec["loss_new"] = float(ls[best])
                    out.append(rec)
                    self.detections.append(rec)
                    client.cluster_id = best
                    self._streak.pop(cid, None)
        if self.verbose:
            for rec in out:
                print(f"  [Round {r}] client {rec['client']}: cluster {rec['src']} -> "
                      f"{rec['dst']} ({rec['trigger']}, p={rec['drift_p']})")
        return out
