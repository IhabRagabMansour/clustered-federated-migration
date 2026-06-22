# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.2640 | 89.7540 |
| membership_only | 0 | clusterTest_maxDrop | -0.0360 | -0.0060 |
| membership_only | 0 | clusterTest_afterMean | 90.5940 | 90.1700 |
| membership_only | 0 | clusterTest_afterStd | 0.1769 | 0.3004 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.1320 | 44.8770 |
| membership_only | 0 | globalTest_maxDrop | -0.0180 | -0.0030 |
| membership_only | 0 | globalTest_afterMean | 45.2970 | 45.0850 |
| membership_only | 0 | globalTest_afterStd | 0.0884 | 0.1502 |
| membership_only | 1 | clusterTest_before | 95.6540 | 95.5280 |
| membership_only | 1 | clusterTest_maxDrop | 34.9940 | 31.8880 |
| membership_only | 1 | clusterTest_afterMean | 82.1740 | 82.6100 |
| membership_only | 1 | clusterTest_afterStd | 13.0866 | 11.9971 |
| membership_only | 1 | clusterTest_recovery | 8 | 4 |
| membership_only | 1 | globalTest_before | 47.8270 | 47.7650 |
| membership_only | 1 | globalTest_maxDrop | 0.7370 | -7.0850 |
| membership_only | 1 | globalTest_afterMean | 66.1140 | 69.4240 |
| membership_only | 1 | globalTest_afterStd | 12.0372 | 10.0964 |
| data_changes | 0 | clusterTest_before | 90.2640 | 89.7540 |
| data_changes | 0 | clusterTest_maxDrop | -0.0360 | 0.1340 |
| data_changes | 0 | clusterTest_afterMean | 90.5940 | 90.1940 |
| data_changes | 0 | clusterTest_afterStd | 0.1769 | 0.3169 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.1320 | 44.8770 |
| data_changes | 0 | globalTest_maxDrop | -0.0180 | 0.0370 |
| data_changes | 0 | globalTest_afterMean | 45.2970 | 45.6620 |
| data_changes | 0 | globalTest_afterStd | 0.0884 | 1.3560 |
| data_changes | 1 | clusterTest_before | 95.6540 | 95.5280 |
| data_changes | 1 | clusterTest_maxDrop | 5.0740 | 0.3280 |
| data_changes | 1 | clusterTest_afterMean | 94.8020 | 95.7120 |
| data_changes | 1 | clusterTest_afterStd | 1.4794 | 0.3082 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.8270 | 47.7650 |
| data_changes | 1 | globalTest_maxDrop | 2.5370 | 0.1650 |
| data_changes | 1 | globalTest_afterMean | 47.4010 | 48.0440 |
| data_changes | 1 | globalTest_afterStd | 0.7397 | 0.4498 |
