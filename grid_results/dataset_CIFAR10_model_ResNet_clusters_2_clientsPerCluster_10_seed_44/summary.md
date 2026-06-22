# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 68.9940 | 68.0260 |
| membership_only | 0 | clusterTest_maxDrop | 0.1940 | 0.6260 |
| membership_only | 0 | clusterTest_afterMean | 69.1500 | 68.0760 |
| membership_only | 0 | clusterTest_afterStd | 0.2448 | 0.3844 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.4970 | 34.0130 |
| membership_only | 0 | globalTest_maxDrop | 0.0970 | 0.3130 |
| membership_only | 0 | globalTest_afterMean | 34.5750 | 34.0380 |
| membership_only | 0 | globalTest_afterStd | 0.1224 | 0.1922 |
| membership_only | 1 | clusterTest_before | 78.7300 | 77.5920 |
| membership_only | 1 | clusterTest_maxDrop | 49.9300 | 52.1520 |
| membership_only | 1 | clusterTest_afterMean | 58.0860 | 56.1280 |
| membership_only | 1 | clusterTest_afterStd | 18.8398 | 20.9487 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 39.3650 | 38.7960 |
| membership_only | 1 | globalTest_maxDrop | 3.9450 | 1.6860 |
| membership_only | 1 | globalTest_afterMean | 38.7730 | 38.8390 |
| membership_only | 1 | globalTest_afterStd | 2.4659 | 1.4426 |
| data_changes | 0 | clusterTest_before | 68.9940 | 68.0260 |
| data_changes | 0 | clusterTest_maxDrop | 0.1940 | 1.6060 |
| data_changes | 0 | clusterTest_afterMean | 69.1500 | 67.7400 |
| data_changes | 0 | clusterTest_afterStd | 0.2448 | 0.6848 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 34.4970 | 34.0130 |
| data_changes | 0 | globalTest_maxDrop | 0.0970 | 0.8030 |
| data_changes | 0 | globalTest_afterMean | 34.5750 | 33.8700 |
| data_changes | 0 | globalTest_afterStd | 0.1224 | 0.3424 |
| data_changes | 1 | clusterTest_before | 78.7300 | 77.5920 |
| data_changes | 1 | clusterTest_maxDrop | 7.5500 | 4.2720 |
| data_changes | 1 | clusterTest_afterMean | 76.8560 | 76.9880 |
| data_changes | 1 | clusterTest_afterStd | 2.5977 | 1.6843 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.3650 | 38.7960 |
| data_changes | 1 | globalTest_maxDrop | 3.7750 | 2.1360 |
| data_changes | 1 | globalTest_afterMean | 38.4280 | 38.4940 |
| data_changes | 1 | globalTest_afterStd | 1.2988 | 0.8422 |
