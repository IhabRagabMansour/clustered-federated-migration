# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 74.2980 | 72.6640 |
| membership_only | 0 | clusterTest_maxDrop | 0.3580 | 21.2240 |
| membership_only | 0 | clusterTest_afterMean | 74.0500 | 68.6380 |
| membership_only | 0 | clusterTest_afterStd | 0.0913 | 6.1539 |
| membership_only | 0 | clusterTest_recovery | 0 | 7 |
| membership_only | 0 | globalTest_before | 37.1490 | 36.3320 |
| membership_only | 0 | globalTest_maxDrop | 0.1790 | 10.6120 |
| membership_only | 0 | globalTest_afterMean | 37.0250 | 34.3190 |
| membership_only | 0 | globalTest_afterStd | 0.0457 | 3.0770 |
| membership_only | 1 | clusterTest_before | 82.4140 | 80.2380 |
| membership_only | 1 | clusterTest_maxDrop | 82.4140 | 80.2380 |
| membership_only | 1 | clusterTest_afterMean | 38.4500 | 38.1180 |
| membership_only | 1 | clusterTest_afterStd | 38.6796 | 37.6524 |
| membership_only | 1 | clusterTest_recovery | 10 | 4 |
| membership_only | 1 | globalTest_before | 41.2070 | 40.1190 |
| membership_only | 1 | globalTest_maxDrop | 15.7570 | 13.7390 |
| membership_only | 1 | globalTest_afterMean | 33.9750 | 34.4970 |
| membership_only | 1 | globalTest_afterStd | 5.4977 | 5.2170 |
| data_changes | 0 | clusterTest_before | 74.2980 | 72.6640 |
| data_changes | 0 | clusterTest_maxDrop | 0.3580 | 17.2240 |
| data_changes | 0 | clusterTest_afterMean | 74.0500 | 68.2560 |
| data_changes | 0 | clusterTest_afterStd | 0.0913 | 4.7306 |
| data_changes | 0 | clusterTest_recovery | 0 | 8 |
| data_changes | 0 | globalTest_before | 37.1490 | 36.3320 |
| data_changes | 0 | globalTest_maxDrop | 0.1790 | 8.6120 |
| data_changes | 0 | globalTest_afterMean | 37.0250 | 34.1440 |
| data_changes | 0 | globalTest_afterStd | 0.0457 | 2.3725 |
| data_changes | 1 | clusterTest_before | 82.4140 | 80.2380 |
| data_changes | 1 | clusterTest_maxDrop | 25.0140 | 14.9580 |
| data_changes | 1 | clusterTest_afterMean | 78.9480 | 79.9280 |
| data_changes | 1 | clusterTest_afterStd | 7.2835 | 4.9618 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 41.2070 | 40.1190 |
| data_changes | 1 | globalTest_maxDrop | 12.5070 | 7.4790 |
| data_changes | 1 | globalTest_afterMean | 39.4740 | 39.9640 |
| data_changes | 1 | globalTest_afterStd | 3.6418 | 2.4809 |
