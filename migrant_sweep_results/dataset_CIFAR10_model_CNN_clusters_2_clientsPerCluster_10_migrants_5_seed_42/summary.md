# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 5

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 0.8820 | 1.1240 |
| data_changes | 0 | clusterTest_afterMean | 79.1360 | 78.6600 |
| data_changes | 0 | clusterTest_afterStd | 0.6673 | 0.7635 |
| data_changes | 0 | clusterTest_recovery | 0 | 9 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 0.4410 | 0.5620 |
| data_changes | 0 | globalTest_afterMean | 39.5680 | 39.3300 |
| data_changes | 0 | globalTest_afterStd | 0.3337 | 0.3817 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 14.2040 | 4.3840 |
| data_changes | 1 | clusterTest_afterMean | 85.0000 | 87.0720 |
| data_changes | 1 | clusterTest_afterStd | 4.7670 | 1.4632 |
| data_changes | 1 | clusterTest_recovery | 5 | 1 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 7.1020 | 2.1920 |
| data_changes | 1 | globalTest_afterMean | 42.5000 | 43.5360 |
| data_changes | 1 | globalTest_afterStd | 2.3835 | 0.7316 |
