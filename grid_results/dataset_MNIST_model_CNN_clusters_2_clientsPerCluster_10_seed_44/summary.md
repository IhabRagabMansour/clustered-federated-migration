# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 10
- **total_clients**: 20
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.5445 | 98.5153 |
| membership_only | 0 | clusterTest_maxDrop | -0.1518 | -0.1810 |
| membership_only | 0 | clusterTest_afterMean | 98.8305 | 98.8227 |
| membership_only | 0 | clusterTest_afterStd | 0.0776 | 0.0989 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.6420 | 50.6270 |
| membership_only | 0 | globalTest_maxDrop | -0.0780 | -0.0930 |
| membership_only | 0 | globalTest_afterMean | 50.7890 | 50.8090 |
| membership_only | 0 | globalTest_afterStd | 0.0399 | 0.0677 |
| membership_only | 1 | clusterTest_before | 97.6075 | 97.3689 |
| membership_only | 1 | clusterTest_maxDrop | 36.2621 | 37.6486 |
| membership_only | 1 | clusterTest_afterMean | 92.7217 | 90.4073 |
| membership_only | 1 | clusterTest_afterStd | 10.5434 | 11.7083 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.4470 | 47.3310 |
| membership_only | 1 | globalTest_maxDrop | 0.4770 | 0.5010 |
| membership_only | 1 | globalTest_afterMean | 76.5620 | 77.2460 |
| membership_only | 1 | globalTest_afterStd | 16.7912 | 15.5154 |
| data_changes | 0 | clusterTest_before | 98.5445 | 98.5153 |
| data_changes | 0 | clusterTest_maxDrop | -0.2102 | -0.2199 |
| data_changes | 0 | clusterTest_afterMean | 98.8539 | 98.8052 |
| data_changes | 0 | clusterTest_afterStd | 0.0587 | 0.0531 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.6420 | 50.6270 |
| data_changes | 0 | globalTest_maxDrop | -0.1080 | -0.1330 |
| data_changes | 0 | globalTest_afterMean | 50.8010 | 51.1870 |
| data_changes | 0 | globalTest_afterStd | 0.0301 | 0.7319 |
| data_changes | 1 | clusterTest_before | 97.6075 | 97.3689 |
| data_changes | 1 | clusterTest_maxDrop | 0.7344 | 0.3724 |
| data_changes | 1 | clusterTest_afterMean | 97.5684 | 97.5005 |
| data_changes | 1 | clusterTest_afterStd | 0.3681 | 0.2857 |
| data_changes | 1 | clusterTest_recovery | 0 | 0 |
| data_changes | 1 | globalTest_before | 47.4470 | 47.3310 |
| data_changes | 1 | globalTest_maxDrop | 0.3570 | 0.1810 |
| data_changes | 1 | globalTest_afterMean | 47.4280 | 47.3950 |
| data_changes | 1 | globalTest_afterStd | 0.1789 | 0.1389 |
