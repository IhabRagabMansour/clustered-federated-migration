# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 5
- **total_clients**: 50
- **seed**: 42
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
| membership_only | 9 | clusterTest_maxDrop | 100.0000 | 100.0000 |
| membership_only | 9 | clusterTest_afterMean | 78.3200 | 88.2300 |
| membership_only | 9 | clusterTest_afterStd | 39.3746 | 29.8344 |
| membership_only | 9 | clusterTest_recovery | 2 | 2 |
| membership_only | 9 | globalTest_before | 10.0000 | 10.0000 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 9 | globalTest_afterMean | 12.4820 | 13.7760 |
| membership_only | 9 | globalTest_afterStd | 3.8587 | 4.0009 |
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
