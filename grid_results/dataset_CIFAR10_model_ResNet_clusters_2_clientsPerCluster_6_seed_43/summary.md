# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.6080 | 69.3340 |
| membership_only | 0 | clusterTest_maxDrop | 0.7480 | 3.3740 |
| membership_only | 0 | clusterTest_afterMean | 70.2320 | 68.0640 |
| membership_only | 0 | clusterTest_afterStd | 0.2820 | 1.2086 |
| membership_only | 0 | clusterTest_recovery | 0 | 11 |
| membership_only | 0 | globalTest_before | 35.3040 | 34.6670 |
| membership_only | 0 | globalTest_maxDrop | 0.3740 | 1.6870 |
| membership_only | 0 | globalTest_afterMean | 35.1160 | 34.0320 |
| membership_only | 0 | globalTest_afterStd | 0.1410 | 0.6043 |
| membership_only | 1 | clusterTest_before | 79.0400 | 77.7160 |
| membership_only | 1 | clusterTest_maxDrop | 79.0400 | 77.6960 |
| membership_only | 1 | clusterTest_afterMean | 38.1180 | 44.0400 |
| membership_only | 1 | clusterTest_afterStd | 37.2482 | 30.8758 |
| membership_only | 1 | clusterTest_recovery | 4 | 6 |
| membership_only | 1 | globalTest_before | 39.5200 | 38.8590 |
| membership_only | 1 | globalTest_maxDrop | 13.6500 | 13.3390 |
| membership_only | 1 | globalTest_afterMean | 32.8750 | 34.7860 |
| membership_only | 1 | globalTest_afterStd | 5.2387 | 4.6240 |
| data_changes | 0 | clusterTest_before | 70.6080 | 69.3340 |
| data_changes | 0 | clusterTest_maxDrop | 0.7480 | 2.5540 |
| data_changes | 0 | clusterTest_afterMean | 70.2320 | 68.7240 |
| data_changes | 0 | clusterTest_afterStd | 0.2820 | 0.8874 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 35.3040 | 34.6670 |
| data_changes | 0 | globalTest_maxDrop | 0.3740 | 1.2770 |
| data_changes | 0 | globalTest_afterMean | 35.1160 | 34.3700 |
| data_changes | 0 | globalTest_afterStd | 0.1410 | 0.4321 |
| data_changes | 1 | clusterTest_before | 79.0400 | 77.7160 |
| data_changes | 1 | clusterTest_maxDrop | 17.0000 | 8.7160 |
| data_changes | 1 | clusterTest_afterMean | 76.7900 | 76.9060 |
| data_changes | 1 | clusterTest_afterStd | 5.3436 | 3.3845 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.5200 | 38.8590 |
| data_changes | 1 | globalTest_maxDrop | 8.5000 | 4.3590 |
| data_changes | 1 | globalTest_afterMean | 38.3950 | 38.4530 |
| data_changes | 1 | globalTest_afterStd | 2.6718 | 1.6922 |
