# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 5
- **total_clients**: 10
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.4960 | 99.4454 |
| membership_only | 0 | clusterTest_maxDrop | -0.0370 | 0.0097 |
| membership_only | 0 | clusterTest_afterMean | 99.6089 | 99.5777 |
| membership_only | 0 | clusterTest_afterStd | 0.0384 | 0.0657 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.1310 | 51.1280 |
| membership_only | 0 | globalTest_maxDrop | -0.0190 | -0.0320 |
| membership_only | 0 | globalTest_afterMean | 51.1890 | 51.5630 |
| membership_only | 0 | globalTest_afterStd | 0.0197 | 0.4425 |
| membership_only | 1 | clusterTest_before | 98.8212 | 98.7965 |
| membership_only | 1 | clusterTest_maxDrop | 78.9488 | 91.4729 |
| membership_only | 1 | clusterTest_afterMean | 79.2923 | 78.6916 |
| membership_only | 1 | clusterTest_afterStd | 28.6802 | 28.7705 |
| membership_only | 1 | clusterTest_recovery | 2 | 4 |
| membership_only | 1 | globalTest_before | 48.0370 | 48.0250 |
| membership_only | 1 | globalTest_maxDrop | 0.2270 | 0.1650 |
| membership_only | 1 | globalTest_afterMean | 73.5350 | 74.3600 |
| membership_only | 1 | globalTest_afterStd | 16.9528 | 17.1078 |
| data_changes | 0 | clusterTest_before | 99.4960 | 99.4454 |
| data_changes | 0 | clusterTest_maxDrop | -0.0370 | 0.0097 |
| data_changes | 0 | clusterTest_afterMean | 99.6108 | 99.5641 |
| data_changes | 0 | clusterTest_afterStd | 0.0452 | 0.0629 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.1310 | 51.1280 |
| data_changes | 0 | globalTest_maxDrop | -0.0190 | -0.0920 |
| data_changes | 0 | globalTest_afterMean | 51.1900 | 53.6890 |
| data_changes | 0 | globalTest_afterStd | 0.0232 | 3.3495 |
| data_changes | 1 | clusterTest_before | 98.8212 | 98.7965 |
| data_changes | 1 | clusterTest_maxDrop | 2.8739 | 0.9360 |
| data_changes | 1 | clusterTest_afterMean | 98.2041 | 98.6093 |
| data_changes | 1 | clusterTest_afterStd | 0.8245 | 0.2756 |
| data_changes | 1 | clusterTest_recovery | 2 | 0 |
| data_changes | 1 | globalTest_before | 48.0370 | 48.0250 |
| data_changes | 1 | globalTest_maxDrop | 1.3970 | 0.4550 |
| data_changes | 1 | globalTest_afterMean | 47.7370 | 47.9340 |
| data_changes | 1 | globalTest_afterStd | 0.4008 | 0.1340 |
