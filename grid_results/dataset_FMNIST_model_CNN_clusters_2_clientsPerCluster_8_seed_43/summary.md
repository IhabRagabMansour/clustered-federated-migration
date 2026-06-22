# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.1180 | 88.6420 |
| membership_only | 0 | clusterTest_maxDrop | -0.3620 | 0.0220 |
| membership_only | 0 | clusterTest_afterMean | 89.7980 | 89.1780 |
| membership_only | 0 | clusterTest_afterStd | 0.2048 | 0.3474 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.5590 | 44.3210 |
| membership_only | 0 | globalTest_maxDrop | -0.1810 | 0.0110 |
| membership_only | 0 | globalTest_afterMean | 44.8990 | 44.6170 |
| membership_only | 0 | globalTest_afterStd | 0.1024 | 0.1666 |
| membership_only | 1 | clusterTest_before | 94.7060 | 94.5660 |
| membership_only | 1 | clusterTest_maxDrop | 28.6860 | 31.5860 |
| membership_only | 1 | clusterTest_afterMean | 82.0140 | 81.4020 |
| membership_only | 1 | clusterTest_afterStd | 11.4681 | 12.0376 |
| membership_only | 1 | clusterTest_recovery | 10 | 12 |
| membership_only | 1 | globalTest_before | 47.3530 | 47.2830 |
| membership_only | 1 | globalTest_maxDrop | 1.3430 | 0.8130 |
| membership_only | 1 | globalTest_afterMean | 62.8460 | 65.7870 |
| membership_only | 1 | globalTest_afterStd | 12.8875 | 11.6051 |
| data_changes | 0 | clusterTest_before | 89.1180 | 88.6420 |
| data_changes | 0 | clusterTest_maxDrop | -0.3620 | 0.4020 |
| data_changes | 0 | clusterTest_afterMean | 89.7980 | 89.0920 |
| data_changes | 0 | clusterTest_afterStd | 0.2048 | 0.4413 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.5590 | 44.3210 |
| data_changes | 0 | globalTest_maxDrop | -0.1810 | 0.1010 |
| data_changes | 0 | globalTest_afterMean | 44.8990 | 45.0170 |
| data_changes | 0 | globalTest_afterStd | 0.1024 | 0.9703 |
| data_changes | 1 | clusterTest_before | 94.7060 | 94.5660 |
| data_changes | 1 | clusterTest_maxDrop | 4.9860 | 0.3660 |
| data_changes | 1 | clusterTest_afterMean | 94.0940 | 94.7140 |
| data_changes | 1 | clusterTest_afterStd | 1.5323 | 0.2890 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.3530 | 47.2830 |
| data_changes | 1 | globalTest_maxDrop | 2.4930 | 0.1830 |
| data_changes | 1 | globalTest_afterMean | 47.0470 | 47.3580 |
| data_changes | 1 | globalTest_afterStd | 0.7662 | 0.1449 |
