# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 42
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.4902 | 99.4649 |
| membership_only | 0 | clusterTest_maxDrop | -0.0234 | 0.0292 |
| membership_only | 0 | clusterTest_afterMean | 99.5816 | 99.5213 |
| membership_only | 0 | clusterTest_afterStd | 0.0524 | 0.0629 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.1280 | 51.1170 |
| membership_only | 0 | globalTest_maxDrop | -0.0120 | 0.0070 |
| membership_only | 0 | globalTest_afterMean | 51.1750 | 51.3570 |
| membership_only | 0 | globalTest_afterStd | 0.0269 | 0.2977 |
| membership_only | 1 | clusterTest_before | 98.8274 | 98.8397 |
| membership_only | 1 | clusterTest_maxDrop | 74.2851 | 88.5127 |
| membership_only | 1 | clusterTest_afterMean | 78.3522 | 79.3499 |
| membership_only | 1 | clusterTest_afterStd | 26.9952 | 27.3222 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 48.0400 | 48.0460 |
| membership_only | 1 | globalTest_maxDrop | 0.3500 | -0.3040 |
| membership_only | 1 | globalTest_afterMean | 71.9950 | 74.2640 |
| membership_only | 1 | globalTest_afterStd | 15.6357 | 16.7517 |
| data_changes | 0 | clusterTest_before | 99.4902 | 99.4649 |
| data_changes | 0 | clusterTest_maxDrop | -0.0428 | 0.0876 |
| data_changes | 0 | clusterTest_afterMean | 99.6303 | 99.6089 |
| data_changes | 0 | clusterTest_afterStd | 0.0522 | 0.0979 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.1280 | 51.1170 |
| data_changes | 0 | globalTest_maxDrop | -0.0220 | -0.1330 |
| data_changes | 0 | globalTest_afterMean | 51.2000 | 53.2500 |
| data_changes | 0 | globalTest_afterStd | 0.0268 | 2.8940 |
| data_changes | 1 | clusterTest_before | 98.8274 | 98.8397 |
| data_changes | 1 | clusterTest_maxDrop | 4.2378 | 0.9998 |
| data_changes | 1 | clusterTest_afterMean | 98.0436 | 98.5929 |
| data_changes | 1 | clusterTest_afterStd | 1.1849 | 0.2837 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.0400 | 48.0460 |
| data_changes | 1 | globalTest_maxDrop | 2.0600 | 0.4860 |
| data_changes | 1 | globalTest_afterMean | 47.6590 | 47.9260 |
| data_changes | 1 | globalTest_afterStd | 0.5760 | 0.1379 |
