"""
Entry point: clustered federated learning with client migration.

Run:  python main.py
Configure everything in config.yaml (Case A vs Case B via clustered.sharing.enabled).
"""

import random

import numpy as np
import torch

from config_loader import config
from data.dataset_loader import DatasetLoader
from data.partition import ClusteredPartitioner
from data.fast_data import materialize
from models.model import create_model
from federated.client import Client
from clustering.cluster_manager import ClusterManager
from migration.migration import MigrationScheduler
from federated.trainer import ClusteredTrainer
from logs.logger import ClusterLogger
from plots.plot import (plot_cluster_accuracy, plot_rolling_std,
                        plot_between_cluster_variance)


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_device() -> str:
    d = config.experiment.device
    if d == "auto":
        return "cuda" if torch.cuda.is_available() else "cpu"
    return d


def build_and_run(sharing_enabled: bool = None, experiment_name: str = None,
                  do_plots: bool = True) -> dict:
    """
    Build the full clustered-FL setup and run one experiment.
    `sharing_enabled` / `experiment_name` override config when provided
    (used by compare.py to run Case A and Case B with the same seed).
    Returns a dict with history, analysis, and migration metadata.
    """
    if sharing_enabled is not None:
        config._config["clustered"]["sharing"]["enabled"] = bool(sharing_enabled)
    if experiment_name is not None:
        config._config["experiment"]["name"] = experiment_name

    set_seed(config.experiment.seed)
    device = get_device()
    num_clusters = config.clustered.num_clusters
    total_clients = config.clustered.total_clients
    batch_size = config.data.batch_size
    sharing_on = config.clustered.sharing.enabled
    print(f"Device: {device} | Clusters: {num_clusters} | Clients: {total_clients} | "
          f"Mode: {'Case B (sharing)' if sharing_on else 'Case A (isolated)'}")

    # ---- Data ----
    loader = DatasetLoader(config.data.dataset, config.data.data_path)
    train_set, test_set = loader.load_data(download=True)
    info = loader.info()

    partitioner = ClusteredPartitioner(
        train_set, test_set, num_classes=info["num_classes"],
        num_clusters=num_clusters, total_clients=total_clients, seed=config.experiment.seed)
    eval_bs = config.data.get("eval_batch_size", batch_size)

    # Materialise datasets onto the device once (GPU-resident tensors)
    X_train, y_train = materialize(train_set, device)
    X_test, y_test = materialize(test_set, device)

    # ---- Migration settings ----
    mig = config.clustered.migration
    schedule = mig.schedule.to_dict() if hasattr(mig.schedule, "to_dict") else mig.schedule
    schedule = list(schedule or [])
    is_control = bool(mig.get("control", False))
    # Hold back one disjoint shard per migrant in EVERY cluster, so data_changes
    # migrants never receive residents' examples, and every client (source,
    # destination, migrant) holds the same amount of data -> migrants carry the
    # same FedAvg weight as residents. Applied in every sub-mode and in controls
    # so the partition is identical across them. Only destination shards are used.
    reserve_slots = {}
    if bool(mig.get("reserve_for_migrants", False)):
        n_migrants = sum(len(e["clients"]) for e in schedule)
        reserve_slots = {c: n_migrants for c in range(num_clusters)}

    client_idx_lists, client_cluster, client_classes = partitioner.build_client_indices(
        reserve_slots=reserve_slots)
    cluster_test_idx = {c: torch.as_tensor(arr, dtype=torch.long, device=device)
                        for c, arr in enumerate(partitioner.cluster_test_index_lists())}
    global_test_idx = torch.as_tensor(partitioner.global_test_indices(),
                                      dtype=torch.long, device=device)

    print("\nCluster -> classes:")
    for c, classes in enumerate(partitioner.cluster_classes):
        print(f"  Cluster {c}: classes {classes} | clients {partitioner.counts[c]}")

    # ---- Model (shared initial weights for all clients/clusters) ----
    init_model = create_model(
        config.model.architecture, num_classes=info["num_classes"],
        input_channels=info["input_channels"], input_size=info["input_size"],
        depth=config.model.resnet_depth)

    # ---- Clients ----
    clients = []
    for cid, idx_arr in enumerate(client_idx_lists):
        idx_t = torch.as_tensor(idx_arr, dtype=torch.long, device=device)
        client = Client(
            client_id=cid, X=X_train, y=y_train, idx=idx_t, cluster_id=client_cluster[cid],
            batch_size=batch_size, lr=config.training.learning_rate,
            optimizer_name=config.training.optimizer, device=device,
            momentum=config.training.momentum, weight_decay=config.training.weight_decay)
        client.set_model(init_model)
        clients.append(client)

    # ---- Cluster manager ----
    manager = ClusterManager(
        clients=clients, num_clusters=num_clusters,
        X_test=X_test, y_test=y_test, cluster_test_idx=cluster_test_idx,
        global_test_idx=global_test_idx, init_model=init_model, device=device,
        eval_batch_size=eval_bs)

    # ---- Migration scheduler (a control keeps the nominal schedule for analysis only) ----
    scheduler = MigrationScheduler(
        schedule=[] if is_control else schedule, behavior_change=mig.behavior_change,
        partitioner=partitioner, verbose=config.logging.verbose)

    # ---- Logger ----
    logger = ClusterLogger(
        experiment_name=config.experiment.name, save_path=config.logging.save_path,
        num_clusters=num_clusters, variance_window=config.clustered.evaluation.variance_window,
        config_dict=config.to_dict(), analysis_events=schedule)

    # ---- Run ----
    print("\n" + "=" * 70)
    print("Training")
    print("=" * 70)
    trainer = ClusteredTrainer(manager, scheduler, config, logger)
    trainer.run()
    analysis = logger.finalize()

    # ---- Plots ----
    if do_plots and config.plotting.enabled:
        rounds = logger.history["rounds"]
        mrounds = scheduler.migration_rounds
        case = "Case B (sharing)" if sharing_on else "Case A (isolated)"
        name = config.experiment.name
        plot_cluster_accuracy(
            rounds, logger.history["cluster_test_acc"], mrounds,
            f"{name} - Cluster Test Accuracy [{case}]",
            config.plotting.save_path, f"{name}_cluster_acc.png")
        plot_rolling_std(
            rounds, analysis["rolling_std"], mrounds,
            f"{name} - Rolling Std of Cluster Accuracy [{case}]",
            config.plotting.save_path, f"{name}_rolling_std.png")
        plot_between_cluster_variance(
            rounds, analysis["between_cluster_variance"], mrounds,
            f"{name} - Between-Cluster Variance [{case}]",
            config.plotting.save_path, f"{name}_between_var.png")

    # Affected clusters (src + dst across all migration events)
    affected = sorted({int(e["src"]) for e in schedule} | {int(e["dst"]) for e in schedule})
    dst_clusters = sorted({int(e["dst"]) for e in schedule})
    return {
        "history": logger.history,
        "analysis": analysis,
        "migration_rounds": sorted({int(e["round"]) for e in schedule}),
        "is_control": is_control,
        "affected_clusters": affected,
        "dst_clusters": dst_clusters,
        "sharing_on": sharing_on,
        "run_dir": logger.run_dir,
    }


def main():
    print("=" * 70)
    print("CLUSTERED FEDERATED LEARNING WITH CLIENT MIGRATION")
    print("=" * 70)
    build_and_run()
    print("\n" + "=" * 70)
    print("DONE")
    print("=" * 70)


if __name__ == "__main__":
    main()
