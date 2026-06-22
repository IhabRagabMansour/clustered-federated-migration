# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 83.4540 | 83.0940 |
| membership_only | 0 | clusterTest_maxDrop | 5.8740 | 5.4940 |
| membership_only | 0 | clusterTest_afterMean | 80.8680 | 79.7480 |
| membership_only | 0 | clusterTest_afterStd | 1.9200 | 1.5398 |
| membership_only | 0 | clusterTest_recovery | 6 | 8 |
| membership_only | 0 | globalTest_before | 41.7270 | 41.5470 |
| membership_only | 0 | globalTest_maxDrop | 2.9370 | 2.7470 |
| membership_only | 0 | globalTest_afterMean | 40.4340 | 39.8740 |
| membership_only | 0 | globalTest_afterStd | 0.9600 | 0.7699 |
| membership_only | 1 | clusterTest_before | 89.1700 | 89.3200 |
| membership_only | 1 | clusterTest_maxDrop | 85.5300 | 85.9800 |
| membership_only | 1 | clusterTest_afterMean | 54.6140 | 60.4700 |
| membership_only | 1 | clusterTest_afterStd | 35.9850 | 34.0084 |
| membership_only | 1 | clusterTest_recovery | 6 | 5 |
| membership_only | 1 | globalTest_before | 44.5850 | 44.6600 |
| membership_only | 1 | globalTest_maxDrop | 3.4250 | 2.6300 |
| membership_only | 1 | globalTest_afterMean | 47.2900 | 50.9020 |
| membership_only | 1 | globalTest_afterStd | 5.4227 | 8.4591 |
| data_changes | 0 | clusterTest_before | 83.4540 | 83.0940 |
| data_changes | 0 | clusterTest_maxDrop | 5.8740 | 9.7940 |
| data_changes | 0 | clusterTest_afterMean | 80.8680 | 78.2060 |
| data_changes | 0 | clusterTest_afterStd | 1.9200 | 2.7235 |
| data_changes | 0 | clusterTest_recovery | 6 | 8 |
| data_changes | 0 | globalTest_before | 41.7270 | 41.5470 |
| data_changes | 0 | globalTest_maxDrop | 2.9370 | 4.8970 |
| data_changes | 0 | globalTest_afterMean | 40.4340 | 39.1030 |
| data_changes | 0 | globalTest_afterStd | 0.9600 | 1.3618 |
| data_changes | 1 | clusterTest_before | 89.1700 | 89.3200 |
| data_changes | 1 | clusterTest_maxDrop | 17.2500 | 3.3600 |
| data_changes | 1 | clusterTest_afterMean | 87.3120 | 89.4640 |
| data_changes | 1 | clusterTest_afterStd | 5.3109 | 1.2379 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.5850 | 44.6600 |
| data_changes | 1 | globalTest_maxDrop | 8.6250 | 1.6800 |
| data_changes | 1 | globalTest_afterMean | 43.6560 | 44.7320 |
| data_changes | 1 | globalTest_afterStd | 2.6555 | 0.6189 |
