# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 81.8460 | 81.6040 |
| membership_only | 0 | clusterTest_maxDrop | 3.3060 | 4.7840 |
| membership_only | 0 | clusterTest_afterMean | 80.8120 | 80.2120 |
| membership_only | 0 | clusterTest_afterStd | 1.4087 | 1.4459 |
| membership_only | 0 | clusterTest_recovery | 2 | 5 |
| membership_only | 0 | globalTest_before | 40.9230 | 40.8020 |
| membership_only | 0 | globalTest_maxDrop | 1.6530 | 2.3920 |
| membership_only | 0 | globalTest_afterMean | 40.4060 | 40.1060 |
| membership_only | 0 | globalTest_afterStd | 0.7043 | 0.7229 |
| membership_only | 1 | clusterTest_before | 89.8700 | 89.5760 |
| membership_only | 1 | clusterTest_maxDrop | 88.7100 | 89.3960 |
| membership_only | 1 | clusterTest_afterMean | 49.5860 | 50.8380 |
| membership_only | 1 | clusterTest_afterStd | 38.3438 | 38.6097 |
| membership_only | 1 | clusterTest_recovery | 16 | -1 |
| membership_only | 1 | globalTest_before | 44.9350 | 44.7880 |
| membership_only | 1 | globalTest_maxDrop | 6.9350 | 6.0480 |
| membership_only | 1 | globalTest_afterMean | 43.1630 | 45.6900 |
| membership_only | 1 | globalTest_afterStd | 3.0115 | 6.3711 |
| data_changes | 0 | clusterTest_before | 81.8460 | 81.6040 |
| data_changes | 0 | clusterTest_maxDrop | 3.3060 | 7.7240 |
| data_changes | 0 | clusterTest_afterMean | 80.8120 | 79.7360 |
| data_changes | 0 | clusterTest_afterStd | 1.4087 | 2.1726 |
| data_changes | 0 | clusterTest_recovery | 2 | 7 |
| data_changes | 0 | globalTest_before | 40.9230 | 40.8020 |
| data_changes | 0 | globalTest_maxDrop | 1.6530 | 3.8620 |
| data_changes | 0 | globalTest_afterMean | 40.4060 | 39.8680 |
| data_changes | 0 | globalTest_afterStd | 0.7043 | 1.0863 |
| data_changes | 1 | clusterTest_before | 89.8700 | 89.5760 |
| data_changes | 1 | clusterTest_maxDrop | 21.6900 | 2.2960 |
| data_changes | 1 | clusterTest_afterMean | 87.0820 | 89.4860 |
| data_changes | 1 | clusterTest_afterStd | 6.5112 | 1.0061 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 44.9350 | 44.7880 |
| data_changes | 1 | globalTest_maxDrop | 10.8450 | 1.1480 |
| data_changes | 1 | globalTest_afterMean | 43.5410 | 44.7430 |
| data_changes | 1 | globalTest_afterStd | 3.2556 | 0.5031 |
