# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 6

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 1.2020 | 1.5840 |
| data_changes | 0 | clusterTest_afterMean | 79.7060 | 78.6980 |
| data_changes | 0 | clusterTest_afterStd | 1.0199 | 0.8502 |
| data_changes | 0 | clusterTest_recovery | 8 | 8 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 0.6010 | 0.7920 |
| data_changes | 0 | globalTest_afterMean | 39.8530 | 39.3490 |
| data_changes | 0 | globalTest_afterStd | 0.5100 | 0.4251 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 17.4640 | 4.3840 |
| data_changes | 1 | clusterTest_afterMean | 83.8800 | 86.7240 |
| data_changes | 1 | clusterTest_afterStd | 5.6744 | 1.4272 |
| data_changes | 1 | clusterTest_recovery | 4 | 3 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 8.7320 | 2.1920 |
| data_changes | 1 | globalTest_afterMean | 41.9400 | 43.3620 |
| data_changes | 1 | globalTest_afterStd | 2.8372 | 0.7136 |
