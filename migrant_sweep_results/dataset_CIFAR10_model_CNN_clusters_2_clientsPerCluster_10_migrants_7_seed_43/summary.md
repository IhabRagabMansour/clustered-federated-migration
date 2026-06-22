# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 7

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 5.7240 | 5.2840 |
| data_changes | 0 | clusterTest_afterMean | 78.0380 | 77.7020 |
| data_changes | 0 | clusterTest_afterStd | 2.0511 | 1.8643 |
| data_changes | 0 | clusterTest_recovery | 10 | 10 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 2.8620 | 2.6420 |
| data_changes | 0 | globalTest_afterMean | 39.0190 | 38.8510 |
| data_changes | 0 | globalTest_afterStd | 1.0255 | 0.9322 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 11.6600 | 4.1940 |
| data_changes | 1 | clusterTest_afterMean | 85.1540 | 87.3000 |
| data_changes | 1 | clusterTest_afterStd | 4.2418 | 1.4693 |
| data_changes | 1 | clusterTest_recovery | 5 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 5.8300 | 2.0970 |
| data_changes | 1 | globalTest_afterMean | 42.5770 | 43.6500 |
| data_changes | 1 | globalTest_afterStd | 2.1209 | 0.7346 |
