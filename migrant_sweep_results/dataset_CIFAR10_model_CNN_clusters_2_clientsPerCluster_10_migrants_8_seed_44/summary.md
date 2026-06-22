# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 8

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 4.9480 | 3.8440 |
| data_changes | 0 | clusterTest_afterMean | 77.4380 | 76.8900 |
| data_changes | 0 | clusterTest_afterStd | 1.5048 | 1.0678 |
| data_changes | 0 | clusterTest_recovery | 8 | 8 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 2.4740 | 1.9220 |
| data_changes | 0 | globalTest_afterMean | 38.7190 | 38.4450 |
| data_changes | 0 | globalTest_afterStd | 0.7524 | 0.5339 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 31.6740 | 6.7260 |
| data_changes | 1 | clusterTest_afterMean | 82.2260 | 86.5660 |
| data_changes | 1 | clusterTest_afterStd | 9.5295 | 2.0305 |
| data_changes | 1 | clusterTest_recovery | 5 | 2 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 15.8370 | 3.3630 |
| data_changes | 1 | globalTest_afterMean | 41.1130 | 43.2830 |
| data_changes | 1 | globalTest_afterStd | 4.7647 | 1.0152 |
