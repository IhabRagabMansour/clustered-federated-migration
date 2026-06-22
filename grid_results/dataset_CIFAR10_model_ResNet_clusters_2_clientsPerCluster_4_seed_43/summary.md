# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 72.1560 | 71.0840 |
| membership_only | 0 | clusterTest_maxDrop | 0.6160 | 18.3040 |
| membership_only | 0 | clusterTest_afterMean | 71.9500 | 66.3100 |
| membership_only | 0 | clusterTest_afterStd | 0.1771 | 5.8493 |
| membership_only | 0 | clusterTest_recovery | 0 | 9 |
| membership_only | 0 | globalTest_before | 36.0780 | 35.5420 |
| membership_only | 0 | globalTest_maxDrop | 0.3080 | 9.1520 |
| membership_only | 0 | globalTest_afterMean | 35.9750 | 33.1550 |
| membership_only | 0 | globalTest_afterStd | 0.0886 | 2.9246 |
| membership_only | 1 | clusterTest_before | 81.8540 | 80.1600 |
| membership_only | 1 | clusterTest_maxDrop | 81.8540 | 80.1600 |
| membership_only | 1 | clusterTest_afterMean | 38.4220 | 41.5680 |
| membership_only | 1 | clusterTest_afterStd | 31.7462 | 35.6825 |
| membership_only | 1 | clusterTest_recovery | 12 | 9 |
| membership_only | 1 | globalTest_before | 40.9270 | 40.0800 |
| membership_only | 1 | globalTest_maxDrop | 14.9270 | 9.3700 |
| membership_only | 1 | globalTest_afterMean | 33.0880 | 35.6270 |
| membership_only | 1 | globalTest_afterStd | 4.4481 | 3.6159 |
| data_changes | 0 | clusterTest_before | 72.1560 | 71.0840 |
| data_changes | 0 | clusterTest_maxDrop | 0.6160 | 18.2640 |
| data_changes | 0 | clusterTest_afterMean | 71.9500 | 65.9080 |
| data_changes | 0 | clusterTest_afterStd | 0.1771 | 5.0954 |
| data_changes | 0 | clusterTest_recovery | 0 | 11 |
| data_changes | 0 | globalTest_before | 36.0780 | 35.5420 |
| data_changes | 0 | globalTest_maxDrop | 0.3080 | 9.1320 |
| data_changes | 0 | globalTest_afterMean | 35.9750 | 32.9550 |
| data_changes | 0 | globalTest_afterStd | 0.0886 | 2.5481 |
| data_changes | 1 | clusterTest_before | 81.8540 | 80.1600 |
| data_changes | 1 | clusterTest_maxDrop | 26.3340 | 9.9200 |
| data_changes | 1 | clusterTest_afterMean | 78.0160 | 79.6760 |
| data_changes | 1 | clusterTest_afterStd | 7.6909 | 3.4505 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 40.9270 | 40.0800 |
| data_changes | 1 | globalTest_maxDrop | 13.1670 | 4.9600 |
| data_changes | 1 | globalTest_afterMean | 39.0080 | 39.8380 |
| data_changes | 1 | globalTest_afterStd | 3.8455 | 1.7253 |
