# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.0140 | 89.3500 |
| membership_only | 0 | clusterTest_maxDrop | -0.0260 | 0.0300 |
| membership_only | 0 | clusterTest_afterMean | 90.4140 | 89.8540 |
| membership_only | 0 | clusterTest_afterStd | 0.2163 | 0.2317 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.0070 | 44.6750 |
| membership_only | 0 | globalTest_maxDrop | -0.0130 | 0.0150 |
| membership_only | 0 | globalTest_afterMean | 45.2070 | 44.9300 |
| membership_only | 0 | globalTest_afterStd | 0.1082 | 0.1147 |
| membership_only | 1 | clusterTest_before | 95.6280 | 95.5180 |
| membership_only | 1 | clusterTest_maxDrop | 38.6280 | 31.0780 |
| membership_only | 1 | clusterTest_afterMean | 81.6720 | 82.4200 |
| membership_only | 1 | clusterTest_afterStd | 13.5028 | 12.2454 |
| membership_only | 1 | clusterTest_recovery | 4 | 2 |
| membership_only | 1 | globalTest_before | 47.8140 | 47.7590 |
| membership_only | 1 | globalTest_maxDrop | 0.6540 | -3.0510 |
| membership_only | 1 | globalTest_afterMean | 65.0800 | 68.0900 |
| membership_only | 1 | globalTest_afterStd | 12.1152 | 10.9433 |
| data_changes | 0 | clusterTest_before | 90.0140 | 89.3500 |
| data_changes | 0 | clusterTest_maxDrop | -0.0260 | -0.1100 |
| data_changes | 0 | clusterTest_afterMean | 90.4140 | 89.8040 |
| data_changes | 0 | clusterTest_afterStd | 0.2163 | 0.2146 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.0070 | 44.6750 |
| data_changes | 0 | globalTest_maxDrop | -0.0130 | -0.0550 |
| data_changes | 0 | globalTest_afterMean | 45.2070 | 46.3690 |
| data_changes | 0 | globalTest_afterStd | 0.1082 | 2.9293 |
| data_changes | 1 | clusterTest_before | 95.6280 | 95.5180 |
| data_changes | 1 | clusterTest_maxDrop | 1.1480 | 0.3580 |
| data_changes | 1 | clusterTest_afterMean | 95.2500 | 95.5440 |
| data_changes | 1 | clusterTest_afterStd | 0.4047 | 0.2221 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.8140 | 47.7590 |
| data_changes | 1 | globalTest_maxDrop | 0.5740 | 0.1790 |
| data_changes | 1 | globalTest_afterMean | 47.6250 | 47.7910 |
| data_changes | 1 | globalTest_afterStd | 0.2023 | 0.1258 |
