# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.9103 | 98.8869 |
| membership_only | 0 | clusterTest_maxDrop | -0.1362 | -0.0428 |
| membership_only | 0 | clusterTest_afterMean | 99.1243 | 99.0893 |
| membership_only | 0 | clusterTest_afterStd | 0.0515 | 0.0891 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.8300 | 50.8180 |
| membership_only | 0 | globalTest_maxDrop | -0.0700 | -0.0620 |
| membership_only | 0 | globalTest_afterMean | 50.9400 | 51.0230 |
| membership_only | 0 | globalTest_afterStd | 0.0265 | 0.1365 |
| membership_only | 1 | clusterTest_before | 98.2555 | 98.0395 |
| membership_only | 1 | clusterTest_maxDrop | 57.1734 | 48.8109 |
| membership_only | 1 | clusterTest_afterMean | 89.4055 | 87.8667 |
| membership_only | 1 | clusterTest_afterStd | 16.5715 | 16.3178 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.7620 | 47.6570 |
| membership_only | 1 | globalTest_maxDrop | 0.3620 | 0.2470 |
| membership_only | 1 | globalTest_afterMean | 76.8640 | 78.1960 |
| membership_only | 1 | globalTest_afterStd | 17.2384 | 15.2089 |
| data_changes | 0 | clusterTest_before | 98.9103 | 98.8869 |
| data_changes | 0 | clusterTest_maxDrop | -0.1362 | -0.0428 |
| data_changes | 0 | clusterTest_afterMean | 99.1243 | 99.0757 |
| data_changes | 0 | clusterTest_afterStd | 0.0515 | 0.0910 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.8300 | 50.8180 |
| data_changes | 0 | globalTest_maxDrop | -0.0700 | -0.0920 |
| data_changes | 0 | globalTest_afterMean | 50.9400 | 51.8250 |
| data_changes | 0 | globalTest_afterStd | 0.0265 | 1.2998 |
| data_changes | 1 | clusterTest_before | 98.2555 | 98.0395 |
| data_changes | 1 | clusterTest_maxDrop | 1.0739 | 0.4464 |
| data_changes | 1 | clusterTest_afterMean | 97.9510 | 97.9572 |
| data_changes | 1 | clusterTest_afterStd | 0.3280 | 0.1847 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.7620 | 47.6570 |
| data_changes | 1 | globalTest_maxDrop | 0.5220 | 0.2170 |
| data_changes | 1 | globalTest_afterMean | 47.6140 | 47.6170 |
| data_changes | 1 | globalTest_afterStd | 0.1594 | 0.0898 |
