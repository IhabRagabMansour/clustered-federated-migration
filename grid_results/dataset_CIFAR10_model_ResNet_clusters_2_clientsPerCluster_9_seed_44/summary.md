# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 68.9040 | 68.0500 |
| membership_only | 0 | clusterTest_maxDrop | 0.1240 | 0.3300 |
| membership_only | 0 | clusterTest_afterMean | 69.3140 | 68.2500 |
| membership_only | 0 | clusterTest_afterStd | 0.2088 | 0.3500 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.4520 | 34.0250 |
| membership_only | 0 | globalTest_maxDrop | 0.0620 | 0.1650 |
| membership_only | 0 | globalTest_afterMean | 34.6570 | 34.1250 |
| membership_only | 0 | globalTest_afterStd | 0.1044 | 0.1750 |
| membership_only | 1 | clusterTest_before | 78.4040 | 77.8780 |
| membership_only | 1 | clusterTest_maxDrop | 59.3640 | 63.1580 |
| membership_only | 1 | clusterTest_afterMean | 50.8120 | 52.1580 |
| membership_only | 1 | clusterTest_afterStd | 25.7189 | 25.1799 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 39.2020 | 38.9390 |
| membership_only | 1 | globalTest_maxDrop | 9.3520 | 5.6190 |
| membership_only | 1 | globalTest_afterMean | 36.2900 | 38.0340 |
| membership_only | 1 | globalTest_afterStd | 3.2626 | 1.6542 |
| data_changes | 0 | clusterTest_before | 68.9040 | 68.0500 |
| data_changes | 0 | clusterTest_maxDrop | 0.1240 | 1.3700 |
| data_changes | 0 | clusterTest_afterMean | 69.3140 | 67.9060 |
| data_changes | 0 | clusterTest_afterStd | 0.2088 | 0.5493 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 34.4520 | 34.0250 |
| data_changes | 0 | globalTest_maxDrop | 0.0620 | 0.6750 |
| data_changes | 0 | globalTest_afterMean | 34.6570 | 33.9540 |
| data_changes | 0 | globalTest_afterStd | 0.1044 | 0.2724 |
| data_changes | 1 | clusterTest_before | 78.4040 | 77.8780 |
| data_changes | 1 | clusterTest_maxDrop | 7.7040 | 5.4380 |
| data_changes | 1 | clusterTest_afterMean | 76.7800 | 77.2440 |
| data_changes | 1 | clusterTest_afterStd | 2.3497 | 1.8810 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 39.2020 | 38.9390 |
| data_changes | 1 | globalTest_maxDrop | 3.8520 | 2.7190 |
| data_changes | 1 | globalTest_afterMean | 38.3900 | 38.6220 |
| data_changes | 1 | globalTest_afterStd | 1.1748 | 0.9405 |
