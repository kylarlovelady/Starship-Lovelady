# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-08 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 748147.47 | 0.2000 / 0.2100 | 75772.49 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 14867.83 | 0.8700 / 0.8800 | 696.59 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0900 / 0.2200 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 29078.97 | 0.8600 / 0.8700 | 0.070742 | CF Benchmarks |
| KXETH15M | ETH 15 min | 63828.16 | 0.4000 / 0.4100 | 2231.59 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 10210.45 | 0.1600 / 0.1900 | 76.9347 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 9138.42 | 0.0910 / 0.0920 | 3.6995 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 32123.23 | 0.2600 / 0.2700 | 89.0128 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 24844.21 | 0.2500 / 0.2700 | 1.1589 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 15259.35 | 0.6300 / 0.6600 | 1259.3941 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 8, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 8, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1476 | 15.5 | 48% | 78% (1411) | 80% (1438) | 87% (1442) | 90% (1457) | 0.133 | 0.099 | 748147.47 |
| KXBNB15M | 1475 | 15.5 | 49% | 79% (1428) | 84% (1438) | 89% (1450) | 91% (1466) | 0.117 | 0.084 | 14867.83 |
| KXDOGE15M | 1475 | 15.5 | 48% | 80% (1436) | 85% (1444) | 89% (1455) | 93% (1465) | 0.110 | 0.079 | 29078.97 |
| KXETH15M | 1474 | 15.5 | 49% | 79% (1427) | 83% (1433) | 89% (1457) | 92% (1465) | 0.122 | 0.084 | 63828.16 |
| KXHYPE15M | 1424 | 15.0 | 49% | 79% (1386) | 85% (1399) | 89% (1405) | 92% (1412) | 0.118 | 0.079 | 10210.45 |
| KXNEAR15M | 1424 | 15.0 | 47% | 79% (1385) | 84% (1399) | 88% (1410) | 92% (1413) | 0.120 | 0.084 | 9138.42 |
| KXSOL15M | 1423 | 15.0 | 48% | 79% (1380) | 85% (1395) | 89% (1405) | 90% (1412) | 0.116 | 0.085 | 32123.23 |
| KXXRP15M | 1423 | 15.0 | 51% | 78% (1395) | 83% (1383) | 87% (1406) | 92% (1409) | 0.121 | 0.092 | 24844.21 |
| KXZEC15M | 1422 | 15.0 | 49% | 80% (1383) | 83% (1390) | 89% (1406) | 92% (1414) | 0.120 | 0.080 | 15259.35 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (703) | 49% (770) | 47% / 48% | 45% / 50% |
| KXBNB15M | 52% (729) | 47% (743) | 53% / 43% | 51% / 50% |
| KXDOGE15M | 47% (714) | 49% (758) | 47% / 49% | 47% / 50% |
| KXETH15M | 45% (715) | 52% (756) | 46% / 52% | 44% / 52% |
| KXHYPE15M | 49% (693) | 48% (728) | 50% / 48% | 48% / 49% |
| KXNEAR15M | 45% (665) | 48% (756) | 49% / 49% | 42% / 46% |
| KXSOL15M | 46% (685) | 51% (735) | 47% / 50% | 44% / 51% |
| KXXRP15M | 48% (718) | 53% (702) | 48% / 53% | 48% / 53% |
| KXZEC15M | 48% (699) | 50% (720) | 47% / 49% | 49% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 435 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 240 | 27% | 29c | -2c |
| KXBTC15M | 40-60c | 196 | 44% | 50c | -5c |
| KXBTC15M | 60-80c | 187 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 418 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 486 | 7% | 7c | +0c |
| KXBNB15M | 20-40c | 181 | 29% | 29c | +1c |
| KXBNB15M | 40-60c | 162 | 46% | 51c | -4c |
| KXBNB15M | 60-80c | 173 | 73% | 70c | +3c |
| KXBNB15M | 80-100c | 473 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 478 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 180 | 23% | 30c | -7c |
| KXDOGE15M | 40-60c | 161 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 181 | 66% | 71c | -4c |
| KXDOGE15M | 80-100c | 475 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 474 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 186 | 30% | 29c | +1c |
| KXETH15M | 40-60c | 175 | 46% | 50c | -3c |
| KXETH15M | 60-80c | 192 | 69% | 71c | -2c |
| KXETH15M | 80-100c | 447 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 458 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 178 | 24% | 29c | -6c |
| KXHYPE15M | 40-60c | 148 | 49% | 49c | -0c |
| KXHYPE15M | 60-80c | 173 | 70% | 70c | +0c |
| KXHYPE15M | 80-100c | 467 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 466 | 6% | 8c | -2c |
| KXNEAR15M | 20-40c | 199 | 30% | 30c | +1c |
| KXNEAR15M | 40-60c | 156 | 42% | 49c | -8c |
| KXNEAR15M | 60-80c | 168 | 65% | 70c | -6c |
| KXNEAR15M | 80-100c | 435 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 454 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 193 | 26% | 28c | -2c |
| KXSOL15M | 40-60c | 148 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 183 | 68% | 70c | -2c |
| KXSOL15M | 80-100c | 445 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 450 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 159 | 33% | 30c | +3c |
| KXXRP15M | 40-60c | 178 | 52% | 49c | +3c |
| KXXRP15M | 60-80c | 179 | 68% | 71c | -3c |
| KXXRP15M | 80-100c | 457 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 453 | 6% | 7c | -1c |
| KXZEC15M | 20-40c | 169 | 28% | 29c | -0c |
| KXZEC15M | 40-60c | 174 | 53% | 50c | +3c |
| KXZEC15M | 60-80c | 145 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 481 | 92% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 519 | -12c (133) | +5c (164) | -11c / -4c | -13c / +15c |
| KXDOGE15M | 525 | -6c (133) | -2c (182) | -12c / -6c | -1c / +3c |
| KXETH15M | 553 | -6c (124) | -0c (151) | -7c / -4c | -4c / +3c |
| KXHYPE15M | 505 | -3c (166) | -2c (168) | -4c / -9c | -2c / +4c |
| KXNEAR15M | 528 | -5c (180) | +1c (167) | -1c / +1c | -9c / +0c |
| KXSOL15M | 527 | -2c (142) | -1c (157) | -1c / -5c | -3c / +3c |
| KXXRP15M | 524 | -2c (149) | +2c (169) | +7c / -4c | -11c / +8c |
| KXZEC15M | 492 | -2c (140) | -1c (166) | -6c / -10c | +1c / +8c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
