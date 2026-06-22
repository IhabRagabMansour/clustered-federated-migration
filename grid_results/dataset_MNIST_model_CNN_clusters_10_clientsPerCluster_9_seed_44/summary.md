# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 9
- **total_clients**: 90
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 100.0000 | 100.0000 |
| membership_only | 0 | clusterTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 0 | clusterTest_afterMean | 100.0000 | 100.0000 |
| membership_only | 0 | clusterTest_afterStd | 0.0000 | 0.0000 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 9.8000 | 9.8000 |
| membership_only | 0 | globalTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 0 | globalTest_afterMean | 9.8000 | 9.8000 |
| membership_only | 0 | globalTest_afterStd | 0.0000 | 0.0000 |
| membership_only | 9 | clusterTest_before | 100.0000 | 100.0000 |
| membership_only | 9 | clusterTest_maxDrop | 1.1893 | 100.0000 |
| membership_only | 9 | clusterTest_afterMean | 99.5639 | 80.5649 |
| membership_only | 9 | clusterTest_afterStd | 0.5377 | 38.6520 |
| membership_only | 9 | clusterTest_recovery | 4 | 2 |
| membership_only | 9 | globalTest_before | 10.0900 | 10.0900 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.2900 |
| membership_only | 9 | globalTest_afterMean | 13.6740 | 10.9390 |
| membership_only | 9 | globalTest_afterStd | 4.3911 | 2.5215 |
| data_changes | 0 | clusterTest_before | 100.0000 | 100.0000 |
| data_changes | 0 | clusterTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 0 | clusterTest_afterMean | 100.0000 | 100.0000 |
| data_changes | 0 | clusterTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 9.8000 | 9.8000 |
| data_changes | 0 | globalTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 0 | globalTest_afterMean | 9.8000 | 9.8000 |
| data_changes | 0 | globalTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_before | 100.0000 | 100.0000 |
| data_changes | 9 | clusterTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_afterMean | 100.0000 | 100.0000 |
| data_changes | 9 | clusterTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_recovery | 0 | 0 |
| data_changes | 9 | globalTest_before | 10.0900 | 10.0900 |
| data_changes | 9 | globalTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 9 | globalTest_afterMean | 10.0900 | 10.0900 |
| data_changes | 9 | globalTest_afterStd | 0.0000 | 0.0000 |
