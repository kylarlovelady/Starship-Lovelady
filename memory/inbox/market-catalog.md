# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-21 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1559835.82 | 0.0370 / 0.0380 | 58043.13 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 11755.69 | 0.0200 / 0.0280 | 526.33 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 17.05 | 0.7900 / 0.8000 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 21408.73 | 0.0620 / 0.0700 | 0.053113 | CF Benchmarks |
| KXETH15M | ETH 15 min | 67787.58 | 0.0590 / 0.0600 | 1643.41 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 16597.28 | 0.0480 / 0.0640 | 58.7167 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 39823.53 | 0.5000 / 0.5200 | 2.7509 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 25640.19 | 0.0380 / 0.0400 | 68.2518 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 39824.48 | 0.1300 / 0.1400 | 0.8956 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 20399.96 | 0.1300 / 0.1400 | 746.2732 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 21, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 21, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2708 | 28.5 | 47% | 78% (2617) | 82% (2643) | 87% (2660) | 91% (2679) | 0.128 | 0.092 | 1559835.82 |
| KXBNB15M | 2707 | 28.5 | 48% | 79% (2626) | 84% (2636) | 89% (2670) | 92% (2687) | 0.119 | 0.082 | 11755.69 |
| KXDOGE15M | 2707 | 28.5 | 48% | 79% (2642) | 84% (2649) | 89% (2669) | 92% (2685) | 0.115 | 0.081 | 21408.73 |
| KXETH15M | 2706 | 28.5 | 48% | 79% (2627) | 83% (2636) | 89% (2672) | 92% (2688) | 0.123 | 0.085 | 67787.58 |
| KXHYPE15M | 2656 | 28.0 | 48% | 79% (2578) | 84% (2595) | 89% (2621) | 92% (2629) | 0.122 | 0.083 | 16597.28 |
| KXNEAR15M | 2656 | 28.0 | 47% | 79% (2584) | 83% (2610) | 88% (2630) | 92% (2636) | 0.121 | 0.083 | 39823.53 |
| KXSOL15M | 2655 | 28.0 | 48% | 79% (2572) | 84% (2606) | 88% (2623) | 91% (2630) | 0.121 | 0.087 | 25640.19 |
| KXXRP15M | 2655 | 28.0 | 49% | 79% (2594) | 83% (2590) | 88% (2625) | 92% (2634) | 0.120 | 0.088 | 39824.48 |
| KXZEC15M | 2654 | 28.0 | 48% | 80% (2577) | 82% (2603) | 89% (2625) | 92% (2630) | 0.125 | 0.083 | 20399.96 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1264) | 48% (1439) | 46% / 49% | 44% / 48% |
| KXBNB15M | 49% (1305) | 48% (1397) | 52% / 46% | 45% / 49% |
| KXDOGE15M | 46% (1295) | 50% (1407) | 48% / 49% | 44% / 50% |
| KXETH15M | 46% (1301) | 51% (1400) | 45% / 52% | 46% / 49% |
| KXHYPE15M | 47% (1271) | 49% (1380) | 49% / 49% | 45% / 49% |
| KXNEAR15M | 45% (1238) | 48% (1413) | 46% / 47% | 45% / 48% |
| KXSOL15M | 46% (1259) | 49% (1391) | 46% / 51% | 45% / 48% |
| KXXRP15M | 47% (1301) | 51% (1349) | 48% / 53% | 47% / 49% |
| KXZEC15M | 46% (1280) | 50% (1369) | 49% / 50% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 855 | 8% | 8c | +1c |
| KXBTC15M | 20-40c | 400 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 334 | 47% | 50c | -2c |
| KXBTC15M | 60-80c | 343 | 64% | 70c | -6c |
| KXBTC15M | 80-100c | 776 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 909 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 345 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 297 | 47% | 50c | -3c |
| KXBNB15M | 60-80c | 323 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 833 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 902 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 331 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 288 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 337 | 64% | 70c | -6c |
| KXDOGE15M | 80-100c | 849 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 894 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 344 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 304 | 44% | 50c | -5c |
| KXETH15M | 60-80c | 352 | 69% | 70c | -1c |
| KXETH15M | 80-100c | 812 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 895 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 335 | 27% | 29c | -2c |
| KXHYPE15M | 40-60c | 286 | 47% | 49c | -2c |
| KXHYPE15M | 60-80c | 297 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 843 | 92% | 93c | -2c |
| KXNEAR15M | 0-20c | 905 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 362 | 31% | 29c | +2c |
| KXNEAR15M | 40-60c | 266 | 43% | 50c | -6c |
| KXNEAR15M | 60-80c | 325 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 798 | 92% | 93c | -1c |
| KXSOL15M | 0-20c | 881 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 353 | 29% | 29c | -0c |
| KXSOL15M | 40-60c | 272 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 326 | 65% | 70c | -6c |
| KXSOL15M | 80-100c | 823 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 887 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 312 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 300 | 51% | 49c | +2c |
| KXXRP15M | 60-80c | 307 | 66% | 71c | -4c |
| KXXRP15M | 80-100c | 849 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 869 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 333 | 28% | 29c | -1c |
| KXZEC15M | 40-60c | 305 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 309 | 64% | 71c | -7c |
| KXZEC15M | 80-100c | 838 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 971 | -9c (256) | +3c (283) | -12c / +6c | -7c / -1c |
| KXDOGE15M | 961 | -5c (259) | +1c (314) | -7c / -2c | -4c / +4c |
| KXETH15M | 1000 | -5c (244) | +2c (270) | -7c / +1c | -2c / +3c |
| KXHYPE15M | 930 | -5c (298) | -1c (307) | -3c / -2c | -8c / +1c |
| KXNEAR15M | 962 | -5c (332) | +2c (314) | -5c / +0c | -5c / +4c |
| KXSOL15M | 957 | -7c (263) | +0c (287) | -2c / -1c | -13c / +1c |
| KXXRP15M | 930 | -4c (271) | +2c (315) | -0c / +2c | -8c / +2c |
| KXZEC15M | 955 | -7c (287) | +0c (330) | -2c / -1c | -11c / +2c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
