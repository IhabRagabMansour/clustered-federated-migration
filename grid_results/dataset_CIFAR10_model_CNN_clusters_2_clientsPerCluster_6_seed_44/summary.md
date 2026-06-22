# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 82.2820 | 81.9400 |
| membership_only | 0 | clusterTest_maxDrop | 2.3620 | 3.5800 |
| membership_only | 0 | clusterTest_afterMean | 81.1440 | 80.7900 |
| membership_only | 0 | clusterTest_afterStd | 0.8072 | 1.3539 |
| membership_only | 0 | clusterTest_recovery | 12 | 5 |
| membership_only | 0 | globalTest_before | 41.1410 | 40.9700 |
| membership_only | 0 | globalTest_maxDrop | 1.1810 | 1.7900 |
| membership_only | 0 | globalTest_afterMean | 40.5720 | 40.3950 |
| membership_only | 0 | globalTest_afterStd | 0.4036 | 0.6769 |
| membership_only | 1 | clusterTest_before | 89.1280 | 88.7100 |
| membership_only | 1 | clusterTest_maxDrop | 87.8680 | 87.3100 |
| membership_only | 1 | clusterTest_afterMean | 53.1880 | 50.7780 |
| membership_only | 1 | clusterTest_afterStd | 34.7005 | 36.9589 |
| membership_only | 1 | clusterTest_recovery | 12 | 10 |
| membership_only | 1 | globalTest_before | 44.5640 | 44.3550 |
| membership_only | 1 | globalTest_maxDrop | 7.6140 | 5.8650 |
| membership_only | 1 | globalTest_afterMean | 44.3250 | 44.8900 |
| membership_only | 1 | globalTest_afterStd | 3.4481 | 3.6693 |
| data_changes | 0 | clusterTest_before | 82.2820 | 81.9400 |
| data_changes | 0 | clusterTest_maxDrop | 2.3620 | 3.2400 |
| data_changes | 0 | clusterTest_afterMean | 81.1440 | 80.7360 |
| data_changes | 0 | clusterTest_afterStd | 0.8072 | 1.0006 |
| data_changes | 0 | clusterTest_recovery | 12 | 5 |
| data_changes | 0 | globalTest_before | 41.1410 | 40.9700 |
| data_changes | 0 | globalTest_maxDrop | 1.1810 | 1.6200 |
| data_changes | 0 | globalTest_afterMean | 40.5720 | 40.3680 |
| data_changes | 0 | globalTest_afterStd | 0.4036 | 0.5003 |
| data_changes | 1 | clusterTest_before | 89.1280 | 88.7100 |
| data_changes | 1 | clusterTest_maxDrop | 24.1480 | 4.4700 |
| data_changes | 1 | clusterTest_afterMean | 85.7920 | 87.9880 |
| data_changes | 1 | clusterTest_afterStd | 7.1330 | 1.4908 |
| data_changes | 1 | clusterTest_recovery | 4 | 1 |
| data_changes | 1 | globalTest_before | 44.5640 | 44.3550 |
| data_changes | 1 | globalTest_maxDrop | 12.0740 | 2.2350 |
| data_changes | 1 | globalTest_afterMean | 42.8960 | 43.9940 |
| data_changes | 1 | globalTest_afterStd | 3.5665 | 0.7454 |
