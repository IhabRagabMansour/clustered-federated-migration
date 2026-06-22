# Migrant-Count Sweep Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 10

Note: this configuration migrates all clients from the source cluster, leaving the source cluster empty after migration.

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| data_changes | 0 | clusterTest_before | 80.2040 | 79.3240 |
| data_changes | 0 | clusterTest_maxDrop | -1.0960 | 0.3240 |
| data_changes | 0 | clusterTest_afterMean | 81.3000 | 79.4100 |
| data_changes | 0 | clusterTest_afterStd | 0.0000 | 0.4100 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 40.1020 | 39.6620 |
| data_changes | 0 | globalTest_maxDrop | -0.5480 | -0.2480 |
| data_changes | 0 | globalTest_afterMean | 40.6500 | 42.5300 |
| data_changes | 0 | globalTest_afterStd | 0.0000 | 2.6200 |
| data_changes | 1 | clusterTest_before | 88.2800 | 87.7140 |
| data_changes | 1 | clusterTest_maxDrop | 15.5000 | 6.1140 |
| data_changes | 1 | clusterTest_afterMean | 83.9060 | 86.7420 |
| data_changes | 1 | clusterTest_afterStd | 4.9387 | 1.9120 |
| data_changes | 1 | clusterTest_recovery | 8 | 3 |
| data_changes | 1 | globalTest_before | 44.1400 | 43.8570 |
| data_changes | 1 | globalTest_maxDrop | 7.7500 | 3.0570 |
| data_changes | 1 | globalTest_afterMean | 41.9530 | 43.3710 |
| data_changes | 1 | globalTest_afterStd | 2.4693 | 0.9560 |
