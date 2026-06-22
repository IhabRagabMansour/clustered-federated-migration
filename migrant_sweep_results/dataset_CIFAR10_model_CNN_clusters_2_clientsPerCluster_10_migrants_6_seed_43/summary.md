# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 6

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | 4.7840 | 3.8240 |
| data_changes | 0 | clusterTest_afterMean | 80.2020 | 79.5940 |
| data_changes | 0 | clusterTest_afterStd | 1.7263 | 1.4918 |
| data_changes | 0 | clusterTest_recovery | 3 | 3 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | 2.3920 | 1.9120 |
| data_changes | 0 | globalTest_afterMean | 40.1010 | 39.7970 |
| data_changes | 0 | globalTest_afterStd | 0.8632 | 0.7459 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 10.3600 | 3.9140 |
| data_changes | 1 | clusterTest_afterMean | 85.8380 | 87.4660 |
| data_changes | 1 | clusterTest_afterStd | 3.9782 | 1.3655 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 5.1800 | 1.9570 |
| data_changes | 1 | globalTest_afterMean | 42.9190 | 43.7330 |
| data_changes | 1 | globalTest_afterStd | 1.9891 | 0.6827 |
