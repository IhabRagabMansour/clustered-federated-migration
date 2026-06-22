# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 88.4880 | 87.6980 |
| membership_only | 0 | clusterTest_maxDrop | -0.3520 | -0.5020 |
| membership_only | 0 | clusterTest_afterMean | 89.1680 | 88.5900 |
| membership_only | 0 | clusterTest_afterStd | 0.2111 | 0.1946 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.2440 | 43.8490 |
| membership_only | 0 | globalTest_maxDrop | -0.1760 | -0.2510 |
| membership_only | 0 | globalTest_afterMean | 44.5840 | 44.3650 |
| membership_only | 0 | globalTest_afterStd | 0.1056 | 0.2347 |
| membership_only | 1 | clusterTest_before | 94.3500 | 94.1120 |
| membership_only | 1 | clusterTest_maxDrop | 32.8100 | 36.0920 |
| membership_only | 1 | clusterTest_afterMean | 80.9420 | 80.3280 |
| membership_only | 1 | clusterTest_afterStd | 12.5117 | 13.1567 |
| membership_only | 1 | clusterTest_recovery | 6 | 8 |
| membership_only | 1 | globalTest_before | 47.1750 | 47.0560 |
| membership_only | 1 | globalTest_maxDrop | 1.6750 | 1.2560 |
| membership_only | 1 | globalTest_afterMean | 60.9640 | 64.7880 |
| membership_only | 1 | globalTest_afterStd | 12.9506 | 11.5021 |
| data_changes | 0 | clusterTest_before | 88.4880 | 87.6980 |
| data_changes | 0 | clusterTest_maxDrop | -0.3520 | -0.4220 |
| data_changes | 0 | clusterTest_afterMean | 89.1680 | 88.5360 |
| data_changes | 0 | clusterTest_afterStd | 0.2111 | 0.2310 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.2440 | 43.8490 |
| data_changes | 0 | globalTest_maxDrop | -0.1760 | -0.2810 |
| data_changes | 0 | globalTest_afterMean | 44.5840 | 44.7740 |
| data_changes | 0 | globalTest_afterStd | 0.1056 | 0.9550 |
| data_changes | 1 | clusterTest_before | 94.3500 | 94.1120 |
| data_changes | 1 | clusterTest_maxDrop | 1.2900 | 0.2520 |
| data_changes | 1 | clusterTest_afterMean | 94.1840 | 94.4040 |
| data_changes | 1 | clusterTest_afterStd | 0.5263 | 0.2615 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.1750 | 47.0560 |
| data_changes | 1 | globalTest_maxDrop | 0.6450 | 0.1260 |
| data_changes | 1 | globalTest_afterMean | 47.0920 | 47.2020 |
| data_changes | 1 | globalTest_afterStd | 0.2632 | 0.1308 |
