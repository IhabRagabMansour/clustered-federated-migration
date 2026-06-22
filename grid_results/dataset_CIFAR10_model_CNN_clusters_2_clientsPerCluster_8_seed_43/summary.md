# Configuration Summary

- **dataset**: CIFAR-10
- **model**: CNN
- **num_clusters**: 2
- **clients_per_cluster**: 8
- **total_clients**: 16
- **seed**: 43
- **migration_round**: 40
- **num_migrants**: 3

| submode | cluster | metric | Case A | Case B |
|---|---:|---|---:|---:|
| membership_only | 0 | clusterTest_before | 80.8400 | 80.2520 |
| membership_only | 0 | clusterTest_maxDrop | 1.8800 | 1.4320 |
| membership_only | 0 | clusterTest_afterMean | 81.4920 | 81.3700 |
| membership_only | 0 | clusterTest_afterStd | 1.1475 | 0.9608 |
| membership_only | 0 | clusterTest_recovery | 1 | 1 |
| membership_only | 0 | globalTest_before | 40.4200 | 40.1260 |
| membership_only | 0 | globalTest_maxDrop | 0.9400 | 0.7160 |
| membership_only | 0 | globalTest_afterMean | 40.7460 | 40.6850 |
| membership_only | 0 | globalTest_afterStd | 0.5738 | 0.4804 |
| membership_only | 1 | clusterTest_before | 88.7700 | 88.4240 |
| membership_only | 1 | clusterTest_maxDrop | 72.9900 | 74.1840 |
| membership_only | 1 | clusterTest_afterMean | 60.7280 | 55.8240 |
| membership_only | 1 | clusterTest_afterStd | 27.0752 | 31.3169 |
| membership_only | 1 | clusterTest_recovery | 6 | 6 |
| membership_only | 1 | globalTest_before | 44.3850 | 44.2120 |
| membership_only | 1 | globalTest_maxDrop | 3.1650 | 7.4020 |
| membership_only | 1 | globalTest_afterMean | 46.0470 | 44.8450 |
| membership_only | 1 | globalTest_afterStd | 4.5289 | 5.2115 |
| data_changes | 0 | clusterTest_before | 80.8400 | 80.2520 |
| data_changes | 0 | clusterTest_maxDrop | 1.8800 | 1.2520 |
| data_changes | 0 | clusterTest_afterMean | 81.4920 | 81.3900 |
| data_changes | 0 | clusterTest_afterStd | 1.1475 | 0.9457 |
| data_changes | 0 | clusterTest_recovery | 1 | 1 |
| data_changes | 0 | globalTest_before | 40.4200 | 40.1260 |
| data_changes | 0 | globalTest_maxDrop | 0.9400 | 0.6260 |
| data_changes | 0 | globalTest_afterMean | 40.7460 | 40.6950 |
| data_changes | 0 | globalTest_afterStd | 0.5738 | 0.4729 |
| data_changes | 1 | clusterTest_before | 88.7700 | 88.4240 |
| data_changes | 1 | clusterTest_maxDrop | 3.9100 | 2.8040 |
| data_changes | 1 | clusterTest_afterMean | 87.8180 | 88.3360 |
| data_changes | 1 | clusterTest_afterStd | 1.7343 | 1.1558 |
| data_changes | 1 | clusterTest_recovery | 2 | 1 |
| data_changes | 1 | globalTest_before | 44.3850 | 44.2120 |
| data_changes | 1 | globalTest_maxDrop | 1.9550 | 1.4020 |
| data_changes | 1 | globalTest_afterMean | 43.9090 | 44.1680 |
| data_changes | 1 | globalTest_afterStd | 0.8671 | 0.5779 |
