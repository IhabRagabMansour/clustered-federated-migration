# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.9420 | 90.3560 |
| membership_only | 0 | clusterTest_maxDrop | 1.3220 | 0.9160 |
| membership_only | 0 | clusterTest_afterMean | 90.6860 | 90.3240 |
| membership_only | 0 | clusterTest_afterStd | 0.5065 | 0.4781 |
| membership_only | 0 | clusterTest_recovery | 1 | 0 |
| membership_only | 0 | globalTest_before | 45.4710 | 45.1780 |
| membership_only | 0 | globalTest_maxDrop | 0.6610 | 0.4580 |
| membership_only | 0 | globalTest_afterMean | 45.3430 | 45.1620 |
| membership_only | 0 | globalTest_afterStd | 0.2533 | 0.2390 |
| membership_only | 1 | clusterTest_before | 96.1520 | 96.0480 |
| membership_only | 1 | clusterTest_maxDrop | 29.9120 | 29.8280 |
| membership_only | 1 | clusterTest_afterMean | 83.0400 | 82.9320 |
| membership_only | 1 | clusterTest_afterStd | 12.2294 | 9.9694 |
| membership_only | 1 | clusterTest_recovery | 4 | 8 |
| membership_only | 1 | globalTest_before | 48.0760 | 48.0390 |
| membership_only | 1 | globalTest_maxDrop | -7.2140 | -11.0210 |
| membership_only | 1 | globalTest_afterMean | 69.2910 | 73.2640 |
| membership_only | 1 | globalTest_afterStd | 10.0621 | 8.3472 |
| data_changes | 0 | clusterTest_before | 90.9420 | 90.3560 |
| data_changes | 0 | clusterTest_maxDrop | 1.3220 | 0.9160 |
| data_changes | 0 | clusterTest_afterMean | 90.6860 | 90.2740 |
| data_changes | 0 | clusterTest_afterStd | 0.5065 | 0.4960 |
| data_changes | 0 | clusterTest_recovery | 1 | 0 |
| data_changes | 0 | globalTest_before | 45.4710 | 45.1780 |
| data_changes | 0 | globalTest_maxDrop | 0.6610 | 0.4580 |
| data_changes | 0 | globalTest_afterMean | 45.3430 | 46.0260 |
| data_changes | 0 | globalTest_afterStd | 0.2533 | 1.8082 |
| data_changes | 1 | clusterTest_before | 96.1520 | 96.0480 |
| data_changes | 1 | clusterTest_maxDrop | 7.5920 | 0.3480 |
| data_changes | 1 | clusterTest_afterMean | 94.9780 | 96.1240 |
| data_changes | 1 | clusterTest_afterStd | 2.1907 | 0.2671 |
| data_changes | 1 | clusterTest_recovery | 3 | 0 |
| data_changes | 1 | globalTest_before | 48.0760 | 48.0390 |
| data_changes | 1 | globalTest_maxDrop | 3.7960 | 0.1890 |
| data_changes | 1 | globalTest_afterMean | 47.4890 | 48.5840 |
| data_changes | 1 | globalTest_afterStd | 1.0953 | 0.7547 |
