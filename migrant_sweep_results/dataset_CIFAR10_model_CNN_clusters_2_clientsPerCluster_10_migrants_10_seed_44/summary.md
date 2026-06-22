# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 10

Note: this configuration migrates all clients from the source cluster, leaving the source cluster empty after migration.

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | -1.1720 | 0.3440 |
| data_changes | 0 | clusterTest_afterMean | 80.5800 | 78.8600 |
| data_changes | 0 | clusterTest_afterStd | 0.0000 | 0.4400 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | -0.5860 | -0.2680 |
| data_changes | 0 | globalTest_afterMean | 40.2900 | 41.9050 |
| data_changes | 0 | globalTest_afterStd | 0.0000 | 2.2550 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 34.9740 | 8.7460 |
| data_changes | 1 | clusterTest_afterMean | 81.1700 | 86.0980 |
| data_changes | 1 | clusterTest_afterStd | 10.4748 | 2.6722 |
| data_changes | 1 | clusterTest_recovery | 7 | 3 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 17.4870 | 4.3730 |
| data_changes | 1 | globalTest_afterMean | 40.5850 | 43.0490 |
| data_changes | 1 | globalTest_afterStd | 5.2374 | 1.3361 |
