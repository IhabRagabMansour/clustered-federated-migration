# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 5

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 79.4080 | 78.7640 |
| data_changes | 0 | clusterTest_maxDrop | 1.2480 | 2.0640 |
| data_changes | 0 | clusterTest_afterMean | 79.8180 | 79.2000 |
| data_changes | 0 | clusterTest_afterStd | 0.7748 | 0.9818 |
| data_changes | 0 | clusterTest_recovery | 9 | 9 |
| data_changes | 0 | globalTest_before | 39.7040 | 39.3820 |
| data_changes | 0 | globalTest_maxDrop | 0.6240 | 1.0320 |
| data_changes | 0 | globalTest_afterMean | 39.9090 | 39.6000 |
| data_changes | 0 | globalTest_afterStd | 0.3874 | 0.4909 |
| data_changes | 1 | clusterTest_before | 87.8540 | 87.4660 |
| data_changes | 1 | clusterTest_maxDrop | 22.7540 | 4.1660 |
| data_changes | 1 | clusterTest_afterMean | 84.1100 | 86.9880 |
| data_changes | 1 | clusterTest_afterStd | 6.8507 | 1.3692 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 43.9270 | 43.7330 |
| data_changes | 1 | globalTest_maxDrop | 11.3770 | 2.0830 |
| data_changes | 1 | globalTest_afterMean | 42.0550 | 43.4940 |
| data_changes | 1 | globalTest_afterStd | 3.4254 | 0.6846 |
