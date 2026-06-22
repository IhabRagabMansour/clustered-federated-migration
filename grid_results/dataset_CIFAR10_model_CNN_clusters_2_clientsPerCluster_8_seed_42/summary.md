# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.4540 | 79.7680 |
| membership_only | 0 | clusterTest_maxDrop | 0.6740 | 0.9880 |
| membership_only | 0 | clusterTest_afterMean | 80.9800 | 80.2800 |
| membership_only | 0 | clusterTest_afterStd | 0.7615 | 0.9082 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 40.2270 | 39.8840 |
| membership_only | 0 | globalTest_maxDrop | 0.3370 | 0.4940 |
| membership_only | 0 | globalTest_afterMean | 40.4900 | 40.1400 |
| membership_only | 0 | globalTest_afterStd | 0.3808 | 0.4541 |
| membership_only | 1 | clusterTest_before | 88.3540 | 87.9800 |
| membership_only | 1 | clusterTest_maxDrop | 76.4140 | 72.6400 |
| membership_only | 1 | clusterTest_afterMean | 58.5040 | 56.6440 |
| membership_only | 1 | clusterTest_afterStd | 29.3639 | 31.0615 |
| membership_only | 1 | clusterTest_recovery | 14 | 6 |
| membership_only | 1 | globalTest_before | 44.1770 | 43.9900 |
| membership_only | 1 | globalTest_maxDrop | 3.6970 | 1.7000 |
| membership_only | 1 | globalTest_afterMean | 45.1530 | 45.8610 |
| membership_only | 1 | globalTest_afterStd | 3.7041 | 4.5490 |
| data_changes | 0 | clusterTest_before | 80.4540 | 79.7680 |
| data_changes | 0 | clusterTest_maxDrop | 0.6740 | 1.0680 |
| data_changes | 0 | clusterTest_afterMean | 80.9800 | 80.1180 |
| data_changes | 0 | clusterTest_afterStd | 0.7615 | 0.9011 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 40.2270 | 39.8840 |
| data_changes | 0 | globalTest_maxDrop | 0.3370 | 0.5340 |
| data_changes | 0 | globalTest_afterMean | 40.4900 | 40.0590 |
| data_changes | 0 | globalTest_afterStd | 0.3808 | 0.4505 |
| data_changes | 1 | clusterTest_before | 88.3540 | 87.9800 |
| data_changes | 1 | clusterTest_maxDrop | 17.2940 | 1.7400 |
| data_changes | 1 | clusterTest_afterMean | 86.2880 | 88.5740 |
| data_changes | 1 | clusterTest_afterStd | 5.4623 | 0.9736 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.1770 | 43.9900 |
| data_changes | 1 | globalTest_maxDrop | 8.6470 | 0.8700 |
| data_changes | 1 | globalTest_afterMean | 43.1440 | 44.2870 |
| data_changes | 1 | globalTest_afterStd | 2.7311 | 0.4868 |
