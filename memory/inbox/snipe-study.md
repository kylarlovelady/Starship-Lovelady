# Sniping study (recorded per-second data, last 5 days)

Rounds with a full recording: 362


## Part 1: seconds left on the clock at the LAST second the market was still open

| left at last recorded second | rounds | share |
|---|---|---|
| 0-2 s | 2 | 1% |
| 2-5 s | 2 | 1% |
| 5-10 s | 8 | 2% |
| 10-30 s | 36 | 10% |
| 30-120 s | 229 | 63% |
| >120 s | 85 | 23% |

Median seconds left at last open second: 70.0 (a high number means Kalshi stopped quoting before the clock ran out, or our recorder missed the last seconds).

Examples of rounds that stopped with more than 10 s left: left 90s, YES bid 1.00 / NO bid 0.00; left 183s, YES bid 0.01 / NO bid 0.99; left 32s, YES bid 0.00 / NO bid 1.00; left 62s, YES bid 0.00 / NO bid 1.00; left 198s, YES bid 0.13 / NO bid 0.86; left 115s, YES bid 0.00 / NO bid 1.00; left 128s, YES bid 0.00 / NO bid 1.00; left 144s, YES bid 1.00 / NO bid 0.00; left 17s, YES bid 1.00 / NO bid 0.00; left 75s, YES bid 0.00 / NO bid 1.00; left 18s, YES bid 1.00 / NO bid 0.00; left 38s, YES bid 0.00 / NO bid 1.00

Rounds with a real settled result in history: 267 of 362

## Part 2: buy the favourite at the last tick that still had at least B seconds left, hold to the result

### B = 3 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 5 | 40.0% | 0.593 | -32.6% | $866 |
| 60-64c | 1 | 100.0% | 0.656 | +52.4% | $1392 |
| 65-69c | 1 | 100.0% | 0.666 | +50.2% | $1492 |
| 70-74c | 3 | 66.7% | 0.734 | -9.2% | $192 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 7 | 85.7% | 0.836 | +2.6% | $1937 |
| 85-89c | 5 | 60.0% | 0.887 | -32.4% | $2778 |
| 90-94c | 16 | 93.8% | 0.927 | +1.1% | $231 |
| 95-99c | 40 | 97.5% | 0.982 | -0.7% | $965 |
| ALL | 81 | | | -3.0% | |

### B = 5 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 5 | 40.0% | 0.593 | -32.6% | $866 |
| 60-64c | 1 | 100.0% | 0.656 | +52.4% | $1392 |
| 65-69c | 2 | 50.0% | 0.685 | -27.1% | $764 |
| 70-74c | 2 | 50.0% | 0.724 | -31.0% | $943 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 7 | 85.7% | 0.836 | +2.6% | $1937 |
| 85-89c | 6 | 66.7% | 0.884 | -24.6% | $1762 |
| 90-94c | 15 | 93.3% | 0.928 | +0.6% | $241 |
| 95-99c | 41 | 97.6% | 0.982 | -0.6% | $902 |
| ALL | 82 | | | -4.2% | |

### B = 10 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 6 | 33.3% | 0.594 | -43.9% | $667 |
| 60-64c | 2 | 100.0% | 0.656 | +52.4% | $786 |
| 65-69c | 1 | 100.0% | 0.666 | +50.2% | $1492 |
| 70-74c | 3 | 66.7% | 0.731 | -8.8% | $192 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 7 | 85.7% | 0.836 | +2.6% | $1937 |
| 85-89c | 5 | 60.0% | 0.887 | -32.4% | $2778 |
| 90-94c | 16 | 93.8% | 0.929 | +0.9% | $290 |
| 95-99c | 41 | 97.6% | 0.982 | -0.6% | $902 |
| ALL | 84 | | | -3.3% | |

### B = 20 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 50-54c | 2 | 0.0% | 0.557 | -100.0% | $215 |
| 55-59c | 5 | 40.0% | 0.593 | -32.6% | $866 |
| 60-64c | 2 | 100.0% | 0.656 | +52.4% | $786 |
| 65-69c | 2 | 100.0% | 0.666 | +50.2% | $1154 |
| 70-74c | 2 | 50.0% | 0.724 | -31.0% | $943 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 8 | 87.5% | 0.837 | +4.5% | $1150 |
| 85-89c | 6 | 50.0% | 0.886 | -43.6% | $1762 |
| 90-94c | 13 | 92.3% | 0.928 | -0.5% | $241 |
| 95-99c | 43 | 95.3% | 0.981 | -2.8% | $902 |
| ALL | 86 | | | -6.2% | |

### B = 40 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 50-54c | 2 | 50.0% | 0.542 | -7.8% | $170 |
| 55-59c | 7 | 57.1% | 0.593 | -3.6% | $866 |
| 60-64c | 1 | 100.0% | 0.656 | +52.4% | $1392 |
| 65-69c | 4 | 75.0% | 0.678 | +10.6% | $1154 |
| 70-74c | 4 | 50.0% | 0.737 | -32.1% | $115 |
| 75-79c | 7 | 57.1% | 0.787 | -27.3% | $961 |
| 80-84c | 8 | 87.5% | 0.832 | +5.2% | $1150 |
| 85-89c | 9 | 66.7% | 0.881 | -24.3% | $745 |
| 90-94c | 17 | 88.2% | 0.926 | -4.7% | $50 |
| 95-99c | 51 | 100.0% | 0.982 | +1.8% | $552 |
| ALL | 110 | | | -3.6% | |

### B = 60 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 50-54c | 3 | 66.7% | 0.541 | +23.3% | $142 |
| 55-59c | 9 | 77.8% | 0.594 | +31.0% | $866 |
| 60-64c | 4 | 75.0% | 0.639 | +17.4% | $1075 |
| 65-69c | 5 | 60.0% | 0.682 | -12.0% | $1492 |
| 70-74c | 5 | 80.0% | 0.730 | +9.6% | $205 |
| 75-79c | 9 | 55.6% | 0.776 | -28.4% | $283 |
| 80-84c | 9 | 77.8% | 0.837 | -7.0% | $1937 |
| 85-89c | 11 | 81.8% | 0.879 | -6.9% | $2778 |
| 90-94c | 27 | 88.9% | 0.929 | -4.4% | $400 |
| 95-99c | 65 | 98.5% | 0.981 | +0.4% | $932 |
| ALL | 147 | | | -1.3% | |

