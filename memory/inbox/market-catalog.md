# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-22 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 841923.37 | 0.1900 / 0.2000 | 60786.43 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 11360.86 | 0.0630 / 0.0730 | 553 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 156.86 | 0.3700 / 0.4400 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 10243.20 | 0.2000 / 0.2100 | 0.055498 | CF Benchmarks |
| KXETH15M | ETH 15 min | 59279.72 | 0.4400 / 0.4600 | 1708.12 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 7393.24 | 0.1900 / 0.2000 | 62.4303 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 12433.45 | 0.2000 / 0.2100 | 2.9784 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 23395.63 | 0.2600 / 0.2700 | 70.4905 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 40455.67 | 0.5000 / 0.5200 | 0.9327 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 13488.14 | 0.1400 / 0.1500 | 799.6756 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 22, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 22, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2804 | 29.5 | 47% | 78% (2707) | 82% (2738) | 87% (2756) | 91% (2774) | 0.127 | 0.092 | 841923.37 |
| KXBNB15M | 2803 | 29.5 | 48% | 79% (2719) | 84% (2730) | 89% (2764) | 92% (2781) | 0.119 | 0.081 | 11360.86 |
| KXDOGE15M | 2803 | 29.5 | 48% | 79% (2736) | 84% (2742) | 89% (2761) | 92% (2781) | 0.115 | 0.081 | 10243.20 |
| KXETH15M | 2802 | 29.5 | 48% | 79% (2723) | 83% (2730) | 89% (2768) | 92% (2782) | 0.123 | 0.085 | 59279.72 |
| KXHYPE15M | 2752 | 29.0 | 48% | 79% (2670) | 84% (2689) | 89% (2716) | 92% (2725) | 0.121 | 0.082 | 7393.24 |
| KXNEAR15M | 2752 | 29.0 | 47% | 79% (2678) | 83% (2705) | 88% (2725) | 92% (2732) | 0.121 | 0.084 | 12433.45 |
| KXSOL15M | 2751 | 29.0 | 48% | 79% (2665) | 84% (2701) | 88% (2719) | 91% (2726) | 0.119 | 0.086 | 23395.63 |
| KXXRP15M | 2751 | 29.0 | 49% | 79% (2687) | 84% (2686) | 88% (2720) | 92% (2729) | 0.119 | 0.087 | 40455.67 |
| KXZEC15M | 2750 | 29.0 | 48% | 80% (2672) | 82% (2695) | 89% (2721) | 92% (2726) | 0.126 | 0.083 | 13488.14 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1312) | 48% (1487) | 47% / 49% | 44% / 48% |
| KXBNB15M | 49% (1357) | 48% (1441) | 52% / 47% | 45% / 49% |
| KXDOGE15M | 47% (1349) | 50% (1449) | 47% / 49% | 46% / 50% |
| KXETH15M | 46% (1353) | 51% (1444) | 45% / 52% | 46% / 50% |
| KXHYPE15M | 48% (1325) | 49% (1422) | 49% / 48% | 47% / 49% |
| KXNEAR15M | 46% (1289) | 48% (1458) | 46% / 47% | 46% / 49% |
| KXSOL15M | 46% (1315) | 50% (1431) | 45% / 51% | 47% / 49% |
| KXXRP15M | 48% (1355) | 51% (1391) | 48% / 54% | 47% / 49% |
| KXZEC15M | 46% (1328) | 50% (1417) | 49% / 50% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 883 | 8% | 8c | +1c |
| KXBTC15M | 20-40c | 418 | 26% | 29c | -4c |
| KXBTC15M | 40-60c | 345 | 47% | 50c | -3c |
| KXBTC15M | 60-80c | 351 | 64% | 70c | -6c |
| KXBTC15M | 80-100c | 807 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 938 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 358 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 306 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 332 | 69% | 71c | -1c |
| KXBNB15M | 80-100c | 869 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 930 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 342 | 29% | 29c | -0c |
| KXDOGE15M | 40-60c | 299 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 349 | 65% | 70c | -5c |
| KXDOGE15M | 80-100c | 883 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 918 | 8% | 7c | +0c |
| KXETH15M | 20-40c | 363 | 33% | 29c | +4c |
| KXETH15M | 40-60c | 311 | 45% | 50c | -5c |
| KXETH15M | 60-80c | 368 | 68% | 70c | -2c |
| KXETH15M | 80-100c | 842 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 921 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 349 | 27% | 30c | -2c |
| KXHYPE15M | 40-60c | 295 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 304 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 883 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 930 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 372 | 31% | 29c | +2c |
| KXNEAR15M | 40-60c | 281 | 44% | 50c | -6c |
| KXNEAR15M | 60-80c | 337 | 64% | 70c | -6c |
| KXNEAR15M | 80-100c | 832 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 909 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 366 | 29% | 29c | +0c |
| KXSOL15M | 40-60c | 277 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 337 | 66% | 70c | -5c |
| KXSOL15M | 80-100c | 862 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 920 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 320 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 305 | 51% | 49c | +1c |
| KXXRP15M | 60-80c | 320 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 886 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 889 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 351 | 28% | 29c | -1c |
| KXZEC15M | 40-60c | 318 | 50% | 50c | +0c |
| KXZEC15M | 60-80c | 320 | 64% | 71c | -7c |
| KXZEC15M | 80-100c | 872 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1003 | -9c (261) | +3c (293) | -12c / +5c | -7c / -1c |
| KXDOGE15M | 995 | -6c (267) | +2c (327) | -7c / -2c | -5c / +5c |
| KXETH15M | 1042 | -5c (252) | +3c (282) | -7c / +1c | -2c / +5c |
| KXHYPE15M | 960 | -6c (304) | -0c (319) | -4c / -2c | -7c / +1c |
| KXNEAR15M | 999 | -5c (345) | +2c (329) | -5c / +0c | -5c / +4c |
| KXSOL15M | 986 | -7c (270) | +0c (298) | -2c / -1c | -13c / +1c |
| KXXRP15M | 956 | -4c (279) | +2c (323) | -1c / +2c | -6c / +2c |
| KXZEC15M | 997 | -8c (297) | +1c (348) | -2c / -1c | -13c / +2c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
