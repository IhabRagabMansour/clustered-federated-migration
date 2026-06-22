# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 10

Note: this configuration migrates all clients from the source cluster, leaving the source cluster empty after migration.

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 0.1220 | -0.2160 |
| data_changes | 0 | clusterTest_afterMean | 78.7800 | 78.8300 |
| data_changes | 0 | clusterTest_afterStd | 0.0000 | 0.5100 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 0.0610 | -0.6180 |
| data_changes | 0 | globalTest_afterMean | 39.3900 | 41.6650 |
| data_changes | 0 | globalTest_afterStd | 0.0000 | 1.9950 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 20.9640 | 6.8840 |
| data_changes | 1 | clusterTest_afterMean | 82.6800 | 86.2760 |
| data_changes | 1 | clusterTest_afterStd | 6.2596 | 2.0846 |
| data_changes | 1 | clusterTest_recovery | 8 | 3 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 10.4820 | 3.4420 |
| data_changes | 1 | globalTest_afterMean | 41.3400 | 43.1380 |
| data_changes | 1 | globalTest_afterStd | 3.1298 | 1.0423 |
