# Average-lock study (can we call the winning side late?)

Rounds with real results and full recordings: 19. Model: the last-minute average is partly known; remaining seconds = random walk (recent 1 s vol). Edge = model P - Kalshi ask - fee.

## 10 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 0 | | | | | |
| edge > 8c | 0 | | | | | |
| edge > 3c AND near target (within 1 sd) | 0 | | | | | |
| always bet model favourite | 0 | | | | | |
| near target only, always bet model favourite | 0 | | | | | |

## 20 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 0 | | | | | |
| edge > 8c | 0 | | | | | |
| edge > 3c AND near target (within 1 sd) | 0 | | | | | |
| always bet model favourite | 2 | 50.0% | 0.501 | -0.1% | 0.99 | 0.50 |
| near target only, always bet model favourite | 0 | | | | | |

## 30 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 3 | 0.0% | 0.020 | -100.0% | 0.84 | 0.02 |
| edge > 8c | 2 | 0.0% | 0.013 | -100.0% | 0.81 | 0.01 |
| edge > 3c AND near target (within 1 sd) | 1 | 0.0% | 0.014 | -100.0% | 0.74 | 0.01 |
| always bet model favourite | 4 | 25.0% | 0.264 | -5.5% | 0.88 | 0.26 |
| near target only, always bet model favourite | 1 | 0.0% | 0.014 | -100.0% | 0.74 | 0.01 |

## 45 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| edge > 8c | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| edge > 3c AND near target (within 1 sd) | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| always bet model favourite | 6 | 16.7% | 0.301 | -44.7% | 0.76 | 0.29 |
| near target only, always bet model favourite | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |

Calibration check (does the model's P match reality?): bucket by model P of the favourite
(left=20) P~0.95: 2 rounds, 50% won
