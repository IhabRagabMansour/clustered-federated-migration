# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 69.6260 | 69.3240 |
| membership_only | 0 | clusterTest_maxDrop | 0.2660 | 0.8240 |
| membership_only | 0 | clusterTest_afterMean | 69.5780 | 69.0940 |
| membership_only | 0 | clusterTest_afterStd | 0.1231 | 0.3408 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.8130 | 34.6620 |
| membership_only | 0 | globalTest_maxDrop | 0.1330 | 0.4120 |
| membership_only | 0 | globalTest_afterMean | 34.7890 | 34.5470 |
| membership_only | 0 | globalTest_afterStd | 0.0616 | 0.1704 |
| membership_only | 1 | clusterTest_before | 79.6080 | 77.7120 |
| membership_only | 1 | clusterTest_maxDrop | 78.5480 | 74.6320 |
| membership_only | 1 | clusterTest_afterMean | 41.5260 | 43.8620 |
| membership_only | 1 | clusterTest_afterStd | 34.9022 | 32.0795 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 39.8040 | 38.8560 |
| membership_only | 1 | globalTest_maxDrop | 17.2840 | 12.6460 |
| membership_only | 1 | globalTest_afterMean | 33.1950 | 34.5270 |
| membership_only | 1 | globalTest_afterStd | 5.9624 | 4.7111 |
| data_changes | 0 | clusterTest_before | 69.6260 | 69.3240 |
| data_changes | 0 | clusterTest_maxDrop | 0.2660 | 2.2440 |
| data_changes | 0 | clusterTest_afterMean | 69.5780 | 68.8560 |
| data_changes | 0 | clusterTest_afterStd | 0.1231 | 0.8256 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 34.8130 | 34.6620 |
| data_changes | 0 | globalTest_maxDrop | 0.1330 | 1.1220 |
| data_changes | 0 | globalTest_afterMean | 34.7890 | 34.4300 |
| data_changes | 0 | globalTest_afterStd | 0.0616 | 0.4092 |
| data_changes | 1 | clusterTest_before | 79.6080 | 77.7120 |
| data_changes | 1 | clusterTest_maxDrop | 16.9080 | 7.5520 |
| data_changes | 1 | clusterTest_afterMean | 76.7300 | 77.3620 |
| data_changes | 1 | clusterTest_afterStd | 4.8990 | 2.5898 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.8040 | 38.8560 |
| data_changes | 1 | globalTest_maxDrop | 8.4540 | 3.7760 |
| data_changes | 1 | globalTest_afterMean | 38.3650 | 38.6810 |
| data_changes | 1 | globalTest_afterStd | 2.4495 | 1.2949 |
