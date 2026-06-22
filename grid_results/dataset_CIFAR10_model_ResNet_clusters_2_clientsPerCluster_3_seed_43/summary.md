# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 73.8040 | 73.2380 |
| membership_only | 0 | clusterTest_maxDrop | 0.2240 | 0.7180 |
| membership_only | 0 | clusterTest_afterMean | 73.7720 | 73.1340 |
| membership_only | 0 | clusterTest_afterStd | 0.1017 | 0.2764 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 36.9020 | 36.6190 |
| membership_only | 0 | globalTest_maxDrop | 0.1120 | 0.3490 |
| membership_only | 0 | globalTest_afterMean | 36.8860 | 36.5680 |
| membership_only | 0 | globalTest_afterStd | 0.0508 | 0.1360 |
| membership_only | 1 | clusterTest_before | 81.7960 | 81.0080 |
| membership_only | 1 | clusterTest_maxDrop | 81.7960 | 81.0080 |
| membership_only | 1 | clusterTest_afterMean | 38.1580 | 42.0780 |
| membership_only | 1 | clusterTest_afterStd | 38.1265 | 35.9778 |
| membership_only | 1 | clusterTest_recovery | 8 | 9 |
| membership_only | 1 | globalTest_before | 40.8980 | 40.5040 |
| membership_only | 1 | globalTest_maxDrop | 16.4680 | 9.9340 |
| membership_only | 1 | globalTest_afterMean | 33.4150 | 35.5760 |
| membership_only | 1 | globalTest_afterStd | 5.8356 | 4.2729 |
| data_changes | 0 | clusterTest_before | 73.8040 | 73.2380 |
| data_changes | 0 | clusterTest_maxDrop | 0.2240 | 16.4580 |
| data_changes | 0 | clusterTest_afterMean | 73.7720 | 68.9600 |
| data_changes | 0 | clusterTest_afterStd | 0.1017 | 5.0238 |
| data_changes | 0 | clusterTest_recovery | 0 | 11 |
| data_changes | 0 | globalTest_before | 36.9020 | 36.6190 |
| data_changes | 0 | globalTest_maxDrop | 0.1120 | 8.2290 |
| data_changes | 0 | globalTest_afterMean | 36.8860 | 34.4870 |
| data_changes | 0 | globalTest_afterStd | 0.0508 | 2.5048 |
| data_changes | 1 | clusterTest_before | 81.7960 | 81.0080 |
| data_changes | 1 | clusterTest_maxDrop | 19.0360 | 9.8080 |
| data_changes | 1 | clusterTest_afterMean | 79.7320 | 80.5080 |
| data_changes | 1 | clusterTest_afterStd | 5.7600 | 3.2716 |
| data_changes | 1 | clusterTest_recovery | 2 | 2 |
| data_changes | 1 | globalTest_before | 40.8980 | 40.5040 |
| data_changes | 1 | globalTest_maxDrop | 9.5180 | 4.9040 |
| data_changes | 1 | globalTest_afterMean | 39.8660 | 40.2540 |
| data_changes | 1 | globalTest_afterStd | 2.8800 | 1.6358 |
