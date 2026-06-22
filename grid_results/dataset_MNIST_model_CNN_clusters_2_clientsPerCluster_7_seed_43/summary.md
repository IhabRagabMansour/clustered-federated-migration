# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.2002 | 99.1769 |
| membership_only | 0 | clusterTest_maxDrop | -0.0603 | -0.1226 |
| membership_only | 0 | clusterTest_afterMean | 99.3870 | 99.3579 |
| membership_only | 0 | clusterTest_afterStd | 0.0653 | 0.0557 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.9790 | 50.9670 |
| membership_only | 0 | globalTest_maxDrop | -0.0310 | -0.0630 |
| membership_only | 0 | globalTest_afterMean | 51.0750 | 51.1860 |
| membership_only | 0 | globalTest_afterStd | 0.0335 | 0.2982 |
| membership_only | 1 | clusterTest_before | 98.5312 | 98.4118 |
| membership_only | 1 | clusterTest_maxDrop | 70.0802 | 56.7949 |
| membership_only | 1 | clusterTest_afterMean | 85.5071 | 84.1000 |
| membership_only | 1 | clusterTest_afterStd | 21.7545 | 21.4657 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.8960 | 47.8380 |
| membership_only | 1 | globalTest_maxDrop | 0.2060 | 0.1580 |
| membership_only | 1 | globalTest_afterMean | 75.7990 | 77.1390 |
| membership_only | 1 | globalTest_afterStd | 17.4790 | 14.7665 |
| data_changes | 0 | clusterTest_before | 99.2002 | 99.1769 |
| data_changes | 0 | clusterTest_maxDrop | -0.0798 | -0.0448 |
| data_changes | 0 | clusterTest_afterMean | 99.3656 | 99.3287 |
| data_changes | 0 | clusterTest_afterStd | 0.0516 | 0.0708 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.9790 | 50.9670 |
| data_changes | 0 | globalTest_maxDrop | -0.0410 | -0.0430 |
| data_changes | 0 | globalTest_afterMean | 51.0640 | 52.2290 |
| data_changes | 0 | globalTest_afterStd | 0.0265 | 2.1904 |
| data_changes | 1 | clusterTest_before | 98.5312 | 98.4118 |
| data_changes | 1 | clusterTest_maxDrop | 2.8718 | 0.6748 |
| data_changes | 1 | clusterTest_afterMean | 97.9408 | 98.3460 |
| data_changes | 1 | clusterTest_afterStd | 0.8025 | 0.2857 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.8960 | 47.8380 |
| data_changes | 1 | globalTest_maxDrop | 1.3960 | 0.3280 |
| data_changes | 1 | globalTest_afterMean | 47.6090 | 47.8060 |
| data_changes | 1 | globalTest_afterStd | 0.3901 | 0.1389 |
