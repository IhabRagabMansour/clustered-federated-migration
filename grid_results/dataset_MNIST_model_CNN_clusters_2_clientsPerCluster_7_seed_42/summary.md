# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.2100 | 99.1613 |
| membership_only | 0 | clusterTest_maxDrop | -0.0701 | -0.0992 |
| membership_only | 0 | clusterTest_afterMean | 99.4162 | 99.3695 |
| membership_only | 0 | clusterTest_afterStd | 0.0749 | 0.0664 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.9840 | 50.9590 |
| membership_only | 0 | globalTest_maxDrop | -0.0360 | -0.0510 |
| membership_only | 0 | globalTest_afterMean | 51.0900 | 51.2760 |
| membership_only | 0 | globalTest_afterStd | 0.0385 | 0.4393 |
| membership_only | 1 | clusterTest_before | 98.5888 | 98.5065 |
| membership_only | 1 | clusterTest_maxDrop | 72.8533 | 60.0370 |
| membership_only | 1 | clusterTest_afterMean | 84.7480 | 84.0547 |
| membership_only | 1 | clusterTest_afterStd | 21.6961 | 20.7057 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.9240 | 47.8840 |
| membership_only | 1 | globalTest_maxDrop | 0.3240 | 0.2640 |
| membership_only | 1 | globalTest_afterMean | 73.9860 | 76.7810 |
| membership_only | 1 | globalTest_afterStd | 17.2870 | 14.4436 |
| data_changes | 0 | clusterTest_before | 99.2100 | 99.1613 |
| data_changes | 0 | clusterTest_maxDrop | -0.1479 | -0.0603 |
| data_changes | 0 | clusterTest_afterMean | 99.4201 | 99.3326 |
| data_changes | 0 | clusterTest_afterStd | 0.0483 | 0.0691 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.9840 | 50.9590 |
| data_changes | 0 | globalTest_maxDrop | -0.0760 | -0.0310 |
| data_changes | 0 | globalTest_afterMean | 51.0920 | 51.8300 |
| data_changes | 0 | globalTest_afterStd | 0.0248 | 1.4891 |
| data_changes | 1 | clusterTest_before | 98.5888 | 98.5065 |
| data_changes | 1 | clusterTest_maxDrop | 2.7237 | 0.7694 |
| data_changes | 1 | clusterTest_afterMean | 98.1012 | 98.4427 |
| data_changes | 1 | clusterTest_afterStd | 0.8231 | 0.3142 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.9240 | 47.8840 |
| data_changes | 1 | globalTest_maxDrop | 1.3240 | 0.3740 |
| data_changes | 1 | globalTest_afterMean | 47.6870 | 47.8530 |
| data_changes | 1 | globalTest_afterStd | 0.4001 | 0.1527 |
