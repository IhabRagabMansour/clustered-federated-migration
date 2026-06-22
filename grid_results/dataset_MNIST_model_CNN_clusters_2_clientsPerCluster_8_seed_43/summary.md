# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.9375 | 98.9006 |
| membership_only | 0 | clusterTest_maxDrop | -0.1284 | -0.1459 |
| membership_only | 0 | clusterTest_afterMean | 99.1516 | 99.1555 |
| membership_only | 0 | clusterTest_afterStd | 0.0604 | 0.0765 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.8440 | 50.8250 |
| membership_only | 0 | globalTest_maxDrop | -0.0660 | -0.0850 |
| membership_only | 0 | globalTest_afterMean | 50.9540 | 51.1420 |
| membership_only | 0 | globalTest_afterStd | 0.0310 | 0.5021 |
| membership_only | 1 | clusterTest_before | 98.3234 | 98.1197 |
| membership_only | 1 | clusterTest_maxDrop | 63.2072 | 56.4822 |
| membership_only | 1 | clusterTest_afterMean | 88.3892 | 87.1508 |
| membership_only | 1 | clusterTest_afterStd | 18.5965 | 18.0236 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.7950 | 47.6960 |
| membership_only | 1 | globalTest_maxDrop | 0.2850 | 0.3060 |
| membership_only | 1 | globalTest_afterMean | 76.3890 | 78.0260 |
| membership_only | 1 | globalTest_afterStd | 17.5508 | 14.6983 |
| data_changes | 0 | clusterTest_before | 98.9375 | 98.9006 |
| data_changes | 0 | clusterTest_maxDrop | -0.1284 | 0.0292 |
| data_changes | 0 | clusterTest_afterMean | 99.1516 | 99.1321 |
| data_changes | 0 | clusterTest_afterStd | 0.0604 | 0.1135 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.8440 | 50.8250 |
| data_changes | 0 | globalTest_maxDrop | -0.0660 | -0.0750 |
| data_changes | 0 | globalTest_afterMean | 50.9540 | 51.7870 |
| data_changes | 0 | globalTest_afterStd | 0.0310 | 1.6066 |
| data_changes | 1 | clusterTest_before | 98.3234 | 98.1197 |
| data_changes | 1 | clusterTest_maxDrop | 2.0675 | 0.6295 |
| data_changes | 1 | clusterTest_afterMean | 97.8873 | 98.0642 |
| data_changes | 1 | clusterTest_afterStd | 0.5773 | 0.2253 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.7950 | 47.6960 |
| data_changes | 1 | globalTest_maxDrop | 1.0050 | 0.3060 |
| data_changes | 1 | globalTest_afterMean | 47.5830 | 47.6690 |
| data_changes | 1 | globalTest_afterStd | 0.2806 | 0.1095 |
