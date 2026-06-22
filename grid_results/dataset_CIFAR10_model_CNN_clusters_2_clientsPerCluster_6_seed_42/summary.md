# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 81.5000 | 81.0120 |
| membership_only | 0 | clusterTest_maxDrop | 3.7400 | 4.5320 |
| membership_only | 0 | clusterTest_afterMean | 79.9920 | 78.7680 |
| membership_only | 0 | clusterTest_afterStd | 1.3434 | 1.5099 |
| membership_only | 0 | clusterTest_recovery | 10 | 10 |
| membership_only | 0 | globalTest_before | 40.7500 | 40.5060 |
| membership_only | 0 | globalTest_maxDrop | 1.8700 | 2.2660 |
| membership_only | 0 | globalTest_afterMean | 39.9960 | 39.3840 |
| membership_only | 0 | globalTest_afterStd | 0.6717 | 0.7549 |
| membership_only | 1 | clusterTest_before | 89.5660 | 89.1200 |
| membership_only | 1 | clusterTest_maxDrop | 86.9660 | 88.0200 |
| membership_only | 1 | clusterTest_afterMean | 49.6700 | 48.8700 |
| membership_only | 1 | clusterTest_afterStd | 37.6279 | 37.9108 |
| membership_only | 1 | clusterTest_recovery | 18 | 12 |
| membership_only | 1 | globalTest_before | 44.7830 | 44.5600 |
| membership_only | 1 | globalTest_maxDrop | 7.2230 | 8.0800 |
| membership_only | 1 | globalTest_afterMean | 42.1960 | 43.5730 |
| membership_only | 1 | globalTest_afterStd | 2.9117 | 3.5292 |
| data_changes | 0 | clusterTest_before | 81.5000 | 81.0120 |
| data_changes | 0 | clusterTest_maxDrop | 3.7400 | 5.2120 |
| data_changes | 0 | clusterTest_afterMean | 79.9920 | 79.1120 |
| data_changes | 0 | clusterTest_afterStd | 1.3434 | 1.6599 |
| data_changes | 0 | clusterTest_recovery | 10 | 10 |
| data_changes | 0 | globalTest_before | 40.7500 | 40.5060 |
| data_changes | 0 | globalTest_maxDrop | 1.8700 | 2.6060 |
| data_changes | 0 | globalTest_afterMean | 39.9960 | 39.5560 |
| data_changes | 0 | globalTest_afterStd | 0.6717 | 0.8300 |
| data_changes | 1 | clusterTest_before | 89.5660 | 89.1200 |
| data_changes | 1 | clusterTest_maxDrop | 22.6860 | 1.9600 |
| data_changes | 1 | clusterTest_afterMean | 86.4980 | 89.1160 |
| data_changes | 1 | clusterTest_afterStd | 6.7874 | 0.9424 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 44.7830 | 44.5600 |
| data_changes | 1 | globalTest_maxDrop | 11.3430 | 0.9800 |
| data_changes | 1 | globalTest_afterMean | 43.2490 | 44.5580 |
| data_changes | 1 | globalTest_afterStd | 3.3937 | 0.4712 |
