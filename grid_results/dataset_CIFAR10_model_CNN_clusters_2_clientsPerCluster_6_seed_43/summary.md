# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 82.7700 | 81.9780 |
| membership_only | 0 | clusterTest_maxDrop | 4.5700 | 1.6380 |
| membership_only | 0 | clusterTest_afterMean | 81.5620 | 81.9800 |
| membership_only | 0 | clusterTest_afterStd | 1.5675 | 0.8468 |
| membership_only | 0 | clusterTest_recovery | 3 | 7 |
| membership_only | 0 | globalTest_before | 41.3850 | 40.9890 |
| membership_only | 0 | globalTest_maxDrop | 2.2850 | 0.8190 |
| membership_only | 0 | globalTest_afterMean | 40.7810 | 40.9900 |
| membership_only | 0 | globalTest_afterStd | 0.7838 | 0.4234 |
| membership_only | 1 | clusterTest_before | 89.0280 | 88.8300 |
| membership_only | 1 | clusterTest_maxDrop | 87.2680 | 80.1100 |
| membership_only | 1 | clusterTest_afterMean | 51.9240 | 51.8240 |
| membership_only | 1 | clusterTest_afterStd | 36.4523 | 35.3008 |
| membership_only | 1 | clusterTest_recovery | 12 | 10 |
| membership_only | 1 | globalTest_before | 44.5140 | 44.4150 |
| membership_only | 1 | globalTest_maxDrop | 7.9340 | 3.0750 |
| membership_only | 1 | globalTest_afterMean | 43.4010 | 45.5130 |
| membership_only | 1 | globalTest_afterStd | 3.7868 | 3.2547 |
| data_changes | 0 | clusterTest_before | 82.7700 | 81.9780 |
| data_changes | 0 | clusterTest_maxDrop | 4.5700 | 1.7580 |
| data_changes | 0 | clusterTest_afterMean | 81.5620 | 81.8700 |
| data_changes | 0 | clusterTest_afterStd | 1.5675 | 0.8922 |
| data_changes | 0 | clusterTest_recovery | 3 | 7 |
| data_changes | 0 | globalTest_before | 41.3850 | 40.9890 |
| data_changes | 0 | globalTest_maxDrop | 2.2850 | 0.8790 |
| data_changes | 0 | globalTest_afterMean | 40.7810 | 40.9350 |
| data_changes | 0 | globalTest_afterStd | 0.7838 | 0.4461 |
| data_changes | 1 | clusterTest_before | 89.0280 | 88.8300 |
| data_changes | 1 | clusterTest_maxDrop | 8.4880 | 2.1300 |
| data_changes | 1 | clusterTest_afterMean | 88.2000 | 89.2340 |
| data_changes | 1 | clusterTest_afterStd | 2.6948 | 0.9491 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.5140 | 44.4150 |
| data_changes | 1 | globalTest_maxDrop | 4.2440 | 1.0650 |
| data_changes | 1 | globalTest_afterMean | 44.1000 | 44.6170 |
| data_changes | 1 | globalTest_afterStd | 1.3474 | 0.4746 |
