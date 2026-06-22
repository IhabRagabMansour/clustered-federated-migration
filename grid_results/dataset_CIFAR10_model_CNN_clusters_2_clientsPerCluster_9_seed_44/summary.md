# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 79.9800 | 79.4500 |
| membership_only | 0 | clusterTest_maxDrop | 1.5800 | 1.9700 |
| membership_only | 0 | clusterTest_afterMean | 80.3600 | 79.6760 |
| membership_only | 0 | clusterTest_afterStd | 1.1560 | 1.2015 |
| membership_only | 0 | clusterTest_recovery | 9 | 9 |
| membership_only | 0 | globalTest_before | 39.9900 | 39.7250 |
| membership_only | 0 | globalTest_maxDrop | 0.7900 | 0.9850 |
| membership_only | 0 | globalTest_afterMean | 40.1800 | 39.8380 |
| membership_only | 0 | globalTest_afterStd | 0.5780 | 0.6007 |
| membership_only | 1 | clusterTest_before | 87.5160 | 87.1060 |
| membership_only | 1 | clusterTest_maxDrop | 66.1960 | 63.8660 |
| membership_only | 1 | clusterTest_afterMean | 67.8040 | 63.9980 |
| membership_only | 1 | clusterTest_afterStd | 21.0905 | 24.0999 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 43.7580 | 43.5530 |
| membership_only | 1 | globalTest_maxDrop | 1.1980 | 3.2430 |
| membership_only | 1 | globalTest_afterMean | 47.7620 | 47.5100 |
| membership_only | 1 | globalTest_afterStd | 6.0554 | 6.6417 |
| data_changes | 0 | clusterTest_before | 79.9800 | 79.4500 |
| data_changes | 0 | clusterTest_maxDrop | 1.5800 | 1.9700 |
| data_changes | 0 | clusterTest_afterMean | 80.3600 | 79.6720 |
| data_changes | 0 | clusterTest_afterStd | 1.1560 | 1.2332 |
| data_changes | 0 | clusterTest_recovery | 9 | 9 |
| data_changes | 0 | globalTest_before | 39.9900 | 39.7250 |
| data_changes | 0 | globalTest_maxDrop | 0.7900 | 0.9850 |
| data_changes | 0 | globalTest_afterMean | 40.1800 | 39.8360 |
| data_changes | 0 | globalTest_afterStd | 0.5780 | 0.6166 |
| data_changes | 1 | clusterTest_before | 87.5160 | 87.1060 |
| data_changes | 1 | clusterTest_maxDrop | 13.9160 | 2.3660 |
| data_changes | 1 | clusterTest_afterMean | 86.4260 | 87.6620 |
| data_changes | 1 | clusterTest_afterStd | 4.4254 | 1.1498 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 43.7580 | 43.5530 |
| data_changes | 1 | globalTest_maxDrop | 6.9580 | 1.1830 |
| data_changes | 1 | globalTest_afterMean | 43.2130 | 43.8310 |
| data_changes | 1 | globalTest_afterStd | 2.2127 | 0.5749 |
