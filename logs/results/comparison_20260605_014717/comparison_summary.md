# Case A vs Case B - Migration Impact (both sub-modes)

Dataset: CIFAR-10 | clusters: 5 | clients: 20 | rounds: 60 | beta: 0.7 | interval: 5

Migration(s): [{'round': 40, 'clients': [0, 1, 2], 'src': 0, 'dst': 4}]

| submode | cluster | metric | Case A (isolated) | Case B (sharing) |
|---|---|---|---|---|
| membership_only | 0 | clusterTest_before | 95.96 | 95.40 |
| membership_only | 0 | clusterTest_maxDrop | 0.56 | 4.45 |
| membership_only | 0 | clusterTest_afterStd | 0.23 | 1.39 |
| membership_only | 0 | clusterTest_recovery | 0 | 0 |
| membership_only | 0 | globalTest_before | 19.19 | 19.08 |
| membership_only | 0 | globalTest_maxDrop | 0.11 | 0.89 |
| membership_only | 0 | globalTest_afterStd | 0.05 | 0.28 |
| membership_only | 4 | clusterTest_before | 95.60 | 94.14 |
| membership_only | 4 | clusterTest_maxDrop | 58.30 | 94.14 |
| membership_only | 4 | clusterTest_afterStd | 13.93 | 36.27 |
| membership_only | 4 | clusterTest_recovery | -1 | 10 |
| membership_only | 4 | globalTest_before | 19.12 | 18.83 |
| membership_only | 4 | globalTest_maxDrop | 3.83 | 2.77 |
| membership_only | 4 | globalTest_afterStd | 2.36 | 2.91 |
| data_changes | 0 | clusterTest_before | 95.96 | 95.40 |
| data_changes | 0 | clusterTest_maxDrop | 0.56 | 2.40 |
| data_changes | 0 | clusterTest_afterStd | 0.23 | 0.96 |
| data_changes | 0 | clusterTest_recovery | 0 | 0 |
| data_changes | 0 | globalTest_before | 19.19 | 19.08 |
| data_changes | 0 | globalTest_maxDrop | 0.11 | 0.48 |
| data_changes | 0 | globalTest_afterStd | 0.05 | 0.19 |
| data_changes | 4 | clusterTest_before | 95.60 | 94.14 |
| data_changes | 4 | clusterTest_maxDrop | 9.00 | 5.73 |
| data_changes | 4 | clusterTest_afterStd | 2.95 | 2.34 |
| data_changes | 4 | clusterTest_recovery | 8 | 3 |
| data_changes | 4 | globalTest_before | 19.12 | 18.83 |
| data_changes | 4 | globalTest_maxDrop | 1.80 | 1.15 |
| data_changes | 4 | globalTest_afterStd | 0.59 | 0.47 |
