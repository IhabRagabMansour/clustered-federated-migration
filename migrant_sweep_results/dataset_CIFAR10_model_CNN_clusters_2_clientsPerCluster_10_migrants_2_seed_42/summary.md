# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | -0.0180 | -0.2960 |
| data_changes | 0 | clusterTest_afterMean | 80.3100 | 79.5560 |
| data_changes | 0 | clusterTest_afterStd | 0.8202 | 0.6284 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | -0.0090 | -0.1480 |
| data_changes | 0 | globalTest_afterMean | 40.1550 | 39.7780 |
| data_changes | 0 | globalTest_afterStd | 0.4101 | 0.3142 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 6.0840 | 1.1440 |
| data_changes | 1 | clusterTest_afterMean | 87.5560 | 87.8140 |
| data_changes | 1 | clusterTest_afterStd | 2.0337 | 0.5871 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 3.0420 | 0.5720 |
| data_changes | 1 | globalTest_afterMean | 43.7780 | 43.9070 |
| data_changes | 1 | globalTest_afterStd | 1.0169 | 0.2935 |
