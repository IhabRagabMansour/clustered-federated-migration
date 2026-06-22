# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 9
- **total_clients**: 90
- **seed**: 43
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
| membership_only | 9 | clusterTest_maxDrop | 87.6115 | 100.0000 |
| membership_only | 9 | clusterTest_afterMean | 90.9812 | 90.0000 |
| membership_only | 9 | clusterTest_afterStd | 26.2005 | 30.0000 |
| membership_only | 9 | clusterTest_recovery | 2 | 2 |
| membership_only | 9 | globalTest_before | 10.0900 | 10.0900 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.2900 |
| membership_only | 9 | globalTest_afterMean | 12.8750 | 10.0610 |
| membership_only | 9 | globalTest_afterStd | 3.9226 | 0.0870 |
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
