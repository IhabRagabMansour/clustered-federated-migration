# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 78.9020 | 78.1040 |
| membership_only | 0 | clusterTest_maxDrop | 1.7420 | 0.8440 |
| membership_only | 0 | clusterTest_afterMean | 79.7480 | 79.3240 |
| membership_only | 0 | clusterTest_afterStd | 1.1599 | 0.8020 |
| membership_only | 0 | clusterTest_recovery | 1 | 0 |
| membership_only | 0 | globalTest_before | 39.4510 | 39.0520 |
| membership_only | 0 | globalTest_maxDrop | 0.8710 | 0.4220 |
| membership_only | 0 | globalTest_afterMean | 39.8740 | 39.6620 |
| membership_only | 0 | globalTest_afterStd | 0.5799 | 0.4010 |
| membership_only | 1 | clusterTest_before | 88.1440 | 87.4840 |
| membership_only | 1 | clusterTest_maxDrop | 49.3440 | 54.3240 |
| membership_only | 1 | clusterTest_afterMean | 74.0120 | 70.1600 |
| membership_only | 1 | clusterTest_afterStd | 15.1723 | 18.3369 |
| membership_only | 1 | clusterTest_recovery | 8 | 8 |
| membership_only | 1 | globalTest_before | 44.0720 | 43.7420 |
| membership_only | 1 | globalTest_maxDrop | 1.7320 | 1.6520 |
| membership_only | 1 | globalTest_afterMean | 48.8950 | 49.2030 |
| membership_only | 1 | globalTest_afterStd | 6.3568 | 7.0477 |
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 1.7420 | 0.4040 |
| data_changes | 0 | clusterTest_afterMean | 79.7480 | 79.4560 |
| data_changes | 0 | clusterTest_afterStd | 1.1599 | 0.7300 |
| data_changes | 0 | clusterTest_recovery | 1 | 0 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 0.8710 | 0.2020 |
| data_changes | 0 | globalTest_afterMean | 39.8740 | 39.7280 |
| data_changes | 0 | globalTest_afterStd | 0.5799 | 0.3650 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 9.2040 | 2.0240 |
| data_changes | 1 | clusterTest_afterMean | 86.5500 | 87.6180 |
| data_changes | 1 | clusterTest_afterStd | 3.1122 | 0.8554 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 4.6020 | 1.0120 |
| data_changes | 1 | globalTest_afterMean | 43.2750 | 43.8090 |
| data_changes | 1 | globalTest_afterStd | 1.5561 | 0.4277 |
