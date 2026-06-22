# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 89.6240 | 89.0540 |
| membership_only | 0 | clusterTest_maxDrop | -0.1760 | -0.0660 |
| membership_only | 0 | clusterTest_afterMean | 90.0700 | 89.5080 |
| membership_only | 0 | clusterTest_afterStd | 0.2231 | 0.1749 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 44.8120 | 44.5270 |
| membership_only | 0 | globalTest_maxDrop | -0.0880 | -0.0330 |
| membership_only | 0 | globalTest_afterMean | 45.0350 | 44.7640 |
| membership_only | 0 | globalTest_afterStd | 0.1116 | 0.0983 |
| membership_only | 1 | clusterTest_before | 95.2960 | 95.1040 |
| membership_only | 1 | clusterTest_maxDrop | 34.5960 | 34.3840 |
| membership_only | 1 | clusterTest_afterMean | 81.8340 | 81.9660 |
| membership_only | 1 | clusterTest_afterStd | 12.6430 | 12.4433 |
| membership_only | 1 | clusterTest_recovery | 6 | 12 |
| membership_only | 1 | globalTest_before | 47.6480 | 47.5520 |
| membership_only | 1 | globalTest_maxDrop | 1.3780 | 0.8320 |
| membership_only | 1 | globalTest_afterMean | 64.2420 | 66.7770 |
| membership_only | 1 | globalTest_afterStd | 12.1578 | 11.4447 |
| data_changes | 0 | clusterTest_before | 89.6240 | 89.0540 |
| data_changes | 0 | clusterTest_maxDrop | -0.1760 | -0.0060 |
| data_changes | 0 | clusterTest_afterMean | 90.0700 | 89.4280 |
| data_changes | 0 | clusterTest_afterStd | 0.2231 | 0.2109 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 44.8120 | 44.5270 |
| data_changes | 0 | globalTest_maxDrop | -0.0880 | -0.0030 |
| data_changes | 0 | globalTest_afterMean | 45.0350 | 45.6690 |
| data_changes | 0 | globalTest_afterStd | 0.1116 | 2.1924 |
| data_changes | 1 | clusterTest_before | 95.2960 | 95.1040 |
| data_changes | 1 | clusterTest_maxDrop | 1.1760 | 0.4640 |
| data_changes | 1 | clusterTest_afterMean | 94.9780 | 95.1400 |
| data_changes | 1 | clusterTest_afterStd | 0.3963 | 0.2420 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.6480 | 47.5520 |
| data_changes | 1 | globalTest_maxDrop | 0.5880 | 0.2320 |
| data_changes | 1 | globalTest_afterMean | 47.4890 | 47.5920 |
| data_changes | 1 | globalTest_afterStd | 0.1982 | 0.1359 |
