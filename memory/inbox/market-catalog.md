# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-28 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1106066.82 | 0.1400 / 0.1500 | 59266.28 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 19590.99 | 0.0260 / 0.0270 | 550.68 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 54.34 | 0.4700 / 0.5500 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 18200.14 | 0.0840 / 0.0950 | 0.056616 | CF Benchmarks |
| KXETH15M | ETH 15 min | 81921.19 | 0.0360 / 0.0370 | 1651.02 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 33074.71 | 0.0030 / 0.0070 | 62.9107 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 18511.51 | 0.0500 / 0.0550 | 2.9959 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 78567.52 | 0.0590 / 0.0600 | 70.8825 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 73899.12 | 0.1400 / 0.1500 | 0.9406 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 8178.42 | 0.0070 / 0.0080 | 730.6398 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 28, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 28, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 3372 | 35.5 | 47% | 78% (3255) | 82% (3288) | 87% (3311) | 91% (3338) | 0.128 | 0.093 | 1106066.82 |
| KXBNB15M | 3371 | 35.5 | 49% | 79% (3270) | 84% (3290) | 89% (3322) | 92% (3340) | 0.121 | 0.083 | 19590.99 |
| KXDOGE15M | 3371 | 35.5 | 49% | 79% (3290) | 84% (3297) | 89% (3316) | 92% (3342) | 0.118 | 0.083 | 18200.14 |
| KXETH15M | 3370 | 35.5 | 49% | 79% (3275) | 82% (3287) | 89% (3331) | 92% (3344) | 0.125 | 0.085 | 81921.19 |
| KXHYPE15M | 3320 | 35.0 | 48% | 79% (3213) | 84% (3244) | 89% (3277) | 92% (3287) | 0.122 | 0.082 | 33074.71 |
| KXNEAR15M | 3320 | 35.0 | 47% | 80% (3235) | 83% (3263) | 88% (3284) | 92% (3293) | 0.121 | 0.084 | 18511.51 |
| KXSOL15M | 3319 | 35.0 | 48% | 79% (3217) | 84% (3259) | 88% (3284) | 91% (3284) | 0.121 | 0.085 | 78567.52 |
| KXXRP15M | 3319 | 35.0 | 49% | 79% (3239) | 83% (3237) | 88% (3276) | 92% (3290) | 0.122 | 0.087 | 73899.12 |
| KXZEC15M | 3318 | 35.0 | 48% | 79% (3230) | 82% (3254) | 88% (3282) | 92% (3289) | 0.125 | 0.082 | 8178.42 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1593) | 49% (1773) | 46% / 50% | 45% / 48% |
| KXBNB15M | 49% (1643) | 48% (1722) | 51% / 47% | 47% / 49% |
| KXDOGE15M | 48% (1639) | 50% (1726) | 47% / 50% | 48% / 50% |
| KXETH15M | 46% (1637) | 51% (1727) | 45% / 52% | 48% / 50% |
| KXHYPE15M | 48% (1604) | 49% (1710) | 49% / 48% | 48% / 49% |
| KXNEAR15M | 46% (1567) | 48% (1747) | 46% / 48% | 47% / 48% |
| KXSOL15M | 47% (1597) | 49% (1716) | 46% / 50% | 48% / 49% |
| KXXRP15M | 48% (1636) | 51% (1677) | 47% / 53% | 49% / 49% |
| KXZEC15M | 46% (1601) | 50% (1711) | 48% / 50% | 45% / 50% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 1050 | 8% | 8c | +1c |
| KXBTC15M | 20-40c | 514 | 27% | 29c | -3c |
| KXBTC15M | 40-60c | 415 | 48% | 50c | -1c |
| KXBTC15M | 60-80c | 433 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 960 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 1108 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 443 | 29% | 29c | -0c |
| KXBNB15M | 40-60c | 378 | 49% | 50c | -1c |
| KXBNB15M | 60-80c | 416 | 69% | 70c | -1c |
| KXBNB15M | 80-100c | 1026 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 1083 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 441 | 29% | 29c | -0c |
| KXDOGE15M | 40-60c | 376 | 50% | 50c | +0c |
| KXDOGE15M | 60-80c | 435 | 66% | 70c | -4c |
| KXDOGE15M | 80-100c | 1036 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 1093 | 8% | 7c | +0c |
| KXETH15M | 20-40c | 454 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 381 | 47% | 50c | -3c |
| KXETH15M | 60-80c | 446 | 68% | 70c | -3c |
| KXETH15M | 80-100c | 996 | 93% | 93c | -0c |
| KXHYPE15M | 0-20c | 1100 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 423 | 28% | 29c | -2c |
| KXHYPE15M | 40-60c | 364 | 48% | 50c | -2c |
| KXHYPE15M | 60-80c | 392 | 70% | 70c | -0c |
| KXHYPE15M | 80-100c | 1041 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 1099 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 460 | 30% | 29c | +1c |
| KXNEAR15M | 40-60c | 353 | 44% | 50c | -6c |
| KXNEAR15M | 60-80c | 403 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 1005 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 1072 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 452 | 28% | 28c | -1c |
| KXSOL15M | 40-60c | 349 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 421 | 67% | 70c | -4c |
| KXSOL15M | 80-100c | 1025 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 1089 | 7% | 7c | +0c |
| KXXRP15M | 20-40c | 399 | 33% | 29c | +4c |
| KXXRP15M | 40-60c | 378 | 49% | 49c | -0c |
| KXXRP15M | 60-80c | 393 | 67% | 71c | -3c |
| KXXRP15M | 80-100c | 1060 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 1076 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 438 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 375 | 51% | 50c | +0c |
| KXZEC15M | 60-80c | 398 | 64% | 71c | -6c |
| KXZEC15M | 80-100c | 1031 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1245 | -9c (315) | +2c (363) | -11c / +4c | -7c / -0c |
| KXDOGE15M | 1260 | -5c (341) | +2c (413) | -4c / -1c | -6c / +6c |
| KXETH15M | 1281 | -4c (310) | +3c (351) | -6c / -0c | -3c / +7c |
| KXHYPE15M | 1194 | -6c (377) | -1c (397) | -5c / -1c | -6c / -0c |
| KXNEAR15M | 1227 | -6c (413) | +1c (412) | -5c / +0c | -7c / +2c |
| KXSOL15M | 1231 | -7c (335) | -1c (375) | -3c / -1c | -11c / -1c |
| KXXRP15M | 1183 | -3c (340) | +0c (395) | -1c / +3c | -4c / -3c |
| KXZEC15M | 1219 | -7c (369) | +0c (421) | -4c / -1c | -10c / +1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
