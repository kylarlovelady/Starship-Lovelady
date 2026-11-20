# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-20 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1775287.22 | 0.9910 / 0.9920 | 61895.88 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 10286.19 | 0.9960 / 0.9970 | 572.67 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0000 / 0.0800 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 13581.41 | 0.9960 / 0.9970 | 0.057064 | CF Benchmarks |
| KXETH15M | ETH 15 min | 95839.01 | 0.9930 / 0.9940 | 1751.1 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 23831.79 | 0.9910 / 0.9940 | 65.0155 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 14797.28 | 0.9910 / 0.9940 | 3.0047 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 38503.67 | 0.9960 / 0.9970 | 72.0378 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 38101.81 | 0.9940 / 0.9950 | 0.9617 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 15169.76 | 0.9940 / 0.9950 | 835.3081 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 20, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 20, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2612 | 27.5 | 47% | 78% (2523) | 82% (2549) | 87% (2566) | 91% (2585) | 0.128 | 0.092 | 1775287.22 |
| KXBNB15M | 2611 | 27.5 | 49% | 79% (2532) | 84% (2545) | 89% (2575) | 92% (2592) | 0.119 | 0.082 | 10286.19 |
| KXDOGE15M | 2611 | 27.5 | 48% | 79% (2547) | 84% (2555) | 89% (2573) | 92% (2591) | 0.116 | 0.081 | 13581.41 |
| KXETH15M | 2610 | 27.5 | 48% | 79% (2535) | 83% (2543) | 89% (2577) | 92% (2592) | 0.123 | 0.085 | 95839.01 |
| KXHYPE15M | 2560 | 27.0 | 48% | 79% (2483) | 84% (2500) | 89% (2528) | 92% (2533) | 0.122 | 0.083 | 23831.79 |
| KXNEAR15M | 2560 | 27.0 | 47% | 79% (2492) | 83% (2516) | 88% (2535) | 92% (2541) | 0.122 | 0.083 | 14797.28 |
| KXSOL15M | 2559 | 27.0 | 48% | 79% (2482) | 84% (2516) | 88% (2529) | 91% (2534) | 0.121 | 0.087 | 38503.67 |
| KXXRP15M | 2559 | 27.0 | 49% | 79% (2499) | 83% (2495) | 88% (2530) | 92% (2540) | 0.120 | 0.088 | 38101.81 |
| KXZEC15M | 2558 | 27.0 | 48% | 79% (2485) | 82% (2508) | 88% (2529) | 92% (2536) | 0.126 | 0.084 | 15169.76 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1226) | 48% (1381) | 46% / 49% | 45% / 48% |
| KXBNB15M | 49% (1264) | 48% (1342) | 52% / 46% | 46% / 50% |
| KXDOGE15M | 46% (1248) | 50% (1358) | 48% / 49% | 44% / 50% |
| KXETH15M | 46% (1255) | 51% (1350) | 45% / 52% | 46% / 49% |
| KXHYPE15M | 48% (1232) | 49% (1323) | 50% / 49% | 46% / 49% |
| KXNEAR15M | 46% (1200) | 48% (1355) | 46% / 47% | 45% / 49% |
| KXSOL15M | 46% (1215) | 50% (1339) | 46% / 50% | 45% / 49% |
| KXXRP15M | 48% (1255) | 51% (1299) | 48% / 53% | 47% / 49% |
| KXZEC15M | 46% (1234) | 50% (1319) | 49% / 50% | 44% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 820 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 387 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 324 | 47% | 50c | -2c |
| KXBTC15M | 60-80c | 329 | 64% | 70c | -6c |
| KXBTC15M | 80-100c | 752 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 870 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 333 | 28% | 29c | -1c |
| KXBNB15M | 40-60c | 288 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 314 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 806 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 868 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 318 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 280 | 47% | 50c | -3c |
| KXDOGE15M | 60-80c | 325 | 64% | 70c | -6c |
| KXDOGE15M | 80-100c | 820 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 862 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 337 | 33% | 29c | +4c |
| KXETH15M | 40-60c | 285 | 44% | 50c | -6c |
| KXETH15M | 60-80c | 338 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 788 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 858 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 321 | 27% | 30c | -2c |
| KXHYPE15M | 40-60c | 276 | 48% | 50c | -1c |
| KXHYPE15M | 60-80c | 286 | 68% | 70c | -2c |
| KXHYPE15M | 80-100c | 819 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 865 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 350 | 32% | 29c | +3c |
| KXNEAR15M | 40-60c | 258 | 43% | 50c | -7c |
| KXNEAR15M | 60-80c | 319 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 768 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 845 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 344 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 259 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 314 | 66% | 70c | -5c |
| KXSOL15M | 80-100c | 797 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 850 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 301 | 33% | 29c | +3c |
| KXXRP15M | 40-60c | 295 | 51% | 50c | +1c |
| KXXRP15M | 60-80c | 291 | 66% | 71c | -5c |
| KXXRP15M | 80-100c | 822 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 830 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 324 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 297 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 299 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 808 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 941 | -9c (248) | +3c (274) | -11c / +5c | -7c / +0c |
| KXDOGE15M | 928 | -5c (252) | +0c (302) | -8c / -2c | -3c / +3c |
| KXETH15M | 960 | -4c (233) | +2c (258) | -7c / +0c | -1c / +3c |
| KXHYPE15M | 894 | -5c (286) | -1c (296) | -3c / -2c | -7c / +1c |
| KXNEAR15M | 935 | -5c (327) | +2c (303) | -5c / -1c | -5c / +6c |
| KXSOL15M | 923 | -7c (254) | -0c (274) | -2c / -1c | -12c / +1c |
| KXXRP15M | 898 | -3c (261) | +2c (303) | +0c / +2c | -7c / +2c |
| KXZEC15M | 928 | -7c (279) | +0c (320) | -2c / -1c | -11c / +1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
