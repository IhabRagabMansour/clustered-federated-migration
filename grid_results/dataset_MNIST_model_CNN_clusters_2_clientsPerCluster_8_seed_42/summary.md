# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.0056 | 98.9298 |
| membership_only | 0 | clusterTest_maxDrop | -0.1187 | -0.1362 |
| membership_only | 0 | clusterTest_afterMean | 99.1886 | 99.1633 |
| membership_only | 0 | clusterTest_afterStd | 0.0326 | 0.0609 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.8790 | 50.8400 |
| membership_only | 0 | globalTest_maxDrop | -0.0610 | -0.0700 |
| membership_only | 0 | globalTest_afterMean | 50.9730 | 51.1310 |
| membership_only | 0 | globalTest_afterStd | 0.0168 | 0.3930 |
| membership_only | 1 | clusterTest_before | 98.3748 | 98.2617 |
| membership_only | 1 | clusterTest_maxDrop | 64.5340 | 61.4791 |
| membership_only | 1 | clusterTest_afterMean | 88.0025 | 87.3030 |
| membership_only | 1 | clusterTest_afterStd | 18.6978 | 18.0242 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.8200 | 47.7650 |
| membership_only | 1 | globalTest_maxDrop | 0.3400 | 0.5050 |
| membership_only | 1 | globalTest_afterMean | 74.8230 | 77.0400 |
| membership_only | 1 | globalTest_afterStd | 17.6227 | 15.0743 |
| data_changes | 0 | clusterTest_before | 99.0056 | 98.9298 |
| data_changes | 0 | clusterTest_maxDrop | -0.1187 | -0.0389 |
| data_changes | 0 | clusterTest_afterMean | 99.1886 | 99.1438 |
| data_changes | 0 | clusterTest_afterStd | 0.0326 | 0.0909 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.8790 | 50.8400 |
| data_changes | 0 | globalTest_maxDrop | -0.0610 | -0.0400 |
| data_changes | 0 | globalTest_afterMean | 50.9730 | 51.5200 |
| data_changes | 0 | globalTest_afterStd | 0.0168 | 1.0326 |
| data_changes | 1 | clusterTest_before | 98.3748 | 98.2617 |
| data_changes | 1 | clusterTest_maxDrop | 2.5921 | 0.7714 |
| data_changes | 1 | clusterTest_afterMean | 97.9469 | 98.2432 |
| data_changes | 1 | clusterTest_afterStd | 0.8166 | 0.3274 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.8200 | 47.7650 |
| data_changes | 1 | globalTest_maxDrop | 1.2600 | 0.3750 |
| data_changes | 1 | globalTest_afterMean | 47.6120 | 47.7560 |
| data_changes | 1 | globalTest_afterStd | 0.3970 | 0.1591 |
