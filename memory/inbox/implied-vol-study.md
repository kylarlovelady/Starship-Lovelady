# Kalshi pricing study (implied volatility, calibration, spreads), last 4 days

Rounds with a full recording and a strike: **479** (414 with a real result).

Settlement = average of the last 60 index prices vs the strike (CF Benchmarks), so inside the last minute part of the answer is already locked in. Sigma below is in dollars per square-root-second.

## A. Implied vs realized volatility (only seconds where the price is between 5c and 95c and BTC is at least $1 from the strike)

| seconds left | samples | median implied sigma | median realized sigma (trailing 60 s) | median ratio implied/realized |
|---|---|---|---|---|
| 600-840 | 7601 | 4.95 | 5.70 | 0.86 |
| 420-600 | 8152 | 4.85 | 6.18 | 0.80 |
| 300-420 | 4750 | 4.65 | 5.85 | 0.79 |
| 180-300 | 3815 | 4.45 | 5.63 | 0.78 |
| 90-180 | 1993 | 3.75 | 5.58 | 0.68 |
| 45-90 | 494 | 3.04 | 6.05 | 0.51 |
| 15-45 | 55 | 2.45 | 6.16 | 0.38 |

Ratio near 1.0 = the market prices with the volatility Bitcoin is actually showing. Above 1 = the market assumes MORE movement than recent (cheaper favourite). Below 1 = it assumes less movement (dearer favourite). A ratio that changes a lot with time left shows how makers adjust near the close.

## B. Calibration: price said p (YES mid), how often did YES win? (one sample per round per checkpoint)

| left | YES mid bucket | rounds | YES won | avg mid | gap (won - mid) | profit per $ buying the CHEAPER side at its ask | profit per $ buying the DEARER side at its ask |
|---|---|---|---|---|---|---|---|
| 420s | 0-20c | 79 | 13% | 10c | +2c | +13.8% | -3.7% |
| 420s | 20-40c | 64 | 34% | 29c | +5c | +11.5% | -10.1% |
| 420s | 40-60c | 48 | 38% | 49c | -12c | -21.4% | +10.1% |
| 420s | 60-80c | 53 | 66% | 72c | -6c | +14.1% | -10.8% |
| 420s | 80-100c | 69 | 83% | 89c | -7c | +47.3% | -8.3% |
| 300s | 0-20c | 98 | 14% | 8c | +6c | +57.4% | -7.3% |
| 300s | 20-40c | 49 | 27% | 28c | -2c | -11.6% | -0.4% |
| 300s | 40-60c | 43 | 51% | 51c | +0c | +4.7% | -11.5% |
| 300s | 60-80c | 33 | 58% | 70c | -12c | +31.9% | -19.7% |
| 300s | 80-100c | 88 | 93% | 92c | +1c | -21.0% | +0.5% |
| 180s | 0-20c | 113 | 12% | 5c | +6c | +111.4% | -8.8% |
| 180s | 20-40c | 29 | 34% | 31c | +4c | +5.4% | -8.0% |
| 180s | 40-60c | 31 | 32% | 48c | -16c | +16.1% | -21.1% |
| 180s | 60-80c | 39 | 64% | 70c | -6c | +12.2% | -10.8% |
| 180s | 80-100c | 99 | 95% | 94c | +1c | -22.8% | +0.7% |
| 90s | 0-20c | 126 | 4% | 5c | -1c | -21.2% | +0.4% |
| 90s | 20-40c | 22 | 32% | 28c | +3c | +5.1% | -7.3% |
| 90s | 40-60c | 13 | 85% | 50c | +34c | -34.6% | +20.6% |
| 90s | 60-80c | 17 | 88% | 71c | +18c | -62.4% | +21.6% |
| 90s | 80-100c | 88 | 99% | 96c | +3c | -72.5% | +4.2% |
| 45s | 0-20c | 94 | 4% | 2c | +2c | +105.1% | -8.3% |
| 45s | 20-40c | 9 | 56% | 30c | +26c | +73.5% | -38.3% |
| 45s | 80-100c | 72 | 99% | 97c | +2c | -53.5% | +2.4% |

## C. What the quotes cost (ask minus bid, in cents)

| seconds left | samples | median spread | 90th percentile |
|---|---|---|---|
| 600-840 | 7995 | 1.0c | 1.0c |
| 420-600 | 8753 | 1.0c | 1.0c |
| 300-420 | 5864 | 1.0c | 1.0c |
| 180-300 | 5793 | 1.0c | 1.0c |
| 90-180 | 3909 | 0.1c | 1.0c |
| 45-90 | 1297 | 0.1c | 1.0c |
| 15-45 | 284 | 0.1c | 1.0c |

| BTC distance from strike | samples | median spread |
|---|---|---|
| $0-25 | 6804 | 1.0c |
| $25-50 | 5708 | 1.0c |
| $50-75 | 4456 | 1.0c |
| $75-100 | 2863 | 1.0c |
| $100-125 | 1773 | 1.0c |
| $125-150 | 1094 | 1.0c |
| $150-175 | 590 | 1.0c |
| $175-200 | 349 | 1.0c |
| $200-225 | 695 | 1.0c |

## Reading this

- Practice only; nothing here changes a setting. About 300 rounds: gaps under a few cents per bucket are noise.
- Look for a bias that repeats across time-left checkpoints and price buckets, and then test it forward on new rounds.
