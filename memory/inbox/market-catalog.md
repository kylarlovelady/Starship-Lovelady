# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-26 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 975391.40 | 0.0140 / 0.0150 | 60742.49 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 23618.91 | 0.0040 / 0.0050 | 552.45 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 2.09 | 0.2200 / 0.4500 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 16364.77 | 0.1500 / 0.1800 | 0.05668 | CF Benchmarks |
| KXETH15M | ETH 15 min | 50157.73 | 0.0410 / 0.0430 | 1700.2 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 11820.23 | 0.0030 / 0.0060 | 61.4759 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 5559.54 | 0.0150 / 0.0170 | 3.0816 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 20037.29 | 0.0950 / 0.0960 | 70.8813 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 25878.08 | 0.0960 / 0.0970 | 0.9516 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 17546.55 | 0.0030 / 0.0040 | 739.7212 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 26, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 26, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 3180 | 33.5 | 47% | 78% (3073) | 82% (3103) | 87% (3124) | 91% (3148) | 0.127 | 0.092 | 975391.40 |
| KXBNB15M | 3179 | 33.5 | 49% | 79% (3085) | 84% (3101) | 89% (3130) | 92% (3151) | 0.120 | 0.082 | 23618.91 |
| KXDOGE15M | 3179 | 33.5 | 48% | 79% (3105) | 83% (3110) | 89% (3129) | 92% (3152) | 0.119 | 0.084 | 16364.77 |
| KXETH15M | 3178 | 33.5 | 49% | 78% (3093) | 83% (3098) | 88% (3142) | 92% (3155) | 0.124 | 0.086 | 50157.73 |
| KXHYPE15M | 3128 | 33.0 | 48% | 79% (3029) | 84% (3058) | 89% (3086) | 92% (3097) | 0.123 | 0.082 | 11820.23 |
| KXNEAR15M | 3128 | 33.0 | 47% | 79% (3046) | 83% (3073) | 88% (3096) | 92% (3102) | 0.121 | 0.083 | 5559.54 |
| KXSOL15M | 3127 | 33.0 | 48% | 79% (3028) | 84% (3071) | 88% (3093) | 91% (3096) | 0.120 | 0.086 | 20037.29 |
| KXXRP15M | 3127 | 33.0 | 49% | 79% (3051) | 83% (3051) | 88% (3086) | 92% (3101) | 0.122 | 0.088 | 25878.08 |
| KXZEC15M | 3126 | 33.0 | 48% | 79% (3039) | 82% (3064) | 88% (3092) | 92% (3099) | 0.126 | 0.083 | 17546.55 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1493) | 49% (1681) | 46% / 49% | 44% / 48% |
| KXBNB15M | 49% (1540) | 48% (1633) | 52% / 47% | 46% / 49% |
| KXDOGE15M | 47% (1539) | 50% (1634) | 48% / 49% | 46% / 50% |
| KXETH15M | 46% (1543) | 51% (1629) | 45% / 52% | 47% / 50% |
| KXHYPE15M | 48% (1504) | 49% (1618) | 49% / 48% | 46% / 50% |
| KXNEAR15M | 46% (1470) | 48% (1652) | 46% / 47% | 46% / 49% |
| KXSOL15M | 47% (1497) | 49% (1624) | 46% / 50% | 48% / 49% |
| KXXRP15M | 48% (1536) | 51% (1585) | 47% / 52% | 48% / 49% |
| KXZEC15M | 46% (1505) | 50% (1615) | 48% / 50% | 45% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 994 | 8% | 8c | +0c |
| KXBTC15M | 20-40c | 482 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 390 | 47% | 50c | -3c |
| KXBTC15M | 60-80c | 407 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 907 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 1061 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 410 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 348 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 393 | 69% | 70c | -1c |
| KXBNB15M | 80-100c | 967 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 1037 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 407 | 30% | 29c | +0c |
| KXDOGE15M | 40-60c | 351 | 50% | 50c | +0c |
| KXDOGE15M | 60-80c | 402 | 65% | 70c | -5c |
| KXDOGE15M | 80-100c | 982 | 93% | 93c | +1c |
| KXETH15M | 0-20c | 1033 | 8% | 7c | +0c |
| KXETH15M | 20-40c | 423 | 32% | 29c | +4c |
| KXETH15M | 40-60c | 354 | 47% | 50c | -3c |
| KXETH15M | 60-80c | 425 | 68% | 71c | -2c |
| KXETH15M | 80-100c | 943 | 93% | 93c | -0c |
| KXHYPE15M | 0-20c | 1044 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 400 | 28% | 30c | -2c |
| KXHYPE15M | 40-60c | 335 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 363 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 986 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 1043 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 427 | 30% | 29c | +1c |
| KXNEAR15M | 40-60c | 330 | 44% | 50c | -6c |
| KXNEAR15M | 60-80c | 384 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 944 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 1022 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 417 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 327 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 391 | 65% | 70c | -5c |
| KXSOL15M | 80-100c | 970 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 1033 | 7% | 7c | +0c |
| KXXRP15M | 20-40c | 371 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 356 | 49% | 49c | -0c |
| KXXRP15M | 60-80c | 367 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 1000 | 92% | 93c | -0c |
| KXZEC15M | 0-20c | 1013 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 405 | 28% | 29c | -1c |
| KXZEC15M | 40-60c | 358 | 50% | 50c | -0c |
| KXZEC15M | 60-80c | 375 | 64% | 71c | -7c |
| KXZEC15M | 80-100c | 975 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1158 | -8c (298) | +2c (334) | -11c / +4c | -6c / +0c |
| KXDOGE15M | 1168 | -6c (315) | +3c (383) | -5c / -2c | -6c / +9c |
| KXETH15M | 1202 | -4c (292) | +3c (329) | -5c / -1c | -3c / +7c |
| KXHYPE15M | 1112 | -5c (352) | -1c (371) | -4c / -2c | -7c / -0c |
| KXNEAR15M | 1150 | -5c (388) | +1c (386) | -6c / +1c | -5c / +2c |
| KXSOL15M | 1144 | -7c (311) | -1c (348) | -4c / -2c | -12c / -0c |
| KXXRP15M | 1107 | -4c (316) | +1c (371) | -2c / +3c | -5c / -1c |
| KXZEC15M | 1146 | -7c (346) | -0c (396) | -4c / -1c | -10c / +0c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
