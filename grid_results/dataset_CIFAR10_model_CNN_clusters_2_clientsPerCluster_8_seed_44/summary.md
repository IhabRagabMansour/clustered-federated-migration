# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.5980 | 80.2200 |
| membership_only | 0 | clusterTest_maxDrop | 0.9580 | 1.6400 |
| membership_only | 0 | clusterTest_afterMean | 80.6080 | 79.8060 |
| membership_only | 0 | clusterTest_afterStd | 0.7685 | 0.8132 |
| membership_only | 0 | clusterTest_recovery | 0 | 4 |
| membership_only | 0 | globalTest_before | 40.2990 | 40.1100 |
| membership_only | 0 | globalTest_maxDrop | 0.4790 | 0.8200 |
| membership_only | 0 | globalTest_afterMean | 40.3040 | 39.9030 |
| membership_only | 0 | globalTest_afterStd | 0.3843 | 0.4066 |
| membership_only | 1 | clusterTest_before | 88.1080 | 87.6320 |
| membership_only | 1 | clusterTest_maxDrop | 79.0080 | 71.5920 |
| membership_only | 1 | clusterTest_afterMean | 60.3860 | 56.9680 |
| membership_only | 1 | clusterTest_afterStd | 27.8984 | 30.2197 |
| membership_only | 1 | clusterTest_recovery | 10 | 8 |
| membership_only | 1 | globalTest_before | 44.0540 | 43.8160 |
| membership_only | 1 | globalTest_maxDrop | 4.9540 | 2.6660 |
| membership_only | 1 | globalTest_afterMean | 46.1370 | 45.9370 |
| membership_only | 1 | globalTest_afterStd | 5.1171 | 4.9763 |
| data_changes | 0 | clusterTest_before | 80.5980 | 80.2200 |
| data_changes | 0 | clusterTest_maxDrop | 0.9580 | 1.9800 |
| data_changes | 0 | clusterTest_afterMean | 80.6080 | 79.9200 |
| data_changes | 0 | clusterTest_afterStd | 0.7685 | 0.9027 |
| data_changes | 0 | clusterTest_recovery | 0 | 7 |
| data_changes | 0 | globalTest_before | 40.2990 | 40.1100 |
| data_changes | 0 | globalTest_maxDrop | 0.4790 | 0.9900 |
| data_changes | 0 | globalTest_afterMean | 40.3040 | 39.9600 |
| data_changes | 0 | globalTest_afterStd | 0.3843 | 0.4513 |
| data_changes | 1 | clusterTest_before | 88.1080 | 87.6320 |
| data_changes | 1 | clusterTest_maxDrop | 17.1280 | 5.6120 |
| data_changes | 1 | clusterTest_afterMean | 85.7840 | 87.3460 |
| data_changes | 1 | clusterTest_afterStd | 5.3378 | 1.8287 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.0540 | 43.8160 |
| data_changes | 1 | globalTest_maxDrop | 8.5640 | 2.8060 |
| data_changes | 1 | globalTest_afterMean | 42.8920 | 43.6730 |
| data_changes | 1 | globalTest_afterStd | 2.6689 | 0.9144 |
