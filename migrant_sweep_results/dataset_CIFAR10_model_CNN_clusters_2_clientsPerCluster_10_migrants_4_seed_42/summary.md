# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 4

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | -0.3180 | -1.0560 |
| data_changes | 0 | clusterTest_afterMean | 80.1520 | 79.6500 |
| data_changes | 0 | clusterTest_afterStd | 0.5622 | 0.2619 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | -0.1590 | -0.5280 |
| data_changes | 0 | globalTest_afterMean | 40.0760 | 39.8250 |
| data_changes | 0 | globalTest_afterStd | 0.2811 | 0.1309 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 12.9640 | 3.0040 |
| data_changes | 1 | clusterTest_afterMean | 85.6780 | 87.0940 |
| data_changes | 1 | clusterTest_afterStd | 3.9985 | 0.9924 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 6.4820 | 1.5020 |
| data_changes | 1 | globalTest_afterMean | 42.8390 | 43.5470 |
| data_changes | 1 | globalTest_afterStd | 1.9992 | 0.4962 |
