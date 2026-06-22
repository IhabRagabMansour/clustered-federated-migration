# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 5

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 0.3840 | 0.2840 |
| data_changes | 0 | clusterTest_afterMean | 80.5980 | 79.9260 |
| data_changes | 0 | clusterTest_afterStd | 0.5042 | 0.6184 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 0.1920 | 0.1420 |
| data_changes | 0 | globalTest_afterMean | 40.2990 | 39.9630 |
| data_changes | 0 | globalTest_afterStd | 0.2521 | 0.3092 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 7.2600 | 3.3740 |
| data_changes | 1 | clusterTest_afterMean | 86.4980 | 87.6120 |
| data_changes | 1 | clusterTest_afterStd | 2.8628 | 1.3189 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 3.6300 | 1.6870 |
| data_changes | 1 | globalTest_afterMean | 43.2490 | 43.8060 |
| data_changes | 1 | globalTest_afterStd | 1.4314 | 0.6594 |
