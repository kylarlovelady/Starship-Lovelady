# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-23 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 925617.48 | 0.8200 / 0.8300 | 61300.55 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 10350.74 | 0.4600 / 0.4800 | 556.17 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 6.00 | 0.0700 / 0.1600 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 14317.21 | 0.9560 / 0.9590 | 0.055403 | CF Benchmarks |
| KXETH15M | ETH 15 min | 108649.25 | 0.4400 / 0.4500 | 1721.42 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 10700.80 | 0.8900 / 0.9050 | 63.7648 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 17475.85 | 0.6800 / 0.7000 | 3.0055 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 31986.48 | 0.6300 / 0.6500 | 72.2065 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 48725.36 | 0.8100 / 0.8200 | 0.938 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 8448.45 | 0.4400 / 0.4600 | 791.8401 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 23, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 23, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2900 | 30.5 | 47% | 78% (2799) | 82% (2829) | 88% (2849) | 91% (2868) | 0.127 | 0.091 | 925617.48 |
| KXBNB15M | 2899 | 30.5 | 49% | 79% (2813) | 84% (2825) | 89% (2859) | 92% (2876) | 0.118 | 0.081 | 10350.74 |
| KXDOGE15M | 2899 | 30.5 | 48% | 79% (2830) | 84% (2834) | 89% (2857) | 92% (2877) | 0.115 | 0.081 | 14317.21 |
| KXETH15M | 2898 | 30.5 | 48% | 79% (2819) | 83% (2825) | 89% (2864) | 92% (2878) | 0.123 | 0.085 | 108649.25 |
| KXHYPE15M | 2848 | 30.0 | 48% | 79% (2763) | 84% (2782) | 89% (2809) | 92% (2820) | 0.122 | 0.083 | 10700.80 |
| KXNEAR15M | 2848 | 30.0 | 47% | 79% (2771) | 83% (2800) | 88% (2820) | 92% (2828) | 0.122 | 0.084 | 17475.85 |
| KXSOL15M | 2847 | 30.0 | 48% | 79% (2755) | 84% (2794) | 88% (2815) | 91% (2821) | 0.119 | 0.086 | 31986.48 |
| KXXRP15M | 2847 | 30.0 | 49% | 79% (2781) | 83% (2779) | 88% (2816) | 92% (2825) | 0.120 | 0.087 | 48725.36 |
| KXZEC15M | 2846 | 30.0 | 48% | 79% (2766) | 82% (2790) | 88% (2814) | 92% (2822) | 0.126 | 0.084 | 8448.45 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1358) | 48% (1537) | 46% / 49% | 45% / 48% |
| KXBNB15M | 49% (1404) | 48% (1490) | 52% / 47% | 46% / 49% |
| KXDOGE15M | 47% (1399) | 50% (1495) | 47% / 50% | 46% / 50% |
| KXETH15M | 46% (1402) | 51% (1491) | 45% / 52% | 47% / 50% |
| KXHYPE15M | 48% (1375) | 49% (1468) | 49% / 48% | 46% / 50% |
| KXNEAR15M | 46% (1336) | 48% (1507) | 45% / 48% | 46% / 48% |
| KXSOL15M | 46% (1366) | 50% (1476) | 46% / 51% | 47% / 49% |
| KXXRP15M | 48% (1403) | 51% (1439) | 48% / 53% | 47% / 49% |
| KXZEC15M | 46% (1373) | 50% (1468) | 48% / 50% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 912 | 8% | 8c | +0c |
| KXBTC15M | 20-40c | 430 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 360 | 47% | 50c | -3c |
| KXBTC15M | 60-80c | 367 | 64% | 70c | -6c |
| KXBTC15M | 80-100c | 831 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 972 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 367 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 314 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 346 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 900 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 960 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 357 | 29% | 29c | -0c |
| KXDOGE15M | 40-60c | 313 | 49% | 50c | -1c |
| KXDOGE15M | 60-80c | 359 | 66% | 70c | -4c |
| KXDOGE15M | 80-100c | 910 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 948 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 379 | 33% | 29c | +4c |
| KXETH15M | 40-60c | 320 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 384 | 68% | 70c | -2c |
| KXETH15M | 80-100c | 867 | 93% | 93c | -1c |
| KXHYPE15M | 0-20c | 948 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 361 | 27% | 29c | -2c |
| KXHYPE15M | 40-60c | 304 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 325 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 910 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 957 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 382 | 31% | 29c | +2c |
| KXNEAR15M | 40-60c | 295 | 43% | 50c | -7c |
| KXNEAR15M | 60-80c | 352 | 64% | 70c | -6c |
| KXNEAR15M | 80-100c | 862 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 934 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 378 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 295 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 346 | 66% | 70c | -5c |
| KXSOL15M | 80-100c | 894 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 951 | 7% | 7c | +0c |
| KXXRP15M | 20-40c | 334 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 316 | 51% | 50c | +1c |
| KXXRP15M | 60-80c | 334 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 912 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 915 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 362 | 28% | 29c | -0c |
| KXZEC15M | 40-60c | 330 | 51% | 50c | +0c |
| KXZEC15M | 60-80c | 338 | 63% | 71c | -7c |
| KXZEC15M | 80-100c | 901 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1034 | -9c (266) | +3c (299) | -12c / +5c | -6c / -1c |
| KXDOGE15M | 1036 | -5c (277) | +1c (336) | -6c / -2c | -5c / +5c |
| KXETH15M | 1083 | -4c (262) | +3c (293) | -7c / -0c | -2c / +7c |
| KXHYPE15M | 1003 | -6c (317) | -0c (330) | -3c / -2c | -9c / +2c |
| KXNEAR15M | 1038 | -5c (354) | +2c (345) | -5c / +1c | -5c / +2c |
| KXSOL15M | 1026 | -7c (277) | +0c (312) | -2c / -1c | -12c / +1c |
| KXXRP15M | 996 | -4c (289) | +2c (333) | -2c / +2c | -6c / +1c |
| KXZEC15M | 1038 | -7c (311) | +0c (358) | -3c / -1c | -11c / +2c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
