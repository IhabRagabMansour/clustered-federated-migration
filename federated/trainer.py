"""
Clustered training loop.

Per round:
  0. apply scheduled migrations (membership changes; migrant keeps its weights)
  1. each cluster: members train locally (from their CURRENT model)
  2. each cluster: intra-cluster FedAvg -> cluster model
  3. distribute cluster model to its members
  4. Case B only (every N rounds): inter-cluster beta-mixing + redistribute
  5. evaluate each cluster on its cluster test set and on the global test set
  6. record metrics

Ordering is train -> aggregate -> distribute so a migrated client injects its
old-cluster weights into the destination cluster before adopting its model.
"""

import copy
from typing import Dict, List

from federated.aggregation import fedavg, inter_cluster_mix
from metrics.distance import l2_distance


class ClusteredTrainer:
    def __init__(self, manager, scheduler, config, logger):
        self.m = manager
        self.scheduler = scheduler
        self.cfg = config
        self.logger = logger

        self.rounds = config.training.global_rounds
        self.local_epochs = config.training.local_epochs
        self.verbose = config.logging.verbose

        sharing = config.clustered.sharing
        self.sharing_enabled = bool(sharing.enabled)
        self.beta = float(sharing.beta)
        self.share_interval = int(sharing.interval)

    def run(self):
        for r in range(1, self.rounds + 1):
            migrations = self.scheduler.apply(r, self.m.clients_by_id)

            # 1-3. intra-cluster train, aggregate, distribute
            train_acc_by_cluster = {}
            for c in range(self.m.num_clusters):
                members = self.m.members(c)
                if not members:
                    continue
                accs = []
                for client in members:
                    metrics = client.train_local(self.local_epochs)
                    accs.append(metrics["accuracy"])
                state_dicts = [cl.get_weights() for cl in members]
                num_samples = [cl.num_samples for cl in members]
                self.m.cluster_models[c] = fedavg(state_dicts, num_samples)
                for client in members:
                    client.load_weights(self.m.cluster_models[c])
                train_acc_by_cluster[c] = sum(accs) / len(accs)

            # 4. Case B: inter-cluster mixing
            weight_shift = {}
            mixed_this_round = False
            if self.sharing_enabled and r % self.share_interval == 0:
                before = {c: copy.deepcopy(sd) for c, sd in self.m.cluster_models.items()}
                self.m.cluster_models = inter_cluster_mix(self.m.cluster_models, self.beta)
                for c in range(self.m.num_clusters):
                    for client in self.m.members(c):
                        client.load_weights(self.m.cluster_models[c])
                weight_shift = {c: l2_distance(before[c], self.m.cluster_models[c])
                                for c in self.m.cluster_models}
                mixed_this_round = True

            # 5. evaluation (load each cluster model once)
            do_cluster = self.cfg.clustered.evaluation.cluster_test
            do_global = self.cfg.clustered.evaluation.global_test
            cluster_test, global_test = {}, {}
            for c in range(self.m.num_clusters):
                cl_acc, gl_acc = self.m.evaluate_both(c, do_cluster, do_global)
                if cl_acc is not None:
                    cluster_test[c] = cl_acc
                if gl_acc is not None:
                    global_test[c] = gl_acc

            # 6. record
            self.logger.log_round(
                round_num=r,
                cluster_test_acc=cluster_test,
                global_test_acc=global_test,
                train_acc=train_acc_by_cluster,
                weight_shift=weight_shift if mixed_this_round else None,
                migrations=migrations,
                cluster_sizes=self.m.cluster_sizes(),
            )

            if self.verbose:
                ct = " ".join(f"C{c}:{a:.1f}" for c, a in cluster_test.items())
                tag = " [MIX]" if mixed_this_round else ""
                mark = " <<MIGRATION" if migrations else ""
                print(f"Round {r:3d}/{self.rounds} | cluster_test_acc {ct}{tag}{mark}")
