# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 68.2000 | 67.5180 |
| membership_only | 0 | clusterTest_maxDrop | 0.1200 | 0.3980 |
| membership_only | 0 | clusterTest_afterMean | 68.4380 | 67.6300 |
| membership_only | 0 | clusterTest_afterStd | 0.1684 | 0.3509 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 34.1000 | 33.7590 |
| membership_only | 0 | globalTest_maxDrop | 0.0600 | 0.1990 |
| membership_only | 0 | globalTest_afterMean | 34.2190 | 33.8150 |
| membership_only | 0 | globalTest_afterStd | 0.0842 | 0.1755 |
| membership_only | 1 | clusterTest_before | 78.1780 | 77.4460 |
| membership_only | 1 | clusterTest_maxDrop | 46.8980 | 48.1860 |
| membership_only | 1 | clusterTest_afterMean | 57.2420 | 56.6280 |
| membership_only | 1 | clusterTest_afterStd | 18.7457 | 19.5235 |
| membership_only | 1 | clusterTest_recovery | 8 | 6 |
| membership_only | 1 | globalTest_before | 39.0890 | 38.7230 |
| membership_only | 1 | globalTest_maxDrop | 5.1590 | 1.3430 |
| membership_only | 1 | globalTest_afterMean | 38.4450 | 39.4130 |
| membership_only | 1 | globalTest_afterStd | 2.5276 | 2.2859 |
| data_changes | 0 | clusterTest_before | 68.2000 | 67.5180 |
| data_changes | 0 | clusterTest_maxDrop | 0.1200 | 1.7180 |
| data_changes | 0 | clusterTest_afterMean | 68.4380 | 67.2540 |
| data_changes | 0 | clusterTest_afterStd | 0.1684 | 0.6615 |
| data_changes | 0 | clusterTest_recovery | 0 | 2 |
| data_changes | 0 | globalTest_before | 34.1000 | 33.7590 |
| data_changes | 0 | globalTest_maxDrop | 0.0600 | 0.8590 |
| data_changes | 0 | globalTest_afterMean | 34.2190 | 33.6270 |
| data_changes | 0 | globalTest_afterStd | 0.0842 | 0.3308 |
| data_changes | 1 | clusterTest_before | 78.1780 | 77.4460 |
| data_changes | 1 | clusterTest_maxDrop | 4.6180 | 3.5260 |
| data_changes | 1 | clusterTest_afterMean | 76.8600 | 77.0320 |
| data_changes | 1 | clusterTest_afterStd | 1.5862 | 1.5915 |
| data_changes | 1 | clusterTest_recovery | 3 | 3 |
| data_changes | 1 | globalTest_before | 39.0890 | 38.7230 |
| data_changes | 1 | globalTest_maxDrop | 2.3090 | 1.7630 |
| data_changes | 1 | globalTest_afterMean | 38.4300 | 38.5160 |
| data_changes | 1 | globalTest_afterStd | 0.7931 | 0.7957 |
