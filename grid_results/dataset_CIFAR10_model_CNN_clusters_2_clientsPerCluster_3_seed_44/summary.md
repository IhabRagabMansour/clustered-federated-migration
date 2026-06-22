# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 83.6540 | 83.3860 |
| membership_only | 0 | clusterTest_maxDrop | 12.8540 | 14.8460 |
| membership_only | 0 | clusterTest_afterMean | 80.9440 | 80.4960 |
| membership_only | 0 | clusterTest_afterStd | 3.5917 | 4.0968 |
| membership_only | 0 | clusterTest_recovery | 5 | 5 |
| membership_only | 0 | globalTest_before | 41.8270 | 41.6930 |
| membership_only | 0 | globalTest_maxDrop | 6.4270 | 7.4230 |
| membership_only | 0 | globalTest_afterMean | 40.4720 | 40.2480 |
| membership_only | 0 | globalTest_afterStd | 1.7958 | 2.0484 |
| membership_only | 1 | clusterTest_before | 90.3280 | 89.8800 |
| membership_only | 1 | clusterTest_maxDrop | 75.0280 | 71.7200 |
| membership_only | 1 | clusterTest_afterMean | 59.8560 | 66.4880 |
| membership_only | 1 | clusterTest_afterStd | 29.0176 | 27.6503 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 45.1640 | 44.9400 |
| membership_only | 1 | globalTest_maxDrop | 1.1640 | -0.1200 |
| membership_only | 1 | globalTest_afterMean | 49.7190 | 56.0380 |
| membership_only | 1 | globalTest_afterStd | 5.0592 | 7.6346 |
| data_changes | 0 | clusterTest_before | 83.6540 | 83.3860 |
| data_changes | 0 | clusterTest_maxDrop | 12.8540 | 12.2060 |
| data_changes | 0 | clusterTest_afterMean | 80.9440 | 80.5740 |
| data_changes | 0 | clusterTest_afterStd | 3.5917 | 3.3581 |
| data_changes | 0 | clusterTest_recovery | 5 | 5 |
| data_changes | 0 | globalTest_before | 41.8270 | 41.6930 |
| data_changes | 0 | globalTest_maxDrop | 6.4270 | 6.1030 |
| data_changes | 0 | globalTest_afterMean | 40.4720 | 40.2870 |
| data_changes | 0 | globalTest_afterStd | 1.7958 | 1.6791 |
| data_changes | 1 | clusterTest_before | 90.3280 | 89.8800 |
| data_changes | 1 | clusterTest_maxDrop | 25.0280 | 1.6400 |
| data_changes | 1 | clusterTest_afterMean | 87.7440 | 90.5260 |
| data_changes | 1 | clusterTest_afterStd | 7.5526 | 0.8533 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 45.1640 | 44.9400 |
| data_changes | 1 | globalTest_maxDrop | 12.5140 | 0.8200 |
| data_changes | 1 | globalTest_afterMean | 43.8720 | 45.2630 |
| data_changes | 1 | globalTest_afterStd | 3.7763 | 0.4267 |
