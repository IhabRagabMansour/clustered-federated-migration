# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 81.6520 | 81.0520 |
| membership_only | 0 | clusterTest_maxDrop | 2.1320 | 2.5520 |
| membership_only | 0 | clusterTest_afterMean | 81.6100 | 81.0740 |
| membership_only | 0 | clusterTest_afterStd | 1.2060 | 1.3264 |
| membership_only | 0 | clusterTest_recovery | 1 | 2 |
| membership_only | 0 | globalTest_before | 40.8260 | 40.5260 |
| membership_only | 0 | globalTest_maxDrop | 1.0660 | 1.2760 |
| membership_only | 0 | globalTest_afterMean | 40.8050 | 40.5370 |
| membership_only | 0 | globalTest_afterStd | 0.6030 | 0.6632 |
| membership_only | 1 | clusterTest_before | 89.0000 | 88.6300 |
| membership_only | 1 | clusterTest_maxDrop | 85.3800 | 85.4700 |
| membership_only | 1 | clusterTest_afterMean | 53.3780 | 51.2320 |
| membership_only | 1 | clusterTest_afterStd | 34.5182 | 35.8160 |
| membership_only | 1 | clusterTest_recovery | 10 | 6 |
| membership_only | 1 | globalTest_before | 44.5000 | 44.3150 |
| membership_only | 1 | globalTest_maxDrop | 9.1800 | 11.6750 |
| membership_only | 1 | globalTest_afterMean | 43.7770 | 43.6730 |
| membership_only | 1 | globalTest_afterStd | 3.4477 | 4.7373 |
| data_changes | 0 | clusterTest_before | 81.6520 | 81.0520 |
| data_changes | 0 | clusterTest_maxDrop | 2.1320 | 2.6120 |
| data_changes | 0 | clusterTest_afterMean | 81.6100 | 81.1580 |
| data_changes | 0 | clusterTest_afterStd | 1.2060 | 1.0802 |
| data_changes | 0 | clusterTest_recovery | 1 | 1 |
| data_changes | 0 | globalTest_before | 40.8260 | 40.5260 |
| data_changes | 0 | globalTest_maxDrop | 1.0660 | 1.3060 |
| data_changes | 0 | globalTest_afterMean | 40.8050 | 40.5790 |
| data_changes | 0 | globalTest_afterStd | 0.6030 | 0.5401 |
| data_changes | 1 | clusterTest_before | 89.0000 | 88.6300 |
| data_changes | 1 | clusterTest_maxDrop | 11.2400 | 1.9900 |
| data_changes | 1 | clusterTest_afterMean | 87.5720 | 88.8180 |
| data_changes | 1 | clusterTest_afterStd | 3.4344 | 1.0578 |
| data_changes | 1 | clusterTest_recovery | 3 | 1 |
| data_changes | 1 | globalTest_before | 44.5000 | 44.3150 |
| data_changes | 1 | globalTest_maxDrop | 5.6200 | 0.9950 |
| data_changes | 1 | globalTest_afterMean | 43.7860 | 44.4090 |
| data_changes | 1 | globalTest_afterStd | 1.7172 | 0.5289 |
