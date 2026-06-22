# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 82.6180 | 82.6840 |
| membership_only | 0 | clusterTest_maxDrop | 8.0380 | 4.6040 |
| membership_only | 0 | clusterTest_afterMean | 79.8180 | 79.5640 |
| membership_only | 0 | clusterTest_afterStd | 2.4083 | 0.9756 |
| membership_only | 0 | clusterTest_recovery | 5 | 10 |
| membership_only | 0 | globalTest_before | 41.3090 | 41.3420 |
| membership_only | 0 | globalTest_maxDrop | 4.0190 | 2.3020 |
| membership_only | 0 | globalTest_afterMean | 39.9090 | 39.7820 |
| membership_only | 0 | globalTest_afterStd | 1.2041 | 0.4878 |
| membership_only | 1 | clusterTest_before | 89.9600 | 89.3740 |
| membership_only | 1 | clusterTest_maxDrop | 87.1600 | 87.9340 |
| membership_only | 1 | clusterTest_afterMean | 53.5860 | 55.7080 |
| membership_only | 1 | clusterTest_afterStd | 37.2891 | 37.5837 |
| membership_only | 1 | clusterTest_recovery | 4 | 5 |
| membership_only | 1 | globalTest_before | 44.9800 | 44.6870 |
| membership_only | 1 | globalTest_maxDrop | 4.3500 | 3.3070 |
| membership_only | 1 | globalTest_afterMean | 46.8690 | 48.1470 |
| membership_only | 1 | globalTest_afterStd | 6.0155 | 6.5414 |
| data_changes | 0 | clusterTest_before | 82.6180 | 82.6840 |
| data_changes | 0 | clusterTest_maxDrop | 8.0380 | 6.9040 |
| data_changes | 0 | clusterTest_afterMean | 79.8180 | 78.4500 |
| data_changes | 0 | clusterTest_afterStd | 2.4083 | 1.6133 |
| data_changes | 0 | clusterTest_recovery | 5 | 14 |
| data_changes | 0 | globalTest_before | 41.3090 | 41.3420 |
| data_changes | 0 | globalTest_maxDrop | 4.0190 | 3.4520 |
| data_changes | 0 | globalTest_afterMean | 39.9090 | 39.2250 |
| data_changes | 0 | globalTest_afterStd | 1.2041 | 0.8067 |
| data_changes | 1 | clusterTest_before | 89.9600 | 89.3740 |
| data_changes | 1 | clusterTest_maxDrop | 29.2800 | 3.3940 |
| data_changes | 1 | clusterTest_afterMean | 86.7180 | 89.7900 |
| data_changes | 1 | clusterTest_afterStd | 8.7623 | 1.3362 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.9800 | 44.6870 |
| data_changes | 1 | globalTest_maxDrop | 14.6400 | 1.6970 |
| data_changes | 1 | globalTest_afterMean | 43.3590 | 44.8950 |
| data_changes | 1 | globalTest_afterStd | 4.3811 | 0.6681 |
