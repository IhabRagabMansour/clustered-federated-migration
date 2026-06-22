# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 7
- **total_clients**: 14
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.1419 | 99.1243 |
| membership_only | 0 | clusterTest_maxDrop | -0.0214 | -0.0389 |
| membership_only | 0 | clusterTest_afterMean | 99.3053 | 99.3053 |
| membership_only | 0 | clusterTest_afterStd | 0.0669 | 0.0844 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 50.9490 | 50.9470 |
| membership_only | 0 | globalTest_maxDrop | -0.0110 | -0.0530 |
| membership_only | 0 | globalTest_afterMean | 51.0330 | 51.2290 |
| membership_only | 0 | globalTest_afterStd | 0.0344 | 0.2134 |
| membership_only | 1 | clusterTest_before | 98.5188 | 98.2740 |
| membership_only | 1 | clusterTest_maxDrop | 65.5009 | 61.3063 |
| membership_only | 1 | clusterTest_afterMean | 86.4616 | 84.9578 |
| membership_only | 1 | clusterTest_afterStd | 19.5422 | 20.2157 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 47.8900 | 47.7710 |
| membership_only | 1 | globalTest_maxDrop | 0.4800 | 0.3010 |
| membership_only | 1 | globalTest_afterMean | 76.3170 | 77.4010 |
| membership_only | 1 | globalTest_afterStd | 17.0647 | 15.5791 |
| data_changes | 0 | clusterTest_before | 99.1419 | 99.1243 |
| data_changes | 0 | clusterTest_maxDrop | -0.0992 | 0.0584 |
| data_changes | 0 | clusterTest_afterMean | 99.3131 | 99.2586 |
| data_changes | 0 | clusterTest_afterStd | 0.0603 | 0.1133 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 50.9490 | 50.9470 |
| data_changes | 0 | globalTest_maxDrop | -0.0510 | -0.2030 |
| data_changes | 0 | globalTest_afterMean | 51.0370 | 52.4790 |
| data_changes | 0 | globalTest_afterStd | 0.0310 | 1.6947 |
| data_changes | 1 | clusterTest_before | 98.5188 | 98.2740 |
| data_changes | 1 | clusterTest_maxDrop | 1.9955 | 0.5575 |
| data_changes | 1 | clusterTest_afterMean | 98.0086 | 98.1958 |
| data_changes | 1 | clusterTest_afterStd | 0.5551 | 0.2378 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 47.8900 | 47.7710 |
| data_changes | 1 | globalTest_maxDrop | 0.9700 | 0.2710 |
| data_changes | 1 | globalTest_afterMean | 47.6420 | 47.7330 |
| data_changes | 1 | globalTest_afterStd | 0.2698 | 0.1156 |
