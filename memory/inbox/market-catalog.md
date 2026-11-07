# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-07 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1001571.51 | 0.5300 / 0.5400 | 75878.36 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 12254.72 | 0.6500 / 0.6600 | 693.87 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 8.85 | 0.5300 / 0.6600 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 38331.34 | 0.9670 / 0.9730 | 0.071659 | CF Benchmarks |
| KXETH15M | ETH 15 min | 84928.19 | 0.9240 / 0.9250 | 2239.92 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 15033.06 | 0.7900 / 0.8000 | 78.2043 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 12924.89 | 0.5400 / 0.5600 | 3.6795 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 36317.49 | 0.6100 / 0.6200 | 89.6887 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 33637.53 | 0.8200 / 0.8300 | 1.167 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 17748.32 | 0.9000 / 0.9050 | 1286.9646 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 7, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 7, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1380 | 14.5 | 48% | 77% (1322) | 80% (1345) | 86% (1348) | 90% (1362) | 0.135 | 0.099 | 1001571.51 |
| KXBNB15M | 1379 | 14.5 | 49% | 80% (1334) | 85% (1343) | 89% (1359) | 91% (1372) | 0.117 | 0.084 | 12254.72 |
| KXDOGE15M | 1379 | 14.5 | 49% | 79% (1341) | 85% (1352) | 89% (1359) | 92% (1370) | 0.113 | 0.081 | 38331.34 |
| KXETH15M | 1378 | 14.5 | 49% | 79% (1333) | 83% (1338) | 89% (1362) | 92% (1370) | 0.125 | 0.085 | 84928.19 |
| KXHYPE15M | 1328 | 14.0 | 49% | 79% (1291) | 85% (1305) | 89% (1309) | 92% (1316) | 0.119 | 0.079 | 15033.06 |
| KXNEAR15M | 1328 | 14.0 | 47% | 79% (1293) | 83% (1305) | 88% (1317) | 92% (1318) | 0.123 | 0.086 | 12924.89 |
| KXSOL15M | 1328 | 14.0 | 48% | 80% (1288) | 85% (1302) | 89% (1311) | 90% (1317) | 0.116 | 0.084 | 36317.49 |
| KXXRP15M | 1328 | 14.0 | 51% | 78% (1305) | 83% (1290) | 87% (1312) | 92% (1314) | 0.123 | 0.093 | 33637.53 |
| KXZEC15M | 1328 | 14.0 | 49% | 80% (1290) | 83% (1300) | 88% (1313) | 92% (1320) | 0.122 | 0.082 | 17748.32 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 47% (659) | 49% (718) | 46% / 47% | 47% / 50% |
| KXBNB15M | 52% (681) | 46% (695) | 53% / 43% | 52% / 50% |
| KXDOGE15M | 48% (669) | 49% (707) | 47% / 49% | 49% / 49% |
| KXETH15M | 45% (671) | 52% (704) | 45% / 50% | 45% / 54% |
| KXHYPE15M | 49% (649) | 49% (676) | 50% / 47% | 49% / 50% |
| KXNEAR15M | 46% (620) | 47% (705) | 47% / 49% | 45% / 46% |
| KXSOL15M | 46% (638) | 51% (687) | 47% / 50% | 44% / 51% |
| KXXRP15M | 48% (670) | 53% (655) | 47% / 54% | 49% / 53% |
| KXZEC15M | 49% (655) | 50% (670) | 47% / 49% | 50% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 406 | 10% | 8c | +2c |
| KXBTC15M | 20-40c | 224 | 27% | 29c | -2c |
| KXBTC15M | 40-60c | 183 | 45% | 50c | -5c |
| KXBTC15M | 60-80c | 172 | 63% | 70c | -7c |
| KXBTC15M | 80-100c | 395 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 458 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 173 | 28% | 29c | -0c |
| KXBNB15M | 40-60c | 149 | 47% | 51c | -4c |
| KXBNB15M | 60-80c | 158 | 74% | 70c | +4c |
| KXBNB15M | 80-100c | 441 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 440 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 171 | 23% | 30c | -6c |
| KXDOGE15M | 40-60c | 150 | 47% | 50c | -3c |
| KXDOGE15M | 60-80c | 175 | 65% | 71c | -6c |
| KXDOGE15M | 80-100c | 443 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 440 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 175 | 31% | 29c | +2c |
| KXETH15M | 40-60c | 162 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 182 | 68% | 71c | -2c |
| KXETH15M | 80-100c | 419 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 419 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 171 | 23% | 29c | -6c |
| KXHYPE15M | 40-60c | 140 | 49% | 49c | -1c |
| KXHYPE15M | 60-80c | 159 | 70% | 70c | +0c |
| KXHYPE15M | 80-100c | 439 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 436 | 6% | 8c | -1c |
| KXNEAR15M | 20-40c | 182 | 31% | 30c | +2c |
| KXNEAR15M | 40-60c | 145 | 41% | 49c | -9c |
| KXNEAR15M | 60-80c | 161 | 63% | 70c | -7c |
| KXNEAR15M | 80-100c | 404 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 421 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 184 | 26% | 29c | -2c |
| KXSOL15M | 40-60c | 139 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 167 | 69% | 70c | -1c |
| KXSOL15M | 80-100c | 417 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 416 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 148 | 33% | 30c | +3c |
| KXXRP15M | 40-60c | 166 | 51% | 49c | +1c |
| KXXRP15M | 60-80c | 169 | 67% | 71c | -3c |
| KXXRP15M | 80-100c | 429 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 420 | 6% | 7c | -1c |
| KXZEC15M | 20-40c | 158 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 164 | 54% | 50c | +3c |
| KXZEC15M | 60-80c | 132 | 61% | 71c | -10c |
| KXZEC15M | 80-100c | 454 | 92% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 483 | -11c (125) | +6c (156) | -14c / -4c | -9c / +16c |
| KXDOGE15M | 499 | -7c (129) | -2c (171) | -14c / -6c | -1c / +3c |
| KXETH15M | 519 | -7c (115) | +1c (143) | -8c / -5c | -5c / +6c |
| KXHYPE15M | 476 | -5c (155) | -2c (161) | -5c / -9c | -4c / +4c |
| KXNEAR15M | 493 | -5c (173) | +0c (153) | -0c / +1c | -10c / -1c |
| KXSOL15M | 492 | -2c (134) | -1c (148) | +1c / -4c | -4c / +3c |
| KXXRP15M | 491 | -2c (142) | +2c (156) | +6c / -5c | -10c / +8c |
| KXZEC15M | 456 | -3c (129) | +0c (158) | -5c / -10c | -1c / +11c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
