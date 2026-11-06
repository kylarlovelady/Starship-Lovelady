# Hindsight / oracle study (last 7 days)

Rounds with a full recording, a strike and a real Kalshi result: **307** (149 UP, 158 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 307 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.1c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 33% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 76% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.77 (0.73 / 0.82)** | **0.85 (0.80 / 0.89)** | **0.89 (0.85 / 0.91)** | **0.93 (0.91 / 0.94)** | **0.98 (0.99 / 0.98)** | **1.00 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.74 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.58) | 0.51 (0.52 / 0.50) | 0.49 (0.50 / 0.48) | 0.52 (0.54 / 0.49) | 0.52 (0.49 / 0.54) | 0.53 (0.55 / 0.52) |
| mom 30s $ | **0.61 (0.62 / 0.61)** | 0.58 (0.61 / 0.56) | 0.54 (0.53 / 0.55) | 0.57 (0.66 / 0.46) | 0.58 (0.57 / 0.60) | 0.56 (0.54 / 0.58) |
| mom 60s $ | 0.58 (0.55 / 0.60) | **0.65 (0.65 / 0.65)** | 0.56 (0.58 / 0.55) | 0.56 (0.65 / 0.47) | **0.62 (0.62 / 0.60)** | **0.63 (0.61 / 0.65)** |
| kraken - coinbase $ | 0.48 (0.52 / 0.44) | 0.49 (0.48 / 0.52) | 0.52 (0.53 / 0.51) | 0.43 (0.32 / 0.55) | 0.42 (0.44 / 0.40) | 0.51 (0.48 / 0.55) |
| trade flow imbalance | 0.50 (0.49 / 0.51) | 0.48 (0.43 / 0.53) | 0.50 (0.51 / 0.51) | 0.53 (0.52 / 0.55) | 0.57 (0.58 / 0.56) | 0.55 (0.59 / 0.52) |
| coinbase book imbalance | 0.51 (0.69 / 0.41) | 0.47 (0.61 / 0.42) | 0.45 (0.55 / 0.39) | 0.50 (0.54 / 0.51) | 0.53 (0.64 / 0.48) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.48 (0.48 / 0.47) | 0.59 (0.57 / 0.61) | 0.45 (0.51 / 0.41) | **0.33 (0.29 / 0.37)** | **0.33 (0.35 / 0.30)** | **0.24 (0.31 / 0.19)** |
| kalshi mid (crowd) | **0.78 (0.72 / 0.83)** | **0.86 (0.80 / 0.91)** | **0.90 (0.87 / 0.92)** | **0.93 (0.91 / 0.94)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | -0.00 | +0.16 | +0.24 | +0.32 | +0.45 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.26 | +0.31 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.05 | -0.08 | -0.01 | +0.03 | +0.09 |
| mom 30s $ | +0.02 | +0.04 | +0.03 | +0.03 | +0.09 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.01 | -0.06 | +0.09 | +0.13 |
| kraken - coinbase $ | +0.02 | +0.05 | +0.05 | -0.09 | -0.18 | +0.10 |
| trade flow imbalance | +0.03 | -0.04 | -0.01 | +0.08 | +0.15 | +0.21 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.04 | +0.14 | -0.00 | -0.04 | -0.06 | -0.14 |
| kalshi mid (crowd) | -0.01 | +0.15 | +0.24 | +0.31 | +0.42 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 69 | 41% | +1.5% | 0.40 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3% | 0.18 |
| 420s | 0.20 | 3 | 0% | -100.0% | 0.09 |
| 300s | 0.05 | 77 | 25% | -4.3% | 0.26 |
| 300s | 0.10 | 36 | 19% | -4.6% | 0.20 |
| 300s | 0.20 | 2 | 50% | +411.5% | 0.10 |
| 180s | 0.05 | 63 | 29% | +1.9% | 0.28 |
| 180s | 0.10 | 32 | 31% | +30.1% | 0.24 |
| 180s | 0.20 | 1 | 100% | +490.3% | 0.17 |
| 90s | 0.05 | 66 | 17% | -11.6% | 0.19 |
| 90s | 0.10 | 35 | 11% | -23.3% | 0.15 |
| 90s | 0.20 | 6 | 0% | -100.0% | 0.09 |
| 45s | 0.05 | 35 | 23% | +42.0% | 0.16 |
| 45s | 0.10 | 33 | 24% | +52.9% | 0.16 |
| 45s | 0.20 | 21 | 14% | +4.1% | 0.14 |

## How much to trust this

- 307 rounds, many signals x checkpoints: a few will look good by luck. Only a signal that stays on the same side in both halves, at several checkpoints, deserves a real test.
- Hindsight always finds a great trade. The test that matters is walk-forward: pick the rule on older rounds, test it on newer ones, after fees.
- Practice only. Nothing here changes any setting.
