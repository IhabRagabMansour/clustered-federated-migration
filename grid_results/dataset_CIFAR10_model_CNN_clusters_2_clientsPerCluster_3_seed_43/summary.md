# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 83.9940 | 83.4000 |
| membership_only | 0 | clusterTest_maxDrop | 10.6940 | 5.1600 |
| membership_only | 0 | clusterTest_afterMean | 81.3720 | 81.2980 |
| membership_only | 0 | clusterTest_afterStd | 3.2556 | 2.1753 |
| membership_only | 0 | clusterTest_recovery | 1 | 4 |
| membership_only | 0 | globalTest_before | 41.9970 | 41.7000 |
| membership_only | 0 | globalTest_maxDrop | 5.3470 | 2.5800 |
| membership_only | 0 | globalTest_afterMean | 40.6860 | 40.6490 |
| membership_only | 0 | globalTest_afterStd | 1.6278 | 1.0877 |
| membership_only | 1 | clusterTest_before | 90.7200 | 90.3920 |
| membership_only | 1 | clusterTest_maxDrop | 65.3000 | 76.9920 |
| membership_only | 1 | clusterTest_afterMean | 60.0320 | 63.1040 |
| membership_only | 1 | clusterTest_afterStd | 28.8255 | 29.3478 |
| membership_only | 1 | clusterTest_recovery | 6 | 4 |
| membership_only | 1 | globalTest_before | 45.3600 | 45.1960 |
| membership_only | 1 | globalTest_maxDrop | 1.4600 | 0.2260 |
| membership_only | 1 | globalTest_afterMean | 49.6140 | 53.7970 |
| membership_only | 1 | globalTest_afterStd | 4.3076 | 7.4792 |
| data_changes | 0 | clusterTest_before | 83.9940 | 83.4000 |
| data_changes | 0 | clusterTest_maxDrop | 10.6940 | 6.4200 |
| data_changes | 0 | clusterTest_afterMean | 81.3720 | 81.2980 |
| data_changes | 0 | clusterTest_afterStd | 3.2556 | 2.0933 |
| data_changes | 0 | clusterTest_recovery | 1 | 3 |
| data_changes | 0 | globalTest_before | 41.9970 | 41.7000 |
| data_changes | 0 | globalTest_maxDrop | 5.3470 | 3.2100 |
| data_changes | 0 | globalTest_afterMean | 40.6860 | 40.6490 |
| data_changes | 0 | globalTest_afterStd | 1.6278 | 1.0466 |
| data_changes | 1 | clusterTest_before | 90.7200 | 90.3920 |
| data_changes | 1 | clusterTest_maxDrop | 11.9000 | 2.0720 |
| data_changes | 1 | clusterTest_afterMean | 89.0420 | 90.2960 |
| data_changes | 1 | clusterTest_afterStd | 3.6529 | 1.0160 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 45.3600 | 45.1960 |
| data_changes | 1 | globalTest_maxDrop | 5.9500 | 1.0360 |
| data_changes | 1 | globalTest_afterMean | 44.5210 | 45.1480 |
| data_changes | 1 | globalTest_afterStd | 1.8264 | 0.5080 |
