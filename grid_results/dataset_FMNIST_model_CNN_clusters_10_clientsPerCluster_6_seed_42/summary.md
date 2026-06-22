# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 10
- **clients_per_cluster**: 6
- **total_clients**: 60
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
| membership_only | 9 | clusterTest_afterMean | 87.8200 | 87.0400 |
| membership_only | 9 | clusterTest_afterStd | 29.5816 | 29.9910 |
| membership_only | 9 | clusterTest_recovery | 2 | 2 |
| membership_only | 9 | globalTest_before | 10.0000 | 10.0000 |
| membership_only | 9 | globalTest_maxDrop | 0.0000 | 0.0000 |
| membership_only | 9 | globalTest_afterMean | 13.9280 | 13.1570 |
| membership_only | 9 | globalTest_afterStd | 3.9803 | 3.9453 |
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
