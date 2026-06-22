# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.7021 | 98.6204 |
| membership_only | 0 | clusterTest_maxDrop | -0.1109 | -0.0953 |
| membership_only | 0 | clusterTest_afterMean | 98.9298 | 98.8928 |
| membership_only | 0 | clusterTest_afterStd | 0.0707 | 0.0800 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.7230 | 50.6810 |
| membership_only | 0 | globalTest_maxDrop | -0.0570 | -0.0490 |
| membership_only | 0 | globalTest_afterMean | 50.8400 | 50.8970 |
| membership_only | 0 | globalTest_afterStd | 0.0363 | 0.2247 |
| membership_only | 1 | clusterTest_before | 97.7906 | 97.5849 |
| membership_only | 1 | clusterTest_maxDrop | 40.0864 | 64.8961 |
| membership_only | 1 | clusterTest_afterMean | 92.2341 | 89.1360 |
| membership_only | 1 | clusterTest_afterStd | 11.6513 | 18.9513 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.5360 | 47.4360 |
| membership_only | 1 | globalTest_maxDrop | 0.1760 | 0.3360 |
| membership_only | 1 | globalTest_afterMean | 75.1440 | 75.0550 |
| membership_only | 1 | globalTest_afterStd | 17.2037 | 16.5482 |
| data_changes | 0 | clusterTest_before | 98.7021 | 98.6204 |
| data_changes | 0 | clusterTest_maxDrop | -0.1109 | 0.0019 |
| data_changes | 0 | clusterTest_afterMean | 98.9375 | 98.8363 |
| data_changes | 0 | clusterTest_afterStd | 0.0760 | 0.1062 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.7230 | 50.6810 |
| data_changes | 0 | globalTest_maxDrop | -0.0570 | 0.0010 |
| data_changes | 0 | globalTest_afterMean | 50.8440 | 51.0260 |
| data_changes | 0 | globalTest_afterStd | 0.0390 | 0.4871 |
| data_changes | 1 | clusterTest_before | 97.7906 | 97.5849 |
| data_changes | 1 | clusterTest_maxDrop | 0.8764 | 0.6501 |
| data_changes | 1 | clusterTest_afterMean | 97.7103 | 97.6486 |
| data_changes | 1 | clusterTest_afterStd | 0.3781 | 0.3264 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 47.5360 | 47.4360 |
| data_changes | 1 | globalTest_maxDrop | 0.4260 | 0.3160 |
| data_changes | 1 | globalTest_afterMean | 47.4970 | 47.4670 |
| data_changes | 1 | globalTest_afterStd | 0.1838 | 0.1587 |
