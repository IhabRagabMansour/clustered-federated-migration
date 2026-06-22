# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 71.7380 | 70.4900 |
| membership_only | 0 | clusterTest_maxDrop | 0.4580 | 2.5700 |
| membership_only | 0 | clusterTest_afterMean | 71.6040 | 69.9280 |
| membership_only | 0 | clusterTest_afterStd | 0.1826 | 0.8493 |
| membership_only | 0 | clusterTest_recovery | 0 | 14 |
| membership_only | 0 | globalTest_before | 35.8690 | 35.2450 |
| membership_only | 0 | globalTest_maxDrop | 0.2290 | 1.2850 |
| membership_only | 0 | globalTest_afterMean | 35.8020 | 34.9640 |
| membership_only | 0 | globalTest_afterStd | 0.0913 | 0.4246 |
| membership_only | 1 | clusterTest_before | 80.0900 | 78.6980 |
| membership_only | 1 | clusterTest_maxDrop | 80.0900 | 78.6980 |
| membership_only | 1 | clusterTest_afterMean | 38.1120 | 49.3000 |
| membership_only | 1 | clusterTest_afterStd | 37.6395 | 26.2959 |
| membership_only | 1 | clusterTest_recovery | 8 | 9 |
| membership_only | 1 | globalTest_before | 40.0450 | 39.3490 |
| membership_only | 1 | globalTest_maxDrop | 14.6950 | 7.1690 |
| membership_only | 1 | globalTest_afterMean | 32.7470 | 37.0450 |
| membership_only | 1 | globalTest_afterStd | 5.4774 | 2.8663 |
| data_changes | 0 | clusterTest_before | 71.7380 | 70.4900 |
| data_changes | 0 | clusterTest_maxDrop | 0.4580 | 9.9700 |
| data_changes | 0 | clusterTest_afterMean | 71.6040 | 67.4960 |
| data_changes | 0 | clusterTest_afterStd | 0.1826 | 3.2674 |
| data_changes | 0 | clusterTest_recovery | 0 | 8 |
| data_changes | 0 | globalTest_before | 35.8690 | 35.2450 |
| data_changes | 0 | globalTest_maxDrop | 0.2290 | 4.9850 |
| data_changes | 0 | globalTest_afterMean | 35.8020 | 33.7510 |
| data_changes | 0 | globalTest_afterStd | 0.0913 | 1.6291 |
| data_changes | 1 | clusterTest_before | 80.0900 | 78.6980 |
| data_changes | 1 | clusterTest_maxDrop | 22.8700 | 10.8380 |
| data_changes | 1 | clusterTest_afterMean | 77.0120 | 78.4680 |
| data_changes | 1 | clusterTest_afterStd | 6.8333 | 3.6980 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 40.0450 | 39.3490 |
| data_changes | 1 | globalTest_maxDrop | 11.4350 | 5.4190 |
| data_changes | 1 | globalTest_afterMean | 38.5060 | 39.2340 |
| data_changes | 1 | globalTest_afterStd | 3.4166 | 1.8490 |
