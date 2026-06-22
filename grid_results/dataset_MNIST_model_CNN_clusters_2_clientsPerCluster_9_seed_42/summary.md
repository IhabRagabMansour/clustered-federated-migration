# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.9220 | 98.8519 |
| membership_only | 0 | clusterTest_maxDrop | -0.0856 | -0.0389 |
| membership_only | 0 | clusterTest_afterMean | 99.1438 | 99.0251 |
| membership_only | 0 | clusterTest_afterStd | 0.0830 | 0.0975 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.8360 | 50.8000 |
| membership_only | 0 | globalTest_maxDrop | -0.0440 | -0.0200 |
| membership_only | 0 | globalTest_afterMean | 50.9500 | 51.0150 |
| membership_only | 0 | globalTest_afterStd | 0.0427 | 0.3578 |
| membership_only | 1 | clusterTest_before | 98.0230 | 97.8297 |
| membership_only | 1 | clusterTest_maxDrop | 53.2586 | 61.9111 |
| membership_only | 1 | clusterTest_afterMean | 89.9280 | 88.0848 |
| membership_only | 1 | clusterTest_afterStd | 15.4390 | 17.9882 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.6490 | 47.5550 |
| membership_only | 1 | globalTest_maxDrop | 0.2990 | 0.4750 |
| membership_only | 1 | globalTest_afterMean | 75.4300 | 76.6010 |
| membership_only | 1 | globalTest_afterStd | 17.4926 | 15.4763 |
| data_changes | 0 | clusterTest_before | 98.9220 | 98.8519 |
| data_changes | 0 | clusterTest_maxDrop | -0.0856 | 0.1362 |
| data_changes | 0 | clusterTest_afterMean | 99.1457 | 99.0387 |
| data_changes | 0 | clusterTest_afterStd | 0.0761 | 0.1315 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.8360 | 50.8000 |
| data_changes | 0 | globalTest_maxDrop | -0.0440 | -0.0500 |
| data_changes | 0 | globalTest_afterMean | 50.9510 | 51.2750 |
| data_changes | 0 | globalTest_afterStd | 0.0391 | 0.7244 |
| data_changes | 1 | clusterTest_before | 98.0230 | 97.8297 |
| data_changes | 1 | clusterTest_maxDrop | 1.8494 | 0.6480 |
| data_changes | 1 | clusterTest_afterMean | 97.7535 | 97.8873 |
| data_changes | 1 | clusterTest_afterStd | 0.5886 | 0.2998 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.6490 | 47.5550 |
| data_changes | 1 | globalTest_maxDrop | 0.8990 | 0.3150 |
| data_changes | 1 | globalTest_afterMean | 47.5180 | 47.5830 |
| data_changes | 1 | globalTest_afterStd | 0.2861 | 0.1457 |
