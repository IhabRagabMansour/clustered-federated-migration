# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 69.6840 | 68.7840 |
| membership_only | 0 | clusterTest_maxDrop | 0.1640 | 0.9240 |
| membership_only | 0 | clusterTest_afterMean | 69.8240 | 68.6280 |
| membership_only | 0 | clusterTest_afterStd | 0.1574 | 0.5089 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.8420 | 34.3920 |
| membership_only | 0 | globalTest_maxDrop | 0.0820 | 0.4620 |
| membership_only | 0 | globalTest_afterMean | 34.9120 | 34.3140 |
| membership_only | 0 | globalTest_afterStd | 0.0787 | 0.2544 |
| membership_only | 1 | clusterTest_before | 79.8320 | 78.2640 |
| membership_only | 1 | clusterTest_maxDrop | 76.7120 | 74.7440 |
| membership_only | 1 | clusterTest_afterMean | 44.0760 | 44.1920 |
| membership_only | 1 | clusterTest_afterStd | 31.6740 | 30.9708 |
| membership_only | 1 | clusterTest_recovery | 10 | 8 |
| membership_only | 1 | globalTest_before | 39.9160 | 39.1320 |
| membership_only | 1 | globalTest_maxDrop | 15.1660 | 10.3020 |
| membership_only | 1 | globalTest_afterMean | 32.9890 | 35.4510 |
| membership_only | 1 | globalTest_afterStd | 5.0555 | 3.1716 |
| data_changes | 0 | clusterTest_before | 69.6840 | 68.7840 |
| data_changes | 0 | clusterTest_maxDrop | 0.1640 | 0.8840 |
| data_changes | 0 | clusterTest_afterMean | 69.8240 | 68.6160 |
| data_changes | 0 | clusterTest_afterStd | 0.1574 | 0.5466 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 34.8420 | 34.3920 |
| data_changes | 0 | globalTest_maxDrop | 0.0820 | 0.4320 |
| data_changes | 0 | globalTest_afterMean | 34.9120 | 34.3100 |
| data_changes | 0 | globalTest_afterStd | 0.0787 | 0.2717 |
| data_changes | 1 | clusterTest_before | 79.8320 | 78.2640 |
| data_changes | 1 | clusterTest_maxDrop | 14.2720 | 5.9040 |
| data_changes | 1 | clusterTest_afterMean | 76.9700 | 77.5100 |
| data_changes | 1 | clusterTest_afterStd | 4.4734 | 2.3690 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 39.9160 | 39.1320 |
| data_changes | 1 | globalTest_maxDrop | 7.1360 | 2.9520 |
| data_changes | 1 | globalTest_afterMean | 38.4850 | 38.7550 |
| data_changes | 1 | globalTest_afterStd | 2.2367 | 1.1845 |
