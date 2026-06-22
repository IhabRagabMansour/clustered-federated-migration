# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 7

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 6.7880 | 3.7040 |
| data_changes | 0 | clusterTest_afterMean | 76.9960 | 77.5740 |
| data_changes | 0 | clusterTest_afterStd | 2.2223 | 1.3658 |
| data_changes | 0 | clusterTest_recovery | 7 | 12 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 3.3940 | 1.8520 |
| data_changes | 0 | globalTest_afterMean | 38.4980 | 38.7870 |
| data_changes | 0 | globalTest_afterStd | 1.1111 | 0.6829 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 29.6740 | 7.3060 |
| data_changes | 1 | clusterTest_afterMean | 82.5260 | 86.3640 |
| data_changes | 1 | clusterTest_afterStd | 9.0138 | 2.2734 |
| data_changes | 1 | clusterTest_recovery | 5 | 2 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 14.8370 | 3.6530 |
| data_changes | 1 | globalTest_afterMean | 41.2630 | 43.1820 |
| data_changes | 1 | globalTest_afterStd | 4.5069 | 1.1367 |
