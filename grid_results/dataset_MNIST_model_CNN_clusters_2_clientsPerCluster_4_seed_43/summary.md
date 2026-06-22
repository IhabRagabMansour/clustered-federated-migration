# Configuration Summary

- **dataset**: MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 4
- **total_clients**: 8
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 99.6536 | 99.6069 |
| membership_only | 0 | clusterTest_maxDrop | 0.0623 | -0.0039 |
| membership_only | 0 | clusterTest_afterMean | 99.7101 | 99.6653 |
| membership_only | 0 | clusterTest_afterStd | 0.0630 | 0.0367 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 51.2120 | 51.2230 |
| membership_only | 0 | globalTest_maxDrop | 0.0320 | -0.0070 |
| membership_only | 0 | globalTest_afterMean | 51.2410 | 51.3710 |
| membership_only | 0 | globalTest_afterStd | 0.0324 | 0.1221 |
| membership_only | 1 | clusterTest_before | 98.9858 | 98.9097 |
| membership_only | 1 | clusterTest_maxDrop | 84.5443 | 77.1652 |
| membership_only | 1 | clusterTest_afterMean | 75.5400 | 77.6054 |
| membership_only | 1 | clusterTest_afterStd | 30.9620 | 26.6209 |
| membership_only | 1 | clusterTest_recovery | 4 | 6 |
| membership_only | 1 | globalTest_before | 48.1170 | 48.0800 |
| membership_only | 1 | globalTest_maxDrop | 0.2270 | -10.0500 |
| membership_only | 1 | globalTest_afterMean | 73.2730 | 76.8250 |
| membership_only | 1 | globalTest_afterStd | 15.1595 | 12.9236 |
| data_changes | 0 | clusterTest_before | 99.6536 | 99.6069 |
| data_changes | 0 | clusterTest_maxDrop | 0.0623 | 0.0739 |
| data_changes | 0 | clusterTest_afterMean | 99.7101 | 99.6303 |
| data_changes | 0 | clusterTest_afterStd | 0.0630 | 0.0543 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 51.2120 | 51.2230 |
| data_changes | 0 | globalTest_maxDrop | 0.0320 | -0.1770 |
| data_changes | 0 | globalTest_afterMean | 51.2410 | 54.5860 |
| data_changes | 0 | globalTest_afterStd | 0.0324 | 4.4416 |
| data_changes | 1 | clusterTest_before | 98.9858 | 98.9097 |
| data_changes | 1 | clusterTest_maxDrop | 2.8533 | 1.0080 |
| data_changes | 1 | clusterTest_afterMean | 98.3069 | 98.7184 |
| data_changes | 1 | clusterTest_afterStd | 0.7844 | 0.2874 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 48.1170 | 48.0800 |
| data_changes | 1 | globalTest_maxDrop | 1.3870 | 0.4900 |
| data_changes | 1 | globalTest_afterMean | 47.7870 | 47.9870 |
| data_changes | 1 | globalTest_afterStd | 0.3813 | 0.1397 |
