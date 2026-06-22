# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.4260 | 99.4435 |
| membership_only | 0 | clusterTest_maxDrop | 0.0097 | 0.0078 |
| membership_only | 0 | clusterTest_afterMean | 99.5155 | 99.5116 |
| membership_only | 0 | clusterTest_afterStd | 0.0567 | 0.0488 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.0950 | 51.1350 |
| membership_only | 0 | globalTest_maxDrop | 0.0050 | -0.0350 |
| membership_only | 0 | globalTest_afterMean | 51.1410 | 51.6560 |
| membership_only | 0 | globalTest_afterStd | 0.0291 | 0.4815 |
| membership_only | 1 | clusterTest_before | 98.8274 | 98.7328 |
| membership_only | 1 | clusterTest_maxDrop | 68.7101 | 85.8136 |
| membership_only | 1 | clusterTest_afterMean | 82.2362 | 81.0451 |
| membership_only | 1 | clusterTest_afterStd | 23.4543 | 25.9072 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 48.0400 | 47.9940 |
| membership_only | 1 | globalTest_maxDrop | 0.3700 | -0.3860 |
| membership_only | 1 | globalTest_afterMean | 75.5690 | 75.6920 |
| membership_only | 1 | globalTest_afterStd | 16.2750 | 16.6255 |
| data_changes | 0 | clusterTest_before | 99.4260 | 99.4435 |
| data_changes | 0 | clusterTest_maxDrop | 0.0097 | 0.1440 |
| data_changes | 0 | clusterTest_afterMean | 99.5408 | 99.5038 |
| data_changes | 0 | clusterTest_afterStd | 0.0565 | 0.0897 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.0950 | 51.1350 |
| data_changes | 0 | globalTest_maxDrop | 0.0050 | -0.3150 |
| data_changes | 0 | globalTest_afterMean | 51.1540 | 53.5210 |
| data_changes | 0 | globalTest_afterStd | 0.0291 | 2.7911 |
| data_changes | 1 | clusterTest_before | 98.8274 | 98.7328 |
| data_changes | 1 | clusterTest_maxDrop | 3.9292 | 0.6665 |
| data_changes | 1 | clusterTest_afterMean | 98.0539 | 98.5908 |
| data_changes | 1 | clusterTest_afterStd | 1.1181 | 0.1939 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.0400 | 47.9940 |
| data_changes | 1 | globalTest_maxDrop | 1.9100 | 0.3240 |
| data_changes | 1 | globalTest_afterMean | 47.6640 | 47.9250 |
| data_changes | 1 | globalTest_afterStd | 0.5435 | 0.0943 |
