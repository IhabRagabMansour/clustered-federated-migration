# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 87.1260 | 86.1840 |
| membership_only | 0 | clusterTest_maxDrop | -0.4540 | -0.3960 |
| membership_only | 0 | clusterTest_afterMean | 88.0280 | 86.9760 |
| membership_only | 0 | clusterTest_afterStd | 0.3127 | 0.2783 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 43.5630 | 43.0920 |
| membership_only | 0 | globalTest_maxDrop | -0.2270 | -0.2280 |
| membership_only | 0 | globalTest_afterMean | 44.0140 | 43.6040 |
| membership_only | 0 | globalTest_afterStd | 0.1563 | 0.2429 |
| membership_only | 1 | clusterTest_before | 93.6400 | 93.4280 |
| membership_only | 1 | clusterTest_maxDrop | 28.4000 | 33.8080 |
| membership_only | 1 | clusterTest_afterMean | 81.3460 | 80.4360 |
| membership_only | 1 | clusterTest_afterStd | 11.1738 | 11.8361 |
| membership_only | 1 | clusterTest_recovery | 6 | 8 |
| membership_only | 1 | globalTest_before | 46.8200 | 46.7140 |
| membership_only | 1 | globalTest_maxDrop | 1.6200 | 1.7040 |
| membership_only | 1 | globalTest_afterMean | 58.8920 | 62.1960 |
| membership_only | 1 | globalTest_afterStd | 13.0348 | 13.1743 |
| data_changes | 0 | clusterTest_before | 87.1260 | 86.1840 |
| data_changes | 0 | clusterTest_maxDrop | -0.4540 | -0.2560 |
| data_changes | 0 | clusterTest_afterMean | 88.0280 | 86.9880 |
| data_changes | 0 | clusterTest_afterStd | 0.3127 | 0.3405 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 43.5630 | 43.0920 |
| data_changes | 0 | globalTest_maxDrop | -0.2270 | -0.2680 |
| data_changes | 0 | globalTest_afterMean | 44.0140 | 44.1330 |
| data_changes | 0 | globalTest_afterStd | 0.1563 | 1.0500 |
| data_changes | 1 | clusterTest_before | 93.6400 | 93.4280 |
| data_changes | 1 | clusterTest_maxDrop | 0.9400 | 0.8480 |
| data_changes | 1 | clusterTest_afterMean | 93.5500 | 93.5960 |
| data_changes | 1 | clusterTest_afterStd | 0.3994 | 0.3648 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 46.8200 | 46.7140 |
| data_changes | 1 | globalTest_maxDrop | 0.4700 | 0.4240 |
| data_changes | 1 | globalTest_afterMean | 46.7750 | 46.7980 |
| data_changes | 1 | globalTest_afterStd | 0.1997 | 0.1824 |
