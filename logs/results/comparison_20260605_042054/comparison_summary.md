# Case A vs Case B - Migration Impact (both sub-modes)

Dataset: F-MNIST | clusters: 5 | clients: 20 | rounds: 60 | beta: 0.9 | interval: 5

Migration(s): [{'round': 40, 'clients': [0, 1, 2], 'src': 0, 'dst': 4}]

| submode | cluster | metric | Case A (isolated) | Case B (sharing) |
|---|---|---|---|---|
| membership_only | 0 | clusterTest_before | 99.16 | 99.02 |
| membership_only | 0 | clusterTest_maxDrop | 0.06 | 0.31 |
| membership_only | 0 | clusterTest_afterStd | 0.06 | 0.17 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 19.83 | 19.80 |
| membership_only | 0 | globalTest_maxDrop | 0.01 | 0.06 |
| membership_only | 0 | globalTest_afterStd | 0.01 | 0.03 |
| membership_only | 4 | clusterTest_before | 99.63 | 99.63 |
| membership_only | 4 | clusterTest_maxDrop | 87.38 | 70.93 |
| membership_only | 4 | clusterTest_afterStd | 32.12 | 26.93 |
| membership_only | 4 | clusterTest_recovery | 2 | 4 |
| membership_only | 4 | globalTest_before | 19.93 | 19.93 |
| membership_only | 4 | globalTest_maxDrop | 0.03 | 0.18 |
| membership_only | 4 | globalTest_afterStd | 7.02 | 5.57 |
| data_changes | 0 | clusterTest_before | 99.16 | 99.02 |
| data_changes | 0 | clusterTest_maxDrop | 0.06 | 0.31 |
| data_changes | 0 | clusterTest_afterStd | 0.06 | 0.18 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 19.83 | 19.80 |
| data_changes | 0 | globalTest_maxDrop | 0.01 | 0.06 |
| data_changes | 0 | globalTest_afterStd | 0.01 | 0.04 |
| data_changes | 4 | clusterTest_before | 99.63 | 99.63 |
| data_changes | 4 | clusterTest_maxDrop | 0.23 | 0.08 |
| data_changes | 4 | clusterTest_afterStd | 0.06 | 0.04 |
| data_changes | 4 | clusterTest_recovery | 0 | 0 |
| data_changes | 4 | globalTest_before | 19.93 | 19.93 |
| data_changes | 4 | globalTest_maxDrop | 0.05 | 0.02 |
| data_changes | 4 | globalTest_afterStd | 0.01 | 0.01 |
