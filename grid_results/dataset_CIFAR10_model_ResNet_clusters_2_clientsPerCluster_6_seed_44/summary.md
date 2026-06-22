# Configuration Summary

- **dataset**: CIFAR-10
- **model**: ResNet
- **num_clusters**: 2
- **clients_per_cluster**: 6
- **total_clients**: 12
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 70.8240 | 70.2860 |
| membership_only | 0 | clusterTest_maxDrop | 0.9640 | 4.5860 |
| membership_only | 0 | clusterTest_afterMean | 70.6760 | 68.7880 |
| membership_only | 0 | clusterTest_afterStd | 0.3358 | 1.9306 |
| membership_only | 0 | clusterTest_recovery | 0 | 6 |
| membership_only | 0 | globalTest_before | 35.4120 | 35.1430 |
| membership_only | 0 | globalTest_maxDrop | 0.4820 | 2.2930 |
| membership_only | 0 | globalTest_afterMean | 35.3380 | 34.3940 |
| membership_only | 0 | globalTest_afterStd | 0.1679 | 0.9653 |
| membership_only | 1 | clusterTest_before | 79.6180 | 78.7020 |
| membership_only | 1 | clusterTest_maxDrop | 79.6180 | 78.7020 |
| membership_only | 1 | clusterTest_afterMean | 38.8120 | 40.2320 |
| membership_only | 1 | clusterTest_afterStd | 37.9033 | 36.0263 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 39.8090 | 39.3510 |
| membership_only | 1 | globalTest_maxDrop | 15.7090 | 12.1510 |
| membership_only | 1 | globalTest_afterMean | 32.3340 | 34.3780 |
| membership_only | 1 | globalTest_afterStd | 6.2352 | 4.8978 |
| data_changes | 0 | clusterTest_before | 70.8240 | 70.2860 |
| data_changes | 0 | clusterTest_maxDrop | 0.9640 | 5.6460 |
| data_changes | 0 | clusterTest_afterMean | 70.6760 | 68.3560 |
| data_changes | 0 | clusterTest_afterStd | 0.3358 | 2.0413 |
| data_changes | 0 | clusterTest_recovery | 0 | 7 |
| data_changes | 0 | globalTest_before | 35.4120 | 35.1430 |
| data_changes | 0 | globalTest_maxDrop | 0.4820 | 2.8230 |
| data_changes | 0 | globalTest_afterMean | 35.3380 | 34.1850 |
| data_changes | 0 | globalTest_afterStd | 0.1679 | 1.0177 |
| data_changes | 1 | clusterTest_before | 79.6180 | 78.7020 |
| data_changes | 1 | clusterTest_maxDrop | 17.9580 | 8.9420 |
| data_changes | 1 | clusterTest_afterMean | 76.6960 | 77.8400 |
| data_changes | 1 | clusterTest_afterStd | 5.5986 | 3.0165 |
| data_changes | 1 | clusterTest_recovery | 3 | 2 |
| data_changes | 1 | globalTest_before | 39.8090 | 39.3510 |
| data_changes | 1 | globalTest_maxDrop | 8.9790 | 4.4710 |
| data_changes | 1 | globalTest_afterMean | 38.3480 | 38.9200 |
| data_changes | 1 | globalTest_afterStd | 2.7993 | 1.5083 |
