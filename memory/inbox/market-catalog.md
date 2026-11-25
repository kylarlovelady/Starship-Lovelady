# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-25 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1069278.60 | 0.7200 / 0.7300 | 58864.34 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 13385.20 | 0.7500 / 0.7700 | 540.26 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0200 / 0.0600 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 39595.72 | 0.8200 / 0.8300 | 0.053933 | CF Benchmarks |
| KXETH15M | ETH 15 min | 72079.90 | 0.6900 / 0.7000 | 1642.82 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 11599.59 | 0.6000 / 0.6300 | 57.8906 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6442.77 | 0.7000 / 0.7300 | 2.8305 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 31744.36 | 0.6900 / 0.7100 | 67.6408 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 30905.16 | 0.5700 / 0.5900 | 0.913 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 10134.00 | 0.9000 / 0.9080 | 723.2732 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 25, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 25, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 3092 | 32.5 | 47% | 78% (2989) | 82% (3016) | 87% (3037) | 91% (3060) | 0.128 | 0.092 | 1069278.60 |
| KXBNB15M | 3091 | 32.5 | 48% | 79% (3002) | 84% (3014) | 89% (3043) | 92% (3066) | 0.120 | 0.082 | 13385.20 |
| KXDOGE15M | 3091 | 32.5 | 48% | 79% (3018) | 83% (3025) | 89% (3042) | 92% (3068) | 0.118 | 0.082 | 39595.72 |
| KXETH15M | 3090 | 32.5 | 49% | 79% (3008) | 83% (3013) | 89% (3055) | 92% (3068) | 0.124 | 0.085 | 72079.90 |
| KXHYPE15M | 3040 | 32.0 | 48% | 79% (2945) | 84% (2972) | 89% (2998) | 92% (3009) | 0.123 | 0.082 | 11599.59 |
| KXNEAR15M | 3040 | 32.0 | 47% | 80% (2959) | 84% (2987) | 88% (3010) | 92% (3017) | 0.121 | 0.083 | 6442.77 |
| KXSOL15M | 3039 | 32.0 | 48% | 79% (2943) | 84% (2984) | 88% (3006) | 91% (3010) | 0.120 | 0.086 | 31744.36 |
| KXXRP15M | 3039 | 32.0 | 49% | 78% (2964) | 83% (2964) | 88% (3000) | 92% (3014) | 0.122 | 0.088 | 30905.16 |
| KXZEC15M | 3038 | 32.0 | 48% | 79% (2952) | 82% (2976) | 88% (3004) | 92% (3013) | 0.126 | 0.083 | 10134.00 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1449) | 48% (1638) | 46% / 49% | 44% / 48% |
| KXBNB15M | 49% (1496) | 48% (1590) | 52% / 47% | 45% / 49% |
| KXDOGE15M | 47% (1492) | 50% (1594) | 48% / 49% | 46% / 50% |
| KXETH15M | 46% (1497) | 51% (1588) | 45% / 52% | 47% / 50% |
| KXHYPE15M | 48% (1461) | 49% (1574) | 49% / 47% | 46% / 50% |
| KXNEAR15M | 46% (1425) | 48% (1610) | 45% / 47% | 46% / 49% |
| KXSOL15M | 46% (1450) | 49% (1584) | 46% / 50% | 47% / 49% |
| KXXRP15M | 48% (1489) | 51% (1545) | 47% / 52% | 48% / 49% |
| KXZEC15M | 46% (1463) | 50% (1570) | 48% / 49% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 973 | 8% | 8c | +1c |
| KXBTC15M | 20-40c | 460 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 385 | 47% | 50c | -3c |
| KXBTC15M | 60-80c | 395 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 879 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 1033 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 396 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 339 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 378 | 69% | 71c | -1c |
| KXBNB15M | 80-100c | 945 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 1018 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 390 | 30% | 29c | +0c |
| KXDOGE15M | 40-60c | 337 | 50% | 50c | -0c |
| KXDOGE15M | 60-80c | 388 | 65% | 70c | -5c |
| KXDOGE15M | 80-100c | 958 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 1009 | 8% | 7c | +0c |
| KXETH15M | 20-40c | 407 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 344 | 47% | 50c | -3c |
| KXETH15M | 60-80c | 413 | 68% | 70c | -2c |
| KXETH15M | 80-100c | 917 | 93% | 93c | -0c |
| KXHYPE15M | 0-20c | 1014 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 389 | 27% | 30c | -2c |
| KXHYPE15M | 40-60c | 327 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 354 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 956 | 92% | 93c | -2c |
| KXNEAR15M | 0-20c | 1017 | 7% | 7c | -1c |
| KXNEAR15M | 20-40c | 416 | 30% | 29c | +1c |
| KXNEAR15M | 40-60c | 317 | 44% | 50c | -6c |
| KXNEAR15M | 60-80c | 372 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 918 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 999 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 404 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 315 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 377 | 65% | 70c | -5c |
| KXSOL15M | 80-100c | 944 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 1008 | 7% | 7c | +0c |
| KXXRP15M | 20-40c | 356 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 348 | 49% | 49c | -1c |
| KXXRP15M | 60-80c | 359 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 968 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 988 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 389 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 352 | 50% | 50c | -1c |
| KXZEC15M | 60-80c | 359 | 64% | 71c | -7c |
| KXZEC15M | 80-100c | 950 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1120 | -9c (285) | +2c (322) | -11c / +6c | -6c / -2c |
| KXDOGE15M | 1123 | -5c (302) | +3c (364) | -5c / -1c | -5c / +7c |
| KXETH15M | 1164 | -4c (280) | +3c (315) | -6c / +0c | -2c / +6c |
| KXHYPE15M | 1083 | -5c (343) | -1c (359) | -5c / -2c | -5c / +0c |
| KXNEAR15M | 1114 | -5c (375) | +1c (372) | -5c / -0c | -5c / +2c |
| KXSOL15M | 1104 | -7c (298) | -1c (333) | -3c / -1c | -11c / -1c |
| KXXRP15M | 1075 | -4c (309) | +1c (358) | -1c / +2c | -7c / -0c |
| KXZEC15M | 1108 | -7c (334) | +0c (380) | -5c / -1c | -10c / +1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
