# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 4

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 1.3680 | 2.3240 |
| data_changes | 0 | clusterTest_afterMean | 79.7100 | 79.1160 |
| data_changes | 0 | clusterTest_afterStd | 1.0582 | 1.1759 |
| data_changes | 0 | clusterTest_recovery | 3 | 5 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 0.6840 | 1.1620 |
| data_changes | 0 | globalTest_afterMean | 39.8550 | 39.5580 |
| data_changes | 0 | globalTest_afterStd | 0.5291 | 0.5879 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 19.0140 | 3.5660 |
| data_changes | 1 | clusterTest_afterMean | 85.5520 | 87.5160 |
| data_changes | 1 | clusterTest_afterStd | 5.7650 | 1.2790 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 9.5070 | 1.7830 |
| data_changes | 1 | globalTest_afterMean | 42.7760 | 43.7580 |
| data_changes | 1 | globalTest_afterStd | 2.8825 | 0.6395 |
