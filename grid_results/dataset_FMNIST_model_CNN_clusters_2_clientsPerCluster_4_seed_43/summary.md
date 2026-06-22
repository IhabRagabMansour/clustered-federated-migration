# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 91.0520 | 90.5820 |
| membership_only | 0 | clusterTest_maxDrop | 0.3120 | 0.4820 |
| membership_only | 0 | clusterTest_afterMean | 91.1580 | 90.7260 |
| membership_only | 0 | clusterTest_afterStd | 0.2023 | 0.3260 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.5260 | 45.2910 |
| membership_only | 0 | globalTest_maxDrop | 0.1560 | 0.2410 |
| membership_only | 0 | globalTest_afterMean | 45.5790 | 45.3630 |
| membership_only | 0 | globalTest_afterStd | 0.1011 | 0.1630 |
| membership_only | 1 | clusterTest_before | 96.4540 | 96.3220 |
| membership_only | 1 | clusterTest_maxDrop | 36.3540 | 28.6620 |
| membership_only | 1 | clusterTest_afterMean | 82.5660 | 83.2240 |
| membership_only | 1 | clusterTest_afterStd | 13.4551 | 11.0085 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 48.2270 | 48.1610 |
| membership_only | 1 | globalTest_maxDrop | -6.9930 | -10.6290 |
| membership_only | 1 | globalTest_afterMean | 68.9460 | 72.0850 |
| membership_only | 1 | globalTest_afterStd | 10.0194 | 9.2777 |
| data_changes | 0 | clusterTest_before | 91.0520 | 90.5820 |
| data_changes | 0 | clusterTest_maxDrop | 0.3120 | 1.2220 |
| data_changes | 0 | clusterTest_afterMean | 91.1580 | 90.5700 |
| data_changes | 0 | clusterTest_afterStd | 0.2023 | 0.4643 |
| data_changes | 0 | clusterTest_recovery | 0 | 1 |
| data_changes | 0 | globalTest_before | 45.5260 | 45.2910 |
| data_changes | 0 | globalTest_maxDrop | 0.1560 | 0.1010 |
| data_changes | 0 | globalTest_afterMean | 45.5790 | 46.9160 |
| data_changes | 0 | globalTest_afterStd | 0.1011 | 3.4516 |
| data_changes | 1 | clusterTest_before | 96.4540 | 96.3220 |
| data_changes | 1 | clusterTest_maxDrop | 3.6140 | 0.9420 |
| data_changes | 1 | clusterTest_afterMean | 95.5140 | 96.1180 |
| data_changes | 1 | clusterTest_afterStd | 1.0055 | 0.3198 |
| data_changes | 1 | clusterTest_recovery | 3 | 0 |
| data_changes | 1 | globalTest_before | 48.2270 | 48.1610 |
| data_changes | 1 | globalTest_maxDrop | 1.8070 | 0.4710 |
| data_changes | 1 | globalTest_afterMean | 47.7570 | 48.0610 |
| data_changes | 1 | globalTest_afterStd | 0.5028 | 0.1610 |
