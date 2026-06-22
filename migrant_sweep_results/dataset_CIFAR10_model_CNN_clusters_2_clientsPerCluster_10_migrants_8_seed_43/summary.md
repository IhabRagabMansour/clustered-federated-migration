# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 8

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 4.1640 | 2.3440 |
| data_changes | 0 | clusterTest_afterMean | 78.8000 | 78.6740 |
| data_changes | 0 | clusterTest_afterStd | 1.2118 | 1.0261 |
| data_changes | 0 | clusterTest_recovery | 5 | 3 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 2.0820 | 1.1720 |
| data_changes | 0 | globalTest_afterMean | 39.4000 | 39.3370 |
| data_changes | 0 | globalTest_afterStd | 0.6059 | 0.5131 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 13.2400 | 4.5140 |
| data_changes | 1 | clusterTest_afterMean | 84.6360 | 87.2240 |
| data_changes | 1 | clusterTest_afterStd | 4.7308 | 1.5929 |
| data_changes | 1 | clusterTest_recovery | 5 | 3 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 6.6200 | 2.2570 |
| data_changes | 1 | globalTest_afterMean | 42.3180 | 43.6120 |
| data_changes | 1 | globalTest_afterStd | 2.3654 | 0.7965 |
