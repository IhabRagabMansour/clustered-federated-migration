"""
Client migration scheduler.

At a scheduled round, a client changes cluster membership while KEEPING its
weights (the core mechanism). Two behaviour-change sub-modes:
  - membership_only : data unchanged
  - data_changes    : local data resampled to the destination cluster's classes

Because the round loop is train -> aggregate -> distribute, a migrated client
trains from its (old-cluster) weights and injects them into the destination
cluster's aggregation before adopting the new cluster model.
"""

from typing import Dict, List


class MigrationScheduler:
    def __init__(self, schedule: List[dict], behavior_change: str, partitioner=None,
                 verbose: bool = True):
        # round -> list of events
        self.by_round: Dict[int, List[dict]] = {}
        for event in (schedule or []):
            self.by_round.setdefault(int(event["round"]), []).append(event)
        self.behavior_change = behavior_change
        self.partitioner = partitioner
        self.verbose = verbose
        self.applied: List[dict] = []          # log of executed migrations
        self.migration_rounds = sorted(self.by_round.keys())

    def apply(self, round_num: int, clients_by_id: Dict[int, "object"]) -> List[dict]:
        events = self.by_round.get(round_num, [])
        executed = []
        for event in events:
            dst = int(event["dst"])
            for cid in event["clients"]:
                client = clients_by_id.get(int(cid))
                if client is None:
                    continue
                src = client.cluster_id
                client.cluster_id = dst          # reassign membership; weights untouched

                data_source = "unchanged"
                if self.behavior_change == "data_changes" and self.partitioner is not None:
                    import torch
                    new_idx = self.partitioner.take_reserved(dst)
                    if new_idx is not None:
                        data_source = "reserved_disjoint"
                    else:
                        # Legacy path: draws from the same pool as resident clients,
                        # so the new data can duplicate residents' examples.
                        new_classes = self.partitioner.cluster_classes[dst]
                        new_idx = self.partitioner.resample_indices(new_classes, client.num_samples)
                        data_source = "resampled_shared_pool"
                    client.set_indices(torch.as_tensor(new_idx, dtype=torch.long,
                                                       device=client.X.device))

                record = {"round": round_num, "client": int(cid), "src": int(src), "dst": dst,
                          "behavior_change": self.behavior_change,
                          "data_source": data_source, "num_samples": client.num_samples}
                self.applied.append(record)
                executed.append(record)
                if self.verbose:
                    print(f"  [Round {round_num}] Migrated client {cid}: "
                          f"cluster {src} -> {dst} ({self.behavior_change})")
        return executed
