# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.3384 | 99.2781 |
| membership_only | 0 | clusterTest_maxDrop | -0.0778 | -0.0409 |
| membership_only | 0 | clusterTest_afterMean | 99.5057 | 99.4571 |
| membership_only | 0 | clusterTest_afterStd | 0.0462 | 0.0859 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.0500 | 51.0190 |
| membership_only | 0 | globalTest_maxDrop | -0.0400 | -0.0210 |
| membership_only | 0 | globalTest_afterMean | 51.1360 | 51.3460 |
| membership_only | 0 | globalTest_afterStd | 0.0237 | 0.4341 |
| membership_only | 1 | clusterTest_before | 98.7163 | 98.6711 |
| membership_only | 1 | clusterTest_maxDrop | 79.3376 | 72.7093 |
| membership_only | 1 | clusterTest_afterMean | 81.7404 | 81.4380 |
| membership_only | 1 | clusterTest_afterStd | 24.6264 | 24.1822 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.9860 | 47.9640 |
| membership_only | 1 | globalTest_maxDrop | 0.3160 | 0.2340 |
| membership_only | 1 | globalTest_afterMean | 72.8760 | 75.6990 |
| membership_only | 1 | globalTest_afterStd | 16.7086 | 15.1324 |
| data_changes | 0 | clusterTest_before | 99.3384 | 99.2781 |
| data_changes | 0 | clusterTest_maxDrop | -0.1168 | 0.1926 |
| data_changes | 0 | clusterTest_afterMean | 99.5116 | 99.4162 |
| data_changes | 0 | clusterTest_afterStd | 0.0412 | 0.1373 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.0500 | 51.0190 |
| data_changes | 0 | globalTest_maxDrop | -0.0600 | -0.1010 |
| data_changes | 0 | globalTest_afterMean | 51.1390 | 52.4280 |
| data_changes | 0 | globalTest_afterStd | 0.0212 | 2.1366 |
| data_changes | 1 | clusterTest_before | 98.7163 | 98.6711 |
| data_changes | 1 | clusterTest_maxDrop | 4.9085 | 0.8928 |
| data_changes | 1 | clusterTest_afterMean | 97.9387 | 98.5127 |
| data_changes | 1 | clusterTest_afterStd | 1.4075 | 0.2859 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.9860 | 47.9640 |
| data_changes | 1 | globalTest_maxDrop | 2.3860 | 0.4340 |
| data_changes | 1 | globalTest_afterMean | 47.6080 | 47.8870 |
| data_changes | 1 | globalTest_afterStd | 0.6842 | 0.1390 |
