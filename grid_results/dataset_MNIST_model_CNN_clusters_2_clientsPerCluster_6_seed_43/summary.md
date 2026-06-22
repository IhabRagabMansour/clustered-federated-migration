# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.3423 | 99.3092 |
| membership_only | 0 | clusterTest_maxDrop | -0.0739 | -0.0876 |
| membership_only | 0 | clusterTest_afterMean | 99.4746 | 99.4610 |
| membership_only | 0 | clusterTest_afterStd | 0.0435 | 0.0469 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.0520 | 51.0370 |
| membership_only | 0 | globalTest_maxDrop | -0.0380 | -0.0530 |
| membership_only | 0 | globalTest_afterMean | 51.1200 | 51.2730 |
| membership_only | 0 | globalTest_afterStd | 0.0224 | 0.3315 |
| membership_only | 1 | clusterTest_before | 98.6813 | 98.5970 |
| membership_only | 1 | clusterTest_maxDrop | 78.3152 | 70.8661 |
| membership_only | 1 | clusterTest_afterMean | 83.0488 | 82.2526 |
| membership_only | 1 | clusterTest_afterStd | 25.0271 | 24.1170 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.9690 | 47.9280 |
| membership_only | 1 | globalTest_maxDrop | 0.2490 | 0.1880 |
| membership_only | 1 | globalTest_afterMean | 75.0510 | 76.8170 |
| membership_only | 1 | globalTest_afterStd | 17.5394 | 15.2326 |
| data_changes | 0 | clusterTest_before | 99.3423 | 99.3092 |
| data_changes | 0 | clusterTest_maxDrop | -0.0739 | 0.0876 |
| data_changes | 0 | clusterTest_afterMean | 99.4727 | 99.3987 |
| data_changes | 0 | clusterTest_afterStd | 0.0353 | 0.0994 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.0520 | 51.0370 |
| data_changes | 0 | globalTest_maxDrop | -0.0380 | -0.0230 |
| data_changes | 0 | globalTest_afterMean | 51.1190 | 52.6880 |
| data_changes | 0 | globalTest_afterStd | 0.0181 | 2.8549 |
| data_changes | 1 | clusterTest_before | 98.6813 | 98.5970 |
| data_changes | 1 | clusterTest_maxDrop | 2.3020 | 0.8393 |
| data_changes | 1 | clusterTest_afterMean | 98.1444 | 98.4592 |
| data_changes | 1 | clusterTest_afterStd | 0.6260 | 0.2593 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.9690 | 47.9280 |
| data_changes | 1 | globalTest_maxDrop | 1.1190 | 0.4080 |
| data_changes | 1 | globalTest_afterMean | 47.7080 | 47.8610 |
| data_changes | 1 | globalTest_afterStd | 0.3043 | 0.1261 |
