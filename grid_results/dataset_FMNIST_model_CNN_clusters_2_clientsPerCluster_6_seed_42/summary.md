# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.6800 | 89.1540 |
| membership_only | 0 | clusterTest_maxDrop | 0.0600 | -0.1060 |
| membership_only | 0 | clusterTest_afterMean | 90.1700 | 89.7560 |
| membership_only | 0 | clusterTest_afterStd | 0.2611 | 0.3138 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.8400 | 44.5770 |
| membership_only | 0 | globalTest_maxDrop | 0.0300 | -0.0530 |
| membership_only | 0 | globalTest_afterMean | 45.0850 | 44.8820 |
| membership_only | 0 | globalTest_afterStd | 0.1306 | 0.1594 |
| membership_only | 1 | clusterTest_before | 95.1240 | 95.0480 |
| membership_only | 1 | clusterTest_maxDrop | 34.2040 | 39.1480 |
| membership_only | 1 | clusterTest_afterMean | 82.0380 | 81.2820 |
| membership_only | 1 | clusterTest_afterStd | 12.7159 | 13.7408 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 47.5620 | 47.5240 |
| membership_only | 1 | globalTest_maxDrop | 0.6420 | -1.3760 |
| membership_only | 1 | globalTest_afterMean | 65.0360 | 67.0880 |
| membership_only | 1 | globalTest_afterStd | 12.3327 | 10.8512 |
| data_changes | 0 | clusterTest_before | 89.6800 | 89.1540 |
| data_changes | 0 | clusterTest_maxDrop | 0.0600 | 0.0740 |
| data_changes | 0 | clusterTest_afterMean | 90.1700 | 89.5940 |
| data_changes | 0 | clusterTest_afterStd | 0.2611 | 0.3633 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.8400 | 44.5770 |
| data_changes | 0 | globalTest_maxDrop | 0.0300 | 0.0370 |
| data_changes | 0 | globalTest_afterMean | 45.0850 | 45.4110 |
| data_changes | 0 | globalTest_afterStd | 0.1306 | 1.1503 |
| data_changes | 1 | clusterTest_before | 95.1240 | 95.0480 |
| data_changes | 1 | clusterTest_maxDrop | 3.1840 | 0.4880 |
| data_changes | 1 | clusterTest_afterMean | 94.6100 | 95.1360 |
| data_changes | 1 | clusterTest_afterStd | 1.0118 | 0.3075 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.5620 | 47.5240 |
| data_changes | 1 | globalTest_maxDrop | 1.5920 | 0.2440 |
| data_changes | 1 | globalTest_afterMean | 47.3050 | 47.6330 |
| data_changes | 1 | globalTest_afterStd | 0.5059 | 0.2162 |
