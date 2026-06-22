# Case A vs Case B - Migration Impact

Dataset: MNIST | clusters: 5 | clients: 20 | rounds: 60 | beta: 0.7 | share interval: 5

Migration(s): [{'round': 30, 'clients': [0], 'src': 0, 'dst': 4}]

| cluster | metric | Case A (isolated) | Case B (sharing) |
|---|---|---|---|
| 0 | before_mean_acc | 99.95 | 99.95 |
| 0 | max_drop | 0.00 | 0.05 |
| 0 | after_std | 0.01 | 0.01 |
| 0 | recovery_time | 0 | 0 |
| 4 | before_mean_acc | 99.40 | 99.13 |
| 4 | max_drop | 38.89 | 50.26 |
| 4 | after_std | 11.38 | 15.36 |
| 4 | recovery_time | 0 | 0 |
