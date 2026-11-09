# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-09 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 878227.65 | 0.0150 / 0.0160 | 74211.28 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 7294.44 | 0.0100 / 0.0110 | 680.89 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0200 / 0.1400 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 24737.20 | 0.0750 / 0.0770 | 0.068807 | CF Benchmarks |
| KXETH15M | ETH 15 min | 52257.71 | 0.0570 / 0.0620 | 2107.1 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 5812.54 | 0.0190 / 0.0200 | 73.0712 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 8270.73 | 0.0070 / 0.0110 | 3.5286 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 20966.12 | 0.0150 / 0.0170 | 86.1612 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 31523.41 | 0.0760 / 0.0840 | 1.0888 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 10933.42 | 0.0110 / 0.0220 | 1207.2587 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 9, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 9, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1572 | 16.5 | 48% | 78% (1504) | 81% (1533) | 87% (1536) | 90% (1553) | 0.132 | 0.097 | 878227.65 |
| KXBNB15M | 1571 | 16.5 | 49% | 79% (1520) | 84% (1532) | 89% (1545) | 91% (1562) | 0.117 | 0.083 | 7294.44 |
| KXDOGE15M | 1571 | 16.5 | 48% | 80% (1528) | 85% (1535) | 89% (1551) | 92% (1559) | 0.111 | 0.080 | 24737.20 |
| KXETH15M | 1570 | 16.5 | 49% | 79% (1522) | 83% (1526) | 89% (1553) | 92% (1561) | 0.124 | 0.086 | 52257.71 |
| KXHYPE15M | 1520 | 16.0 | 48% | 79% (1480) | 85% (1492) | 89% (1500) | 92% (1507) | 0.118 | 0.079 | 5812.54 |
| KXNEAR15M | 1520 | 16.0 | 47% | 79% (1479) | 84% (1494) | 88% (1505) | 92% (1509) | 0.121 | 0.085 | 8270.73 |
| KXSOL15M | 1519 | 16.0 | 48% | 79% (1471) | 85% (1491) | 88% (1500) | 90% (1504) | 0.117 | 0.086 | 20966.12 |
| KXXRP15M | 1519 | 16.0 | 50% | 78% (1489) | 83% (1476) | 87% (1500) | 92% (1505) | 0.123 | 0.092 | 31523.41 |
| KXZEC15M | 1518 | 16.0 | 49% | 80% (1476) | 83% (1484) | 89% (1502) | 92% (1510) | 0.123 | 0.081 | 10933.42 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (749) | 49% (820) | 47% / 49% | 45% / 49% |
| KXBNB15M | 52% (775) | 47% (793) | 53% / 44% | 51% / 49% |
| KXDOGE15M | 47% (761) | 49% (807) | 47% / 49% | 47% / 50% |
| KXETH15M | 46% (762) | 52% (805) | 46% / 52% | 45% / 51% |
| KXHYPE15M | 49% (731) | 47% (786) | 50% / 48% | 48% / 47% |
| KXNEAR15M | 45% (706) | 47% (811) | 48% / 49% | 42% / 46% |
| KXSOL15M | 46% (727) | 50% (789) | 47% / 50% | 45% / 49% |
| KXXRP15M | 47% (757) | 52% (759) | 49% / 54% | 46% / 51% |
| KXZEC15M | 48% (741) | 49% (774) | 47% / 48% | 50% / 51% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 464 | 9% | 8c | +2c |
| KXBTC15M | 20-40c | 257 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 201 | 44% | 50c | -6c |
| KXBTC15M | 60-80c | 199 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 451 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 519 | 7% | 7c | +0c |
| KXBNB15M | 20-40c | 195 | 31% | 29c | +2c |
| KXBNB15M | 40-60c | 170 | 46% | 51c | -4c |
| KXBNB15M | 60-80c | 181 | 73% | 70c | +3c |
| KXBNB15M | 80-100c | 506 | 92% | 93c | -1c |
| KXDOGE15M | 0-20c | 509 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 190 | 24% | 30c | -6c |
| KXDOGE15M | 40-60c | 171 | 49% | 50c | -1c |
| KXDOGE15M | 60-80c | 192 | 66% | 71c | -5c |
| KXDOGE15M | 80-100c | 509 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 507 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 195 | 30% | 29c | +1c |
| KXETH15M | 40-60c | 184 | 48% | 50c | -2c |
| KXETH15M | 60-80c | 206 | 68% | 71c | -2c |
| KXETH15M | 80-100c | 478 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 497 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 187 | 24% | 29c | -6c |
| KXHYPE15M | 40-60c | 158 | 48% | 49c | -1c |
| KXHYPE15M | 60-80c | 180 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 498 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 501 | 6% | 8c | -1c |
| KXNEAR15M | 20-40c | 208 | 31% | 30c | +1c |
| KXNEAR15M | 40-60c | 167 | 41% | 49c | -9c |
| KXNEAR15M | 60-80c | 184 | 64% | 70c | -7c |
| KXNEAR15M | 80-100c | 460 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 484 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 205 | 26% | 29c | -2c |
| KXSOL15M | 40-60c | 158 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 194 | 68% | 70c | -2c |
| KXSOL15M | 80-100c | 478 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 485 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 172 | 33% | 30c | +3c |
| KXXRP15M | 40-60c | 191 | 51% | 49c | +2c |
| KXXRP15M | 60-80c | 188 | 66% | 71c | -5c |
| KXXRP15M | 80-100c | 483 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 483 | 6% | 7c | -1c |
| KXZEC15M | 20-40c | 181 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 188 | 53% | 50c | +3c |
| KXZEC15M | 60-80c | 160 | 62% | 71c | -8c |
| KXZEC15M | 80-100c | 506 | 91% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 550 | -11c (144) | +6c (171) | -8c / -4c | -14c / +16c |
| KXDOGE15M | 557 | -5c (144) | -1c (194) | -10c / -6c | -1c / +4c |
| KXETH15M | 585 | -6c (135) | -0c (160) | -4c / -4c | -7c / +4c |
| KXHYPE15M | 532 | -5c (176) | -3c (176) | -3c / -9c | -7c / +4c |
| KXNEAR15M | 565 | -5c (196) | -0c (177) | -1c / -1c | -10c / +0c |
| KXSOL15M | 560 | -3c (154) | -1c (165) | -1c / -6c | -5c / +4c |
| KXXRP15M | 560 | -2c (164) | +2c (179) | +5c / -5c | -10c / +10c |
| KXZEC15M | 534 | -4c (156) | -1c (179) | -6c / -12c | -2c / +11c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
