# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 1

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | -0.2780 | -0.5760 |
| data_changes | 0 | clusterTest_afterMean | 80.5560 | 79.6520 |
| data_changes | 0 | clusterTest_afterStd | 0.9292 | 0.7803 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | -0.1390 | -0.2880 |
| data_changes | 0 | globalTest_afterMean | 40.2780 | 39.8260 |
| data_changes | 0 | globalTest_afterStd | 0.4646 | 0.3902 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 1.7640 | 0.3240 |
| data_changes | 1 | clusterTest_afterMean | 88.3680 | 87.9500 |
| data_changes | 1 | clusterTest_afterStd | 0.7918 | 0.4492 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 0.8820 | 0.1620 |
| data_changes | 1 | globalTest_afterMean | 44.1840 | 43.9750 |
| data_changes | 1 | globalTest_afterStd | 0.3959 | 0.2246 |
