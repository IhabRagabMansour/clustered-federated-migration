# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 87.5220 | 86.5860 |
| membership_only | 0 | clusterTest_maxDrop | 0.4220 | 1.9860 |
| membership_only | 0 | clusterTest_afterMean | 88.0400 | 86.5280 |
| membership_only | 0 | clusterTest_afterStd | 0.6173 | 1.1140 |
| membership_only | 0 | clusterTest_recovery | 0 | 8 |
| membership_only | 0 | globalTest_before | 43.7610 | 43.2930 |
| membership_only | 0 | globalTest_maxDrop | 0.2110 | 0.9830 |
| membership_only | 0 | globalTest_afterMean | 44.0200 | 43.3060 |
| membership_only | 0 | globalTest_afterStd | 0.3086 | 0.5195 |
| membership_only | 1 | clusterTest_before | 94.0620 | 93.7540 |
| membership_only | 1 | clusterTest_maxDrop | 26.5420 | 31.9740 |
| membership_only | 1 | clusterTest_afterMean | 81.8260 | 80.8520 |
| membership_only | 1 | clusterTest_afterStd | 11.0898 | 12.2190 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 47.0310 | 46.8770 |
| membership_only | 1 | globalTest_maxDrop | 1.6810 | 1.0770 |
| membership_only | 1 | globalTest_afterMean | 60.5380 | 64.5070 |
| membership_only | 1 | globalTest_afterStd | 13.1125 | 12.0972 |
| data_changes | 0 | clusterTest_before | 87.5220 | 86.5860 |
| data_changes | 0 | clusterTest_maxDrop | 0.4220 | 2.5260 |
| data_changes | 0 | clusterTest_afterMean | 88.0400 | 86.5440 |
| data_changes | 0 | clusterTest_afterStd | 0.6173 | 1.1076 |
| data_changes | 0 | clusterTest_recovery | 0 | 8 |
| data_changes | 0 | globalTest_before | 43.7610 | 43.2930 |
| data_changes | 0 | globalTest_maxDrop | 0.2110 | 1.0830 |
| data_changes | 0 | globalTest_afterMean | 44.0200 | 43.5880 |
| data_changes | 0 | globalTest_afterStd | 0.3086 | 0.7486 |
| data_changes | 1 | clusterTest_before | 94.0620 | 93.7540 |
| data_changes | 1 | clusterTest_maxDrop | 0.9620 | 0.4540 |
| data_changes | 1 | clusterTest_afterMean | 93.9960 | 94.0720 |
| data_changes | 1 | clusterTest_afterStd | 0.4791 | 0.4008 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 47.0310 | 46.8770 |
| data_changes | 1 | globalTest_maxDrop | 0.4810 | 0.2270 |
| data_changes | 1 | globalTest_afterMean | 46.9980 | 47.0360 |
| data_changes | 1 | globalTest_afterStd | 0.2396 | 0.2004 |
