# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 73.3940 | 71.4660 |
| membership_only | 0 | clusterTest_maxDrop | 0.4340 | -0.1540 |
| membership_only | 0 | clusterTest_afterMean | 73.1600 | 71.8900 |
| membership_only | 0 | clusterTest_afterStd | 0.1159 | 0.1224 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 36.6970 | 35.7330 |
| membership_only | 0 | globalTest_maxDrop | 0.2170 | -0.0770 |
| membership_only | 0 | globalTest_afterMean | 36.5800 | 35.9450 |
| membership_only | 0 | globalTest_afterStd | 0.0580 | 0.0612 |
| membership_only | 1 | clusterTest_before | 81.5740 | 79.7780 |
| membership_only | 1 | clusterTest_maxDrop | 81.5740 | 79.7780 |
| membership_only | 1 | clusterTest_afterMean | 37.2240 | 38.6620 |
| membership_only | 1 | clusterTest_afterStd | 37.7368 | 33.4755 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 40.7870 | 39.8890 |
| membership_only | 1 | globalTest_maxDrop | 15.6570 | 12.1890 |
| membership_only | 1 | globalTest_afterMean | 32.8060 | 34.1940 |
| membership_only | 1 | globalTest_afterStd | 5.6757 | 4.1455 |
| data_changes | 0 | clusterTest_before | 73.3940 | 71.4660 |
| data_changes | 0 | clusterTest_maxDrop | 0.4340 | 1.9260 |
| data_changes | 0 | clusterTest_afterMean | 73.1600 | 71.2400 |
| data_changes | 0 | clusterTest_afterStd | 0.1159 | 0.7733 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 36.6970 | 35.7330 |
| data_changes | 0 | globalTest_maxDrop | 0.2170 | 0.8330 |
| data_changes | 0 | globalTest_afterMean | 36.5800 | 35.7260 |
| data_changes | 0 | globalTest_afterStd | 0.0580 | 0.2942 |
| data_changes | 1 | clusterTest_before | 81.5740 | 79.7780 |
| data_changes | 1 | clusterTest_maxDrop | 26.3340 | 9.5980 |
| data_changes | 1 | clusterTest_afterMean | 77.8440 | 80.3840 |
| data_changes | 1 | clusterTest_afterStd | 7.6685 | 3.6065 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 40.7870 | 39.8890 |
| data_changes | 1 | globalTest_maxDrop | 13.1670 | 4.7990 |
| data_changes | 1 | globalTest_afterMean | 38.9220 | 40.1920 |
| data_changes | 1 | globalTest_afterStd | 3.8343 | 1.8032 |
