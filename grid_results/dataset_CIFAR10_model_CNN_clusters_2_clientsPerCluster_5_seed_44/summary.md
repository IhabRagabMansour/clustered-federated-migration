# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 82.5880 | 82.2880 |
| membership_only | 0 | clusterTest_maxDrop | 4.0880 | 3.8080 |
| membership_only | 0 | clusterTest_afterMean | 80.8660 | 80.8820 |
| membership_only | 0 | clusterTest_afterStd | 1.1836 | 0.9204 |
| membership_only | 0 | clusterTest_recovery | 7 | 7 |
| membership_only | 0 | globalTest_before | 41.2940 | 41.1440 |
| membership_only | 0 | globalTest_maxDrop | 2.0440 | 1.9040 |
| membership_only | 0 | globalTest_afterMean | 40.4330 | 40.4410 |
| membership_only | 0 | globalTest_afterStd | 0.5918 | 0.4602 |
| membership_only | 1 | clusterTest_before | 89.3520 | 89.4580 |
| membership_only | 1 | clusterTest_maxDrop | 89.0920 | 89.3780 |
| membership_only | 1 | clusterTest_afterMean | 51.7660 | 54.8880 |
| membership_only | 1 | clusterTest_afterStd | 37.2567 | 37.3364 |
| membership_only | 1 | clusterTest_recovery | 10 | 10 |
| membership_only | 1 | globalTest_before | 44.6760 | 44.7290 |
| membership_only | 1 | globalTest_maxDrop | 6.5260 | 5.7990 |
| membership_only | 1 | globalTest_afterMean | 44.3220 | 47.4690 |
| membership_only | 1 | globalTest_afterStd | 4.0712 | 8.1058 |
| data_changes | 0 | clusterTest_before | 82.5880 | 82.2880 |
| data_changes | 0 | clusterTest_maxDrop | 4.0880 | 3.2080 |
| data_changes | 0 | clusterTest_afterMean | 80.8660 | 80.6040 |
| data_changes | 0 | clusterTest_afterStd | 1.1836 | 0.8027 |
| data_changes | 0 | clusterTest_recovery | 7 | 7 |
| data_changes | 0 | globalTest_before | 41.2940 | 41.1440 |
| data_changes | 0 | globalTest_maxDrop | 2.0440 | 1.6040 |
| data_changes | 0 | globalTest_afterMean | 40.4330 | 40.3020 |
| data_changes | 0 | globalTest_afterStd | 0.5918 | 0.4013 |
| data_changes | 1 | clusterTest_before | 89.3520 | 89.4580 |
| data_changes | 1 | clusterTest_maxDrop | 41.3320 | 5.4580 |
| data_changes | 1 | clusterTest_afterMean | 84.5620 | 88.7760 |
| data_changes | 1 | clusterTest_afterStd | 12.2445 | 1.7324 |
| data_changes | 1 | clusterTest_recovery | 4 | 1 |
| data_changes | 1 | globalTest_before | 44.6760 | 44.7290 |
| data_changes | 1 | globalTest_maxDrop | 20.6660 | 2.7290 |
| data_changes | 1 | globalTest_afterMean | 42.2810 | 44.3880 |
| data_changes | 1 | globalTest_afterStd | 6.1222 | 0.8662 |
