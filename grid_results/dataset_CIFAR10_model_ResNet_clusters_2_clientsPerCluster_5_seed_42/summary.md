# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.6440 | 69.9320 |
| membership_only | 0 | clusterTest_maxDrop | 0.0840 | 8.3120 |
| membership_only | 0 | clusterTest_afterMean | 70.8180 | 67.9640 |
| membership_only | 0 | clusterTest_afterStd | 0.1263 | 2.7595 |
| membership_only | 0 | clusterTest_recovery | 0 | 9 |
| membership_only | 0 | globalTest_before | 35.3220 | 34.9660 |
| membership_only | 0 | globalTest_maxDrop | 0.0420 | 4.1560 |
| membership_only | 0 | globalTest_afterMean | 35.4090 | 33.9820 |
| membership_only | 0 | globalTest_afterStd | 0.0632 | 1.3797 |
| membership_only | 1 | clusterTest_before | 79.6220 | 78.1000 |
| membership_only | 1 | clusterTest_maxDrop | 79.6220 | 78.1000 |
| membership_only | 1 | clusterTest_afterMean | 36.7060 | 39.1560 |
| membership_only | 1 | clusterTest_afterStd | 36.8648 | 34.6541 |
| membership_only | 1 | clusterTest_recovery | 10 | 6 |
| membership_only | 1 | globalTest_before | 39.8110 | 39.0500 |
| membership_only | 1 | globalTest_maxDrop | 13.1110 | 11.2500 |
| membership_only | 1 | globalTest_afterMean | 32.9120 | 34.7650 |
| membership_only | 1 | globalTest_afterStd | 4.3418 | 3.8346 |
| data_changes | 0 | clusterTest_before | 70.6440 | 69.9320 |
| data_changes | 0 | clusterTest_maxDrop | 0.0840 | 8.5520 |
| data_changes | 0 | clusterTest_afterMean | 70.8180 | 67.1660 |
| data_changes | 0 | clusterTest_afterStd | 0.1263 | 3.0651 |
| data_changes | 0 | clusterTest_recovery | 0 | 8 |
| data_changes | 0 | globalTest_before | 35.3220 | 34.9660 |
| data_changes | 0 | globalTest_maxDrop | 0.0420 | 4.2760 |
| data_changes | 0 | globalTest_afterMean | 35.4090 | 33.5910 |
| data_changes | 0 | globalTest_afterStd | 0.0632 | 1.5266 |
| data_changes | 1 | clusterTest_before | 79.6220 | 78.1000 |
| data_changes | 1 | clusterTest_maxDrop | 19.4420 | 8.9800 |
| data_changes | 1 | clusterTest_afterMean | 76.8260 | 77.6260 |
| data_changes | 1 | clusterTest_afterStd | 5.8527 | 3.1942 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.8110 | 39.0500 |
| data_changes | 1 | globalTest_maxDrop | 9.7210 | 4.4900 |
| data_changes | 1 | globalTest_afterMean | 38.4130 | 38.8130 |
| data_changes | 1 | globalTest_afterStd | 2.9264 | 1.5971 |
