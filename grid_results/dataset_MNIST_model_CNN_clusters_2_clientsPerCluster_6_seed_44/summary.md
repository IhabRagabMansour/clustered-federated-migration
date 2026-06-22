# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.2528 | 99.2664 |
| membership_only | 0 | clusterTest_maxDrop | -0.0662 | -0.0720 |
| membership_only | 0 | clusterTest_afterMean | 99.4162 | 99.4221 |
| membership_only | 0 | clusterTest_afterStd | 0.0645 | 0.0564 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.0060 | 51.0230 |
| membership_only | 0 | globalTest_maxDrop | -0.0340 | -0.1070 |
| membership_only | 0 | globalTest_afterMean | 51.0900 | 51.5090 |
| membership_only | 0 | globalTest_afterStd | 0.0332 | 0.4512 |
| membership_only | 1 | clusterTest_before | 98.6793 | 98.5600 |
| membership_only | 1 | clusterTest_maxDrop | 68.5826 | 77.5149 |
| membership_only | 1 | clusterTest_afterMean | 84.9043 | 84.0095 |
| membership_only | 1 | clusterTest_afterStd | 21.4079 | 23.2136 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.9680 | 47.9100 |
| membership_only | 1 | globalTest_maxDrop | 0.3080 | 0.0800 |
| membership_only | 1 | globalTest_afterMean | 76.0600 | 76.8820 |
| membership_only | 1 | globalTest_afterStd | 17.2293 | 16.9343 |
| data_changes | 0 | clusterTest_before | 99.2528 | 99.2664 |
| data_changes | 0 | clusterTest_maxDrop | -0.0272 | 0.0837 |
| data_changes | 0 | clusterTest_afterMean | 99.4201 | 99.3734 |
| data_changes | 0 | clusterTest_afterStd | 0.0684 | 0.1110 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.0060 | 51.0230 |
| data_changes | 0 | globalTest_maxDrop | -0.0140 | -0.3170 |
| data_changes | 0 | globalTest_afterMean | 51.0920 | 53.0220 |
| data_changes | 0 | globalTest_afterStd | 0.0352 | 2.1014 |
| data_changes | 1 | clusterTest_before | 98.6793 | 98.5600 |
| data_changes | 1 | clusterTest_maxDrop | 2.1354 | 0.4114 |
| data_changes | 1 | clusterTest_afterMean | 98.2349 | 98.5188 |
| data_changes | 1 | clusterTest_afterStd | 0.6137 | 0.1847 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.9680 | 47.9100 |
| data_changes | 1 | globalTest_maxDrop | 1.0380 | 0.2000 |
| data_changes | 1 | globalTest_afterMean | 47.7520 | 47.8900 |
| data_changes | 1 | globalTest_afterStd | 0.2983 | 0.0898 |
