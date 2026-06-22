# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 69.4280 | 68.6800 |
| membership_only | 0 | clusterTest_maxDrop | 0.1880 | 0.3200 |
| membership_only | 0 | clusterTest_afterMean | 69.7800 | 68.7900 |
| membership_only | 0 | clusterTest_afterStd | 0.2682 | 0.2389 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.7140 | 34.3400 |
| membership_only | 0 | globalTest_maxDrop | 0.0940 | 0.1600 |
| membership_only | 0 | globalTest_afterMean | 34.8900 | 34.3950 |
| membership_only | 0 | globalTest_afterStd | 0.1341 | 0.1194 |
| membership_only | 1 | clusterTest_before | 78.0680 | 77.1360 |
| membership_only | 1 | clusterTest_maxDrop | 47.4480 | 48.9560 |
| membership_only | 1 | clusterTest_afterMean | 57.5620 | 56.2380 |
| membership_only | 1 | clusterTest_afterStd | 19.4095 | 20.4760 |
| membership_only | 1 | clusterTest_recovery | 6 | 4 |
| membership_only | 1 | globalTest_before | 39.0340 | 38.5680 |
| membership_only | 1 | globalTest_maxDrop | 4.7540 | 2.3580 |
| membership_only | 1 | globalTest_afterMean | 37.7990 | 38.4910 |
| membership_only | 1 | globalTest_afterStd | 1.9294 | 1.6017 |
| data_changes | 0 | clusterTest_before | 69.4280 | 68.6800 |
| data_changes | 0 | clusterTest_maxDrop | 0.1880 | 0.5200 |
| data_changes | 0 | clusterTest_afterMean | 69.7800 | 68.6920 |
| data_changes | 0 | clusterTest_afterStd | 0.2682 | 0.3755 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 34.7140 | 34.3400 |
| data_changes | 0 | globalTest_maxDrop | 0.0940 | 0.2600 |
| data_changes | 0 | globalTest_afterMean | 34.8900 | 34.3470 |
| data_changes | 0 | globalTest_afterStd | 0.1341 | 0.1871 |
| data_changes | 1 | clusterTest_before | 78.0680 | 77.1360 |
| data_changes | 1 | clusterTest_maxDrop | 6.6880 | 3.6760 |
| data_changes | 1 | clusterTest_afterMean | 76.7440 | 76.6900 |
| data_changes | 1 | clusterTest_afterStd | 2.1210 | 1.3502 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 39.0340 | 38.5680 |
| data_changes | 1 | globalTest_maxDrop | 3.3440 | 1.8380 |
| data_changes | 1 | globalTest_afterMean | 38.3720 | 38.3450 |
| data_changes | 1 | globalTest_afterStd | 1.0605 | 0.6751 |
