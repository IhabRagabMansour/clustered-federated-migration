# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 9
- **total_clients**: 18
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 98.8169 | 98.7858 |
| membership_only | 0 | clusterTest_maxDrop | -0.1129 | -0.0856 |
| membership_only | 0 | clusterTest_afterMean | 99.0212 | 98.9842 |
| membership_only | 0 | clusterTest_afterStd | 0.0578 | 0.0556 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.7820 | 50.7670 |
| membership_only | 0 | globalTest_maxDrop | -0.0580 | -0.0630 |
| membership_only | 0 | globalTest_afterMean | 50.8870 | 50.9720 |
| membership_only | 0 | globalTest_afterStd | 0.0297 | 0.1950 |
| membership_only | 1 | clusterTest_before | 97.8708 | 97.6713 |
| membership_only | 1 | clusterTest_maxDrop | 52.6126 | 46.9821 |
| membership_only | 1 | clusterTest_afterMean | 90.4937 | 88.6114 |
| membership_only | 1 | clusterTest_afterStd | 15.2548 | 14.8339 |
| membership_only | 1 | clusterTest_recovery | 2 | 2 |
| membership_only | 1 | globalTest_before | 47.5750 | 47.4780 |
| membership_only | 1 | globalTest_maxDrop | 0.2650 | 0.2980 |
| membership_only | 1 | globalTest_afterMean | 76.8700 | 78.0840 |
| membership_only | 1 | globalTest_afterStd | 17.1029 | 14.8749 |
| data_changes | 0 | clusterTest_before | 98.8169 | 98.7858 |
| data_changes | 0 | clusterTest_maxDrop | -0.0934 | 0.0506 |
| data_changes | 0 | clusterTest_afterMean | 99.0056 | 98.9531 |
| data_changes | 0 | clusterTest_afterStd | 0.0660 | 0.1110 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.7820 | 50.7670 |
| data_changes | 0 | globalTest_maxDrop | -0.0480 | -0.0430 |
| data_changes | 0 | globalTest_afterMean | 50.8790 | 51.4730 |
| data_changes | 0 | globalTest_afterStd | 0.0339 | 1.0456 |
| data_changes | 1 | clusterTest_before | 97.8708 | 97.6713 |
| data_changes | 1 | clusterTest_maxDrop | 1.2446 | 0.7159 |
| data_changes | 1 | clusterTest_afterMean | 97.7042 | 97.7042 |
| data_changes | 1 | clusterTest_afterStd | 0.4187 | 0.3144 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.5750 | 47.4780 |
| data_changes | 1 | globalTest_maxDrop | 0.6050 | 0.3480 |
| data_changes | 1 | globalTest_afterMean | 47.4940 | 47.4940 |
| data_changes | 1 | globalTest_afterStd | 0.2035 | 0.1529 |
