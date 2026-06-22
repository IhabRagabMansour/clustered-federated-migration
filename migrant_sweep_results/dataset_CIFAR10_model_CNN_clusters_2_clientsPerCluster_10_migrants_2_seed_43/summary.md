# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | -0.3560 | -0.7360 |
| data_changes | 0 | clusterTest_afterMean | 81.2540 | 80.6800 |
| data_changes | 0 | clusterTest_afterStd | 0.3527 | 0.2831 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | -0.1780 | -0.3680 |
| data_changes | 0 | globalTest_afterMean | 40.6270 | 40.3400 |
| data_changes | 0 | globalTest_afterStd | 0.1764 | 0.1416 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 2.6400 | 1.4940 |
| data_changes | 1 | clusterTest_afterMean | 87.9400 | 87.8060 |
| data_changes | 1 | clusterTest_afterStd | 1.0123 | 0.8025 |
| data_changes | 1 | clusterTest_recovery | 2 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 1.3200 | 0.7470 |
| data_changes | 1 | globalTest_afterMean | 43.9700 | 43.9030 |
| data_changes | 1 | globalTest_afterStd | 0.5062 | 0.4013 |
