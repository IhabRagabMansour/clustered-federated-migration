# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 71.5240 | 71.1080 |
| membership_only | 0 | clusterTest_maxDrop | 0.8040 | 20.2080 |
| membership_only | 0 | clusterTest_afterMean | 71.3460 | 65.2980 |
| membership_only | 0 | clusterTest_afterStd | 0.2503 | 6.0919 |
| membership_only | 0 | clusterTest_recovery | 0 | 15 |
| membership_only | 0 | globalTest_before | 35.7620 | 35.5540 |
| membership_only | 0 | globalTest_maxDrop | 0.4020 | 10.1040 |
| membership_only | 0 | globalTest_afterMean | 35.6730 | 32.6510 |
| membership_only | 0 | globalTest_afterStd | 0.1251 | 3.0452 |
| membership_only | 1 | clusterTest_before | 81.1720 | 79.4560 |
| membership_only | 1 | clusterTest_maxDrop | 81.1720 | 79.4560 |
| membership_only | 1 | clusterTest_afterMean | 36.9340 | 42.9680 |
| membership_only | 1 | clusterTest_afterStd | 37.0939 | 31.3313 |
| membership_only | 1 | clusterTest_recovery | 10 | 11 |
| membership_only | 1 | globalTest_before | 40.5860 | 39.7280 |
| membership_only | 1 | globalTest_maxDrop | 14.4360 | 9.2280 |
| membership_only | 1 | globalTest_afterMean | 33.2670 | 35.9830 |
| membership_only | 1 | globalTest_afterStd | 4.4429 | 3.8572 |
| data_changes | 0 | clusterTest_before | 71.5240 | 71.1080 |
| data_changes | 0 | clusterTest_maxDrop | 0.8040 | 23.9680 |
| data_changes | 0 | clusterTest_afterMean | 71.3460 | 64.7820 |
| data_changes | 0 | clusterTest_afterStd | 0.2503 | 6.7890 |
| data_changes | 0 | clusterTest_recovery | 0 | 9 |
| data_changes | 0 | globalTest_before | 35.7620 | 35.5540 |
| data_changes | 0 | globalTest_maxDrop | 0.4020 | 11.9840 |
| data_changes | 0 | globalTest_afterMean | 35.6730 | 32.4230 |
| data_changes | 0 | globalTest_afterStd | 0.1251 | 3.4077 |
| data_changes | 1 | clusterTest_before | 81.1720 | 79.4560 |
| data_changes | 1 | clusterTest_maxDrop | 28.5920 | 13.6960 |
| data_changes | 1 | clusterTest_afterMean | 77.2240 | 78.0860 |
| data_changes | 1 | clusterTest_afterStd | 8.4445 | 4.6045 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 40.5860 | 39.7280 |
| data_changes | 1 | globalTest_maxDrop | 14.2960 | 6.8480 |
| data_changes | 1 | globalTest_afterMean | 38.6120 | 39.0430 |
| data_changes | 1 | globalTest_afterStd | 4.2222 | 2.3023 |
