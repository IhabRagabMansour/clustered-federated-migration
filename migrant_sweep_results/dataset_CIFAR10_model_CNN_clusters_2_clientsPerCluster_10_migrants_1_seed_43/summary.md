# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 1

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 0.3840 | -0.4160 |
| data_changes | 0 | clusterTest_afterMean | 81.1040 | 80.6460 |
| data_changes | 0 | clusterTest_afterStd | 0.7276 | 0.5946 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 0.1920 | -0.2080 |
| data_changes | 0 | globalTest_afterMean | 40.5520 | 40.3230 |
| data_changes | 0 | globalTest_afterStd | 0.3638 | 0.2973 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 1.4200 | 0.5340 |
| data_changes | 1 | clusterTest_afterMean | 88.3620 | 88.1940 |
| data_changes | 1 | clusterTest_afterStd | 0.7132 | 0.6151 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 0.7100 | 0.2670 |
| data_changes | 1 | globalTest_afterMean | 44.1810 | 44.0970 |
| data_changes | 1 | globalTest_afterStd | 0.3566 | 0.3075 |
