# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 44
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 91.8940 | 91.2840 |
| membership_only | 0 | clusterTest_maxDrop | 1.6940 | 4.1640 |
| membership_only | 0 | clusterTest_afterMean | 91.7560 | 90.7940 |
| membership_only | 0 | clusterTest_afterStd | 0.6185 | 1.2731 |
| membership_only | 0 | clusterTest_recovery | 7 | 7 |
| membership_only | 0 | globalTest_before | 45.9470 | 45.6420 |
| membership_only | 0 | globalTest_maxDrop | 0.8470 | 2.0820 |
| membership_only | 0 | globalTest_afterMean | 45.8780 | 45.3970 |
| membership_only | 0 | globalTest_afterStd | 0.3093 | 0.6366 |
| membership_only | 1 | clusterTest_before | 96.8520 | 96.7100 |
| membership_only | 1 | clusterTest_maxDrop | 28.9520 | 26.7700 |
| membership_only | 1 | clusterTest_afterMean | 84.8820 | 84.6980 |
| membership_only | 1 | clusterTest_afterStd | 11.5865 | 10.9647 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 48.4260 | 48.3550 |
| membership_only | 1 | globalTest_maxDrop | -5.2340 | -10.8950 |
| membership_only | 1 | globalTest_afterMean | 70.0330 | 72.3690 |
| membership_only | 1 | globalTest_afterStd | 11.2614 | 9.7538 |
| data_changes | 0 | clusterTest_before | 91.8940 | 91.2840 |
| data_changes | 0 | clusterTest_maxDrop | 1.6940 | 6.4040 |
| data_changes | 0 | clusterTest_afterMean | 91.7560 | 90.4980 |
| data_changes | 0 | clusterTest_afterStd | 0.6185 | 1.9467 |
| data_changes | 0 | clusterTest_recovery | 7 | 7 |
| data_changes | 0 | globalTest_before | 45.9470 | 45.6420 |
| data_changes | 0 | globalTest_maxDrop | 0.8470 | 3.2020 |
| data_changes | 0 | globalTest_afterMean | 45.8780 | 46.0540 |
| data_changes | 0 | globalTest_afterStd | 0.3093 | 2.5695 |
| data_changes | 1 | clusterTest_before | 96.8520 | 96.7100 |
| data_changes | 1 | clusterTest_maxDrop | 2.8920 | 0.6100 |
| data_changes | 1 | clusterTest_afterMean | 96.1380 | 96.6460 |
| data_changes | 1 | clusterTest_afterStd | 0.7821 | 0.2713 |
| data_changes | 1 | clusterTest_recovery | 1 | 0 |
| data_changes | 1 | globalTest_before | 48.4260 | 48.3550 |
| data_changes | 1 | globalTest_maxDrop | 1.4460 | 0.3050 |
| data_changes | 1 | globalTest_afterMean | 48.0690 | 48.4140 |
| data_changes | 1 | globalTest_afterStd | 0.3910 | 0.2579 |
