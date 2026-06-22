# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 82.6040 | 82.0860 |
| membership_only | 0 | clusterTest_maxDrop | 13.3040 | 14.1660 |
| membership_only | 0 | clusterTest_afterMean | 78.5240 | 78.1360 |
| membership_only | 0 | clusterTest_afterStd | 3.6270 | 4.5794 |
| membership_only | 0 | clusterTest_recovery | 7 | 2 |
| membership_only | 0 | globalTest_before | 41.3020 | 41.0430 |
| membership_only | 0 | globalTest_maxDrop | 6.6520 | 7.0830 |
| membership_only | 0 | globalTest_afterMean | 39.2620 | 39.0680 |
| membership_only | 0 | globalTest_afterStd | 1.8135 | 2.2897 |
| membership_only | 1 | clusterTest_before | 89.8460 | 89.6980 |
| membership_only | 1 | clusterTest_maxDrop | 89.3060 | 83.9380 |
| membership_only | 1 | clusterTest_afterMean | 51.2940 | 58.3840 |
| membership_only | 1 | clusterTest_afterStd | 38.2792 | 33.9541 |
| membership_only | 1 | clusterTest_recovery | 10 | 7 |
| membership_only | 1 | globalTest_before | 44.9230 | 44.8490 |
| membership_only | 1 | globalTest_maxDrop | 5.4430 | 1.7290 |
| membership_only | 1 | globalTest_afterMean | 45.7730 | 49.9660 |
| membership_only | 1 | globalTest_afterStd | 5.4490 | 7.2665 |
| data_changes | 0 | clusterTest_before | 82.6040 | 82.0860 |
| data_changes | 0 | clusterTest_maxDrop | 13.3040 | 16.2460 |
| data_changes | 0 | clusterTest_afterMean | 78.5240 | 77.2340 |
| data_changes | 0 | clusterTest_afterStd | 3.6270 | 5.6777 |
| data_changes | 0 | clusterTest_recovery | 7 | 4 |
| data_changes | 0 | globalTest_before | 41.3020 | 41.0430 |
| data_changes | 0 | globalTest_maxDrop | 6.6520 | 8.1230 |
| data_changes | 0 | globalTest_afterMean | 39.2620 | 38.6170 |
| data_changes | 0 | globalTest_afterStd | 1.8135 | 2.8389 |
| data_changes | 1 | clusterTest_before | 89.8460 | 89.6980 |
| data_changes | 1 | clusterTest_maxDrop | 22.1060 | 3.6380 |
| data_changes | 1 | clusterTest_afterMean | 86.7820 | 89.8580 |
| data_changes | 1 | clusterTest_afterStd | 6.7004 | 1.4486 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.9230 | 44.8490 |
| data_changes | 1 | globalTest_maxDrop | 11.0530 | 1.8190 |
| data_changes | 1 | globalTest_afterMean | 43.3910 | 44.9290 |
| data_changes | 1 | globalTest_afterStd | 3.3502 | 0.7243 |
