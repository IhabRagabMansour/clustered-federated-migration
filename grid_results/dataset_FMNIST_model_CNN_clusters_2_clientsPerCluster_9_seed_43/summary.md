# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 88.4320 | 87.6720 |
| membership_only | 0 | clusterTest_maxDrop | 1.3320 | 6.9320 |
| membership_only | 0 | clusterTest_afterMean | 88.6840 | 87.0340 |
| membership_only | 0 | clusterTest_afterStd | 0.7688 | 2.3492 |
| membership_only | 0 | clusterTest_recovery | 4 | 4 |
| membership_only | 0 | globalTest_before | 44.2160 | 43.8360 |
| membership_only | 0 | globalTest_maxDrop | 0.6660 | 3.4660 |
| membership_only | 0 | globalTest_afterMean | 44.3420 | 43.5240 |
| membership_only | 0 | globalTest_afterStd | 0.3844 | 1.1729 |
| membership_only | 1 | clusterTest_before | 94.3520 | 93.8640 |
| membership_only | 1 | clusterTest_maxDrop | 26.6120 | 30.8240 |
| membership_only | 1 | clusterTest_afterMean | 82.1080 | 81.2400 |
| membership_only | 1 | clusterTest_afterStd | 11.2492 | 12.2669 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 47.1760 | 46.9320 |
| membership_only | 1 | globalTest_maxDrop | 1.3460 | 0.8420 |
| membership_only | 1 | globalTest_afterMean | 62.2500 | 65.0760 |
| membership_only | 1 | globalTest_afterStd | 12.9231 | 11.6776 |
| data_changes | 0 | clusterTest_before | 88.4320 | 87.6720 |
| data_changes | 0 | clusterTest_maxDrop | 1.3320 | 6.9520 |
| data_changes | 0 | clusterTest_afterMean | 88.6840 | 86.9400 |
| data_changes | 0 | clusterTest_afterStd | 0.7688 | 2.3912 |
| data_changes | 0 | clusterTest_recovery | 4 | 4 |
| data_changes | 0 | globalTest_before | 44.2160 | 43.8360 |
| data_changes | 0 | globalTest_maxDrop | 0.6660 | 3.4760 |
| data_changes | 0 | globalTest_afterMean | 44.3420 | 43.6440 |
| data_changes | 0 | globalTest_afterStd | 0.3844 | 1.2775 |
| data_changes | 1 | clusterTest_before | 94.3520 | 93.8640 |
| data_changes | 1 | clusterTest_maxDrop | 5.9720 | 2.2840 |
| data_changes | 1 | clusterTest_afterMean | 93.2880 | 93.9700 |
| data_changes | 1 | clusterTest_afterStd | 2.2824 | 1.0094 |
| data_changes | 1 | clusterTest_recovery | 2 | 2 |
| data_changes | 1 | globalTest_before | 47.1760 | 46.9320 |
| data_changes | 1 | globalTest_maxDrop | 2.9860 | 1.1420 |
| data_changes | 1 | globalTest_afterMean | 46.6440 | 46.9860 |
| data_changes | 1 | globalTest_afterStd | 1.1412 | 0.5054 |
