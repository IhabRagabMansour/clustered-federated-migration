# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.1680 | 88.5380 |
| membership_only | 0 | clusterTest_maxDrop | -0.3920 | -0.0220 |
| membership_only | 0 | clusterTest_afterMean | 89.7280 | 89.0740 |
| membership_only | 0 | clusterTest_afterStd | 0.1324 | 0.2813 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.5840 | 44.2690 |
| membership_only | 0 | globalTest_maxDrop | -0.1960 | -0.0110 |
| membership_only | 0 | globalTest_afterMean | 44.8640 | 44.5620 |
| membership_only | 0 | globalTest_afterStd | 0.0662 | 0.1267 |
| membership_only | 1 | clusterTest_before | 94.9160 | 94.7560 |
| membership_only | 1 | clusterTest_maxDrop | 29.6960 | 33.3960 |
| membership_only | 1 | clusterTest_afterMean | 82.3320 | 81.9160 |
| membership_only | 1 | clusterTest_afterStd | 11.5186 | 12.1599 |
| membership_only | 1 | clusterTest_recovery | 10 | 10 |
| membership_only | 1 | globalTest_before | 47.4580 | 47.3780 |
| membership_only | 1 | globalTest_maxDrop | 1.3280 | 0.7180 |
| membership_only | 1 | globalTest_afterMean | 63.2560 | 66.0870 |
| membership_only | 1 | globalTest_afterStd | 12.2176 | 11.4781 |
| data_changes | 0 | clusterTest_before | 89.1680 | 88.5380 |
| data_changes | 0 | clusterTest_maxDrop | -0.3920 | -0.0420 |
| data_changes | 0 | clusterTest_afterMean | 89.7280 | 89.0660 |
| data_changes | 0 | clusterTest_afterStd | 0.1324 | 0.3005 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.5840 | 44.2690 |
| data_changes | 0 | globalTest_maxDrop | -0.1960 | -0.0210 |
| data_changes | 0 | globalTest_afterMean | 44.8640 | 45.2720 |
| data_changes | 0 | globalTest_afterStd | 0.0662 | 1.7826 |
| data_changes | 1 | clusterTest_before | 94.9160 | 94.7560 |
| data_changes | 1 | clusterTest_maxDrop | 1.1360 | 0.5760 |
| data_changes | 1 | clusterTest_afterMean | 94.7420 | 94.8460 |
| data_changes | 1 | clusterTest_afterStd | 0.4310 | 0.2561 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.4580 | 47.3780 |
| data_changes | 1 | globalTest_maxDrop | 0.5680 | 0.2880 |
| data_changes | 1 | globalTest_afterMean | 47.3710 | 47.4340 |
| data_changes | 1 | globalTest_afterStd | 0.2155 | 0.1343 |
