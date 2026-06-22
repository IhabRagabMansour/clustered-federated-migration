# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 68.7320 | 68.0680 |
| membership_only | 0 | clusterTest_maxDrop | 0.0520 | -0.0320 |
| membership_only | 0 | clusterTest_afterMean | 69.1420 | 68.3220 |
| membership_only | 0 | clusterTest_afterStd | 0.2878 | 0.1712 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.3660 | 34.0340 |
| membership_only | 0 | globalTest_maxDrop | 0.0260 | -0.0160 |
| membership_only | 0 | globalTest_afterMean | 34.5710 | 34.1610 |
| membership_only | 0 | globalTest_afterStd | 0.1439 | 0.0856 |
| membership_only | 1 | clusterTest_before | 79.0220 | 78.3080 |
| membership_only | 1 | clusterTest_maxDrop | 65.5620 | 63.2080 |
| membership_only | 1 | clusterTest_afterMean | 50.6280 | 50.9800 |
| membership_only | 1 | clusterTest_afterStd | 25.9651 | 24.6429 |
| membership_only | 1 | clusterTest_recovery | 6 | 8 |
| membership_only | 1 | globalTest_before | 39.5110 | 39.1540 |
| membership_only | 1 | globalTest_maxDrop | 9.9610 | 6.2640 |
| membership_only | 1 | globalTest_afterMean | 36.1270 | 37.8320 |
| membership_only | 1 | globalTest_afterStd | 3.0436 | 2.1394 |
| data_changes | 0 | clusterTest_before | 68.7320 | 68.0680 |
| data_changes | 0 | clusterTest_maxDrop | 0.0520 | 1.4680 |
| data_changes | 0 | clusterTest_afterMean | 69.1420 | 68.0320 |
| data_changes | 0 | clusterTest_afterStd | 0.2878 | 0.5882 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 34.3660 | 34.0340 |
| data_changes | 0 | globalTest_maxDrop | 0.0260 | 0.7340 |
| data_changes | 0 | globalTest_afterMean | 34.5710 | 34.0160 |
| data_changes | 0 | globalTest_afterStd | 0.1439 | 0.2941 |
| data_changes | 1 | clusterTest_before | 79.0220 | 78.3080 |
| data_changes | 1 | clusterTest_maxDrop | 12.0820 | 8.2080 |
| data_changes | 1 | clusterTest_afterMean | 76.9720 | 77.0960 |
| data_changes | 1 | clusterTest_afterStd | 3.5009 | 2.6720 |
| data_changes | 1 | clusterTest_recovery | 4 | 3 |
| data_changes | 1 | globalTest_before | 39.5110 | 39.1540 |
| data_changes | 1 | globalTest_maxDrop | 6.0410 | 4.1040 |
| data_changes | 1 | globalTest_afterMean | 38.4860 | 38.5480 |
| data_changes | 1 | globalTest_afterStd | 1.7505 | 1.3360 |
