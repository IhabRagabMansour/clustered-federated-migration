# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 71.5540 | 70.7740 |
| membership_only | 0 | clusterTest_maxDrop | 0.5140 | 9.6740 |
| membership_only | 0 | clusterTest_afterMean | 71.2060 | 68.6580 |
| membership_only | 0 | clusterTest_afterStd | 0.1024 | 2.9118 |
| membership_only | 0 | clusterTest_recovery | 0 | 7 |
| membership_only | 0 | globalTest_before | 35.7770 | 35.3870 |
| membership_only | 0 | globalTest_maxDrop | 0.2570 | 4.8370 |
| membership_only | 0 | globalTest_afterMean | 35.6030 | 34.3290 |
| membership_only | 0 | globalTest_afterStd | 0.0512 | 1.4559 |
| membership_only | 1 | clusterTest_before | 79.8660 | 79.2400 |
| membership_only | 1 | clusterTest_maxDrop | 79.8660 | 79.2400 |
| membership_only | 1 | clusterTest_afterMean | 37.9040 | 38.9300 |
| membership_only | 1 | clusterTest_afterStd | 37.9913 | 36.3460 |
| membership_only | 1 | clusterTest_recovery | 8 | 4 |
| membership_only | 1 | globalTest_before | 39.9330 | 39.6200 |
| membership_only | 1 | globalTest_maxDrop | 15.1530 | 12.2700 |
| membership_only | 1 | globalTest_afterMean | 32.8480 | 34.8550 |
| membership_only | 1 | globalTest_afterStd | 5.3995 | 4.6539 |
| data_changes | 0 | clusterTest_before | 71.5540 | 70.7740 |
| data_changes | 0 | clusterTest_maxDrop | 0.5140 | 9.6340 |
| data_changes | 0 | clusterTest_afterMean | 71.2060 | 67.6720 |
| data_changes | 0 | clusterTest_afterStd | 0.1024 | 3.2837 |
| data_changes | 0 | clusterTest_recovery | 0 | 6 |
| data_changes | 0 | globalTest_before | 35.7770 | 35.3870 |
| data_changes | 0 | globalTest_maxDrop | 0.2570 | 4.8170 |
| data_changes | 0 | globalTest_afterMean | 35.6030 | 33.8430 |
| data_changes | 0 | globalTest_afterStd | 0.0512 | 1.6416 |
| data_changes | 1 | clusterTest_before | 79.8660 | 79.2400 |
| data_changes | 1 | clusterTest_maxDrop | 24.9860 | 12.1400 |
| data_changes | 1 | clusterTest_afterMean | 76.1860 | 78.2600 |
| data_changes | 1 | clusterTest_afterStd | 7.8751 | 3.8992 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.9330 | 39.6200 |
| data_changes | 1 | globalTest_maxDrop | 12.4930 | 6.0700 |
| data_changes | 1 | globalTest_afterMean | 38.0930 | 39.1300 |
| data_changes | 1 | globalTest_afterStd | 3.9375 | 1.9496 |
