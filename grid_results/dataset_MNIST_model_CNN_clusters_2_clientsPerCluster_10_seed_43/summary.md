# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.6087 | 98.5737 |
| membership_only | 0 | clusterTest_maxDrop | -0.1459 | -0.1226 |
| membership_only | 0 | clusterTest_afterMean | 98.8363 | 98.8130 |
| membership_only | 0 | clusterTest_afterStd | 0.0701 | 0.1026 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.6750 | 50.6570 |
| membership_only | 0 | globalTest_maxDrop | -0.0750 | -0.0630 |
| membership_only | 0 | globalTest_afterMean | 50.7920 | 50.8350 |
| membership_only | 0 | globalTest_afterStd | 0.0360 | 0.1479 |
| membership_only | 1 | clusterTest_before | 97.6815 | 97.3462 |
| membership_only | 1 | clusterTest_maxDrop | 43.3306 | 54.8241 |
| membership_only | 1 | clusterTest_afterMean | 91.7280 | 90.0082 |
| membership_only | 1 | clusterTest_afterStd | 12.5880 | 16.0615 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.4830 | 47.3200 |
| membership_only | 1 | globalTest_maxDrop | 0.3030 | 0.1900 |
| membership_only | 1 | globalTest_afterMean | 75.4480 | 77.2230 |
| membership_only | 1 | globalTest_afterStd | 17.0647 | 15.5736 |
| data_changes | 0 | clusterTest_before | 98.6087 | 98.5737 |
| data_changes | 0 | clusterTest_maxDrop | -0.1459 | -0.0253 |
| data_changes | 0 | clusterTest_afterMean | 98.8441 | 98.7974 |
| data_changes | 0 | clusterTest_afterStd | 0.0604 | 0.0904 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.6750 | 50.6570 |
| data_changes | 0 | globalTest_maxDrop | -0.0750 | -0.0830 |
| data_changes | 0 | globalTest_afterMean | 50.7960 | 51.0070 |
| data_changes | 0 | globalTest_afterStd | 0.0310 | 0.4494 |
| data_changes | 1 | clusterTest_before | 97.6815 | 97.3462 |
| data_changes | 1 | clusterTest_maxDrop | 1.4462 | 0.2880 |
| data_changes | 1 | clusterTest_afterMean | 97.5643 | 97.5375 |
| data_changes | 1 | clusterTest_afterStd | 0.4991 | 0.2474 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.4830 | 47.3200 |
| data_changes | 1 | globalTest_maxDrop | 0.7030 | 0.1400 |
| data_changes | 1 | globalTest_afterMean | 47.4260 | 47.4130 |
| data_changes | 1 | globalTest_afterStd | 0.2426 | 0.1203 |
