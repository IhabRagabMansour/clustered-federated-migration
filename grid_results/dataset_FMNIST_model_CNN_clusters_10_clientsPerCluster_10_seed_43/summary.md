# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 10
- **total_clients**: 100
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
| membership_only | 0 | globalTest_before | 10.0000 | 10.0000 |
| membership_only | 0 | globalTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 0 | globalTest_afterMean | 10.0000 | 10.0000 |
| membership_only | 0 | globalTest_afterStd | 0.0000 | 0.0000 |
| membership_only | 9 | clusterTest_before | 100.0000 | 100.0000 |
| membership_only | 9 | clusterTest_maxDrop | 1.3000 | 3.7000 |
| membership_only | 9 | clusterTest_afterMean | 99.7700 | 99.2300 |
| membership_only | 9 | clusterTest_afterStd | 0.4291 | 1.2370 |
| membership_only | 9 | clusterTest_recovery | 8 | 2 |
| membership_only | 9 | globalTest_before | 10.0000 | 10.0000 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 9 | globalTest_afterMean | 13.6190 | 14.6530 |
| membership_only | 9 | globalTest_afterStd | 4.5152 | 4.6964 |
| data_changes | 0 | clusterTest_before | 100.0000 | 100.0000 |
| data_changes | 0 | clusterTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 0 | clusterTest_afterMean | 100.0000 | 100.0000 |
| data_changes | 0 | clusterTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 10.0000 | 10.0000 |
| data_changes | 0 | globalTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 0 | globalTest_afterMean | 10.0000 | 10.0000 |
| data_changes | 0 | globalTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_before | 100.0000 | 100.0000 |
| data_changes | 9 | clusterTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_afterMean | 100.0000 | 100.0000 |
| data_changes | 9 | clusterTest_afterStd | 0.0000 | 0.0000 |
| data_changes | 9 | clusterTest_recovery | 0 | 0 |
| data_changes | 9 | globalTest_before | 10.0000 | 10.0000 |
| data_changes | 9 | globalTest_maxDrop | 0.0000 | 0.0000 |
| data_changes | 9 | globalTest_afterMean | 10.0000 | 10.0000 |
| data_changes | 9 | globalTest_afterStd | 0.0000 | 0.0000 |
