# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 88.1520 | 86.7760 |
| membership_only | 0 | clusterTest_maxDrop | 0.5720 | 3.5560 |
| membership_only | 0 | clusterTest_afterMean | 88.9760 | 87.2360 |
| membership_only | 0 | clusterTest_afterStd | 0.6022 | 2.0307 |
| membership_only | 0 | clusterTest_recovery | 0 | 3 |
| membership_only | 0 | globalTest_before | 44.0760 | 43.3880 |
| membership_only | 0 | globalTest_maxDrop | 0.2860 | 1.7780 |
| membership_only | 0 | globalTest_afterMean | 44.4880 | 43.6300 |
| membership_only | 0 | globalTest_afterStd | 0.3011 | 1.0219 |
| membership_only | 1 | clusterTest_before | 94.4300 | 94.1380 |
| membership_only | 1 | clusterTest_maxDrop | 27.3700 | 34.6380 |
| membership_only | 1 | clusterTest_afterMean | 82.2500 | 81.5740 |
| membership_only | 1 | clusterTest_afterStd | 11.4221 | 12.1400 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 47.2150 | 47.0690 |
| membership_only | 1 | globalTest_maxDrop | 1.5150 | 0.9690 |
| membership_only | 1 | globalTest_afterMean | 62.1740 | 65.4820 |
| membership_only | 1 | globalTest_afterStd | 12.2544 | 11.5505 |
| data_changes | 0 | clusterTest_before | 88.1520 | 86.7760 |
| data_changes | 0 | clusterTest_maxDrop | 0.5720 | 4.8560 |
| data_changes | 0 | clusterTest_afterMean | 88.9760 | 87.1300 |
| data_changes | 0 | clusterTest_afterStd | 0.6022 | 2.2709 |
| data_changes | 0 | clusterTest_recovery | 0 | 3 |
| data_changes | 0 | globalTest_before | 44.0760 | 43.3880 |
| data_changes | 0 | globalTest_maxDrop | 0.2860 | 2.4280 |
| data_changes | 0 | globalTest_afterMean | 44.4880 | 43.7100 |
| data_changes | 0 | globalTest_afterStd | 0.3011 | 1.2294 |
| data_changes | 1 | clusterTest_before | 94.4300 | 94.1380 |
| data_changes | 1 | clusterTest_maxDrop | 1.7900 | 2.3980 |
| data_changes | 1 | clusterTest_afterMean | 94.1940 | 94.1660 |
| data_changes | 1 | clusterTest_afterStd | 0.6824 | 0.8522 |
| data_changes | 1 | clusterTest_recovery | 4 | 4 |
| data_changes | 1 | globalTest_before | 47.2150 | 47.0690 |
| data_changes | 1 | globalTest_maxDrop | 0.8950 | 1.1990 |
| data_changes | 1 | globalTest_afterMean | 47.0970 | 47.1070 |
| data_changes | 1 | globalTest_afterStd | 0.3412 | 0.4381 |
