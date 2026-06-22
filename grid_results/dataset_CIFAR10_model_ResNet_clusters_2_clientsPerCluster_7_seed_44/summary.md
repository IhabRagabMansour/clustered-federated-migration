# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.7500 | 69.7280 |
| membership_only | 0 | clusterTest_maxDrop | 0.1900 | 1.2480 |
| membership_only | 0 | clusterTest_afterMean | 70.8280 | 69.5800 |
| membership_only | 0 | clusterTest_afterStd | 0.1357 | 0.4358 |
| membership_only | 0 | clusterTest_recovery | 0 | 6 |
| membership_only | 0 | globalTest_before | 35.3750 | 34.8640 |
| membership_only | 0 | globalTest_maxDrop | 0.0950 | 0.6240 |
| membership_only | 0 | globalTest_afterMean | 35.4140 | 34.7900 |
| membership_only | 0 | globalTest_afterStd | 0.0679 | 0.2179 |
| membership_only | 1 | clusterTest_before | 80.2460 | 78.4140 |
| membership_only | 1 | clusterTest_maxDrop | 80.0260 | 78.2340 |
| membership_only | 1 | clusterTest_afterMean | 41.8420 | 41.7040 |
| membership_only | 1 | clusterTest_afterStd | 34.9261 | 34.3600 |
| membership_only | 1 | clusterTest_recovery | 10 | 4 |
| membership_only | 1 | globalTest_before | 40.1230 | 39.2070 |
| membership_only | 1 | globalTest_maxDrop | 14.4630 | 11.3870 |
| membership_only | 1 | globalTest_afterMean | 33.3940 | 34.7940 |
| membership_only | 1 | globalTest_afterStd | 5.4749 | 4.0804 |
| data_changes | 0 | clusterTest_before | 70.7500 | 69.7280 |
| data_changes | 0 | clusterTest_maxDrop | 0.1900 | 2.5880 |
| data_changes | 0 | clusterTest_afterMean | 70.8280 | 68.7760 |
| data_changes | 0 | clusterTest_afterStd | 0.1357 | 0.9182 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 35.3750 | 34.8640 |
| data_changes | 0 | globalTest_maxDrop | 0.0950 | 1.2940 |
| data_changes | 0 | globalTest_afterMean | 35.4140 | 34.3960 |
| data_changes | 0 | globalTest_afterStd | 0.0679 | 0.4477 |
| data_changes | 1 | clusterTest_before | 80.2460 | 78.4140 |
| data_changes | 1 | clusterTest_maxDrop | 12.0660 | 9.1540 |
| data_changes | 1 | clusterTest_afterMean | 77.6740 | 77.3800 |
| data_changes | 1 | clusterTest_afterStd | 3.5228 | 2.9619 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 40.1230 | 39.2070 |
| data_changes | 1 | globalTest_maxDrop | 6.0330 | 4.5770 |
| data_changes | 1 | globalTest_afterMean | 38.8370 | 38.6900 |
| data_changes | 1 | globalTest_afterStd | 1.7614 | 1.4809 |
