# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 9

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 16.5680 | 13.9640 |
| data_changes | 0 | clusterTest_afterMean | 73.2500 | 72.3040 |
| data_changes | 0 | clusterTest_afterStd | 3.9848 | 3.1115 |
| data_changes | 0 | clusterTest_recovery | 17 | -1 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 8.2840 | 6.9820 |
| data_changes | 0 | globalTest_afterMean | 36.6250 | 36.1520 |
| data_changes | 0 | globalTest_afterStd | 1.9924 | 1.5558 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 33.7140 | 9.1660 |
| data_changes | 1 | clusterTest_afterMean | 81.8560 | 86.1680 |
| data_changes | 1 | clusterTest_afterStd | 10.0283 | 2.7156 |
| data_changes | 1 | clusterTest_recovery | 7 | 2 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 16.8570 | 4.5830 |
| data_changes | 1 | globalTest_afterMean | 40.9280 | 43.0840 |
| data_changes | 1 | globalTest_afterStd | 5.0141 | 1.3578 |
