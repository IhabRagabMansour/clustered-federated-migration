# v2 analysis tables

Analysis of results_v2/summary_long.csv (v2 run, 1584 CNN jobs).

Run from the project folder:  python analysis_v2/analyze_v2.py
Writes tables (CSV + one markdown file) and figures into analysis_v2/.

Definitions (10-round windows around the migration round R):
  dip      = before_mean - after_mean   (mean accuracy lost in rounds R..R+9; >0 = worse)
  max_drop = before_mean - min(after)   (worst single round)
  below    = rounds in R..59 more than 1 point under before_mean
  final    = mean(last 10 rounds) - before_mean
  excess_X = X(migration run) - X(matched no-migration control), matched on
             dataset, K, M, q, migration round, case, beta, seed, cluster role.

## 1. Destination cluster, main grid (mean over M=3..10 and 3 seeds)

|                                                                  |    dip |   ex_dip |   ex_dip_se |   ex_max_drop |   ex_rounds_below_threshold |   ex_final_minus_before |   never_recovered_% |   n |
|:-----------------------------------------------------------------|-------:|---------:|------------:|--------------:|----------------------------:|------------------------:|--------------------:|----:|
| ('CIFAR-10', 2, 'data_changes', 'adopt_destination', 'caseA')    | -1.277 |   -0.563 |       0.073 |        -0.794 |                      -0.833 |                   0.94  |               0     |  24 |
| ('CIFAR-10', 2, 'data_changes', 'adopt_destination', 'caseB')    | -1.256 |   -0.645 |       0.096 |        -1.138 |                      -1.083 |                   0.853 |               0     |  24 |
| ('CIFAR-10', 2, 'data_changes', 'keep_weights', 'caseA')         |  1.725 |    2.439 |       0.226 |        12.192 |                       2.208 |                   0.477 |               0     |  24 |
| ('CIFAR-10', 2, 'data_changes', 'keep_weights', 'caseB')         | -0.279 |    0.331 |       0.081 |         2.245 |                       0.458 |                   0.66  |               0     |  24 |
| ('CIFAR-10', 2, 'membership_only', 'adopt_destination', 'caseA') | 29.625 |   30.339 |       2.461 |        74.847 |                      15.667 |                 -23.699 |               0     |  24 |
| ('CIFAR-10', 2, 'membership_only', 'adopt_destination', 'caseB') | 30.102 |   30.713 |       1.977 |        84.672 |                      14.833 |                 -24.514 |               0     |  24 |
| ('CIFAR-10', 2, 'membership_only', 'keep_weights', 'caseA')      | 28.683 |   29.397 |       2.205 |        71.56  |                      17     |                 -24.252 |              20.833 |  24 |
| ('CIFAR-10', 2, 'membership_only', 'keep_weights', 'caseB')      | 29.125 |   29.736 |       1.77  |        72.58  |                      15.167 |                 -24.589 |               8.333 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'adopt_destination', 'caseA')    | -1.093 |   -0.278 |       0.172 |        -0.702 |                      -0.958 |                   0.413 |               0     |  24 |
| ('CIFAR-10', 5, 'data_changes', 'adopt_destination', 'caseB')    | -0.949 |    0.108 |       0.134 |         0.608 |                      -0.083 |                  -0.003 |               0     |  24 |
| ('CIFAR-10', 5, 'data_changes', 'keep_weights', 'caseA')         |  1.234 |    2.05  |       0.234 |         5.479 |                       2.583 |                  -0.162 |               0     |  24 |
| ('CIFAR-10', 5, 'data_changes', 'keep_weights', 'caseB')         |  0.027 |    1.084 |       0.154 |         2.544 |                       1.708 |                  -0.068 |               0     |  24 |
| ('CIFAR-10', 5, 'membership_only', 'adopt_destination', 'caseA') | 31.268 |   32.083 |       3.118 |        66.042 |                      12.833 |                 -25.891 |               4.167 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'adopt_destination', 'caseB') | 32.011 |   33.068 |       3.056 |        71.308 |                      12.542 |                 -26.645 |               8.333 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'keep_weights', 'caseA')      | 31.225 |   32.04  |       2.961 |        74.615 |                      12.75  |                 -25.871 |               4.167 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'keep_weights', 'caseB')      | 31.564 |   32.621 |       2.813 |        83.837 |                      13.125 |                 -26.369 |              16.667 |  24 |
| ('F-MNIST', 2, 'data_changes', 'adopt_destination', 'caseA')     | -0.667 |    0.015 |       0.061 |         0.138 |                       0     |                   0.016 |               0     |  24 |
| ('F-MNIST', 2, 'data_changes', 'adopt_destination', 'caseB')     | -0.758 |   -0.061 |       0.036 |        -0.088 |                      -0.167 |                   0.021 |               0     |  24 |
| ('F-MNIST', 2, 'data_changes', 'keep_weights', 'caseA')          |  0.52  |    1.203 |       0.078 |         3.702 |                       1.875 |                  -0.376 |               0     |  24 |
| ('F-MNIST', 2, 'data_changes', 'keep_weights', 'caseB')          | -0.225 |    0.472 |       0.046 |         0.945 |                       0.083 |                  -0.16  |               0     |  24 |
| ('F-MNIST', 2, 'membership_only', 'adopt_destination', 'caseA')  | 12.344 |   13.027 |       0.53  |        40.661 |                      12.333 |                 -10.939 |               0     |  24 |
| ('F-MNIST', 2, 'membership_only', 'adopt_destination', 'caseB')  | 14.105 |   14.801 |       0.466 |        54.204 |                      14.208 |                 -11.418 |               0     |  24 |
| ('F-MNIST', 2, 'membership_only', 'keep_weights', 'caseA')       | 13.572 |   14.254 |       0.402 |        34.605 |                      14.042 |                 -11.599 |               0     |  24 |
| ('F-MNIST', 2, 'membership_only', 'keep_weights', 'caseB')       | 13.553 |   14.25  |       0.265 |        35.742 |                      15.167 |                 -11.863 |               0     |  24 |
| ('F-MNIST', 5, 'data_changes', 'adopt_destination', 'caseA')     | -0.013 |    0.009 |       0.003 |        -0.002 |                       0     |                  -0.013 |               0     |  24 |
| ('F-MNIST', 5, 'data_changes', 'adopt_destination', 'caseB')     | -0.013 |    0.007 |       0.003 |        -0     |                       0     |                  -0.008 |               0     |  24 |
| ('F-MNIST', 5, 'data_changes', 'keep_weights', 'caseA')          |  0.011 |    0.033 |       0.014 |         0.158 |                       0.042 |                  -0.021 |               0     |  24 |
| ('F-MNIST', 5, 'data_changes', 'keep_weights', 'caseB')          |  0.005 |    0.025 |       0.006 |         0.046 |                       0     |                  -0.019 |               0     |  24 |
| ('F-MNIST', 5, 'membership_only', 'adopt_destination', 'caseA')  | 12.199 |   12.221 |       1.307 |        58.217 |                       8.708 |                  -1.07  |               0     |  24 |
| ('F-MNIST', 5, 'membership_only', 'adopt_destination', 'caseB')  | 14.9   |   14.92  |       1.4   |        83.456 |                      10.5   |                  -1.74  |               0     |  24 |
| ('F-MNIST', 5, 'membership_only', 'keep_weights', 'caseA')       | 11.203 |   11.225 |       0.887 |        66.517 |                       8.583 |                  -1.338 |               0     |  24 |
| ('F-MNIST', 5, 'membership_only', 'keep_weights', 'caseB')       | 13.129 |   13.15  |       1.166 |        58.596 |                       9.833 |                  -1.541 |               0     |  24 |
| ('MNIST', 2, 'data_changes', 'adopt_destination', 'caseA')       | -0.458 |   -0.032 |       0.008 |        -0.05  |                       0     |                   0.033 |               0     |  24 |
| ('MNIST', 2, 'data_changes', 'adopt_destination', 'caseB')       | -0.487 |   -0.05  |       0.008 |        -0.055 |                       0     |                   0.047 |               0     |  24 |
| ('MNIST', 2, 'data_changes', 'keep_weights', 'caseA')            |  0.383 |    0.809 |       0.05  |         2.238 |                       1.25  |                  -0.222 |               0     |  24 |
| ('MNIST', 2, 'data_changes', 'keep_weights', 'caseB')            | -0.022 |    0.416 |       0.022 |         0.916 |                       0.125 |                  -0.1   |               0     |  24 |
| ('MNIST', 2, 'membership_only', 'adopt_destination', 'caseA')    | 14.166 |   14.592 |       1.478 |        74.767 |                      11.333 |                  -2.366 |               0     |  24 |
| ('MNIST', 2, 'membership_only', 'adopt_destination', 'caseB')    | 13.665 |   14.102 |       0.814 |        92.947 |                      11.042 |                  -3.073 |               0     |  24 |
| ('MNIST', 2, 'membership_only', 'keep_weights', 'caseA')         | 13.904 |   14.33  |       1.255 |        69.205 |                      11.833 |                  -2.513 |               0     |  24 |
| ('MNIST', 2, 'membership_only', 'keep_weights', 'caseB')         | 14.553 |   14.99  |       0.969 |        71.079 |                      11.458 |                  -3.23  |               0     |  24 |
| ('MNIST', 5, 'data_changes', 'adopt_destination', 'caseA')       | -0.308 |   -0.019 |       0.029 |        -0.069 |                      -0.125 |                   0.03  |               0     |  24 |
| ('MNIST', 5, 'data_changes', 'adopt_destination', 'caseB')       | -0.33  |   -0.007 |       0.038 |        -0.05  |                      -0.208 |                   0.124 |               0     |  24 |
| ('MNIST', 5, 'data_changes', 'keep_weights', 'caseA')            |  0.037 |    0.326 |       0.071 |         0.803 |                       0.042 |                  -0.132 |               0     |  24 |
| ('MNIST', 5, 'data_changes', 'keep_weights', 'caseB')            |  0.038 |    0.362 |       0.04  |         0.435 |                       0     |                  -0.048 |               0     |  24 |
| ('MNIST', 5, 'membership_only', 'adopt_destination', 'caseA')    | 11.927 |   12.215 |       1.696 |        49.815 |                      13.75  |                  -5.137 |               4.167 |  24 |
| ('MNIST', 5, 'membership_only', 'adopt_destination', 'caseB')    | 14.473 |   14.797 |       0.977 |        86.994 |                      17     |                  -6.097 |               4.167 |  24 |
| ('MNIST', 5, 'membership_only', 'keep_weights', 'caseA')         | 13.844 |   14.132 |       1.062 |        78.536 |                      15.958 |                  -4.795 |              25     |  24 |
| ('MNIST', 5, 'membership_only', 'keep_weights', 'caseB')         | 16.811 |   17.135 |       1.24  |        78.492 |                      16.792 |                  -6.943 |              33.333 |  24 |


## 1b. Source cluster, main grid

|                                                                  |   ex_dip |   ex_dip_se |   ex_max_drop |   ex_final_minus_before |   n |
|:-----------------------------------------------------------------|---------:|------------:|--------------:|------------------------:|----:|
| ('CIFAR-10', 2, 'data_changes', 'adopt_destination', 'caseA')    |    1.976 |       0.314 |         4.199 |                  -0.98  |  24 |
| ('CIFAR-10', 2, 'data_changes', 'adopt_destination', 'caseB')    |    1.88  |       0.301 |         4.097 |                  -1.189 |  24 |
| ('CIFAR-10', 2, 'data_changes', 'keep_weights', 'caseA')         |    1.976 |       0.314 |         4.199 |                  -0.98  |  24 |
| ('CIFAR-10', 2, 'data_changes', 'keep_weights', 'caseB')         |    1.794 |       0.303 |         3.992 |                  -1.029 |  24 |
| ('CIFAR-10', 2, 'membership_only', 'adopt_destination', 'caseA') |    1.946 |       0.327 |         3.705 |                  -0.98  |  24 |
| ('CIFAR-10', 2, 'membership_only', 'adopt_destination', 'caseB') |    1.959 |       0.34  |         3.793 |                  -1.086 |  24 |
| ('CIFAR-10', 2, 'membership_only', 'keep_weights', 'caseA')      |    1.946 |       0.327 |         3.705 |                  -0.98  |  24 |
| ('CIFAR-10', 2, 'membership_only', 'keep_weights', 'caseB')      |    1.706 |       0.319 |         3.557 |                  -0.772 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'adopt_destination', 'caseA')    |    0.617 |       0.255 |         2.11  |                  -0.636 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'adopt_destination', 'caseB')    |    0.671 |       0.284 |         2.552 |                  -0.774 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'keep_weights', 'caseA')         |    0.617 |       0.255 |         2.11  |                  -0.636 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'keep_weights', 'caseB')         |    0.63  |       0.28  |         2.575 |                  -0.729 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'adopt_destination', 'caseA') |    0.741 |       0.217 |         2.685 |                  -0.403 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'adopt_destination', 'caseB') |    0.982 |       0.368 |         2.956 |                  -0.542 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'keep_weights', 'caseA')      |    0.741 |       0.217 |         2.685 |                  -0.403 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'keep_weights', 'caseB')      |    0.972 |       0.376 |         2.988 |                  -0.483 |  24 |
| ('F-MNIST', 2, 'data_changes', 'adopt_destination', 'caseA')     |    0.403 |       0.068 |         0.609 |                  -0.391 |  24 |
| ('F-MNIST', 2, 'data_changes', 'adopt_destination', 'caseB')     |    0.496 |       0.079 |         1.35  |                  -0.482 |  24 |
| ('F-MNIST', 2, 'data_changes', 'keep_weights', 'caseA')          |    0.403 |       0.068 |         0.609 |                  -0.391 |  24 |
| ('F-MNIST', 2, 'data_changes', 'keep_weights', 'caseB')          |    0.45  |       0.07  |         1.453 |                  -0.35  |  24 |
| ('F-MNIST', 2, 'membership_only', 'adopt_destination', 'caseA')  |    0.571 |       0.118 |         0.937 |                  -0.284 |  24 |
| ('F-MNIST', 2, 'membership_only', 'adopt_destination', 'caseB')  |    0.767 |       0.174 |         1.627 |                  -0.305 |  24 |
| ('F-MNIST', 2, 'membership_only', 'keep_weights', 'caseA')       |    0.571 |       0.118 |         0.937 |                  -0.284 |  24 |
| ('F-MNIST', 2, 'membership_only', 'keep_weights', 'caseB')       |    0.683 |       0.173 |         1.529 |                  -0.15  |  24 |
| ('F-MNIST', 5, 'data_changes', 'adopt_destination', 'caseA')     |    0.065 |       0.021 |         0.179 |                  -0.071 |  24 |
| ('F-MNIST', 5, 'data_changes', 'adopt_destination', 'caseB')     |    0.233 |       0.073 |         0.519 |                  -0.194 |  24 |
| ('F-MNIST', 5, 'data_changes', 'keep_weights', 'caseA')          |    0.065 |       0.021 |         0.179 |                  -0.071 |  24 |
| ('F-MNIST', 5, 'data_changes', 'keep_weights', 'caseB')          |    0.265 |       0.128 |         0.533 |                   0.032 |  24 |
| ('F-MNIST', 5, 'membership_only', 'adopt_destination', 'caseA')  |    0.065 |       0.021 |         0.162 |                  -0.069 |  24 |
| ('F-MNIST', 5, 'membership_only', 'adopt_destination', 'caseB')  |    0.216 |       0.077 |         0.448 |                  -0.003 |  24 |
| ('F-MNIST', 5, 'membership_only', 'keep_weights', 'caseA')       |    0.065 |       0.021 |         0.162 |                  -0.069 |  24 |
| ('F-MNIST', 5, 'membership_only', 'keep_weights', 'caseB')       |    0.231 |       0.081 |         0.446 |                   0.044 |  24 |
| ('MNIST', 2, 'data_changes', 'adopt_destination', 'caseA')       |    0.046 |       0.008 |         0.051 |                  -0.057 |  24 |
| ('MNIST', 2, 'data_changes', 'adopt_destination', 'caseB')       |    0.058 |       0.01  |         0.066 |                  -0.063 |  24 |
| ('MNIST', 2, 'data_changes', 'keep_weights', 'caseA')            |    0.046 |       0.008 |         0.051 |                  -0.057 |  24 |
| ('MNIST', 2, 'data_changes', 'keep_weights', 'caseB')            |    0.067 |       0.01  |         0.146 |                  -0.044 |  24 |
| ('MNIST', 2, 'membership_only', 'adopt_destination', 'caseA')    |    0.036 |       0.007 |         0.058 |                  -0.043 |  24 |
| ('MNIST', 2, 'membership_only', 'adopt_destination', 'caseB')    |    0.058 |       0.007 |         0.092 |                  -0.041 |  24 |
| ('MNIST', 2, 'membership_only', 'keep_weights', 'caseA')         |    0.036 |       0.007 |         0.058 |                  -0.043 |  24 |
| ('MNIST', 2, 'membership_only', 'keep_weights', 'caseB')         |    0.033 |       0.007 |         0.043 |                  -0.015 |  24 |
| ('MNIST', 5, 'data_changes', 'adopt_destination', 'caseA')       |    0.007 |       0.003 |         0.024 |                  -0.01  |  24 |
| ('MNIST', 5, 'data_changes', 'adopt_destination', 'caseB')       |    0.006 |       0.004 |         0.024 |                  -0.002 |  24 |
| ('MNIST', 5, 'data_changes', 'keep_weights', 'caseA')            |    0.007 |       0.003 |         0.024 |                  -0.01  |  24 |
| ('MNIST', 5, 'data_changes', 'keep_weights', 'caseB')            |    0.006 |       0.004 |         0.024 |                  -0.001 |  24 |
| ('MNIST', 5, 'membership_only', 'adopt_destination', 'caseA')    |    0.007 |       0.003 |         0.02  |                  -0.009 |  24 |
| ('MNIST', 5, 'membership_only', 'adopt_destination', 'caseB')    |    0.008 |       0.004 |         0.012 |                  -0     |  24 |
| ('MNIST', 5, 'membership_only', 'keep_weights', 'caseA')         |    0.007 |       0.003 |         0.02  |                  -0.009 |  24 |
| ('MNIST', 5, 'membership_only', 'keep_weights', 'caseB')         |    0.007 |       0.004 |         0.012 |                   0.004 |  24 |


## 2. Case B minus Case A, control-adjusted dip of the destination (paired by M, seed)

Negative B_minus_A = sharing reduces the migration dip. migration_impact = after mixing (as in v1); _premix = before mixing; _global = global test set.

|                                                                                    |   A_ex_dip |   B_ex_dip |   B_minus_A |    se |   B_better_% |   n |
|:-----------------------------------------------------------------------------------|-----------:|-----------:|------------:|------:|-------------:|----:|
| ('migration_impact', 'CIFAR-10', 2, 'data_changes', 'adopt_destination')           |     -0.563 |     -0.645 |      -0.082 | 0.062 |       62.5   |  24 |
| ('migration_impact', 'CIFAR-10', 2, 'data_changes', 'keep_weights')                |      2.439 |      0.331 |      -2.108 | 0.222 |      100     |  24 |
| ('migration_impact', 'CIFAR-10', 2, 'membership_only', 'adopt_destination')        |     30.339 |     30.713 |       0.374 | 0.537 |       41.667 |  24 |
| ('migration_impact', 'CIFAR-10', 2, 'membership_only', 'keep_weights')             |     29.397 |     29.736 |       0.339 | 0.651 |       37.5   |  24 |
| ('migration_impact', 'CIFAR-10', 5, 'data_changes', 'adopt_destination')           |     -0.278 |      0.108 |       0.385 | 0.14  |       29.167 |  24 |
| ('migration_impact', 'CIFAR-10', 5, 'data_changes', 'keep_weights')                |      2.05  |      1.084 |      -0.965 | 0.204 |       87.5   |  24 |
| ('migration_impact', 'CIFAR-10', 5, 'membership_only', 'adopt_destination')        |     32.083 |     33.068 |       0.985 | 0.267 |       29.167 |  24 |
| ('migration_impact', 'CIFAR-10', 5, 'membership_only', 'keep_weights')             |     32.04  |     32.621 |       0.581 | 0.298 |       50     |  24 |
| ('migration_impact', 'F-MNIST', 2, 'data_changes', 'adopt_destination')            |      0.015 |     -0.061 |      -0.076 | 0.047 |       66.667 |  24 |
| ('migration_impact', 'F-MNIST', 2, 'data_changes', 'keep_weights')                 |      1.203 |      0.472 |      -0.731 | 0.078 |      100     |  24 |
| ('migration_impact', 'F-MNIST', 2, 'membership_only', 'adopt_destination')         |     13.027 |     14.801 |       1.775 | 0.308 |       12.5   |  24 |
| ('migration_impact', 'F-MNIST', 2, 'membership_only', 'keep_weights')              |     14.254 |     14.25  |      -0.004 | 0.222 |       50     |  24 |
| ('migration_impact', 'F-MNIST', 5, 'data_changes', 'adopt_destination')            |      0.009 |      0.007 |      -0.002 | 0.003 |       41.667 |  24 |
| ('migration_impact', 'F-MNIST', 5, 'data_changes', 'keep_weights')                 |      0.033 |      0.025 |      -0.008 | 0.011 |       45.833 |  24 |
| ('migration_impact', 'F-MNIST', 5, 'membership_only', 'adopt_destination')         |     12.221 |     14.92  |       2.699 | 0.637 |       25     |  24 |
| ('migration_impact', 'F-MNIST', 5, 'membership_only', 'keep_weights')              |     11.225 |     13.15  |       1.924 | 0.482 |       20.833 |  24 |
| ('migration_impact', 'MNIST', 2, 'data_changes', 'adopt_destination')              |     -0.032 |     -0.05  |      -0.018 | 0.009 |       66.667 |  24 |
| ('migration_impact', 'MNIST', 2, 'data_changes', 'keep_weights')                   |      0.809 |      0.416 |      -0.393 | 0.047 |      100     |  24 |
| ('migration_impact', 'MNIST', 2, 'membership_only', 'adopt_destination')           |     14.592 |     14.102 |      -0.489 | 0.687 |       54.167 |  24 |
| ('migration_impact', 'MNIST', 2, 'membership_only', 'keep_weights')                |     14.33  |     14.99  |       0.66  | 0.409 |       29.167 |  24 |
| ('migration_impact', 'MNIST', 5, 'data_changes', 'adopt_destination')              |     -0.019 |     -0.007 |       0.012 | 0.048 |       45.833 |  24 |
| ('migration_impact', 'MNIST', 5, 'data_changes', 'keep_weights')                   |      0.326 |      0.362 |       0.036 | 0.076 |       29.167 |  24 |
| ('migration_impact', 'MNIST', 5, 'membership_only', 'adopt_destination')           |     12.215 |     14.797 |       2.582 | 0.911 |       29.167 |  24 |
| ('migration_impact', 'MNIST', 5, 'membership_only', 'keep_weights')                |     14.132 |     17.135 |       3.002 | 0.42  |        0     |  24 |
| ('migration_impact_premix', 'CIFAR-10', 2, 'data_changes', 'adopt_destination')    |     -0.563 |     -0.66  |      -0.097 | 0.06  |       66.667 |  24 |
| ('migration_impact_premix', 'CIFAR-10', 2, 'data_changes', 'keep_weights')         |      2.439 |      0.367 |      -2.072 | 0.221 |      100     |  24 |
| ('migration_impact_premix', 'CIFAR-10', 2, 'membership_only', 'adopt_destination') |     30.339 |     30.604 |       0.265 | 0.514 |       41.667 |  24 |
| ('migration_impact_premix', 'CIFAR-10', 2, 'membership_only', 'keep_weights')      |     29.397 |     29.103 |      -0.294 | 0.689 |       37.5   |  24 |
| ('migration_impact_premix', 'CIFAR-10', 5, 'data_changes', 'adopt_destination')    |     -0.278 |      0.121 |       0.399 | 0.149 |       25     |  24 |
| ('migration_impact_premix', 'CIFAR-10', 5, 'data_changes', 'keep_weights')         |      2.05  |      1.144 |      -0.906 | 0.2   |       87.5   |  24 |
| ('migration_impact_premix', 'CIFAR-10', 5, 'membership_only', 'adopt_destination') |     32.083 |     33.065 |       0.982 | 0.255 |       20.833 |  24 |
| ('migration_impact_premix', 'CIFAR-10', 5, 'membership_only', 'keep_weights')      |     32.04  |     32.897 |       0.857 | 0.302 |       37.5   |  24 |
| ('migration_impact_premix', 'F-MNIST', 2, 'data_changes', 'adopt_destination')     |      0.015 |     -0.063 |      -0.079 | 0.049 |       62.5   |  24 |
| ('migration_impact_premix', 'F-MNIST', 2, 'data_changes', 'keep_weights')          |      1.203 |      0.474 |      -0.728 | 0.078 |      100     |  24 |
| ('migration_impact_premix', 'F-MNIST', 2, 'membership_only', 'adopt_destination')  |     13.027 |     14.147 |       1.121 | 0.291 |       16.667 |  24 |
| ('migration_impact_premix', 'F-MNIST', 2, 'membership_only', 'keep_weights')       |     14.254 |     14.057 |      -0.197 | 0.249 |       50     |  24 |
| ('migration_impact_premix', 'F-MNIST', 5, 'data_changes', 'adopt_destination')     |      0.009 |      0.007 |      -0.002 | 0.003 |       41.667 |  24 |
| ('migration_impact_premix', 'F-MNIST', 5, 'data_changes', 'keep_weights')          |      0.033 |      0.025 |      -0.008 | 0.011 |       45.833 |  24 |
| ('migration_impact_premix', 'F-MNIST', 5, 'membership_only', 'adopt_destination')  |     12.221 |     14.888 |       2.667 | 0.644 |       25     |  24 |
| ('migration_impact_premix', 'F-MNIST', 5, 'membership_only', 'keep_weights')       |     11.225 |     13.27  |       2.045 | 0.5   |       20.833 |  24 |
| ('migration_impact_premix', 'MNIST', 2, 'data_changes', 'adopt_destination')       |     -0.032 |     -0.05  |      -0.019 | 0.009 |       66.667 |  24 |
| ('migration_impact_premix', 'MNIST', 2, 'data_changes', 'keep_weights')            |      0.809 |      0.42  |      -0.389 | 0.047 |      100     |  24 |
| ('migration_impact_premix', 'MNIST', 2, 'membership_only', 'adopt_destination')    |     14.592 |     13.914 |      -0.678 | 0.649 |       58.333 |  24 |
| ('migration_impact_premix', 'MNIST', 2, 'membership_only', 'keep_weights')         |     14.33  |     14.723 |       0.392 | 0.418 |       29.167 |  24 |
| ('migration_impact_premix', 'MNIST', 5, 'data_changes', 'adopt_destination')       |     -0.019 |     -0.007 |       0.012 | 0.048 |       45.833 |  24 |
| ('migration_impact_premix', 'MNIST', 5, 'data_changes', 'keep_weights')            |      0.326 |      0.359 |       0.033 | 0.075 |       33.333 |  24 |
| ('migration_impact_premix', 'MNIST', 5, 'membership_only', 'adopt_destination')    |     12.215 |     14.636 |       2.421 | 0.907 |       33.333 |  24 |
| ('migration_impact_premix', 'MNIST', 5, 'membership_only', 'keep_weights')         |     14.132 |     17.036 |       2.903 | 0.419 |        0     |  24 |
| ('migration_impact_global', 'CIFAR-10', 2, 'data_changes', 'adopt_destination')    |     -0.282 |     -0.323 |      -0.041 | 0.031 |       62.5   |  24 |
| ('migration_impact_global', 'CIFAR-10', 2, 'data_changes', 'keep_weights')         |      1.22  |      0.166 |      -1.054 | 0.111 |      100     |  24 |
| ('migration_impact_global', 'CIFAR-10', 2, 'membership_only', 'adopt_destination') |      3.138 |     -0.244 |      -3.382 | 0.239 |      100     |  24 |
| ('migration_impact_global', 'CIFAR-10', 2, 'membership_only', 'keep_weights')      |     -0.779 |     -2.185 |      -1.406 | 0.293 |       87.5   |  24 |
| ('migration_impact_global', 'CIFAR-10', 5, 'data_changes', 'adopt_destination')    |     -0.056 |      0.022 |       0.077 | 0.028 |       29.167 |  24 |
| ('migration_impact_global', 'CIFAR-10', 5, 'data_changes', 'keep_weights')         |      0.41  |      0.217 |      -0.193 | 0.041 |       87.5   |  24 |
| ('migration_impact_global', 'CIFAR-10', 5, 'membership_only', 'adopt_destination') |      0.007 |     -0.567 |      -0.574 | 0.081 |       95.833 |  24 |
| ('migration_impact_global', 'CIFAR-10', 5, 'membership_only', 'keep_weights')      |     -0.687 |     -0.524 |       0.163 | 0.062 |       29.167 |  24 |
| ('migration_impact_global', 'F-MNIST', 2, 'data_changes', 'adopt_destination')     |      0.008 |     -0.031 |      -0.039 | 0.024 |       70.833 |  24 |
| ('migration_impact_global', 'F-MNIST', 2, 'data_changes', 'keep_weights')          |      0.601 |      0.225 |      -0.376 | 0.044 |      100     |  24 |
| ('migration_impact_global', 'F-MNIST', 2, 'membership_only', 'adopt_destination')  |    -10.594 |    -16.753 |      -6.159 | 0.295 |      100     |  24 |
| ('migration_impact_global', 'F-MNIST', 2, 'membership_only', 'keep_weights')       |    -14.907 |    -17.774 |      -2.867 | 0.144 |      100     |  24 |
| ('migration_impact_global', 'F-MNIST', 5, 'data_changes', 'adopt_destination')     |      0.002 |      0.001 |      -0     | 0.001 |       41.667 |  24 |
| ('migration_impact_global', 'F-MNIST', 5, 'data_changes', 'keep_weights')          |      0.007 |      0.005 |      -0.002 | 0.002 |       45.833 |  24 |
| ('migration_impact_global', 'F-MNIST', 5, 'membership_only', 'adopt_destination')  |     -8.232 |     -8.846 |      -0.614 | 0.462 |       62.5   |  24 |
| ('migration_impact_global', 'F-MNIST', 5, 'membership_only', 'keep_weights')       |     -9.377 |     -8.68  |       0.697 | 0.276 |       25     |  24 |
| ('migration_impact_global', 'MNIST', 2, 'data_changes', 'adopt_destination')       |     -0.015 |     -0.025 |      -0.01  | 0.004 |       70.833 |  24 |
| ('migration_impact_global', 'MNIST', 2, 'data_changes', 'keep_weights')            |      0.393 |      0.204 |      -0.189 | 0.023 |      100     |  24 |
| ('migration_impact_global', 'MNIST', 2, 'membership_only', 'adopt_destination')    |    -26.596 |    -31.594 |      -4.998 | 0.292 |      100     |  24 |
| ('migration_impact_global', 'MNIST', 2, 'membership_only', 'keep_weights')         |    -26.258 |    -27.908 |      -1.649 | 0.251 |       91.667 |  24 |
| ('migration_impact_global', 'MNIST', 5, 'data_changes', 'adopt_destination')       |     -0.004 |     -0.001 |       0.002 | 0.01  |       45.833 |  24 |
| ('migration_impact_global', 'MNIST', 5, 'data_changes', 'keep_weights')            |      0.065 |      0.072 |       0.007 | 0.015 |       29.167 |  24 |
| ('migration_impact_global', 'MNIST', 5, 'membership_only', 'adopt_destination')    |     -9.562 |    -10.784 |      -1.222 | 0.375 |       70.833 |  24 |
| ('migration_impact_global', 'MNIST', 5, 'membership_only', 'keep_weights')         |    -10.521 |     -8.754 |       1.768 | 0.178 |        4.167 |  24 |


## 3. Handover: control-adjusted dst dip, keep_weights vs adopt_destination

Positive keep_minus_adopt = injecting the migrant's own weights costs extra accuracy.

|                                             |   keep |   adopt |   keep_minus_adopt |    se |   n |
|:--------------------------------------------|-------:|--------:|-------------------:|------:|----:|
| ('CIFAR-10', 2, 'data_changes', 'caseA')    |  2.439 |  -0.563 |              3.002 | 0.238 |  24 |
| ('CIFAR-10', 2, 'data_changes', 'caseB')    |  0.331 |  -0.645 |              0.977 | 0.053 |  24 |
| ('CIFAR-10', 2, 'membership_only', 'caseA') | 29.397 |  30.339 |             -0.942 | 0.471 |  24 |
| ('CIFAR-10', 2, 'membership_only', 'caseB') | 29.736 |  30.713 |             -0.977 | 0.674 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'caseA')    |  2.05  |  -0.278 |              2.327 | 0.189 |  24 |
| ('CIFAR-10', 5, 'data_changes', 'caseB')    |  1.084 |   0.108 |              0.977 | 0.181 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'caseA') | 32.04  |  32.083 |             -0.043 | 0.376 |  24 |
| ('CIFAR-10', 5, 'membership_only', 'caseB') | 32.621 |  33.068 |             -0.447 | 0.477 |  24 |
| ('F-MNIST', 2, 'data_changes', 'caseA')     |  1.203 |   0.015 |              1.187 | 0.079 |  24 |
| ('F-MNIST', 2, 'data_changes', 'caseB')     |  0.472 |  -0.061 |              0.533 | 0.02  |  24 |
| ('F-MNIST', 2, 'membership_only', 'caseA')  | 14.254 |  13.027 |              1.228 | 0.304 |  24 |
| ('F-MNIST', 2, 'membership_only', 'caseB')  | 14.25  |  14.801 |             -0.551 | 0.274 |  24 |
| ('F-MNIST', 5, 'data_changes', 'caseA')     |  0.033 |   0.009 |              0.024 | 0.013 |  24 |
| ('F-MNIST', 5, 'data_changes', 'caseB')     |  0.025 |   0.007 |              0.018 | 0.006 |  24 |
| ('F-MNIST', 5, 'membership_only', 'caseA')  | 11.225 |  12.221 |             -0.996 | 0.62  |  24 |
| ('F-MNIST', 5, 'membership_only', 'caseB')  | 13.15  |  14.92  |             -1.771 | 0.58  |  24 |
| ('MNIST', 2, 'data_changes', 'caseA')       |  0.809 |  -0.032 |              0.84  | 0.05  |  24 |
| ('MNIST', 2, 'data_changes', 'caseB')       |  0.416 |  -0.05  |              0.465 | 0.019 |  24 |
| ('MNIST', 2, 'membership_only', 'caseA')    | 14.33  |  14.592 |             -0.261 | 0.305 |  24 |
| ('MNIST', 2, 'membership_only', 'caseB')    | 14.99  |  14.102 |              0.888 | 0.28  |  24 |
| ('MNIST', 5, 'data_changes', 'caseA')       |  0.326 |  -0.019 |              0.345 | 0.066 |  24 |
| ('MNIST', 5, 'data_changes', 'caseB')       |  0.362 |  -0.007 |              0.368 | 0.031 |  24 |
| ('MNIST', 5, 'membership_only', 'caseA')    | 14.132 |  12.215 |              1.917 | 0.811 |  24 |
| ('MNIST', 5, 'membership_only', 'caseB')    | 17.135 |  14.797 |              2.338 | 0.569 |  24 |


## 4. No-migration controls (what the window statistics show with nobody moving)

|                                                            |   before_mean |    dip |   max_drop |   after_std |
|:-----------------------------------------------------------|--------------:|-------:|-----------:|------------:|
| ('CIFAR-10', 2, 'caseA', 'migration_impact', 'dst')        |        87.206 | -0.714 |      0.612 |       0.678 |
| ('CIFAR-10', 2, 'caseA', 'migration_impact', 'src')        |        78.855 | -1.056 |      0.576 |       0.809 |
| ('CIFAR-10', 2, 'caseA', 'migration_impact_global', 'dst') |        43.603 | -0.357 |      0.306 |       0.339 |
| ('CIFAR-10', 2, 'caseA', 'migration_impact_global', 'src') |        39.428 | -0.528 |      0.288 |       0.405 |
| ('CIFAR-10', 2, 'caseA', 'migration_impact_premix', 'dst') |        87.206 | -0.714 |      0.612 |       0.678 |
| ('CIFAR-10', 2, 'caseA', 'migration_impact_premix', 'src') |        78.855 | -1.056 |      0.576 |       0.809 |
| ('CIFAR-10', 2, 'caseB', 'migration_impact', 'dst')        |        86.72  | -0.61  |      1.168 |       0.859 |
| ('CIFAR-10', 2, 'caseB', 'migration_impact', 'src')        |        78.23  | -0.958 |      0.773 |       0.909 |
| ('CIFAR-10', 2, 'caseB', 'migration_impact_global', 'dst') |        43.36  | -0.305 |      0.584 |       0.43  |
| ('CIFAR-10', 2, 'caseB', 'migration_impact_global', 'src') |        39.115 | -0.479 |      0.387 |       0.455 |
| ('CIFAR-10', 2, 'caseB', 'migration_impact_premix', 'dst') |        86.729 | -0.603 |      1.153 |       0.862 |
| ('CIFAR-10', 2, 'caseB', 'migration_impact_premix', 'src') |        78.247 | -0.93  |      0.836 |       0.934 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact', 'dst')        |        91.109 | -0.815 |      2.449 |       1.388 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact', 'src')        |        92.542 | -0.962 |      0.713 |       0.785 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact_global', 'dst') |        18.222 | -0.163 |      0.49  |       0.278 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact_global', 'src') |        18.508 | -0.192 |      0.143 |       0.157 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact_premix', 'dst') |        91.109 | -0.815 |      2.449 |       1.388 |
| ('CIFAR-10', 5, 'caseA', 'migration_impact_premix', 'src') |        92.542 | -0.962 |      0.713 |       0.785 |
| ('CIFAR-10', 5, 'caseB', 'migration_impact', 'dst')        |        90.191 | -1.057 |      2.26  |       1.407 |
| ('CIFAR-10', 5, 'caseB', 'migration_impact', 'src')        |        92.146 | -0.645 |      1.34  |       1.011 |
| ('CIFAR-10', 5, 'caseB', 'migration_impact_global', 'dst') |        18.038 | -0.211 |      0.452 |       0.281 |
| ('CIFAR-10', 5, 'caseB', 'migration_impact_global', 'src') |        18.429 | -0.129 |      0.268 |       0.202 |
| ('CIFAR-10', 5, 'caseB', 'migration_impact_premix', 'dst') |        90.202 | -1.08  |      2.213 |       1.4   |
| ('CIFAR-10', 5, 'caseB', 'migration_impact_premix', 'src') |        92.146 | -0.659 |      1.406 |       1.034 |
| ('F-MNIST', 2, 'caseA', 'migration_impact', 'dst')         |        94.02  | -0.682 |     -0.262 |       0.232 |
| ('F-MNIST', 2, 'caseA', 'migration_impact', 'src')         |        88.057 | -0.755 |      0.24  |       0.449 |
| ('F-MNIST', 2, 'caseA', 'migration_impact_global', 'dst')  |        47.01  | -0.341 |     -0.131 |       0.116 |
| ('F-MNIST', 2, 'caseA', 'migration_impact_global', 'src')  |        44.029 | -0.377 |      0.12  |       0.225 |
| ('F-MNIST', 2, 'caseA', 'migration_impact_premix', 'dst')  |        94.02  | -0.682 |     -0.262 |       0.232 |
| ('F-MNIST', 2, 'caseA', 'migration_impact_premix', 'src')  |        88.057 | -0.755 |      0.24  |       0.449 |
| ('F-MNIST', 2, 'caseB', 'migration_impact', 'dst')         |        93.732 | -0.697 |     -0.139 |       0.292 |
| ('F-MNIST', 2, 'caseB', 'migration_impact', 'src')         |        87.206 | -0.707 |      0.368 |       0.512 |
| ('F-MNIST', 2, 'caseB', 'migration_impact_global', 'dst')  |        46.866 | -0.367 |     -0.074 |       0.176 |
| ('F-MNIST', 2, 'caseB', 'migration_impact_global', 'src')  |        43.603 | -0.366 |      0.169 |       0.258 |
| ('F-MNIST', 2, 'caseB', 'migration_impact_premix', 'dst')  |        93.747 | -0.691 |     -0.16  |       0.289 |
| ('F-MNIST', 2, 'caseB', 'migration_impact_premix', 'src')  |        87.238 | -0.696 |      0.409 |       0.51  |
| ('F-MNIST', 5, 'caseA', 'migration_impact', 'dst')         |        99.56  | -0.022 |      0.015 |       0.025 |
| ('F-MNIST', 5, 'caseA', 'migration_impact', 'src')         |        98.696 | -0.152 |      0.056 |       0.117 |
| ('F-MNIST', 5, 'caseA', 'migration_impact_global', 'dst')  |        19.912 | -0.004 |      0.003 |       0.005 |
| ('F-MNIST', 5, 'caseA', 'migration_impact_global', 'src')  |        19.739 | -0.03  |      0.011 |       0.023 |
| ('F-MNIST', 5, 'caseA', 'migration_impact_premix', 'dst')  |        99.56  | -0.022 |      0.015 |       0.025 |
| ('F-MNIST', 5, 'caseA', 'migration_impact_premix', 'src')  |        98.696 | -0.152 |      0.056 |       0.117 |
| ('F-MNIST', 5, 'caseB', 'migration_impact', 'dst')         |        99.563 | -0.02  |      0.023 |       0.031 |
| ('F-MNIST', 5, 'caseB', 'migration_impact', 'src')         |        98.431 | -0.095 |      0.279 |       0.185 |
| ('F-MNIST', 5, 'caseB', 'migration_impact_global', 'dst')  |        19.913 | -0.004 |      0.005 |       0.006 |
| ('F-MNIST', 5, 'caseB', 'migration_impact_global', 'src')  |        19.686 | -0.019 |      0.056 |       0.037 |
| ('F-MNIST', 5, 'caseB', 'migration_impact_premix', 'dst')  |        99.564 | -0.02  |      0.025 |       0.032 |
| ('F-MNIST', 5, 'caseB', 'migration_impact_premix', 'src')  |        98.45  | -0.093 |      0.256 |       0.176 |
| ('MNIST', 2, 'caseA', 'migration_impact', 'dst')           |        97.732 | -0.426 |     -0.238 |       0.115 |
| ('MNIST', 2, 'caseA', 'migration_impact', 'src')           |        98.781 | -0.22  |     -0.106 |       0.068 |
| ('MNIST', 2, 'caseA', 'migration_impact_global', 'dst')    |        47.507 | -0.207 |     -0.116 |       0.056 |
| ('MNIST', 2, 'caseA', 'migration_impact_global', 'src')    |        50.764 | -0.113 |     -0.054 |       0.035 |
| ('MNIST', 2, 'caseA', 'migration_impact_premix', 'dst')    |        97.732 | -0.426 |     -0.238 |       0.115 |
| ('MNIST', 2, 'caseA', 'migration_impact_premix', 'src')    |        98.781 | -0.22  |     -0.106 |       0.068 |
| ('MNIST', 2, 'caseB', 'migration_impact', 'dst')           |        97.496 | -0.438 |     -0.218 |       0.13  |
| ('MNIST', 2, 'caseB', 'migration_impact', 'src')           |        98.742 | -0.213 |     -0.09  |       0.076 |
| ('MNIST', 2, 'caseB', 'migration_impact_global', 'dst')    |        47.393 | -0.215 |     -0.107 |       0.065 |
| ('MNIST', 2, 'caseB', 'migration_impact_global', 'src')    |        50.747 | -0.199 |     -0.06  |       0.14  |
| ('MNIST', 2, 'caseB', 'migration_impact_premix', 'dst')    |        97.511 | -0.435 |     -0.213 |       0.127 |
| ('MNIST', 2, 'caseB', 'migration_impact_premix', 'src')    |        98.747 | -0.213 |     -0.092 |       0.073 |
| ('MNIST', 5, 'caseA', 'migration_impact', 'dst')           |        97.534 | -0.289 |      0.007 |       0.164 |
| ('MNIST', 5, 'caseA', 'migration_impact', 'src')           |        99.809 | -0.028 |     -0.012 |       0.013 |
| ('MNIST', 5, 'caseA', 'migration_impact_global', 'dst')    |        19.341 | -0.057 |      0.001 |       0.033 |
| ('MNIST', 5, 'caseA', 'migration_impact_global', 'src')    |        21.11  | -0.006 |     -0.002 |       0.003 |
| ('MNIST', 5, 'caseA', 'migration_impact_premix', 'dst')    |        97.534 | -0.289 |      0.007 |       0.164 |
| ('MNIST', 5, 'caseA', 'migration_impact_premix', 'src')    |        99.809 | -0.028 |     -0.012 |       0.013 |
| ('MNIST', 5, 'caseB', 'migration_impact', 'dst')           |        97.261 | -0.324 |      0.194 |       0.246 |
| ('MNIST', 5, 'caseB', 'migration_impact', 'src')           |        99.772 | -0.02  |      0.02  |       0.029 |
| ('MNIST', 5, 'caseB', 'migration_impact_global', 'dst')    |        19.287 | -0.064 |      0.038 |       0.049 |
| ('MNIST', 5, 'caseB', 'migration_impact_global', 'src')    |        21.102 | -0.004 |      0.004 |       0.006 |
| ('MNIST', 5, 'caseB', 'migration_impact_premix', 'dst')    |        97.269 | -0.322 |      0.199 |       0.247 |
| ('MNIST', 5, 'caseB', 'migration_impact_premix', 'src')    |        99.772 | -0.02  |      0.017 |       0.028 |


## 5. Control-adjusted dst dip by cluster size M (data_changes, keep_weights)

|                     |   caseA |   caseB |
|:--------------------|--------:|--------:|
| ('CIFAR-10', 2, 3)  |   3.385 |   0.121 |
| ('CIFAR-10', 2, 4)  |   3.415 |   0.187 |
| ('CIFAR-10', 2, 5)  |   2.939 |  -0.107 |
| ('CIFAR-10', 2, 6)  |   2.865 |   0.935 |
| ('CIFAR-10', 2, 7)  |   2.319 |   0.408 |
| ('CIFAR-10', 2, 8)  |   2.043 |   0.623 |
| ('CIFAR-10', 2, 9)  |   1.299 |   0.237 |
| ('CIFAR-10', 2, 10) |   1.248 |   0.247 |
| ('CIFAR-10', 5, 3)  |   3.112 |   1.418 |
| ('CIFAR-10', 5, 4)  |   2.252 |   1.64  |
| ('CIFAR-10', 5, 5)  |   2.882 |   1.882 |
| ('CIFAR-10', 5, 6)  |   2.255 |   0.908 |
| ('CIFAR-10', 5, 7)  |   2.202 |   0.58  |
| ('CIFAR-10', 5, 8)  |   2.065 |   1.197 |
| ('CIFAR-10', 5, 9)  |   0.977 |   0.203 |
| ('CIFAR-10', 5, 10) |   0.653 |   0.847 |
| ('F-MNIST', 2, 3)   |   1.201 |   0.352 |
| ('F-MNIST', 2, 4)   |   1.527 |   0.48  |
| ('F-MNIST', 2, 5)   |   1.595 |   0.476 |
| ('F-MNIST', 2, 6)   |   1.047 |   0.385 |
| ('F-MNIST', 2, 7)   |   1.178 |   0.485 |
| ('F-MNIST', 2, 8)   |   1.004 |   0.521 |
| ('F-MNIST', 2, 9)   |   0.867 |   0.531 |
| ('F-MNIST', 2, 10)  |   1.201 |   0.547 |
| ('F-MNIST', 5, 3)   |   0.068 |   0.038 |
| ('F-MNIST', 5, 4)   |   0.075 |   0.035 |
| ('F-MNIST', 5, 5)   |   0.057 |   0.047 |
| ('F-MNIST', 5, 6)   |   0.072 |   0.027 |
| ('F-MNIST', 5, 7)   |   0     |   0.007 |
| ('F-MNIST', 5, 8)   |  -0.003 |   0.023 |
| ('F-MNIST', 5, 9)   |   0.003 |   0.022 |
| ('F-MNIST', 5, 10)  |  -0.007 |   0.002 |
| ('MNIST', 2, 3)     |   0.712 |   0.211 |
| ('MNIST', 2, 4)     |   1.124 |   0.398 |
| ('MNIST', 2, 5)     |   1.059 |   0.463 |
| ('MNIST', 2, 6)     |   1.001 |   0.507 |
| ('MNIST', 2, 7)     |   0.846 |   0.509 |
| ('MNIST', 2, 8)     |   0.628 |   0.389 |
| ('MNIST', 2, 9)     |   0.583 |   0.427 |
| ('MNIST', 2, 10)    |   0.517 |   0.422 |
| ('MNIST', 5, 3)     |   0.756 |   0.296 |
| ('MNIST', 5, 4)     |   0.506 |   0.415 |
| ('MNIST', 5, 5)     |   0.345 |   0.496 |
| ('MNIST', 5, 6)     |   0.254 |   0.161 |
| ('MNIST', 5, 7)     |   0.245 |   0.36  |
| ('MNIST', 5, 8)     |   0.227 |   0.444 |
| ('MNIST', 5, 9)     |   0.259 |   0.388 |
| ('MNIST', 5, 10)    |   0.013 |   0.333 |


## 6. Migrant sweep: control-adjusted dip vs number of migrants q (CIFAR-10, K=2, M=10)

|   num_migrants |   ('dst', 'caseA') |   ('dst', 'caseB') |   ('src', 'caseA') |   ('src', 'caseB') |
|---------------:|-------------------:|-------------------:|-------------------:|-------------------:|
|              1 |              0.219 |              0.194 |              0.213 |              0.093 |
|              2 |              0.145 |             -0.028 |              0.708 |              0.424 |
|              3 |              1.248 |              0.247 |              0.957 |              0.904 |
|              4 |              2.005 |              0.591 |              0.247 |              0.29  |
|              5 |              3.419 |              1.206 |              0.934 |              0.73  |
|              6 |              3.829 |              1.62  |              2.669 |              2.317 |
|              7 |              4.177 |              1.779 |              1.195 |              1.219 |
|              8 |              3.689 |              1.349 |              3.149 |              3.131 |
|              9 |              4.231 |              1.013 |             10.639 |             10.628 |


## 7. Sharing sweep: control-adjusted dip vs sharing 1-beta (CIFAR-10, K=2, M=10, q=5)

|   sharing |   ('migration_impact', 'dst') |   ('migration_impact', 'src') |   ('migration_impact_global', 'dst') |   ('migration_impact_global', 'src') |   ('migration_impact_premix', 'dst') |   ('migration_impact_premix', 'src') |
|----------:|------------------------------:|------------------------------:|-------------------------------------:|-------------------------------------:|-------------------------------------:|-------------------------------------:|
|      0    |                         3.419 |                         0.934 |                                1.709 |                                0.467 |                                3.419 |                                0.934 |
|      0.05 |                         1.759 |                         0.739 |                                0.879 |                                0.369 |                                1.767 |                                0.805 |
|      0.1  |                         1.206 |                         0.73  |                                0.603 |                                0.365 |                                1.261 |                                0.816 |
|      0.2  |                         0.713 |                         0.845 |                                0.356 |                                0.092 |                                0.775 |                                0.923 |
|      0.3  |                         0.648 |                         4.819 |                               -0.137 |                               -1.078 |                                0.657 |                                1.423 |
|      0.4  |                        -2.678 |                        -1.28  |                               -0.561 |                                0.151 |                                0.389 |                                0.447 |
|      0.5  |                         0.272 |                        -0.805 |                               -0.455 |                               -0.374 |                                0.559 |                                0.422 |


## 7b. Sharing sweep, raw values (before-mean, raw dip, control dip)

|   sharing |   ('before_mean', 'dst') |   ('before_mean', 'src') |   ('ctrl_dip', 'dst') |   ('ctrl_dip', 'src') |   ('dip', 'dst') |   ('dip', 'src') |
|----------:|-------------------------:|-------------------------:|----------------------:|----------------------:|-----------------:|-----------------:|
|      0    |                   85.831 |                   76.598 |                -1.217 |                -1.375 |            2.202 |           -0.441 |
|      0.05 |                   85.431 |                   76.123 |                -1.213 |                -1.453 |            0.546 |           -0.714 |
|      0.1  |                   85.095 |                   75.566 |                -1.249 |                -1.654 |           -0.043 |           -0.924 |
|      0.2  |                   84.442 |                   74.913 |                -1.476 |                -1.789 |           -0.763 |           -0.943 |
|      0.3  |                   84.11  |                   74.345 |                -1.512 |                -1.944 |           -0.864 |            2.875 |
|      0.4  |                   80.293 |                   70.597 |                 3.286 |                 2.439 |            0.608 |            1.159 |
|      0.5  |                   73.825 |                   64.559 |                -2.363 |                -2.446 |           -2.091 |           -3.251 |


## 8. Timing: migration at round 40 (= mixing round) vs 42 (CIFAR-10, K=2, M=10, keep_weights, dst)

|                                                    |   ('ex_dip', 'caseA') |   ('ex_dip', 'caseB') |   ('ex_max_drop', 'caseA') |   ('ex_max_drop', 'caseB') |
|:---------------------------------------------------|----------------------:|----------------------:|---------------------------:|---------------------------:|
| ('data_changes', 'migration_impact', 40)           |                 1.248 |                 0.247 |                      3.693 |                      1.48  |
| ('data_changes', 'migration_impact', 42)           |                 1.063 |                 0.38  |                      3.953 |                      2.1   |
| ('data_changes', 'migration_impact_global', 40)    |                 0.624 |                 0.124 |                      1.847 |                      0.74  |
| ('data_changes', 'migration_impact_global', 42)    |                 0.531 |                 0.19  |                      1.977 |                      1.05  |
| ('data_changes', 'migration_impact_premix', 40)    |                 1.248 |                 0.285 |                      3.693 |                      1.82  |
| ('data_changes', 'migration_impact_premix', 42)    |                 1.063 |                 0.374 |                      3.953 |                      2.1   |
| ('membership_only', 'migration_impact', 40)        |                13.067 |                15.62  |                     37.88  |                     51.62  |
| ('membership_only', 'migration_impact', 42)        |                12.841 |                15.121 |                     36.26  |                     72.387 |
| ('membership_only', 'migration_impact_global', 40) |                -3.921 |                -5.309 |                      2.26  |                      1.993 |
| ('membership_only', 'migration_impact_global', 42) |                -4.091 |                -4.831 |                      2.393 |                      2.62  |
| ('membership_only', 'migration_impact_premix', 40) |                13.067 |                14.907 |                     37.88  |                     51.8   |
| ('membership_only', 'migration_impact_premix', 42) |                12.841 |                15.098 |                     36.26  |                     72.387 |


## 9. Global test accuracy, mean of last 10 rounds

|                          |   final_mean |
|:-------------------------|-------------:|
| ('CIFAR-10', 2, 'caseA') |        45.5  |
| ('CIFAR-10', 2, 'caseB') |        45.9  |
| ('CIFAR-10', 5, 'caseA') |        19.37 |
| ('CIFAR-10', 5, 'caseB') |        19.19 |
| ('F-MNIST', 2, 'caseA')  |        55.62 |
| ('F-MNIST', 2, 'caseB')  |        56.54 |
| ('F-MNIST', 5, 'caseA')  |        26.98 |
| ('F-MNIST', 5, 'caseB')  |        26.89 |
| ('MNIST', 2, 'caseA')    |        65.66 |
| ('MNIST', 2, 'caseB')    |        65.39 |
| ('MNIST', 5, 'caseA')    |        26.19 |
| ('MNIST', 5, 'caseB')    |        25.76 |
