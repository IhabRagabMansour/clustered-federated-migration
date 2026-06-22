# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.1740 | 68.9980 |
| membership_only | 0 | clusterTest_maxDrop | 2.9340 | 2.8380 |
| membership_only | 0 | clusterTest_afterMean | 69.2540 | 68.5740 |
| membership_only | 0 | clusterTest_afterStd | 1.0152 | 1.2505 |
| membership_only | 0 | clusterTest_recovery | 7 | 4 |
| membership_only | 0 | globalTest_before | 35.0870 | 34.4990 |
| membership_only | 0 | globalTest_maxDrop | 1.4670 | 1.4190 |
| membership_only | 0 | globalTest_afterMean | 34.6270 | 34.2870 |
| membership_only | 0 | globalTest_afterStd | 0.5076 | 0.6253 |
| membership_only | 1 | clusterTest_before | 77.6160 | 77.6180 |
| membership_only | 1 | clusterTest_maxDrop | 72.1360 | 72.7780 |
| membership_only | 1 | clusterTest_afterMean | 44.5500 | 47.8920 |
| membership_only | 1 | clusterTest_afterStd | 30.7236 | 28.5711 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 38.8080 | 38.8090 |
| membership_only | 1 | globalTest_maxDrop | 15.2680 | 7.6590 |
| membership_only | 1 | globalTest_afterMean | 33.6240 | 36.5990 |
| membership_only | 1 | globalTest_afterStd | 4.7389 | 2.2110 |
| data_changes | 0 | clusterTest_before | 70.1740 | 68.9980 |
| data_changes | 0 | clusterTest_maxDrop | 2.9340 | 2.8780 |
| data_changes | 0 | clusterTest_afterMean | 69.2540 | 68.1960 |
| data_changes | 0 | clusterTest_afterStd | 1.0152 | 1.1001 |
| data_changes | 0 | clusterTest_recovery | 7 | 6 |
| data_changes | 0 | globalTest_before | 35.0870 | 34.4990 |
| data_changes | 0 | globalTest_maxDrop | 1.4670 | 1.4390 |
| data_changes | 0 | globalTest_afterMean | 34.6270 | 34.0980 |
| data_changes | 0 | globalTest_afterStd | 0.5076 | 0.5500 |
| data_changes | 1 | clusterTest_before | 77.6160 | 77.6180 |
| data_changes | 1 | clusterTest_maxDrop | 11.9360 | 5.1180 |
| data_changes | 1 | clusterTest_afterMean | 76.1600 | 77.0520 |
| data_changes | 1 | clusterTest_afterStd | 3.7761 | 2.1067 |
| data_changes | 1 | clusterTest_recovery | 2 | 2 |
| data_changes | 1 | globalTest_before | 38.8080 | 38.8090 |
| data_changes | 1 | globalTest_maxDrop | 5.9680 | 2.5590 |
| data_changes | 1 | globalTest_afterMean | 38.0800 | 38.5260 |
| data_changes | 1 | globalTest_afterStd | 1.8880 | 1.0533 |
