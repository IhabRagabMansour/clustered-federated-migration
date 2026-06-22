# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.7980 | 69.2900 |
| membership_only | 0 | clusterTest_maxDrop | 0.4980 | 1.2100 |
| membership_only | 0 | clusterTest_afterMean | 70.7020 | 69.3020 |
| membership_only | 0 | clusterTest_afterStd | 0.2432 | 0.6653 |
| membership_only | 0 | clusterTest_recovery | 0 | 2 |
| membership_only | 0 | globalTest_before | 35.3990 | 34.6450 |
| membership_only | 0 | globalTest_maxDrop | 0.2490 | 0.6050 |
| membership_only | 0 | globalTest_afterMean | 35.3510 | 34.6510 |
| membership_only | 0 | globalTest_afterStd | 0.1216 | 0.3327 |
| membership_only | 1 | clusterTest_before | 78.8360 | 78.1280 |
| membership_only | 1 | clusterTest_maxDrop | 76.5360 | 74.6080 |
| membership_only | 1 | clusterTest_afterMean | 45.8100 | 44.9220 |
| membership_only | 1 | clusterTest_afterStd | 31.1754 | 31.8905 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 39.4180 | 39.0640 |
| membership_only | 1 | globalTest_maxDrop | 13.4380 | 10.2740 |
| membership_only | 1 | globalTest_afterMean | 34.2410 | 35.4160 |
| membership_only | 1 | globalTest_afterStd | 4.8008 | 3.5469 |
| data_changes | 0 | clusterTest_before | 70.7980 | 69.2900 |
| data_changes | 0 | clusterTest_maxDrop | 0.4980 | 1.1300 |
| data_changes | 0 | clusterTest_afterMean | 70.7020 | 69.3180 |
| data_changes | 0 | clusterTest_afterStd | 0.2432 | 0.6341 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 35.3990 | 34.6450 |
| data_changes | 0 | globalTest_maxDrop | 0.2490 | 0.5650 |
| data_changes | 0 | globalTest_afterMean | 35.3510 | 34.6600 |
| data_changes | 0 | globalTest_afterStd | 0.1216 | 0.3170 |
| data_changes | 1 | clusterTest_before | 78.8360 | 78.1280 |
| data_changes | 1 | clusterTest_maxDrop | 12.0360 | 5.9080 |
| data_changes | 1 | clusterTest_afterMean | 76.8420 | 77.5900 |
| data_changes | 1 | clusterTest_afterStd | 3.6661 | 2.0772 |
| data_changes | 1 | clusterTest_recovery | 3 | 3 |
| data_changes | 1 | globalTest_before | 39.4180 | 39.0640 |
| data_changes | 1 | globalTest_maxDrop | 6.0180 | 2.9540 |
| data_changes | 1 | globalTest_afterMean | 38.4210 | 38.7950 |
| data_changes | 1 | globalTest_afterStd | 1.8330 | 1.0386 |
