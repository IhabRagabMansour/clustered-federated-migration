# Configuration Summary

- **dataset**: F-MNIST
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 3
- **total_clients**: 6
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 2

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 91.5340 | 91.1000 |
| membership_only | 0 | clusterTest_maxDrop | 0.7740 | 1.4800 |
| membership_only | 0 | clusterTest_afterMean | 91.7080 | 90.9580 |
| membership_only | 0 | clusterTest_afterStd | 0.5615 | 0.7739 |
| membership_only | 0 | clusterTest_recovery | 0 | 7 |
| membership_only | 0 | globalTest_before | 45.7670 | 45.5500 |
| membership_only | 0 | globalTest_maxDrop | 0.3870 | 0.7400 |
| membership_only | 0 | globalTest_afterMean | 45.8540 | 45.4790 |
| membership_only | 0 | globalTest_afterStd | 0.2808 | 0.3870 |
| membership_only | 1 | clusterTest_before | 96.9660 | 96.7120 |
| membership_only | 1 | clusterTest_maxDrop | 29.7660 | 27.9320 |
| membership_only | 1 | clusterTest_afterMean | 84.5220 | 84.3820 |
| membership_only | 1 | clusterTest_afterStd | 11.7176 | 10.9462 |
| membership_only | 1 | clusterTest_recovery | 4 | 4 |
| membership_only | 1 | globalTest_before | 48.4830 | 48.3560 |
| membership_only | 1 | globalTest_maxDrop | -8.4570 | -11.6840 |
| membership_only | 1 | globalTest_afterMean | 70.1710 | 72.4740 |
| membership_only | 1 | globalTest_afterStd | 10.5698 | 9.7535 |
| data_changes | 0 | clusterTest_before | 91.5340 | 91.1000 |
| data_changes | 0 | clusterTest_maxDrop | 0.7740 | 1.3000 |
| data_changes | 0 | clusterTest_afterMean | 91.7080 | 90.8380 |
| data_changes | 0 | clusterTest_afterStd | 0.5615 | 0.7187 |
| data_changes | 0 | clusterTest_recovery | 0 | 9 |
| data_changes | 0 | globalTest_before | 45.7670 | 45.5500 |
| data_changes | 0 | globalTest_maxDrop | 0.3870 | 0.6400 |
| data_changes | 0 | globalTest_afterMean | 45.8540 | 46.4520 |
| data_changes | 0 | globalTest_afterStd | 0.2808 | 2.0670 |
| data_changes | 1 | clusterTest_before | 96.9660 | 96.7120 |
| data_changes | 1 | clusterTest_maxDrop | 4.0860 | 0.6120 |
| data_changes | 1 | clusterTest_afterMean | 95.9540 | 96.6820 |
| data_changes | 1 | clusterTest_afterStd | 1.1105 | 0.2681 |
| data_changes | 1 | clusterTest_recovery | 3 | 0 |
| data_changes | 1 | globalTest_before | 48.4830 | 48.3560 |
| data_changes | 1 | globalTest_maxDrop | 2.0430 | 0.3060 |
| data_changes | 1 | globalTest_afterMean | 47.9770 | 48.3410 |
| data_changes | 1 | globalTest_afterStd | 0.5552 | 0.1340 |
