# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.7237 | 99.7217 |
| membership_only | 0 | clusterTest_maxDrop | 0.2102 | 0.0720 |
| membership_only | 0 | clusterTest_afterMean | 99.6673 | 99.7003 |
| membership_only | 0 | clusterTest_afterStd | 0.0618 | 0.0350 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.2480 | 51.4660 |
| membership_only | 0 | globalTest_maxDrop | 0.1080 | 0.0660 |
| membership_only | 0 | globalTest_afterMean | 51.2190 | 51.9540 |
| membership_only | 0 | globalTest_afterStd | 0.0318 | 0.4220 |
| membership_only | 1 | clusterTest_before | 99.0784 | 99.0660 |
| membership_only | 1 | clusterTest_maxDrop | 66.4925 | 60.7200 |
| membership_only | 1 | clusterTest_afterMean | 81.9687 | 83.3532 |
| membership_only | 1 | clusterTest_afterStd | 25.4713 | 23.2714 |
| membership_only | 1 | clusterTest_recovery | 4 | 6 |
| membership_only | 1 | globalTest_before | 48.1620 | 48.1560 |
| membership_only | 1 | globalTest_maxDrop | 0.1220 | -4.5540 |
| membership_only | 1 | globalTest_afterMean | 77.1920 | 80.6970 |
| membership_only | 1 | globalTest_afterStd | 16.1149 | 14.0790 |
| data_changes | 0 | clusterTest_before | 99.7237 | 99.7217 |
| data_changes | 0 | clusterTest_maxDrop | 0.2102 | 0.1693 |
| data_changes | 0 | clusterTest_afterMean | 99.6653 | 99.6789 |
| data_changes | 0 | clusterTest_afterStd | 0.0690 | 0.0635 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.2480 | 51.4660 |
| data_changes | 0 | globalTest_maxDrop | 0.1080 | -1.0840 |
| data_changes | 0 | globalTest_afterMean | 51.2180 | 54.8540 |
| data_changes | 0 | globalTest_afterStd | 0.0354 | 3.2869 |
| data_changes | 1 | clusterTest_before | 99.0784 | 99.0660 |
| data_changes | 1 | clusterTest_maxDrop | 2.0613 | 0.3209 |
| data_changes | 1 | clusterTest_afterMean | 98.6690 | 98.9899 |
| data_changes | 1 | clusterTest_afterStd | 0.5939 | 0.1473 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 48.1620 | 48.1560 |
| data_changes | 1 | globalTest_maxDrop | 1.0020 | 0.1560 |
| data_changes | 1 | globalTest_afterMean | 47.9630 | 48.1190 |
| data_changes | 1 | globalTest_afterStd | 0.2887 | 0.0716 |
