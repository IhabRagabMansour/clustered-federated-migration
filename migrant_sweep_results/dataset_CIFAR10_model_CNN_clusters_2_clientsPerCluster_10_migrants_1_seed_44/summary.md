# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 1

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 1.1280 | 0.2440 |
| data_changes | 0 | clusterTest_afterMean | 80.1320 | 79.7780 |
| data_changes | 0 | clusterTest_afterStd | 1.0423 | 0.7614 |
| data_changes | 0 | clusterTest_recovery | 1 | 0 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 0.5640 | 0.1220 |
| data_changes | 0 | globalTest_afterMean | 40.0660 | 39.8890 |
| data_changes | 0 | globalTest_afterStd | 0.5212 | 0.3807 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 0.8340 | -0.4340 |
| data_changes | 1 | clusterTest_afterMean | 88.4240 | 88.2220 |
| data_changes | 1 | clusterTest_afterStd | 0.5097 | 0.2007 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 0.4170 | -0.2170 |
| data_changes | 1 | globalTest_afterMean | 44.2120 | 44.1110 |
| data_changes | 1 | globalTest_afterStd | 0.2548 | 0.1003 |
