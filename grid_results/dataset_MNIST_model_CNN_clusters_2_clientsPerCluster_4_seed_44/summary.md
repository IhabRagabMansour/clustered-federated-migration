# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.5933 | 99.6167 |
| membership_only | 0 | clusterTest_maxDrop | 0.1965 | 0.2004 |
| membership_only | 0 | clusterTest_afterMean | 99.5544 | 99.5797 |
| membership_only | 0 | clusterTest_afterStd | 0.0736 | 0.0901 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.1810 | 51.2660 |
| membership_only | 0 | globalTest_maxDrop | 0.1010 | 0.1260 |
| membership_only | 0 | globalTest_afterMean | 51.1610 | 51.8620 |
| membership_only | 0 | globalTest_afterStd | 0.0378 | 0.7637 |
| membership_only | 1 | clusterTest_before | 98.9426 | 98.8871 |
| membership_only | 1 | clusterTest_maxDrop | 83.0611 | 83.2936 |
| membership_only | 1 | clusterTest_afterMean | 78.5312 | 78.6896 |
| membership_only | 1 | clusterTest_afterStd | 27.5639 | 28.5016 |
| membership_only | 1 | clusterTest_recovery | 4 | 5 |
| membership_only | 1 | globalTest_before | 48.0960 | 48.0690 |
| membership_only | 1 | globalTest_maxDrop | 0.1860 | -8.1110 |
| membership_only | 1 | globalTest_afterMean | 75.6780 | 77.2650 |
| membership_only | 1 | globalTest_afterStd | 14.8371 | 13.7462 |
| data_changes | 0 | clusterTest_before | 99.5933 | 99.6167 |
| data_changes | 0 | clusterTest_maxDrop | 0.1965 | 0.2199 |
| data_changes | 0 | clusterTest_afterMean | 99.5544 | 99.5388 |
| data_changes | 0 | clusterTest_afterStd | 0.0736 | 0.0950 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.1810 | 51.2660 |
| data_changes | 0 | globalTest_maxDrop | 0.1010 | -0.2940 |
| data_changes | 0 | globalTest_afterMean | 51.1610 | 54.4120 |
| data_changes | 0 | globalTest_afterStd | 0.0378 | 3.9590 |
| data_changes | 1 | clusterTest_before | 98.9426 | 98.8871 |
| data_changes | 1 | clusterTest_maxDrop | 4.0033 | 0.8414 |
| data_changes | 1 | clusterTest_afterMean | 98.1958 | 98.7245 |
| data_changes | 1 | clusterTest_afterStd | 1.1265 | 0.2518 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.0960 | 48.0690 |
| data_changes | 1 | globalTest_maxDrop | 1.9460 | 0.4090 |
| data_changes | 1 | globalTest_afterMean | 47.7330 | 47.9900 |
| data_changes | 1 | globalTest_afterStd | 0.5476 | 0.1224 |
