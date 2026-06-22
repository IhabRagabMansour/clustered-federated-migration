# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.8344 | 98.7605 |
| membership_only | 0 | clusterTest_maxDrop | -0.1343 | -0.2277 |
| membership_only | 0 | clusterTest_afterMean | 99.0776 | 99.0776 |
| membership_only | 0 | clusterTest_afterStd | 0.0745 | 0.0652 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.7910 | 50.7530 |
| membership_only | 0 | globalTest_maxDrop | -0.0690 | -0.1370 |
| membership_only | 0 | globalTest_afterMean | 50.9160 | 50.9510 |
| membership_only | 0 | globalTest_afterStd | 0.0383 | 0.0877 |
| membership_only | 1 | clusterTest_before | 97.9490 | 97.6713 |
| membership_only | 1 | clusterTest_maxDrop | 55.9823 | 55.3549 |
| membership_only | 1 | clusterTest_afterMean | 89.9753 | 88.8459 |
| membership_only | 1 | clusterTest_afterStd | 16.2751 | 16.4721 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.6130 | 47.4780 |
| membership_only | 1 | globalTest_maxDrop | 0.2830 | 0.2980 |
| membership_only | 1 | globalTest_afterMean | 76.4080 | 78.1850 |
| membership_only | 1 | globalTest_afterStd | 17.4709 | 15.2262 |
| data_changes | 0 | clusterTest_before | 98.8344 | 98.7605 |
| data_changes | 0 | clusterTest_maxDrop | -0.1537 | -0.1498 |
| data_changes | 0 | clusterTest_afterMean | 99.1010 | 99.0348 |
| data_changes | 0 | clusterTest_afterStd | 0.0727 | 0.0880 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.7910 | 50.7530 |
| data_changes | 0 | globalTest_maxDrop | -0.0790 | -0.0970 |
| data_changes | 0 | globalTest_afterMean | 50.9280 | 51.2850 |
| data_changes | 0 | globalTest_afterStd | 0.0374 | 0.7762 |
| data_changes | 1 | clusterTest_before | 97.9490 | 97.6713 |
| data_changes | 1 | clusterTest_maxDrop | 1.7342 | 0.4896 |
| data_changes | 1 | clusterTest_afterMean | 97.6774 | 97.7515 |
| data_changes | 1 | clusterTest_afterStd | 0.5555 | 0.2795 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.6130 | 47.4780 |
| data_changes | 1 | globalTest_maxDrop | 0.8430 | 0.2380 |
| data_changes | 1 | globalTest_afterMean | 47.4810 | 47.5170 |
| data_changes | 1 | globalTest_afterStd | 0.2700 | 0.1359 |
