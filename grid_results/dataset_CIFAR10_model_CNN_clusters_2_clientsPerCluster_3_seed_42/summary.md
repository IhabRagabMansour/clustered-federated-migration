# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 83.0480 | 82.6920 |
| membership_only | 0 | clusterTest_maxDrop | 1.8080 | 4.9720 |
| membership_only | 0 | clusterTest_afterMean | 82.3400 | 80.0300 |
| membership_only | 0 | clusterTest_afterStd | 0.6793 | 1.3464 |
| membership_only | 0 | clusterTest_recovery | 2 | 4 |
| membership_only | 0 | globalTest_before | 41.5240 | 41.3460 |
| membership_only | 0 | globalTest_maxDrop | 0.9040 | 2.4860 |
| membership_only | 0 | globalTest_afterMean | 41.1700 | 40.0150 |
| membership_only | 0 | globalTest_afterStd | 0.3396 | 0.6732 |
| membership_only | 1 | clusterTest_before | 90.7060 | 89.5840 |
| membership_only | 1 | clusterTest_maxDrop | 73.0260 | 81.8040 |
| membership_only | 1 | clusterTest_afterMean | 57.9780 | 58.8820 |
| membership_only | 1 | clusterTest_afterStd | 31.1467 | 32.2082 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 45.3530 | 44.7920 |
| membership_only | 1 | globalTest_maxDrop | 1.0430 | 0.3220 |
| membership_only | 1 | globalTest_afterMean | 48.6180 | 51.2940 |
| membership_only | 1 | globalTest_afterStd | 3.9762 | 6.5257 |
| data_changes | 0 | clusterTest_before | 83.0480 | 82.6920 |
| data_changes | 0 | clusterTest_maxDrop | 1.8080 | 4.9120 |
| data_changes | 0 | clusterTest_afterMean | 82.3400 | 80.8980 |
| data_changes | 0 | clusterTest_afterStd | 0.6793 | 1.6219 |
| data_changes | 0 | clusterTest_recovery | 2 | 4 |
| data_changes | 0 | globalTest_before | 41.5240 | 41.3460 |
| data_changes | 0 | globalTest_maxDrop | 0.9040 | 2.4560 |
| data_changes | 0 | globalTest_afterMean | 41.1700 | 40.4490 |
| data_changes | 0 | globalTest_afterStd | 0.3396 | 0.8110 |
| data_changes | 1 | clusterTest_before | 90.7060 | 89.5840 |
| data_changes | 1 | clusterTest_maxDrop | 27.5260 | 1.0040 |
| data_changes | 1 | clusterTest_afterMean | 87.3360 | 90.2100 |
| data_changes | 1 | clusterTest_afterStd | 8.1720 | 0.8002 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 45.3530 | 44.7920 |
| data_changes | 1 | globalTest_maxDrop | 13.7630 | 0.5020 |
| data_changes | 1 | globalTest_afterMean | 43.6680 | 45.1050 |
| data_changes | 1 | globalTest_afterStd | 4.0860 | 0.4001 |
