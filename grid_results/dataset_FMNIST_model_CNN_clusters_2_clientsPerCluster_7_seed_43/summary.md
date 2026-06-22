# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.5360 | 89.0780 |
| membership_only | 0 | clusterTest_maxDrop | 0.0160 | 0.0380 |
| membership_only | 0 | clusterTest_afterMean | 90.0020 | 89.4160 |
| membership_only | 0 | clusterTest_afterStd | 0.2598 | 0.3071 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.7680 | 44.5390 |
| membership_only | 0 | globalTest_maxDrop | 0.0080 | 0.0190 |
| membership_only | 0 | globalTest_afterMean | 45.0010 | 44.7150 |
| membership_only | 0 | globalTest_afterStd | 0.1299 | 0.1532 |
| membership_only | 1 | clusterTest_before | 95.0760 | 94.9080 |
| membership_only | 1 | clusterTest_maxDrop | 33.3560 | 32.9680 |
| membership_only | 1 | clusterTest_afterMean | 81.8700 | 81.3180 |
| membership_only | 1 | clusterTest_afterStd | 12.3722 | 12.6180 |
| membership_only | 1 | clusterTest_recovery | 8 | 10 |
| membership_only | 1 | globalTest_before | 47.5380 | 47.4540 |
| membership_only | 1 | globalTest_maxDrop | 1.0080 | 0.7240 |
| membership_only | 1 | globalTest_afterMean | 64.0800 | 66.4760 |
| membership_only | 1 | globalTest_afterStd | 12.2421 | 11.4136 |
| data_changes | 0 | clusterTest_before | 89.5360 | 89.0780 |
| data_changes | 0 | clusterTest_maxDrop | 0.0160 | 0.3380 |
| data_changes | 0 | clusterTest_afterMean | 90.0020 | 89.3360 |
| data_changes | 0 | clusterTest_afterStd | 0.2598 | 0.3089 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.7680 | 44.5390 |
| data_changes | 0 | globalTest_maxDrop | 0.0080 | -0.0210 |
| data_changes | 0 | globalTest_afterMean | 45.0010 | 45.0920 |
| data_changes | 0 | globalTest_afterStd | 0.1299 | 0.8693 |
| data_changes | 1 | clusterTest_before | 95.0760 | 94.9080 |
| data_changes | 1 | clusterTest_maxDrop | 2.6560 | 0.4480 |
| data_changes | 1 | clusterTest_afterMean | 94.6800 | 95.0820 |
| data_changes | 1 | clusterTest_afterStd | 0.8535 | 0.3013 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.5380 | 47.4540 |
| data_changes | 1 | globalTest_maxDrop | 1.3280 | 0.2240 |
| data_changes | 1 | globalTest_afterMean | 47.3400 | 47.5470 |
| data_changes | 1 | globalTest_afterStd | 0.4267 | 0.1536 |
