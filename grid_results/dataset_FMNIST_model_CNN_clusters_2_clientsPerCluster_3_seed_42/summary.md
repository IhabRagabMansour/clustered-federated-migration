# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 91.3960 | 91.0000 |
| membership_only | 0 | clusterTest_maxDrop | 1.4560 | 2.1200 |
| membership_only | 0 | clusterTest_afterMean | 91.3800 | 90.7620 |
| membership_only | 0 | clusterTest_afterStd | 0.6627 | 0.7645 |
| membership_only | 0 | clusterTest_recovery | 8 | 8 |
| membership_only | 0 | globalTest_before | 45.6980 | 45.5000 |
| membership_only | 0 | globalTest_maxDrop | 0.7280 | 1.0600 |
| membership_only | 0 | globalTest_afterMean | 45.6900 | 45.3810 |
| membership_only | 0 | globalTest_afterStd | 0.3314 | 0.3822 |
| membership_only | 1 | clusterTest_before | 96.9060 | 96.7560 |
| membership_only | 1 | clusterTest_maxDrop | 28.3260 | 28.8160 |
| membership_only | 1 | clusterTest_afterMean | 84.6380 | 84.4060 |
| membership_only | 1 | clusterTest_afterStd | 11.4405 | 11.1222 |
| membership_only | 1 | clusterTest_recovery | 10 | 4 |
| membership_only | 1 | globalTest_before | 48.4530 | 48.3950 |
| membership_only | 1 | globalTest_maxDrop | -7.4570 | -9.1750 |
| membership_only | 1 | globalTest_afterMean | 70.1940 | 72.2080 |
| membership_only | 1 | globalTest_afterStd | 10.8531 | 9.9707 |
| data_changes | 0 | clusterTest_before | 91.3960 | 91.0000 |
| data_changes | 0 | clusterTest_maxDrop | 1.4560 | 3.2200 |
| data_changes | 0 | clusterTest_afterMean | 91.3800 | 90.5120 |
| data_changes | 0 | clusterTest_afterStd | 0.6627 | 1.0976 |
| data_changes | 0 | clusterTest_recovery | 8 | 8 |
| data_changes | 0 | globalTest_before | 45.6980 | 45.5000 |
| data_changes | 0 | globalTest_maxDrop | 0.7280 | 1.6000 |
| data_changes | 0 | globalTest_afterMean | 45.6900 | 45.5470 |
| data_changes | 0 | globalTest_afterStd | 0.3314 | 0.9512 |
| data_changes | 1 | clusterTest_before | 96.9060 | 96.7560 |
| data_changes | 1 | clusterTest_maxDrop | 2.8860 | 0.7360 |
| data_changes | 1 | clusterTest_afterMean | 96.0520 | 96.5960 |
| data_changes | 1 | clusterTest_afterStd | 0.7880 | 0.3170 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.4530 | 48.3950 |
| data_changes | 1 | globalTest_maxDrop | 1.4430 | 0.3850 |
| data_changes | 1 | globalTest_afterMean | 48.0260 | 49.0120 |
| data_changes | 1 | globalTest_afterStd | 0.3940 | 0.9510 |
