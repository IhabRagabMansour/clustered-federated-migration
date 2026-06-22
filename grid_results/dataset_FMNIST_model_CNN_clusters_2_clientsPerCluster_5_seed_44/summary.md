# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.4140 | 89.9420 |
| membership_only | 0 | clusterTest_maxDrop | 0.0940 | 0.4620 |
| membership_only | 0 | clusterTest_afterMean | 90.6940 | 90.0980 |
| membership_only | 0 | clusterTest_afterStd | 0.2198 | 0.2918 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.2070 | 44.9710 |
| membership_only | 0 | globalTest_maxDrop | 0.0470 | 0.2310 |
| membership_only | 0 | globalTest_afterMean | 45.3470 | 45.0510 |
| membership_only | 0 | globalTest_afterStd | 0.1099 | 0.1473 |
| membership_only | 1 | clusterTest_before | 95.9180 | 95.8460 |
| membership_only | 1 | clusterTest_maxDrop | 36.9580 | 29.4860 |
| membership_only | 1 | clusterTest_afterMean | 82.1300 | 82.9700 |
| membership_only | 1 | clusterTest_afterStd | 13.5156 | 11.7529 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.9590 | 47.9230 |
| membership_only | 1 | globalTest_maxDrop | -0.2210 | -5.7470 |
| membership_only | 1 | globalTest_afterMean | 66.1290 | 69.6570 |
| membership_only | 1 | globalTest_afterStd | 12.0251 | 10.3322 |
| data_changes | 0 | clusterTest_before | 90.4140 | 89.9420 |
| data_changes | 0 | clusterTest_maxDrop | 0.0940 | 0.4220 |
| data_changes | 0 | clusterTest_afterMean | 90.6940 | 90.0440 |
| data_changes | 0 | clusterTest_afterStd | 0.2198 | 0.3010 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.2070 | 44.9710 |
| data_changes | 0 | globalTest_maxDrop | 0.0470 | 0.2110 |
| data_changes | 0 | globalTest_afterMean | 45.3470 | 46.4940 |
| data_changes | 0 | globalTest_afterStd | 0.1099 | 3.4163 |
| data_changes | 1 | clusterTest_before | 95.9180 | 95.8460 |
| data_changes | 1 | clusterTest_maxDrop | 2.2780 | 0.6460 |
| data_changes | 1 | clusterTest_afterMean | 95.4300 | 95.8740 |
| data_changes | 1 | clusterTest_afterStd | 0.6992 | 0.2679 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.9590 | 47.9230 |
| data_changes | 1 | globalTest_maxDrop | 1.1390 | 0.3230 |
| data_changes | 1 | globalTest_afterMean | 47.7150 | 47.9910 |
| data_changes | 1 | globalTest_afterStd | 0.3496 | 0.1860 |
