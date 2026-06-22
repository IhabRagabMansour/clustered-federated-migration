# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 6

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 2.3680 | 2.4640 |
| data_changes | 0 | clusterTest_afterMean | 78.3040 | 77.7700 |
| data_changes | 0 | clusterTest_afterStd | 0.9416 | 0.9461 |
| data_changes | 0 | clusterTest_recovery | 9 | 3 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 1.1840 | 1.2320 |
| data_changes | 0 | globalTest_afterMean | 39.1520 | 38.8850 |
| data_changes | 0 | globalTest_afterStd | 0.4708 | 0.4731 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 26.3740 | 5.7660 |
| data_changes | 1 | clusterTest_afterMean | 83.5720 | 86.9660 |
| data_changes | 1 | clusterTest_afterStd | 8.0823 | 1.9029 |
| data_changes | 1 | clusterTest_recovery | 4 | 2 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 13.1870 | 2.8830 |
| data_changes | 1 | globalTest_afterMean | 41.7860 | 43.4830 |
| data_changes | 1 | globalTest_afterStd | 4.0411 | 0.9515 |
