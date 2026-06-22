# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.7548 | 99.7101 |
| membership_only | 0 | clusterTest_maxDrop | 0.0467 | 0.0798 |
| membership_only | 0 | clusterTest_afterMean | 99.7723 | 99.7587 |
| membership_only | 0 | clusterTest_afterStd | 0.0380 | 0.0516 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.2640 | 51.3540 |
| membership_only | 0 | globalTest_maxDrop | 0.0240 | -0.0260 |
| membership_only | 0 | globalTest_afterMean | 51.2730 | 52.1120 |
| membership_only | 0 | globalTest_afterStd | 0.0195 | 0.7157 |
| membership_only | 1 | clusterTest_before | 99.1113 | 99.0722 |
| membership_only | 1 | clusterTest_maxDrop | 73.9724 | 76.4843 |
| membership_only | 1 | clusterTest_afterMean | 79.5865 | 81.5182 |
| membership_only | 1 | clusterTest_afterStd | 27.7945 | 26.3204 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 48.1780 | 48.1590 |
| membership_only | 1 | globalTest_maxDrop | 0.0480 | -1.8210 |
| membership_only | 1 | globalTest_afterMean | 74.8880 | 78.8190 |
| membership_only | 1 | globalTest_afterStd | 15.9076 | 14.9975 |
| data_changes | 0 | clusterTest_before | 99.7548 | 99.7101 |
| data_changes | 0 | clusterTest_maxDrop | 0.0078 | 0.0409 |
| data_changes | 0 | clusterTest_afterMean | 99.7918 | 99.7470 |
| data_changes | 0 | clusterTest_afterStd | 0.0289 | 0.0536 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.2640 | 51.3540 |
| data_changes | 0 | globalTest_maxDrop | 0.0040 | -0.3260 |
| data_changes | 0 | globalTest_afterMean | 51.2830 | 54.6420 |
| data_changes | 0 | globalTest_afterStd | 0.0149 | 3.9227 |
| data_changes | 1 | clusterTest_before | 99.1113 | 99.0722 |
| data_changes | 1 | clusterTest_maxDrop | 2.5468 | 0.5534 |
| data_changes | 1 | clusterTest_afterMean | 98.5847 | 98.9611 |
| data_changes | 1 | clusterTest_afterStd | 0.6949 | 0.1717 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 48.1780 | 48.1590 |
| data_changes | 1 | globalTest_maxDrop | 1.2380 | 0.2690 |
| data_changes | 1 | globalTest_afterMean | 47.9220 | 48.1050 |
| data_changes | 1 | globalTest_afterStd | 0.3378 | 0.0835 |
