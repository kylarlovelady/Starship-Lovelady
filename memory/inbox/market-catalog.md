# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-11 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1172597.55 | 0.9350 / 0.9360 | 73918.43 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 6463.90 | 0.8000 / 0.8100 | 680.86 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 18.00 | 0.3100 / 0.4300 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 12829.69 | 0.9700 / 0.9710 | 0.068226 | CF Benchmarks |
| KXETH15M | ETH 15 min | 39630.03 | 0.7200 / 0.7300 | 2060.07 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 12852.42 | 0.9630 / 0.9640 | 72.4353 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6523.89 | 0.9820 / 0.9830 | 3.6358 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 16540.97 | 0.9700 / 0.9710 | 83.7905 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 50890.07 | 0.9760 / 0.9800 | 1.0625 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 14418.92 | 0.6500 / 0.6800 | 995.3581 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 11, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 11, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1764 | 18.5 | 48% | 78% (1693) | 81% (1722) | 87% (1728) | 91% (1743) | 0.130 | 0.095 | 1172597.55 |
| KXBNB15M | 1763 | 18.5 | 49% | 79% (1709) | 84% (1719) | 89% (1734) | 91% (1752) | 0.116 | 0.082 | 6463.90 |
| KXDOGE15M | 1763 | 18.5 | 48% | 80% (1716) | 85% (1724) | 90% (1742) | 92% (1749) | 0.110 | 0.077 | 12829.69 |
| KXETH15M | 1762 | 18.5 | 49% | 79% (1711) | 83% (1715) | 89% (1740) | 92% (1752) | 0.122 | 0.084 | 39630.03 |
| KXHYPE15M | 1712 | 18.0 | 48% | 79% (1666) | 84% (1679) | 89% (1691) | 93% (1697) | 0.118 | 0.078 | 12852.42 |
| KXNEAR15M | 1712 | 18.0 | 47% | 79% (1666) | 84% (1682) | 88% (1696) | 92% (1700) | 0.120 | 0.084 | 6523.89 |
| KXSOL15M | 1711 | 18.0 | 48% | 79% (1660) | 85% (1681) | 88% (1689) | 90% (1693) | 0.118 | 0.088 | 16540.97 |
| KXXRP15M | 1711 | 18.0 | 50% | 78% (1676) | 83% (1665) | 87% (1690) | 92% (1696) | 0.121 | 0.089 | 50890.07 |
| KXZEC15M | 1710 | 18.0 | 49% | 80% (1662) | 83% (1674) | 89% (1692) | 92% (1698) | 0.122 | 0.080 | 14418.92 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (841) | 49% (920) | 47% / 49% | 45% / 50% |
| KXBNB15M | 51% (867) | 48% (893) | 53% / 45% | 48% / 50% |
| KXDOGE15M | 46% (854) | 50% (906) | 47% / 49% | 46% / 52% |
| KXETH15M | 45% (856) | 52% (903) | 47% / 53% | 44% / 51% |
| KXHYPE15M | 48% (827) | 48% (882) | 49% / 48% | 48% / 49% |
| KXNEAR15M | 46% (807) | 48% (902) | 48% / 46% | 44% / 50% |
| KXSOL15M | 45% (815) | 50% (893) | 46% / 50% | 45% / 50% |
| KXXRP15M | 47% (849) | 53% (859) | 48% / 53% | 46% / 52% |
| KXZEC15M | 48% (833) | 50% (874) | 47% / 48% | 48% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 532 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 276 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 219 | 45% | 50c | -5c |
| KXBTC15M | 60-80c | 224 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 513 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 588 | 7% | 7c | -0c |
| KXBNB15M | 20-40c | 215 | 32% | 29c | +3c |
| KXBNB15M | 40-60c | 186 | 47% | 51c | -3c |
| KXBNB15M | 60-80c | 212 | 71% | 71c | +1c |
| KXBNB15M | 80-100c | 562 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 574 | 5% | 7c | -2c |
| KXDOGE15M | 20-40c | 217 | 26% | 30c | -4c |
| KXDOGE15M | 40-60c | 187 | 49% | 50c | -1c |
| KXDOGE15M | 60-80c | 219 | 66% | 71c | -5c |
| KXDOGE15M | 80-100c | 566 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 571 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 221 | 29% | 29c | +1c |
| KXETH15M | 40-60c | 203 | 48% | 50c | -2c |
| KXETH15M | 60-80c | 225 | 68% | 71c | -3c |
| KXETH15M | 80-100c | 542 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 567 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 205 | 24% | 29c | -5c |
| KXHYPE15M | 40-60c | 180 | 50% | 49c | +1c |
| KXHYPE15M | 60-80c | 200 | 68% | 70c | -2c |
| KXHYPE15M | 80-100c | 560 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 563 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 229 | 31% | 29c | +2c |
| KXNEAR15M | 40-60c | 183 | 41% | 49c | -9c |
| KXNEAR15M | 60-80c | 213 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 524 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 553 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 233 | 27% | 29c | -2c |
| KXSOL15M | 40-60c | 173 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 216 | 67% | 70c | -4c |
| KXSOL15M | 80-100c | 536 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 561 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 189 | 33% | 30c | +4c |
| KXXRP15M | 40-60c | 209 | 53% | 49c | +4c |
| KXXRP15M | 60-80c | 211 | 66% | 71c | -4c |
| KXXRP15M | 80-100c | 541 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 548 | 6% | 7c | -1c |
| KXZEC15M | 20-40c | 209 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 204 | 52% | 50c | +2c |
| KXZEC15M | 60-80c | 184 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 565 | 92% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 617 | -11c (166) | +4c (193) | -9c / +0c | -14c / +10c |
| KXDOGE15M | 627 | -4c (167) | -1c (216) | -12c / -6c | +2c / +5c |
| KXETH15M | 649 | -6c (152) | -0c (180) | -5c / -2c | -7c / +2c |
| KXHYPE15M | 593 | -5c (194) | -1c (197) | -3c / -9c | -6c / +7c |
| KXNEAR15M | 631 | -5c (220) | +0c (203) | -2c / -2c | -7c / +3c |
| KXSOL15M | 625 | -4c (171) | -1c (186) | -1c / -4c | -7c / +2c |
| KXXRP15M | 618 | -3c (182) | +4c (199) | +4c / -5c | -10c / +13c |
| KXZEC15M | 602 | -4c (182) | -1c (201) | -6c / -9c | -2c / +10c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
