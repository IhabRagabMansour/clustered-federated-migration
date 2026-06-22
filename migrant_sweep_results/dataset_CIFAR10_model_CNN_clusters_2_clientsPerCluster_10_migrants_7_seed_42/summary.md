# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 7

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 2.4620 | 4.2240 |
| data_changes | 0 | clusterTest_afterMean | 78.4560 | 77.1400 |
| data_changes | 0 | clusterTest_afterStd | 1.0927 | 1.3223 |
| data_changes | 0 | clusterTest_recovery | 1 | 3 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 1.2310 | 2.1120 |
| data_changes | 0 | globalTest_afterMean | 39.2280 | 38.5700 |
| data_changes | 0 | globalTest_afterStd | 0.5463 | 0.6611 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 20.4840 | 5.3040 |
| data_changes | 1 | clusterTest_afterMean | 83.4860 | 86.4060 |
| data_changes | 1 | clusterTest_afterStd | 6.2089 | 1.5473 |
| data_changes | 1 | clusterTest_recovery | 6 | 3 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 10.2420 | 2.6520 |
| data_changes | 1 | globalTest_afterMean | 41.7430 | 43.2030 |
| data_changes | 1 | globalTest_afterStd | 3.1044 | 0.7737 |
