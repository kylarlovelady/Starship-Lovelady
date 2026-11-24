# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-24 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1015235.98 | 0.0290 / 0.0300 | 59838.03 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 14362.97 | 0.4000 / 0.4200 | 545.99 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 21.00 | 0.0100 / 0.0600 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 12327.69 | 0.0790 / 0.0850 | 0.055556 | CF Benchmarks |
| KXETH15M | ETH 15 min | 54410.89 | 0.2000 / 0.2100 | 1684.18 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 12665.05 | 0.1100 / 0.1200 | 62.9551 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 9290.88 | 0.0140 / 0.0150 | 2.9355 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 18701.71 | 0.0290 / 0.0310 | 70.6275 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 32114.04 | 0.0700 / 0.0710 | 0.9311 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 15877.54 | 0.0410 / 0.0490 | 741.4395 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 24, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 24, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2996 | 31.5 | 47% | 78% (2895) | 82% (2923) | 88% (2943) | 91% (2964) | 0.127 | 0.091 | 1015235.98 |
| KXBNB15M | 2995 | 31.5 | 48% | 79% (2907) | 84% (2919) | 90% (2952) | 92% (2971) | 0.118 | 0.080 | 14362.97 |
| KXDOGE15M | 2995 | 31.5 | 48% | 79% (2923) | 84% (2929) | 89% (2951) | 92% (2972) | 0.116 | 0.081 | 12327.69 |
| KXETH15M | 2994 | 31.5 | 48% | 79% (2914) | 83% (2920) | 89% (2960) | 92% (2974) | 0.123 | 0.084 | 54410.89 |
| KXHYPE15M | 2944 | 31.0 | 48% | 79% (2852) | 84% (2877) | 89% (2904) | 92% (2914) | 0.123 | 0.083 | 12665.05 |
| KXNEAR15M | 2944 | 31.0 | 47% | 80% (2864) | 83% (2894) | 88% (2914) | 92% (2923) | 0.121 | 0.083 | 9290.88 |
| KXSOL15M | 2943 | 31.0 | 48% | 79% (2850) | 84% (2890) | 88% (2910) | 91% (2915) | 0.119 | 0.086 | 18701.71 |
| KXXRP15M | 2943 | 31.0 | 49% | 79% (2871) | 83% (2872) | 88% (2908) | 92% (2921) | 0.121 | 0.087 | 32114.04 |
| KXZEC15M | 2942 | 31.0 | 48% | 79% (2862) | 82% (2883) | 89% (2908) | 92% (2918) | 0.126 | 0.083 | 15877.54 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1403) | 48% (1588) | 46% / 49% | 44% / 47% |
| KXBNB15M | 49% (1449) | 48% (1541) | 52% / 47% | 46% / 49% |
| KXDOGE15M | 47% (1446) | 50% (1544) | 47% / 50% | 46% / 50% |
| KXETH15M | 46% (1450) | 51% (1539) | 45% / 52% | 47% / 50% |
| KXHYPE15M | 48% (1418) | 49% (1521) | 49% / 47% | 47% / 50% |
| KXNEAR15M | 46% (1377) | 48% (1562) | 45% / 47% | 46% / 48% |
| KXSOL15M | 46% (1404) | 49% (1534) | 46% / 50% | 47% / 48% |
| KXXRP15M | 47% (1440) | 51% (1498) | 48% / 52% | 47% / 49% |
| KXZEC15M | 46% (1416) | 50% (1521) | 48% / 50% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 947 | 8% | 8c | +0c |
| KXBTC15M | 20-40c | 445 | 27% | 29c | -3c |
| KXBTC15M | 40-60c | 369 | 47% | 50c | -2c |
| KXBTC15M | 60-80c | 381 | 64% | 70c | -6c |
| KXBTC15M | 80-100c | 854 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 1006 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 384 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 327 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 354 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 924 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 993 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 372 | 29% | 29c | -0c |
| KXDOGE15M | 40-60c | 321 | 50% | 50c | -0c |
| KXDOGE15M | 60-80c | 372 | 66% | 70c | -4c |
| KXDOGE15M | 80-100c | 937 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 982 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 395 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 329 | 47% | 50c | -3c |
| KXETH15M | 60-80c | 395 | 68% | 70c | -2c |
| KXETH15M | 80-100c | 893 | 93% | 93c | -0c |
| KXHYPE15M | 0-20c | 978 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 375 | 27% | 29c | -2c |
| KXHYPE15M | 40-60c | 316 | 48% | 49c | -2c |
| KXHYPE15M | 60-80c | 340 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 935 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 989 | 7% | 7c | -1c |
| KXNEAR15M | 20-40c | 399 | 31% | 29c | +1c |
| KXNEAR15M | 40-60c | 307 | 43% | 50c | -6c |
| KXNEAR15M | 60-80c | 359 | 64% | 70c | -6c |
| KXNEAR15M | 80-100c | 890 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 969 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 394 | 28% | 29c | -1c |
| KXSOL15M | 40-60c | 301 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 360 | 66% | 70c | -5c |
| KXSOL15M | 80-100c | 919 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 984 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 343 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 331 | 49% | 49c | -0c |
| KXXRP15M | 60-80c | 345 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 940 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 955 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 372 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 343 | 50% | 50c | -1c |
| KXZEC15M | 60-80c | 347 | 64% | 71c | -7c |
| KXZEC15M | 80-100c | 925 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1072 | -9c (272) | +2c (315) | -11c / +5c | -6c / -2c |
| KXDOGE15M | 1072 | -5c (285) | +2c (353) | -6c / -2c | -5c / +6c |
| KXETH15M | 1119 | -4c (268) | +3c (308) | -5c / +0c | -3c / +7c |
| KXHYPE15M | 1044 | -6c (326) | -1c (352) | -5c / -2c | -7c / -0c |
| KXNEAR15M | 1074 | -5c (365) | +1c (361) | -5c / -0c | -5c / +2c |
| KXSOL15M | 1063 | -7c (286) | -0c (326) | -2c / -1c | -13c / -0c |
| KXXRP15M | 1031 | -4c (298) | +0c (349) | -1c / +2c | -7c / -1c |
| KXZEC15M | 1070 | -7c (321) | -0c (371) | -4c / -1c | -10c / +0c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
