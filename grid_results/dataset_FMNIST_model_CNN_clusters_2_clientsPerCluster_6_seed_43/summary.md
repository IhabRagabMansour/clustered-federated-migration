# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.0540 | 89.5520 |
| membership_only | 0 | clusterTest_maxDrop | 0.1140 | 0.0720 |
| membership_only | 0 | clusterTest_afterMean | 90.3560 | 90.0200 |
| membership_only | 0 | clusterTest_afterStd | 0.1813 | 0.2408 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.0270 | 44.7760 |
| membership_only | 0 | globalTest_maxDrop | 0.0570 | 0.0160 |
| membership_only | 0 | globalTest_afterMean | 45.1780 | 45.0120 |
| membership_only | 0 | globalTest_afterStd | 0.0906 | 0.1160 |
| membership_only | 1 | clusterTest_before | 95.4360 | 95.2820 |
| membership_only | 1 | clusterTest_maxDrop | 36.4160 | 29.0220 |
| membership_only | 1 | clusterTest_afterMean | 81.7480 | 82.2440 |
| membership_only | 1 | clusterTest_afterStd | 13.1785 | 12.0090 |
| membership_only | 1 | clusterTest_recovery | 6 | 2 |
| membership_only | 1 | globalTest_before | 47.7180 | 47.6410 |
| membership_only | 1 | globalTest_maxDrop | 0.7680 | 0.3710 |
| membership_only | 1 | globalTest_afterMean | 64.9930 | 67.6630 |
| membership_only | 1 | globalTest_afterStd | 12.0434 | 11.3636 |
| data_changes | 0 | clusterTest_before | 90.0540 | 89.5520 |
| data_changes | 0 | clusterTest_maxDrop | 0.1140 | 0.1920 |
| data_changes | 0 | clusterTest_afterMean | 90.3560 | 89.9820 |
| data_changes | 0 | clusterTest_afterStd | 0.1813 | 0.3109 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.0270 | 44.7760 |
| data_changes | 0 | globalTest_maxDrop | 0.0570 | 0.0660 |
| data_changes | 0 | globalTest_afterMean | 45.1780 | 45.5690 |
| data_changes | 0 | globalTest_afterStd | 0.0906 | 1.1877 |
| data_changes | 1 | clusterTest_before | 95.4360 | 95.2820 |
| data_changes | 1 | clusterTest_maxDrop | 3.4160 | 0.9620 |
| data_changes | 1 | clusterTest_afterMean | 94.8920 | 95.3360 |
| data_changes | 1 | clusterTest_afterStd | 1.0230 | 0.3881 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.7180 | 47.6410 |
| data_changes | 1 | globalTest_maxDrop | 1.7080 | 0.4810 |
| data_changes | 1 | globalTest_afterMean | 47.4460 | 47.6780 |
| data_changes | 1 | globalTest_afterStd | 0.5115 | 0.2018 |
