# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 0.9040 | 0.2640 |
| data_changes | 0 | clusterTest_afterMean | 80.6880 | 80.2980 |
| data_changes | 0 | clusterTest_afterStd | 0.7471 | 0.6714 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 0.4520 | 0.1320 |
| data_changes | 0 | globalTest_afterMean | 40.3440 | 40.1490 |
| data_changes | 0 | globalTest_afterStd | 0.3736 | 0.3357 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 4.3200 | 2.0540 |
| data_changes | 1 | clusterTest_afterMean | 87.7780 | 87.8200 |
| data_changes | 1 | clusterTest_afterStd | 1.4422 | 0.9598 |
| data_changes | 1 | clusterTest_recovery | 1 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 2.1600 | 1.0270 |
| data_changes | 1 | globalTest_afterMean | 43.8890 | 43.9100 |
| data_changes | 1 | globalTest_afterStd | 0.7211 | 0.4799 |
