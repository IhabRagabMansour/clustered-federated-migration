# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.5860 | 69.2260 |
| membership_only | 0 | clusterTest_maxDrop | 0.2260 | 0.6660 |
| membership_only | 0 | clusterTest_afterMean | 70.5740 | 69.4480 |
| membership_only | 0 | clusterTest_afterStd | 0.1475 | 0.4865 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 35.2930 | 34.6130 |
| membership_only | 0 | globalTest_maxDrop | 0.1130 | 0.3330 |
| membership_only | 0 | globalTest_afterMean | 35.2870 | 34.7240 |
| membership_only | 0 | globalTest_afterStd | 0.0738 | 0.2432 |
| membership_only | 1 | clusterTest_before | 79.7800 | 78.7660 |
| membership_only | 1 | clusterTest_maxDrop | 78.9200 | 78.3860 |
| membership_only | 1 | clusterTest_afterMean | 41.0900 | 42.0280 |
| membership_only | 1 | clusterTest_afterStd | 34.7503 | 34.1132 |
| membership_only | 1 | clusterTest_recovery | 10 | 6 |
| membership_only | 1 | globalTest_before | 39.8900 | 39.3830 |
| membership_only | 1 | globalTest_maxDrop | 13.0700 | 11.2930 |
| membership_only | 1 | globalTest_afterMean | 33.1440 | 35.0360 |
| membership_only | 1 | globalTest_afterStd | 4.8834 | 4.1440 |
| data_changes | 0 | clusterTest_before | 70.5860 | 69.2260 |
| data_changes | 0 | clusterTest_maxDrop | 0.2260 | 1.8460 |
| data_changes | 0 | clusterTest_afterMean | 70.5740 | 69.1960 |
| data_changes | 0 | clusterTest_afterStd | 0.1475 | 0.8848 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 35.2930 | 34.6130 |
| data_changes | 0 | globalTest_maxDrop | 0.1130 | 0.9230 |
| data_changes | 0 | globalTest_afterMean | 35.2870 | 34.6010 |
| data_changes | 0 | globalTest_afterStd | 0.0738 | 0.4371 |
| data_changes | 1 | clusterTest_before | 79.7800 | 78.7660 |
| data_changes | 1 | clusterTest_maxDrop | 12.8200 | 5.8660 |
| data_changes | 1 | clusterTest_afterMean | 77.6800 | 77.8280 |
| data_changes | 1 | clusterTest_afterStd | 4.2132 | 2.3178 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 39.8900 | 39.3830 |
| data_changes | 1 | globalTest_maxDrop | 6.4100 | 2.9330 |
| data_changes | 1 | globalTest_afterMean | 38.8400 | 38.9140 |
| data_changes | 1 | globalTest_afterStd | 2.1066 | 1.1589 |
