# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 9

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 78.9020 | 78.1040 |
| data_changes | 0 | clusterTest_maxDrop | 15.7820 | 14.3240 |
| data_changes | 0 | clusterTest_afterMean | 71.9540 | 71.2920 |
| data_changes | 0 | clusterTest_afterStd | 4.2639 | 4.0268 |
| data_changes | 0 | clusterTest_recovery | 5 | 5 |
| data_changes | 0 | globalTest_before | 39.4510 | 39.0520 |
| data_changes | 0 | globalTest_maxDrop | 7.8910 | 7.1620 |
| data_changes | 0 | globalTest_afterMean | 35.9770 | 35.6460 |
| data_changes | 0 | globalTest_afterStd | 2.1320 | 2.0134 |
| data_changes | 1 | clusterTest_before | 88.1440 | 87.4840 |
| data_changes | 1 | clusterTest_maxDrop | 23.9640 | 7.1240 |
| data_changes | 1 | clusterTest_afterMean | 82.2960 | 85.7300 |
| data_changes | 1 | clusterTest_afterStd | 6.7766 | 1.9384 |
| data_changes | 1 | clusterTest_recovery | 10 | 4 |
| data_changes | 1 | globalTest_before | 44.0720 | 43.7420 |
| data_changes | 1 | globalTest_maxDrop | 11.9820 | 3.5620 |
| data_changes | 1 | globalTest_afterMean | 41.1480 | 42.8650 |
| data_changes | 1 | globalTest_afterStd | 3.3883 | 0.9692 |
