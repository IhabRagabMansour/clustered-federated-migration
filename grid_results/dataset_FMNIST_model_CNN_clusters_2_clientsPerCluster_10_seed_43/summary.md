# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 88.4080 | 87.6220 |
| membership_only | 0 | clusterTest_maxDrop | -0.2520 | 0.0820 |
| membership_only | 0 | clusterTest_afterMean | 89.0460 | 88.2020 |
| membership_only | 0 | clusterTest_afterStd | 0.2222 | 0.3571 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.2040 | 43.8110 |
| membership_only | 0 | globalTest_maxDrop | -0.1260 | -0.0690 |
| membership_only | 0 | globalTest_afterMean | 44.5230 | 44.1530 |
| membership_only | 0 | globalTest_afterStd | 0.1111 | 0.1477 |
| membership_only | 1 | clusterTest_before | 93.8660 | 93.6940 |
| membership_only | 1 | clusterTest_maxDrop | 23.5460 | 33.0940 |
| membership_only | 1 | clusterTest_afterMean | 82.4500 | 81.0520 |
| membership_only | 1 | clusterTest_afterStd | 10.1311 | 11.6595 |
| membership_only | 1 | clusterTest_recovery | 8 | 8 |
| membership_only | 1 | globalTest_before | 46.9330 | 46.8470 |
| membership_only | 1 | globalTest_maxDrop | 1.6530 | 1.3670 |
| membership_only | 1 | globalTest_afterMean | 60.0980 | 63.6900 |
| membership_only | 1 | globalTest_afterStd | 13.0455 | 12.2828 |
| data_changes | 0 | clusterTest_before | 88.4080 | 87.6220 |
| data_changes | 0 | clusterTest_maxDrop | -0.2520 | -0.0980 |
| data_changes | 0 | clusterTest_afterMean | 89.0460 | 88.2340 |
| data_changes | 0 | clusterTest_afterStd | 0.2222 | 0.2907 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.2040 | 43.8110 |
| data_changes | 0 | globalTest_maxDrop | -0.1260 | -0.0490 |
| data_changes | 0 | globalTest_afterMean | 44.5230 | 44.4060 |
| data_changes | 0 | globalTest_afterStd | 0.1111 | 0.5894 |
| data_changes | 1 | clusterTest_before | 93.8660 | 93.6940 |
| data_changes | 1 | clusterTest_maxDrop | 3.0660 | 0.5140 |
| data_changes | 1 | clusterTest_afterMean | 93.6320 | 93.9760 |
| data_changes | 1 | clusterTest_afterStd | 1.0232 | 0.3847 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 46.9330 | 46.8470 |
| data_changes | 1 | globalTest_maxDrop | 1.5330 | 0.2570 |
| data_changes | 1 | globalTest_afterMean | 46.8160 | 46.9880 |
| data_changes | 1 | globalTest_afterStd | 0.5116 | 0.1923 |
