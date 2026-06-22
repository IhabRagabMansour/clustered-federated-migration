# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 83.0140 | 82.6400 |
| membership_only | 0 | clusterTest_maxDrop | 2.8340 | 4.9200 |
| membership_only | 0 | clusterTest_afterMean | 82.0360 | 81.2900 |
| membership_only | 0 | clusterTest_afterStd | 0.9655 | 1.6456 |
| membership_only | 0 | clusterTest_recovery | 4 | 7 |
| membership_only | 0 | globalTest_before | 41.5070 | 41.3200 |
| membership_only | 0 | globalTest_maxDrop | 1.4170 | 2.4600 |
| membership_only | 0 | globalTest_afterMean | 41.0180 | 40.6450 |
| membership_only | 0 | globalTest_afterStd | 0.4828 | 0.8228 |
| membership_only | 1 | clusterTest_before | 89.1500 | 89.2140 |
| membership_only | 1 | clusterTest_maxDrop | 87.3300 | 87.0340 |
| membership_only | 1 | clusterTest_afterMean | 51.5300 | 52.2480 |
| membership_only | 1 | clusterTest_afterStd | 37.1323 | 35.9687 |
| membership_only | 1 | clusterTest_recovery | 8 | 8 |
| membership_only | 1 | globalTest_before | 44.5750 | 44.6070 |
| membership_only | 1 | globalTest_maxDrop | 5.7050 | 4.6470 |
| membership_only | 1 | globalTest_afterMean | 44.3070 | 46.9450 |
| membership_only | 1 | globalTest_afterStd | 3.0342 | 4.8912 |
| data_changes | 0 | clusterTest_before | 83.0140 | 82.6400 |
| data_changes | 0 | clusterTest_maxDrop | 2.8340 | 7.5200 |
| data_changes | 0 | clusterTest_afterMean | 82.0360 | 80.5240 |
| data_changes | 0 | clusterTest_afterStd | 0.9655 | 2.5772 |
| data_changes | 0 | clusterTest_recovery | 4 | 4 |
| data_changes | 0 | globalTest_before | 41.5070 | 41.3200 |
| data_changes | 0 | globalTest_maxDrop | 1.4170 | 3.7600 |
| data_changes | 0 | globalTest_afterMean | 41.0180 | 40.2620 |
| data_changes | 0 | globalTest_afterStd | 0.4828 | 1.2886 |
| data_changes | 1 | clusterTest_before | 89.1500 | 89.2140 |
| data_changes | 1 | clusterTest_maxDrop | 19.7700 | 2.3340 |
| data_changes | 1 | clusterTest_afterMean | 87.2420 | 89.4920 |
| data_changes | 1 | clusterTest_afterStd | 6.0453 | 1.0103 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.5750 | 44.6070 |
| data_changes | 1 | globalTest_maxDrop | 9.8850 | 1.1670 |
| data_changes | 1 | globalTest_afterMean | 43.6210 | 44.7460 |
| data_changes | 1 | globalTest_afterStd | 3.0226 | 0.5051 |
