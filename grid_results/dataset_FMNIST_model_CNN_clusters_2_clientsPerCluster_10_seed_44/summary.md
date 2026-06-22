# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 88.4160 | 87.7020 |
| membership_only | 0 | clusterTest_maxDrop | -0.3240 | -0.1980 |
| membership_only | 0 | clusterTest_afterMean | 89.1420 | 88.4020 |
| membership_only | 0 | clusterTest_afterStd | 0.1911 | 0.2258 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.2080 | 43.8510 |
| membership_only | 0 | globalTest_maxDrop | -0.1620 | -0.0990 |
| membership_only | 0 | globalTest_afterMean | 44.5710 | 44.2370 |
| membership_only | 0 | globalTest_afterStd | 0.0955 | 0.1875 |
| membership_only | 1 | clusterTest_before | 94.3080 | 94.1920 |
| membership_only | 1 | clusterTest_maxDrop | 25.2280 | 38.8320 |
| membership_only | 1 | clusterTest_afterMean | 83.2880 | 81.4480 |
| membership_only | 1 | clusterTest_afterStd | 10.0132 | 12.5926 |
| membership_only | 1 | clusterTest_recovery | 8 | 14 |
| membership_only | 1 | globalTest_before | 47.1540 | 47.0960 |
| membership_only | 1 | globalTest_maxDrop | 1.3140 | 1.4360 |
| membership_only | 1 | globalTest_afterMean | 61.3910 | 64.1660 |
| membership_only | 1 | globalTest_afterStd | 12.4995 | 11.4156 |
| data_changes | 0 | clusterTest_before | 88.4160 | 87.7020 |
| data_changes | 0 | clusterTest_maxDrop | -0.3240 | -0.3380 |
| data_changes | 0 | clusterTest_afterMean | 89.1420 | 88.4080 |
| data_changes | 0 | clusterTest_afterStd | 0.1911 | 0.2030 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.2080 | 43.8510 |
| data_changes | 0 | globalTest_maxDrop | -0.1620 | -0.1690 |
| data_changes | 0 | globalTest_afterMean | 44.5710 | 44.3560 |
| data_changes | 0 | globalTest_afterStd | 0.0955 | 0.4330 |
| data_changes | 1 | clusterTest_before | 94.3080 | 94.1920 |
| data_changes | 1 | clusterTest_maxDrop | 0.7880 | 0.2320 |
| data_changes | 1 | clusterTest_afterMean | 94.3440 | 94.3500 |
| data_changes | 1 | clusterTest_afterStd | 0.3297 | 0.2130 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 47.1540 | 47.0960 |
| data_changes | 1 | globalTest_maxDrop | 0.3940 | 0.1160 |
| data_changes | 1 | globalTest_afterMean | 47.1720 | 47.1760 |
| data_changes | 1 | globalTest_afterStd | 0.1649 | 0.1072 |
