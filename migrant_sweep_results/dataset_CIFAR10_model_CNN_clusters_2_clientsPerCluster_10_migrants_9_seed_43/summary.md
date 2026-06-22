# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 9

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 12.6440 | 12.5640 |
| data_changes | 0 | clusterTest_afterMean | 73.9260 | 72.1840 |
| data_changes | 0 | clusterTest_afterStd | 3.3778 | 3.5052 |
| data_changes | 0 | clusterTest_recovery | 14 | -1 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 6.3220 | 6.2820 |
| data_changes | 0 | globalTest_afterMean | 36.9630 | 36.0920 |
| data_changes | 0 | globalTest_afterStd | 1.6889 | 1.7526 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 14.7400 | 4.6940 |
| data_changes | 1 | clusterTest_afterMean | 84.4100 | 87.0600 |
| data_changes | 1 | clusterTest_afterStd | 4.8708 | 1.6503 |
| data_changes | 1 | clusterTest_recovery | 6 | 3 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 7.3700 | 2.3470 |
| data_changes | 1 | globalTest_afterMean | 42.2050 | 43.5300 |
| data_changes | 1 | globalTest_afterStd | 2.4354 | 0.8252 |
