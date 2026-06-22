# Case A vs Case B - Migration Impact

Dataset: MNIST | clusters: 5 | clients: 20 | rounds: 60 | beta: 0.7 | share interval: 5

Migration(s): [{'round': 30, 'clients': [0], 'src': 0, 'dst': 4}]

| cluster | metric | Case A (isolated) | Case B (sharing) |
|---|---|---|---|
| 0 | clusterTest_before | 99.95 | 99.95 |
| 0 | clusterTest_maxDrop | 0.00 | 0.05 |
| 0 | clusterTest_afterStd | 0.01 | 0.01 |
| 0 | clusterTest_recovery | 0 | 0 |
| 0 | globalTest_before | 21.14 | 21.14 |
| 0 | globalTest_maxDrop | -0.00 | 0.01 |
| 0 | globalTest_afterStd | 0.00 | 0.00 |
| 4 | clusterTest_before | 99.40 | 99.13 |
| 4 | clusterTest_maxDrop | 38.89 | 50.26 |
| 4 | clusterTest_afterStd | 11.38 | 15.36 |
| 4 | clusterTest_recovery | 0 | 0 |
| 4 | globalTest_before | 19.71 | 19.66 |
| 4 | globalTest_maxDrop | 0.11 | 0.16 |
| 4 | globalTest_afterStd | 7.43 | 7.69 |
