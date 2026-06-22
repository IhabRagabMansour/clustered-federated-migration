# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.6322 | 99.5622 |
| membership_only | 0 | clusterTest_maxDrop | 0.0019 | -0.0097 |
| membership_only | 0 | clusterTest_afterMean | 99.7062 | 99.7023 |
| membership_only | 0 | clusterTest_afterStd | 0.0560 | 0.0628 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.2010 | 51.1860 |
| membership_only | 0 | globalTest_maxDrop | 0.0010 | -0.0140 |
| membership_only | 0 | globalTest_afterMean | 51.2390 | 51.6150 |
| membership_only | 0 | globalTest_afterStd | 0.0288 | 0.4493 |
| membership_only | 1 | clusterTest_before | 98.9940 | 98.9405 |
| membership_only | 1 | clusterTest_maxDrop | 88.0498 | 86.5768 |
| membership_only | 1 | clusterTest_afterMean | 75.3775 | 76.8998 |
| membership_only | 1 | clusterTest_afterStd | 30.6907 | 29.0155 |
| membership_only | 1 | clusterTest_recovery | 6 | 5 |
| membership_only | 1 | globalTest_before | 48.1210 | 48.0950 |
| membership_only | 1 | globalTest_maxDrop | 0.3010 | -5.6450 |
| membership_only | 1 | globalTest_afterMean | 72.8330 | 74.3870 |
| membership_only | 1 | globalTest_afterStd | 15.1390 | 13.8603 |
| data_changes | 0 | clusterTest_before | 99.6322 | 99.5622 |
| data_changes | 0 | clusterTest_maxDrop | 0.0019 | 0.0292 |
| data_changes | 0 | clusterTest_afterMean | 99.7062 | 99.6770 |
| data_changes | 0 | clusterTest_afterStd | 0.0560 | 0.0774 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.2010 | 51.1860 |
| data_changes | 0 | globalTest_maxDrop | 0.0010 | -0.0540 |
| data_changes | 0 | globalTest_afterMean | 51.2390 | 53.8430 |
| data_changes | 0 | globalTest_afterStd | 0.0288 | 3.4296 |
| data_changes | 1 | clusterTest_before | 98.9940 | 98.9405 |
| data_changes | 1 | clusterTest_maxDrop | 3.6227 | 1.0595 |
| data_changes | 1 | clusterTest_afterMean | 98.2452 | 98.7245 |
| data_changes | 1 | clusterTest_afterStd | 1.0076 | 0.2971 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 48.1210 | 48.0950 |
| data_changes | 1 | globalTest_maxDrop | 1.7610 | 0.5150 |
| data_changes | 1 | globalTest_afterMean | 47.7570 | 47.9900 |
| data_changes | 1 | globalTest_afterStd | 0.4898 | 0.1444 |
