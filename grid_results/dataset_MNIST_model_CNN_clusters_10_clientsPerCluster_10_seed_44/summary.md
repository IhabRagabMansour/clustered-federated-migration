# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 10
- **total_clients**: 100
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
| membership_only | 9 | clusterTest_maxDrop | 0.4955 | 100.0000 |
| membership_only | 9 | clusterTest_afterMean | 99.9207 | 85.0842 |
| membership_only | 9 | clusterTest_afterStd | 0.1647 | 31.9244 |
| membership_only | 9 | clusterTest_recovery | 0 | 2 |
| membership_only | 9 | globalTest_before | 10.0900 | 10.0900 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.2900 |
| membership_only | 9 | globalTest_afterMean | 12.0470 | 10.5450 |
| membership_only | 9 | globalTest_afterStd | 3.0327 | 1.4642 |
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
