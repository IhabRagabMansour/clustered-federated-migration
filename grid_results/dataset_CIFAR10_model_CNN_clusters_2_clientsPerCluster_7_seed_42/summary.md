# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.9480 | 80.0840 |
| membership_only | 0 | clusterTest_maxDrop | 2.2080 | 2.4640 |
| membership_only | 0 | clusterTest_afterMean | 80.9940 | 80.6700 |
| membership_only | 0 | clusterTest_afterStd | 0.8738 | 1.1400 |
| membership_only | 0 | clusterTest_recovery | 2 | 2 |
| membership_only | 0 | globalTest_before | 40.4740 | 40.0420 |
| membership_only | 0 | globalTest_maxDrop | 1.1040 | 1.2320 |
| membership_only | 0 | globalTest_afterMean | 40.4970 | 40.3350 |
| membership_only | 0 | globalTest_afterStd | 0.4369 | 0.5700 |
| membership_only | 1 | clusterTest_before | 89.4960 | 89.0480 |
| membership_only | 1 | clusterTest_maxDrop | 85.8760 | 84.1880 |
| membership_only | 1 | clusterTest_afterMean | 52.1040 | 51.6200 |
| membership_only | 1 | clusterTest_afterStd | 34.4526 | 34.4859 |
| membership_only | 1 | clusterTest_recovery | -1 | -1 |
| membership_only | 1 | globalTest_before | 44.7480 | 44.5240 |
| membership_only | 1 | globalTest_maxDrop | 9.9380 | 8.5640 |
| membership_only | 1 | globalTest_afterMean | 42.7700 | 44.0370 |
| membership_only | 1 | globalTest_afterStd | 3.7816 | 4.7877 |
| data_changes | 0 | clusterTest_before | 80.9480 | 80.0840 |
| data_changes | 0 | clusterTest_maxDrop | 2.2080 | 2.7240 |
| data_changes | 0 | clusterTest_afterMean | 80.9940 | 80.6900 |
| data_changes | 0 | clusterTest_afterStd | 0.8738 | 1.2015 |
| data_changes | 0 | clusterTest_recovery | 2 | 2 |
| data_changes | 0 | globalTest_before | 40.4740 | 40.0420 |
| data_changes | 0 | globalTest_maxDrop | 1.1040 | 1.3620 |
| data_changes | 0 | globalTest_afterMean | 40.4970 | 40.3450 |
| data_changes | 0 | globalTest_afterStd | 0.4369 | 0.6007 |
| data_changes | 1 | clusterTest_before | 89.4960 | 89.0480 |
| data_changes | 1 | clusterTest_maxDrop | 19.5760 | 3.4280 |
| data_changes | 1 | clusterTest_afterMean | 86.8320 | 88.8220 |
| data_changes | 1 | clusterTest_afterStd | 5.8070 | 1.0973 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.7480 | 44.5240 |
| data_changes | 1 | globalTest_maxDrop | 9.7880 | 1.7140 |
| data_changes | 1 | globalTest_afterMean | 43.4160 | 44.4110 |
| data_changes | 1 | globalTest_afterStd | 2.9035 | 0.5486 |
