# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 79.4080 | 78.7640 |
| membership_only | 0 | clusterTest_maxDrop | 1.2480 | 0.0640 |
| membership_only | 0 | clusterTest_afterMean | 79.9400 | 79.8600 |
| membership_only | 0 | clusterTest_afterStd | 0.7214 | 0.5614 |
| membership_only | 0 | clusterTest_recovery | 9 | 0 |
| membership_only | 0 | globalTest_before | 39.7040 | 39.3820 |
| membership_only | 0 | globalTest_maxDrop | 0.6240 | 0.0320 |
| membership_only | 0 | globalTest_afterMean | 39.9700 | 39.9300 |
| membership_only | 0 | globalTest_afterStd | 0.3607 | 0.2807 |
| membership_only | 1 | clusterTest_before | 87.8540 | 87.4660 |
| membership_only | 1 | clusterTest_maxDrop | 48.4140 | 61.8460 |
| membership_only | 1 | clusterTest_afterMean | 73.1800 | 70.0100 |
| membership_only | 1 | clusterTest_afterStd | 14.4761 | 19.4567 |
| membership_only | 1 | clusterTest_recovery | 10 | 2 |
| membership_only | 1 | globalTest_before | 43.9270 | 43.7330 |
| membership_only | 1 | globalTest_maxDrop | 2.4570 | 1.4030 |
| membership_only | 1 | globalTest_afterMean | 48.7170 | 49.0360 |
| membership_only | 1 | globalTest_afterStd | 6.4170 | 6.7004 |
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 1.2480 | 0.0240 |
| data_changes | 0 | clusterTest_afterMean | 79.9400 | 79.8440 |
| data_changes | 0 | clusterTest_afterStd | 0.7214 | 0.5585 |
| data_changes | 0 | clusterTest_recovery | 9 | 0 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 0.6240 | 0.0120 |
| data_changes | 0 | globalTest_afterMean | 39.9700 | 39.9220 |
| data_changes | 0 | globalTest_afterStd | 0.3607 | 0.2792 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 11.3940 | 1.4460 |
| data_changes | 1 | clusterTest_afterMean | 86.6800 | 87.7480 |
| data_changes | 1 | clusterTest_afterStd | 3.5665 | 0.6762 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 5.6970 | 0.7230 |
| data_changes | 1 | globalTest_afterMean | 43.3400 | 43.8740 |
| data_changes | 1 | globalTest_afterStd | 1.7832 | 0.3381 |
