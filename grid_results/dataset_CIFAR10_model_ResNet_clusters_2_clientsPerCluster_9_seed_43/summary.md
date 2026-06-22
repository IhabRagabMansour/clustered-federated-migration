# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.6880 | 69.5680 |
| membership_only | 0 | clusterTest_maxDrop | 0.0080 | 0.5280 |
| membership_only | 0 | clusterTest_afterMean | 70.9680 | 69.5920 |
| membership_only | 0 | clusterTest_afterStd | 0.1429 | 0.2695 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 35.3440 | 34.7840 |
| membership_only | 0 | globalTest_maxDrop | 0.0040 | 0.2640 |
| membership_only | 0 | globalTest_afterMean | 35.4840 | 34.7960 |
| membership_only | 0 | globalTest_afterStd | 0.0714 | 0.1348 |
| membership_only | 1 | clusterTest_before | 78.1760 | 78.0540 |
| membership_only | 1 | clusterTest_maxDrop | 62.1160 | 63.3540 |
| membership_only | 1 | clusterTest_afterMean | 51.0760 | 51.8080 |
| membership_only | 1 | clusterTest_afterStd | 25.9193 | 24.4665 |
| membership_only | 1 | clusterTest_recovery | 6 | 8 |
| membership_only | 1 | globalTest_before | 39.0880 | 39.0270 |
| membership_only | 1 | globalTest_maxDrop | 9.8680 | 6.4670 |
| membership_only | 1 | globalTest_afterMean | 35.6130 | 37.1580 |
| membership_only | 1 | globalTest_afterStd | 3.3151 | 1.6729 |
| data_changes | 0 | clusterTest_before | 70.6880 | 69.5680 |
| data_changes | 0 | clusterTest_maxDrop | 0.0080 | 1.8680 |
| data_changes | 0 | clusterTest_afterMean | 70.9680 | 69.3020 |
| data_changes | 0 | clusterTest_afterStd | 0.1429 | 0.7160 |
| data_changes | 0 | clusterTest_recovery | 0 | 6 |
| data_changes | 0 | globalTest_before | 35.3440 | 34.7840 |
| data_changes | 0 | globalTest_maxDrop | 0.0040 | 0.9140 |
| data_changes | 0 | globalTest_afterMean | 35.4840 | 34.6530 |
| data_changes | 0 | globalTest_afterStd | 0.0714 | 0.3535 |
| data_changes | 1 | clusterTest_before | 78.1760 | 78.0540 |
| data_changes | 1 | clusterTest_maxDrop | 6.6360 | 4.3740 |
| data_changes | 1 | clusterTest_afterMean | 77.0320 | 77.2760 |
| data_changes | 1 | clusterTest_afterStd | 2.0680 | 1.7822 |
| data_changes | 1 | clusterTest_recovery | 2 | 3 |
| data_changes | 1 | globalTest_before | 39.0880 | 39.0270 |
| data_changes | 1 | globalTest_maxDrop | 3.3180 | 2.1870 |
| data_changes | 1 | globalTest_afterMean | 38.5160 | 38.6380 |
| data_changes | 1 | globalTest_afterStd | 1.0340 | 0.8911 |
