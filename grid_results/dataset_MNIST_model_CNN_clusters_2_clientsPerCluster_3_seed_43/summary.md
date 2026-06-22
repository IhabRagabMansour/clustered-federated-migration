# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.7587 | 99.7373 |
| membership_only | 0 | clusterTest_maxDrop | 0.1868 | 0.0681 |
| membership_only | 0 | clusterTest_afterMean | 99.7334 | 99.7373 |
| membership_only | 0 | clusterTest_afterStd | 0.0680 | 0.0401 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.2660 | 51.4720 |
| membership_only | 0 | globalTest_maxDrop | 0.0960 | 0.1020 |
| membership_only | 0 | globalTest_afterMean | 51.2530 | 52.3020 |
| membership_only | 0 | globalTest_afterStd | 0.0349 | 0.7678 |
| membership_only | 1 | clusterTest_before | 99.1545 | 99.0557 |
| membership_only | 1 | clusterTest_maxDrop | 72.3287 | 82.0839 |
| membership_only | 1 | clusterTest_afterMean | 81.0574 | 82.0592 |
| membership_only | 1 | clusterTest_afterStd | 27.7075 | 26.0115 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 48.1990 | 48.1520 |
| membership_only | 1 | globalTest_maxDrop | 0.1790 | -1.4380 |
| membership_only | 1 | globalTest_afterMean | 76.4030 | 78.2640 |
| membership_only | 1 | globalTest_afterStd | 16.8674 | 16.2823 |
| data_changes | 0 | clusterTest_before | 99.7587 | 99.7373 |
| data_changes | 0 | clusterTest_maxDrop | 0.0506 | 0.1070 |
| data_changes | 0 | clusterTest_afterMean | 99.7607 | 99.7354 |
| data_changes | 0 | clusterTest_afterStd | 0.0326 | 0.0478 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.2660 | 51.4720 |
| data_changes | 0 | globalTest_maxDrop | 0.0260 | -0.6180 |
| data_changes | 0 | globalTest_afterMean | 51.2670 | 55.4900 |
| data_changes | 0 | globalTest_afterStd | 0.0168 | 4.2577 |
| data_changes | 1 | clusterTest_before | 99.1545 | 99.0557 |
| data_changes | 1 | clusterTest_maxDrop | 2.0551 | 0.5164 |
| data_changes | 1 | clusterTest_afterMean | 98.6464 | 98.9529 |
| data_changes | 1 | clusterTest_afterStd | 0.5557 | 0.1521 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 48.1990 | 48.1520 |
| data_changes | 1 | globalTest_maxDrop | 0.9990 | 0.2520 |
| data_changes | 1 | globalTest_afterMean | 47.9520 | 48.1010 |
| data_changes | 1 | globalTest_afterStd | 0.2701 | 0.0740 |
