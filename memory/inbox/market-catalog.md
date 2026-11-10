# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-10 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 752019.11 | 0.2000 / 0.2100 | 74219.78 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 4491.67 | 0.1600 / 0.1700 | 687.92 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 160.12 | 0.0000 / 0.1200 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 15756.63 | 0.1300 / 0.1400 | 0.069451 | CF Benchmarks |
| KXETH15M | ETH 15 min | 25731.38 | 0.1700 / 0.1800 | 2091.52 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 8691.09 | 0.0140 / 0.0190 | 74.0874 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6023.80 | 0.0110 / 0.0150 | 3.6026 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 56820.62 | 0.0050 / 0.0060 | 85.1413 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 40479.61 | 0.0690 / 0.0700 | 1.0806 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 6605.51 | 0.1800 / 0.1900 | 1144.3297 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 10, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 10, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1668 | 17.5 | 48% | 78% (1600) | 81% (1629) | 87% (1632) | 91% (1648) | 0.130 | 0.095 | 752019.11 |
| KXBNB15M | 1667 | 17.5 | 49% | 80% (1613) | 84% (1625) | 89% (1638) | 91% (1657) | 0.117 | 0.082 | 4491.67 |
| KXDOGE15M | 1667 | 17.5 | 48% | 80% (1622) | 85% (1629) | 89% (1646) | 92% (1653) | 0.111 | 0.079 | 15756.63 |
| KXETH15M | 1666 | 17.5 | 49% | 79% (1618) | 83% (1622) | 89% (1646) | 92% (1656) | 0.123 | 0.085 | 25731.38 |
| KXHYPE15M | 1616 | 17.0 | 48% | 80% (1573) | 85% (1585) | 89% (1595) | 92% (1603) | 0.117 | 0.079 | 8691.09 |
| KXNEAR15M | 1616 | 17.0 | 47% | 79% (1573) | 84% (1587) | 88% (1600) | 92% (1604) | 0.120 | 0.085 | 6023.80 |
| KXSOL15M | 1615 | 17.0 | 48% | 79% (1565) | 84% (1586) | 88% (1595) | 90% (1598) | 0.119 | 0.088 | 56820.62 |
| KXXRP15M | 1615 | 17.0 | 50% | 78% (1584) | 83% (1570) | 87% (1596) | 92% (1600) | 0.122 | 0.091 | 40479.61 |
| KXZEC15M | 1614 | 17.0 | 49% | 80% (1570) | 83% (1579) | 89% (1596) | 92% (1605) | 0.123 | 0.081 | 6605.51 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (798) | 50% (867) | 47% / 49% | 45% / 50% |
| KXBNB15M | 51% (824) | 47% (840) | 54% / 45% | 49% / 50% |
| KXDOGE15M | 47% (807) | 50% (857) | 48% / 49% | 46% / 51% |
| KXETH15M | 45% (811) | 52% (852) | 46% / 52% | 44% / 52% |
| KXHYPE15M | 49% (779) | 48% (834) | 49% / 49% | 48% / 48% |
| KXNEAR15M | 46% (758) | 48% (855) | 48% / 47% | 43% / 49% |
| KXSOL15M | 46% (772) | 50% (840) | 47% / 51% | 44% / 49% |
| KXXRP15M | 47% (806) | 53% (806) | 48% / 54% | 46% / 52% |
| KXZEC15M | 47% (786) | 50% (825) | 47% / 47% | 48% / 53% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 502 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 263 | 27% | 29c | -3c |
| KXBTC15M | 40-60c | 209 | 44% | 50c | -5c |
| KXBTC15M | 60-80c | 209 | 66% | 70c | -4c |
| KXBTC15M | 80-100c | 485 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 552 | 7% | 7c | -0c |
| KXBNB15M | 20-40c | 203 | 31% | 29c | +2c |
| KXBNB15M | 40-60c | 182 | 48% | 51c | -3c |
| KXBNB15M | 60-80c | 196 | 72% | 70c | +2c |
| KXBNB15M | 80-100c | 534 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 542 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 201 | 25% | 30c | -4c |
| KXDOGE15M | 40-60c | 181 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 207 | 65% | 71c | -6c |
| KXDOGE15M | 80-100c | 536 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 539 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 209 | 29% | 29c | +0c |
| KXETH15M | 40-60c | 191 | 49% | 50c | -1c |
| KXETH15M | 60-80c | 217 | 69% | 71c | -2c |
| KXETH15M | 80-100c | 510 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 534 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 194 | 24% | 29c | -5c |
| KXHYPE15M | 40-60c | 168 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 187 | 68% | 70c | -1c |
| KXHYPE15M | 80-100c | 533 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 527 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 222 | 32% | 29c | +2c |
| KXNEAR15M | 40-60c | 176 | 41% | 49c | -8c |
| KXNEAR15M | 60-80c | 198 | 64% | 70c | -7c |
| KXNEAR15M | 80-100c | 493 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 522 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 218 | 27% | 29c | -1c |
| KXSOL15M | 40-60c | 163 | 47% | 50c | -3c |
| KXSOL15M | 60-80c | 205 | 67% | 70c | -3c |
| KXSOL15M | 80-100c | 507 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 527 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 177 | 33% | 30c | +4c |
| KXXRP15M | 40-60c | 200 | 52% | 49c | +3c |
| KXXRP15M | 60-80c | 198 | 67% | 71c | -4c |
| KXXRP15M | 80-100c | 513 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 518 | 6% | 7c | -1c |
| KXZEC15M | 20-40c | 195 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 194 | 53% | 50c | +3c |
| KXZEC15M | 60-80c | 172 | 62% | 71c | -9c |
| KXZEC15M | 80-100c | 535 | 91% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 585 | -10c (157) | +4c (183) | -9c / -1c | -12c / +10c |
| KXDOGE15M | 593 | -4c (158) | -1c (205) | -10c / -6c | +1c / +4c |
| KXETH15M | 617 | -5c (147) | -1c (171) | -4c / -6c | -5c / +4c |
| KXHYPE15M | 556 | -4c (185) | -2c (184) | -2c / -9c | -6c / +5c |
| KXNEAR15M | 602 | -5c (209) | +0c (193) | -2c / -2c | -8c / +3c |
| KXSOL15M | 589 | -3c (163) | -2c (175) | -0c / -6c | -6c / +2c |
| KXXRP15M | 584 | -1c (174) | +3c (189) | +4c / -5c | -6c / +10c |
| KXZEC15M | 566 | -4c (172) | -1c (189) | -5c / -11c | -3c / +9c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
