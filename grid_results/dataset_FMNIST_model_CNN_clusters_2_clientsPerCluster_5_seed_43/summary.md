# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 90.4440 | 89.8900 |
| membership_only | 0 | clusterTest_maxDrop | -0.1160 | -0.0500 |
| membership_only | 0 | clusterTest_afterMean | 90.9220 | 90.4620 |
| membership_only | 0 | clusterTest_afterStd | 0.2133 | 0.2478 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 45.2220 | 44.9450 |
| membership_only | 0 | globalTest_maxDrop | -0.0580 | -0.0250 |
| membership_only | 0 | globalTest_afterMean | 45.4610 | 45.2320 |
| membership_only | 0 | globalTest_afterStd | 0.1066 | 0.1255 |
| membership_only | 1 | clusterTest_before | 95.9860 | 95.8180 |
| membership_only | 1 | clusterTest_maxDrop | 36.8260 | 31.2580 |
| membership_only | 1 | clusterTest_afterMean | 82.5320 | 82.8680 |
| membership_only | 1 | clusterTest_afterStd | 13.2276 | 12.0230 |
| membership_only | 1 | clusterTest_recovery | 6 | 4 |
| membership_only | 1 | globalTest_before | 47.9930 | 47.9090 |
| membership_only | 1 | globalTest_maxDrop | 0.5130 | -3.8810 |
| membership_only | 1 | globalTest_afterMean | 66.4530 | 69.3570 |
| membership_only | 1 | globalTest_afterStd | 11.9177 | 10.5807 |
| data_changes | 0 | clusterTest_before | 90.4440 | 89.8900 |
| data_changes | 0 | clusterTest_maxDrop | -0.1160 | 0.0900 |
| data_changes | 0 | clusterTest_afterMean | 90.9220 | 90.3340 |
| data_changes | 0 | clusterTest_afterStd | 0.2133 | 0.2520 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 45.2220 | 44.9450 |
| data_changes | 0 | globalTest_maxDrop | -0.0580 | -0.1150 |
| data_changes | 0 | globalTest_afterMean | 45.4610 | 46.1380 |
| data_changes | 0 | globalTest_afterStd | 0.1066 | 2.1008 |
| data_changes | 1 | clusterTest_before | 95.9860 | 95.8180 |
| data_changes | 1 | clusterTest_maxDrop | 3.0860 | 0.6180 |
| data_changes | 1 | clusterTest_afterMean | 95.2560 | 95.8100 |
| data_changes | 1 | clusterTest_afterStd | 0.8943 | 0.2903 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 47.9930 | 47.9090 |
| data_changes | 1 | globalTest_maxDrop | 1.5430 | 0.3090 |
| data_changes | 1 | globalTest_afterMean | 47.6280 | 47.9060 |
| data_changes | 1 | globalTest_afterStd | 0.4471 | 0.1458 |
