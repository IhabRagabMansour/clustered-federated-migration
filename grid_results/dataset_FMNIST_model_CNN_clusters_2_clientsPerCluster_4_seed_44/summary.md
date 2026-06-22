# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.9820 | 90.4940 |
| membership_only | 0 | clusterTest_maxDrop | 0.3620 | 0.5140 |
| membership_only | 0 | clusterTest_afterMean | 91.0880 | 90.6040 |
| membership_only | 0 | clusterTest_afterStd | 0.2757 | 0.3070 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.4910 | 45.2470 |
| membership_only | 0 | globalTest_maxDrop | 0.1810 | 0.2570 |
| membership_only | 0 | globalTest_afterMean | 45.5440 | 45.3020 |
| membership_only | 0 | globalTest_afterStd | 0.1379 | 0.1535 |
| membership_only | 1 | clusterTest_before | 96.4280 | 96.2840 |
| membership_only | 1 | clusterTest_maxDrop | 32.3280 | 27.4440 |
| membership_only | 1 | clusterTest_afterMean | 83.0880 | 83.1860 |
| membership_only | 1 | clusterTest_afterStd | 12.8077 | 10.9787 |
| membership_only | 1 | clusterTest_recovery | 4 | 6 |
| membership_only | 1 | globalTest_before | 48.2140 | 48.1420 |
| membership_only | 1 | globalTest_maxDrop | -7.3060 | -9.0180 |
| membership_only | 1 | globalTest_afterMean | 68.8970 | 71.5560 |
| membership_only | 1 | globalTest_afterStd | 10.6156 | 9.4905 |
| data_changes | 0 | clusterTest_before | 90.9820 | 90.4940 |
| data_changes | 0 | clusterTest_maxDrop | 0.3620 | 0.8140 |
| data_changes | 0 | clusterTest_afterMean | 91.0880 | 90.5900 |
| data_changes | 0 | clusterTest_afterStd | 0.2757 | 0.4958 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.4910 | 45.2470 |
| data_changes | 0 | globalTest_maxDrop | 0.1810 | 0.4070 |
| data_changes | 0 | globalTest_afterMean | 45.5440 | 47.4980 |
| data_changes | 0 | globalTest_afterStd | 0.1379 | 4.4854 |
| data_changes | 1 | clusterTest_before | 96.4280 | 96.2840 |
| data_changes | 1 | clusterTest_maxDrop | 2.7080 | 0.7840 |
| data_changes | 1 | clusterTest_afterMean | 95.6840 | 96.2300 |
| data_changes | 1 | clusterTest_afterStd | 0.7735 | 0.3012 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.2140 | 48.1420 |
| data_changes | 1 | globalTest_maxDrop | 1.3540 | 0.3920 |
| data_changes | 1 | globalTest_afterMean | 47.8420 | 48.2380 |
| data_changes | 1 | globalTest_afterStd | 0.3868 | 0.3099 |
