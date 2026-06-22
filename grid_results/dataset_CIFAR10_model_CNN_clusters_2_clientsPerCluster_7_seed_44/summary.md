# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.9180 | 80.4080 |
| membership_only | 0 | clusterTest_maxDrop | 1.3180 | 2.2080 |
| membership_only | 0 | clusterTest_afterMean | 81.2120 | 80.6220 |
| membership_only | 0 | clusterTest_afterStd | 0.8612 | 1.2157 |
| membership_only | 0 | clusterTest_recovery | 3 | 3 |
| membership_only | 0 | globalTest_before | 40.4590 | 40.2040 |
| membership_only | 0 | globalTest_maxDrop | 0.6590 | 1.1040 |
| membership_only | 0 | globalTest_afterMean | 40.6060 | 40.3110 |
| membership_only | 0 | globalTest_afterStd | 0.4306 | 0.6078 |
| membership_only | 1 | clusterTest_before | 88.6860 | 88.2940 |
| membership_only | 1 | clusterTest_maxDrop | 80.1260 | 81.4540 |
| membership_only | 1 | clusterTest_afterMean | 54.9120 | 52.7880 |
| membership_only | 1 | clusterTest_afterStd | 33.2225 | 35.0054 |
| membership_only | 1 | clusterTest_recovery | 8 | 8 |
| membership_only | 1 | globalTest_before | 44.3430 | 44.1470 |
| membership_only | 1 | globalTest_maxDrop | 4.8530 | 4.6670 |
| membership_only | 1 | globalTest_afterMean | 44.5280 | 44.9220 |
| membership_only | 1 | globalTest_afterStd | 3.7575 | 3.7491 |
| data_changes | 0 | clusterTest_before | 80.9180 | 80.4080 |
| data_changes | 0 | clusterTest_maxDrop | 1.3180 | 2.1280 |
| data_changes | 0 | clusterTest_afterMean | 81.2120 | 80.5220 |
| data_changes | 0 | clusterTest_afterStd | 0.8612 | 1.1868 |
| data_changes | 0 | clusterTest_recovery | 3 | 3 |
| data_changes | 0 | globalTest_before | 40.4590 | 40.2040 |
| data_changes | 0 | globalTest_maxDrop | 0.6590 | 1.0640 |
| data_changes | 0 | globalTest_afterMean | 40.6060 | 40.2610 |
| data_changes | 0 | globalTest_afterStd | 0.4306 | 0.5934 |
| data_changes | 1 | clusterTest_before | 88.6860 | 88.2940 |
| data_changes | 1 | clusterTest_maxDrop | 22.3460 | 2.8340 |
| data_changes | 1 | clusterTest_afterMean | 86.0660 | 88.6440 |
| data_changes | 1 | clusterTest_afterStd | 6.9079 | 1.1498 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.3430 | 44.1470 |
| data_changes | 1 | globalTest_maxDrop | 11.1730 | 1.4170 |
| data_changes | 1 | globalTest_afterMean | 43.0330 | 44.3220 |
| data_changes | 1 | globalTest_afterStd | 3.4540 | 0.5749 |
