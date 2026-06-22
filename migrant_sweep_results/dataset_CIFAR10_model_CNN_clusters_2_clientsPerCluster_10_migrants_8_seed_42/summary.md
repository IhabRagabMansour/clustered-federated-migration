# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 8

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 5.0820 | 3.5840 |
| data_changes | 0 | clusterTest_afterMean | 77.2520 | 76.8140 |
| data_changes | 0 | clusterTest_afterStd | 1.4426 | 1.4836 |
| data_changes | 0 | clusterTest_recovery | 3 | 3 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 2.5410 | 1.7920 |
| data_changes | 0 | globalTest_afterMean | 38.6260 | 38.4070 |
| data_changes | 0 | globalTest_afterStd | 0.7213 | 0.7418 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 19.7040 | 6.5440 |
| data_changes | 1 | clusterTest_afterMean | 83.4360 | 86.5200 |
| data_changes | 1 | clusterTest_afterStd | 6.1135 | 2.0120 |
| data_changes | 1 | clusterTest_recovery | 7 | 3 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 9.8520 | 3.2720 |
| data_changes | 1 | globalTest_afterMean | 41.7180 | 43.2600 |
| data_changes | 1 | globalTest_afterStd | 3.0567 | 1.0060 |
