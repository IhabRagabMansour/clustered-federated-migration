# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.7100 | 79.9560 |
| membership_only | 0 | clusterTest_maxDrop | -0.2100 | 0.1360 |
| membership_only | 0 | clusterTest_afterMean | 81.6200 | 81.0240 |
| membership_only | 0 | clusterTest_afterStd | 0.4834 | 0.5371 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 40.3550 | 39.9780 |
| membership_only | 0 | globalTest_maxDrop | -0.1050 | 0.0680 |
| membership_only | 0 | globalTest_afterMean | 40.8100 | 40.5120 |
| membership_only | 0 | globalTest_afterStd | 0.2417 | 0.2685 |
| membership_only | 1 | clusterTest_before | 88.6480 | 88.2160 |
| membership_only | 1 | clusterTest_maxDrop | 60.2680 | 68.5160 |
| membership_only | 1 | clusterTest_afterMean | 68.4440 | 63.6900 |
| membership_only | 1 | clusterTest_afterStd | 20.0234 | 25.1450 |
| membership_only | 1 | clusterTest_recovery | 10 | 10 |
| membership_only | 1 | globalTest_before | 44.3240 | 44.1080 |
| membership_only | 1 | globalTest_maxDrop | 1.7440 | 3.1380 |
| membership_only | 1 | globalTest_afterMean | 48.3040 | 47.5410 |
| membership_only | 1 | globalTest_afterStd | 6.1491 | 6.6665 |
| data_changes | 0 | clusterTest_before | 80.7100 | 79.9560 |
| data_changes | 0 | clusterTest_maxDrop | -0.2100 | 0.0760 |
| data_changes | 0 | clusterTest_afterMean | 81.6200 | 81.0100 |
| data_changes | 0 | clusterTest_afterStd | 0.4834 | 0.5024 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.3550 | 39.9780 |
| data_changes | 0 | globalTest_maxDrop | -0.1050 | 0.0380 |
| data_changes | 0 | globalTest_afterMean | 40.8100 | 40.5050 |
| data_changes | 0 | globalTest_afterStd | 0.2417 | 0.2512 |
| data_changes | 1 | clusterTest_before | 88.6480 | 88.2160 |
| data_changes | 1 | clusterTest_maxDrop | 9.1080 | 2.7560 |
| data_changes | 1 | clusterTest_afterMean | 87.5020 | 88.0520 |
| data_changes | 1 | clusterTest_afterStd | 2.7863 | 1.0776 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.3240 | 44.1080 |
| data_changes | 1 | globalTest_maxDrop | 4.5540 | 1.3780 |
| data_changes | 1 | globalTest_afterMean | 43.7510 | 44.0260 |
| data_changes | 1 | globalTest_afterStd | 1.3931 | 0.5388 |
