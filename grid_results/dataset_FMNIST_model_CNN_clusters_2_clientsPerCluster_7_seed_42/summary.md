# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.0960 | 88.4460 |
| membership_only | 0 | clusterTest_maxDrop | -0.2440 | -0.4140 |
| membership_only | 0 | clusterTest_afterMean | 89.7320 | 89.0680 |
| membership_only | 0 | clusterTest_afterStd | 0.1912 | 0.1744 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.5480 | 44.2230 |
| membership_only | 0 | globalTest_maxDrop | -0.1220 | -0.2070 |
| membership_only | 0 | globalTest_afterMean | 44.8660 | 44.5530 |
| membership_only | 0 | globalTest_afterStd | 0.0956 | 0.0884 |
| membership_only | 1 | clusterTest_before | 94.8020 | 94.6000 |
| membership_only | 1 | clusterTest_maxDrop | 31.8820 | 34.4000 |
| membership_only | 1 | clusterTest_afterMean | 81.3460 | 80.9560 |
| membership_only | 1 | clusterTest_afterStd | 12.5021 | 12.9216 |
| membership_only | 1 | clusterTest_recovery | 8 | 8 |
| membership_only | 1 | globalTest_before | 47.4010 | 47.3000 |
| membership_only | 1 | globalTest_maxDrop | 1.1310 | 0.5400 |
| membership_only | 1 | globalTest_afterMean | 63.3700 | 66.0050 |
| membership_only | 1 | globalTest_afterStd | 12.4466 | 11.3536 |
| data_changes | 0 | clusterTest_before | 89.0960 | 88.4460 |
| data_changes | 0 | clusterTest_maxDrop | -0.2440 | -0.1940 |
| data_changes | 0 | clusterTest_afterMean | 89.7320 | 89.0780 |
| data_changes | 0 | clusterTest_afterStd | 0.1912 | 0.2068 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.5480 | 44.2230 |
| data_changes | 0 | globalTest_maxDrop | -0.1220 | -0.2570 |
| data_changes | 0 | globalTest_afterMean | 44.8660 | 45.0710 |
| data_changes | 0 | globalTest_afterStd | 0.0956 | 0.9989 |
| data_changes | 1 | clusterTest_before | 94.8020 | 94.6000 |
| data_changes | 1 | clusterTest_maxDrop | 4.1620 | 0.5800 |
| data_changes | 1 | clusterTest_afterMean | 94.1740 | 94.6800 |
| data_changes | 1 | clusterTest_afterStd | 1.2334 | 0.2751 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.4010 | 47.3000 |
| data_changes | 1 | globalTest_maxDrop | 2.0810 | 0.2900 |
| data_changes | 1 | globalTest_afterMean | 47.0870 | 47.3420 |
| data_changes | 1 | globalTest_afterStd | 0.6167 | 0.1378 |
