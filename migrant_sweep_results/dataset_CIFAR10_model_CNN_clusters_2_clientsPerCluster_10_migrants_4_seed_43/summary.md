# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 4

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 0.9040 | 0.2240 |
| data_changes | 0 | clusterTest_afterMean | 80.4840 | 80.1420 |
| data_changes | 0 | clusterTest_afterStd | 0.9038 | 0.6490 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 0.4520 | 0.1120 |
| data_changes | 0 | globalTest_afterMean | 40.2420 | 40.0710 |
| data_changes | 0 | globalTest_afterStd | 0.4519 | 0.3245 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 5.6600 | 2.7940 |
| data_changes | 1 | clusterTest_afterMean | 87.1140 | 87.6580 |
| data_changes | 1 | clusterTest_afterStd | 1.9291 | 1.1957 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 2.8300 | 1.3970 |
| data_changes | 1 | globalTest_afterMean | 43.5570 | 43.8290 |
| data_changes | 1 | globalTest_afterStd | 0.9645 | 0.5979 |
