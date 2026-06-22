# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.7400 | 69.3480 |
| membership_only | 0 | clusterTest_maxDrop | 0.4000 | 4.0680 |
| membership_only | 0 | clusterTest_afterMean | 70.7680 | 68.5540 |
| membership_only | 0 | clusterTest_afterStd | 0.2189 | 2.1911 |
| membership_only | 0 | clusterTest_recovery | 0 | 6 |
| membership_only | 0 | globalTest_before | 35.3700 | 34.6740 |
| membership_only | 0 | globalTest_maxDrop | 0.2000 | 2.0340 |
| membership_only | 0 | globalTest_afterMean | 35.3840 | 34.2770 |
| membership_only | 0 | globalTest_afterStd | 0.1095 | 1.0956 |
| membership_only | 1 | clusterTest_before | 79.6720 | 78.9440 |
| membership_only | 1 | clusterTest_maxDrop | 79.6520 | 78.9440 |
| membership_only | 1 | clusterTest_afterMean | 38.2040 | 40.1200 |
| membership_only | 1 | clusterTest_afterStd | 37.8424 | 35.4629 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 39.8360 | 39.4720 |
| membership_only | 1 | globalTest_maxDrop | 14.4560 | 10.3020 |
| membership_only | 1 | globalTest_afterMean | 32.2400 | 35.2800 |
| membership_only | 1 | globalTest_afterStd | 5.9073 | 3.7392 |
| data_changes | 0 | clusterTest_before | 70.7400 | 69.3480 |
| data_changes | 0 | clusterTest_maxDrop | 0.4000 | 5.7680 |
| data_changes | 0 | clusterTest_afterMean | 70.7680 | 67.2280 |
| data_changes | 0 | clusterTest_afterStd | 0.2189 | 2.0288 |
| data_changes | 0 | clusterTest_recovery | 0 | 9 |
| data_changes | 0 | globalTest_before | 35.3700 | 34.6740 |
| data_changes | 0 | globalTest_maxDrop | 0.2000 | 2.8840 |
| data_changes | 0 | globalTest_afterMean | 35.3840 | 33.6200 |
| data_changes | 0 | globalTest_afterStd | 0.1095 | 1.0046 |
| data_changes | 1 | clusterTest_before | 79.6720 | 78.9440 |
| data_changes | 1 | clusterTest_maxDrop | 18.3920 | 9.0440 |
| data_changes | 1 | clusterTest_afterMean | 77.2600 | 77.8800 |
| data_changes | 1 | clusterTest_afterStd | 5.6198 | 3.2663 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.8360 | 39.4720 |
| data_changes | 1 | globalTest_maxDrop | 9.1960 | 4.5220 |
| data_changes | 1 | globalTest_afterMean | 38.6300 | 38.9400 |
| data_changes | 1 | globalTest_afterStd | 2.8099 | 1.6332 |
