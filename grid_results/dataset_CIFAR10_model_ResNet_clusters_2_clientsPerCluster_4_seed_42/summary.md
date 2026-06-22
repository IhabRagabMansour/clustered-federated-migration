# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 71.7220 | 71.0040 |
| membership_only | 0 | clusterTest_maxDrop | 0.3820 | 20.1040 |
| membership_only | 0 | clusterTest_afterMean | 71.5860 | 65.8020 |
| membership_only | 0 | clusterTest_afterStd | 0.1357 | 6.1634 |
| membership_only | 0 | clusterTest_recovery | 0 | 6 |
| membership_only | 0 | globalTest_before | 35.8610 | 35.5020 |
| membership_only | 0 | globalTest_maxDrop | 0.1910 | 10.0520 |
| membership_only | 0 | globalTest_afterMean | 35.7930 | 32.9010 |
| membership_only | 0 | globalTest_afterStd | 0.0678 | 3.0817 |
| membership_only | 1 | clusterTest_before | 80.6420 | 79.4840 |
| membership_only | 1 | clusterTest_maxDrop | 80.6420 | 79.4840 |
| membership_only | 1 | clusterTest_afterMean | 36.6700 | 40.0900 |
| membership_only | 1 | clusterTest_afterStd | 37.0666 | 34.4269 |
| membership_only | 1 | clusterTest_recovery | 8 | 9 |
| membership_only | 1 | globalTest_before | 40.3210 | 39.7420 |
| membership_only | 1 | globalTest_maxDrop | 14.1110 | 9.9120 |
| membership_only | 1 | globalTest_afterMean | 33.0410 | 34.3500 |
| membership_only | 1 | globalTest_afterStd | 4.9426 | 3.6788 |
| data_changes | 0 | clusterTest_before | 71.7220 | 71.0040 |
| data_changes | 0 | clusterTest_maxDrop | 0.3820 | 13.4440 |
| data_changes | 0 | clusterTest_afterMean | 71.5860 | 65.4220 |
| data_changes | 0 | clusterTest_afterStd | 0.1357 | 4.6053 |
| data_changes | 0 | clusterTest_recovery | 0 | 8 |
| data_changes | 0 | globalTest_before | 35.8610 | 35.5020 |
| data_changes | 0 | globalTest_maxDrop | 0.1910 | 6.7220 |
| data_changes | 0 | globalTest_afterMean | 35.7930 | 32.7200 |
| data_changes | 0 | globalTest_afterStd | 0.0678 | 2.2881 |
| data_changes | 1 | clusterTest_before | 80.6420 | 79.4840 |
| data_changes | 1 | clusterTest_maxDrop | 24.1020 | 13.7840 |
| data_changes | 1 | clusterTest_afterMean | 77.6040 | 78.6260 |
| data_changes | 1 | clusterTest_afterStd | 7.3341 | 4.5308 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 40.3210 | 39.7420 |
| data_changes | 1 | globalTest_maxDrop | 12.0510 | 6.8920 |
| data_changes | 1 | globalTest_afterMean | 38.8020 | 39.3130 |
| data_changes | 1 | globalTest_afterStd | 3.6671 | 2.2654 |
