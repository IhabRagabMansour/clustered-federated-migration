# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 1.9480 | 2.0040 |
| data_changes | 0 | clusterTest_afterMean | 79.9560 | 79.4400 |
| data_changes | 0 | clusterTest_afterStd | 1.3730 | 1.3742 |
| data_changes | 0 | clusterTest_recovery | 8 | 8 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 0.9740 | 1.0020 |
| data_changes | 0 | globalTest_afterMean | 39.9780 | 39.7200 |
| data_changes | 0 | globalTest_afterStd | 0.6865 | 0.6871 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 4.7340 | 1.0060 |
| data_changes | 1 | clusterTest_afterMean | 87.9220 | 87.9960 |
| data_changes | 1 | clusterTest_afterStd | 1.6720 | 0.6140 |
| data_changes | 1 | clusterTest_recovery | 1 | 1 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 2.3670 | 0.5030 |
| data_changes | 1 | globalTest_afterMean | 43.9610 | 43.9980 |
| data_changes | 1 | globalTest_afterStd | 0.8360 | 0.3070 |
