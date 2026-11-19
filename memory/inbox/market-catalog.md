# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-19 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 848895.01 | 0.6700 / 0.6800 | 63756.71 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 14023.75 | 0.5600 / 0.5800 | 590.2 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 11.00 | 0.0100 / 0.1100 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 11153.11 | 0.8600 / 0.8700 | 0.059297 | CF Benchmarks |
| KXETH15M | ETH 15 min | 85585.05 | 0.8100 / 0.8300 | 1803.18 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 17528.75 | 0.5400 / 0.5500 | 68.3631 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6983.45 | 0.4800 / 0.4900 | 3.3961 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 32498.99 | 0.8800 / 0.8900 | 74.4107 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 46580.17 | 0.5300 / 0.5400 | 0.9807 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 22504.86 | 0.8400 / 0.8500 | 946.1977 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 19, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 19, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2516 | 26.5 | 47% | 78% (2429) | 82% (2455) | 87% (2471) | 91% (2490) | 0.128 | 0.092 | 848895.01 |
| KXBNB15M | 2515 | 26.5 | 49% | 79% (2437) | 84% (2453) | 89% (2479) | 92% (2497) | 0.120 | 0.082 | 14023.75 |
| KXDOGE15M | 2515 | 26.5 | 48% | 79% (2454) | 84% (2461) | 89% (2479) | 92% (2497) | 0.116 | 0.081 | 11153.11 |
| KXETH15M | 2514 | 26.5 | 48% | 79% (2441) | 83% (2449) | 89% (2482) | 92% (2497) | 0.123 | 0.084 | 85585.05 |
| KXHYPE15M | 2464 | 26.0 | 48% | 79% (2389) | 84% (2406) | 89% (2432) | 92% (2440) | 0.122 | 0.083 | 17528.75 |
| KXNEAR15M | 2464 | 26.0 | 47% | 79% (2400) | 83% (2423) | 88% (2440) | 92% (2445) | 0.121 | 0.082 | 6983.45 |
| KXSOL15M | 2463 | 26.0 | 48% | 79% (2388) | 84% (2423) | 88% (2434) | 91% (2438) | 0.120 | 0.086 | 32498.99 |
| KXXRP15M | 2463 | 26.0 | 49% | 79% (2408) | 83% (2404) | 88% (2434) | 92% (2445) | 0.120 | 0.089 | 46580.17 |
| KXZEC15M | 2462 | 26.0 | 49% | 79% (2393) | 82% (2413) | 88% (2433) | 92% (2440) | 0.127 | 0.084 | 22504.86 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1189) | 49% (1322) | 46% / 48% | 45% / 50% |
| KXBNB15M | 49% (1223) | 48% (1287) | 53% / 46% | 46% / 51% |
| KXDOGE15M | 46% (1211) | 50% (1299) | 48% / 48% | 44% / 52% |
| KXETH15M | 46% (1213) | 51% (1296) | 46% / 52% | 46% / 50% |
| KXHYPE15M | 48% (1188) | 49% (1271) | 50% / 48% | 46% / 50% |
| KXNEAR15M | 46% (1163) | 48% (1296) | 46% / 46% | 46% / 50% |
| KXSOL15M | 46% (1173) | 50% (1285) | 46% / 50% | 45% / 49% |
| KXXRP15M | 48% (1213) | 51% (1245) | 48% / 53% | 47% / 48% |
| KXZEC15M | 47% (1194) | 51% (1263) | 50% / 49% | 44% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 786 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 378 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 314 | 48% | 50c | -1c |
| KXBTC15M | 60-80c | 312 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 726 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 837 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 324 | 29% | 29c | -0c |
| KXBNB15M | 40-60c | 273 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 300 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 781 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 831 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 313 | 29% | 29c | -0c |
| KXDOGE15M | 40-60c | 269 | 47% | 50c | -3c |
| KXDOGE15M | 60-80c | 303 | 65% | 70c | -5c |
| KXDOGE15M | 80-100c | 799 | 93% | 93c | +0c |
| KXETH15M | 0-20c | 828 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 327 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 274 | 45% | 50c | -5c |
| KXETH15M | 60-80c | 324 | 69% | 70c | -1c |
| KXETH15M | 80-100c | 761 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 821 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 309 | 27% | 30c | -3c |
| KXHYPE15M | 40-60c | 269 | 49% | 50c | -1c |
| KXHYPE15M | 60-80c | 275 | 67% | 70c | -3c |
| KXHYPE15M | 80-100c | 790 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 827 | 7% | 7c | -1c |
| KXNEAR15M | 20-40c | 335 | 33% | 29c | +3c |
| KXNEAR15M | 40-60c | 247 | 43% | 50c | -7c |
| KXNEAR15M | 60-80c | 310 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 745 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 810 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 332 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 247 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 305 | 66% | 70c | -4c |
| KXSOL15M | 80-100c | 769 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 818 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 293 | 32% | 29c | +2c |
| KXXRP15M | 40-60c | 283 | 52% | 49c | +2c |
| KXXRP15M | 60-80c | 277 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 792 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 793 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 311 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 290 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 282 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 786 | 92% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 903 | -9c (234) | +3c (265) | -11c / +5c | -7c / +2c |
| KXDOGE15M | 890 | -5c (236) | +0c (294) | -8c / -3c | -2c / +4c |
| KXETH15M | 925 | -4c (220) | +2c (249) | -7c / +1c | -1c / +3c |
| KXHYPE15M | 864 | -6c (273) | -1c (290) | -3c / -4c | -9c / +3c |
| KXNEAR15M | 900 | -5c (310) | +2c (296) | -5c / -2c | -4c / +6c |
| KXSOL15M | 890 | -8c (242) | +0c (266) | -2c / -1c | -13c / +1c |
| KXXRP15M | 864 | -3c (249) | +2c (292) | +3c / +2c | -8c / +2c |
| KXZEC15M | 891 | -6c (260) | +0c (311) | -3c / -0c | -10c / +1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
