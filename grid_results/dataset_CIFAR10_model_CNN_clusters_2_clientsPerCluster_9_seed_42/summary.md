# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 79.3920 | 78.8400 |
| membership_only | 0 | clusterTest_maxDrop | 1.7120 | 1.7000 |
| membership_only | 0 | clusterTest_afterMean | 79.9300 | 79.5380 |
| membership_only | 0 | clusterTest_afterStd | 1.5427 | 1.2650 |
| membership_only | 0 | clusterTest_recovery | 3 | 2 |
| membership_only | 0 | globalTest_before | 39.6960 | 39.4200 |
| membership_only | 0 | globalTest_maxDrop | 0.8560 | 0.8500 |
| membership_only | 0 | globalTest_afterMean | 39.9650 | 39.7690 |
| membership_only | 0 | globalTest_afterStd | 0.7714 | 0.6325 |
| membership_only | 1 | clusterTest_before | 88.4640 | 87.8440 |
| membership_only | 1 | clusterTest_maxDrop | 61.1440 | 68.5840 |
| membership_only | 1 | clusterTest_afterMean | 68.5640 | 63.9400 |
| membership_only | 1 | clusterTest_afterStd | 20.3528 | 25.1280 |
| membership_only | 1 | clusterTest_recovery | 14 | 6 |
| membership_only | 1 | globalTest_before | 44.2320 | 43.9220 |
| membership_only | 1 | globalTest_maxDrop | 1.4720 | 3.2020 |
| membership_only | 1 | globalTest_afterMean | 48.5750 | 47.9870 |
| membership_only | 1 | globalTest_afterStd | 6.4052 | 7.0269 |
| data_changes | 0 | clusterTest_before | 79.3920 | 78.8400 |
| data_changes | 0 | clusterTest_maxDrop | 1.7120 | 1.0800 |
| data_changes | 0 | clusterTest_afterMean | 79.9300 | 79.5840 |
| data_changes | 0 | clusterTest_afterStd | 1.5427 | 1.1176 |
| data_changes | 0 | clusterTest_recovery | 3 | 2 |
| data_changes | 0 | globalTest_before | 39.6960 | 39.4200 |
| data_changes | 0 | globalTest_maxDrop | 0.8560 | 0.5400 |
| data_changes | 0 | globalTest_afterMean | 39.9650 | 39.7920 |
| data_changes | 0 | globalTest_afterStd | 0.7714 | 0.5588 |
| data_changes | 1 | clusterTest_before | 88.4640 | 87.8440 |
| data_changes | 1 | clusterTest_maxDrop | 16.8640 | 3.0440 |
| data_changes | 1 | clusterTest_afterMean | 85.8300 | 87.6000 |
| data_changes | 1 | clusterTest_afterStd | 5.1779 | 1.0838 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.2320 | 43.9220 |
| data_changes | 1 | globalTest_maxDrop | 8.4320 | 1.5220 |
| data_changes | 1 | globalTest_afterMean | 42.9150 | 43.8000 |
| data_changes | 1 | globalTest_afterStd | 2.5889 | 0.5419 |
