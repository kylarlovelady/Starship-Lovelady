# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-13 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1209033.61 | 0.7300 / 0.7400 | 69225.46 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 19372.82 | 0.4100 / 0.4200 | 638.55 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0000 / 0.0200 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 17619.31 | 0.1900 / 0.2100 | 0.065074 | CF Benchmarks |
| KXETH15M | ETH 15 min | 71205.04 | 0.6500 / 0.6600 | 1948.98 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 16519.92 | 0.9090 / 0.9180 | 72.4917 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 10731.29 | 0.2100 / 0.2200 | 3.483 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 30622.08 | 0.1400 / 0.1500 | 80.431 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 59862.97 | 0.0070 / 0.0090 | 1.0275 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 9316.21 | 0.2600 / 0.2800 | 944.857 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 13, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 13, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1948 | 20.5 | 47% | 78% (1871) | 81% (1899) | 87% (1909) | 91% (1926) | 0.129 | 0.095 | 1209033.61 |
| KXBNB15M | 1947 | 20.5 | 49% | 79% (1884) | 84% (1901) | 89% (1914) | 92% (1935) | 0.118 | 0.083 | 19372.82 |
| KXDOGE15M | 1947 | 20.5 | 48% | 80% (1897) | 85% (1903) | 89% (1924) | 92% (1931) | 0.112 | 0.079 | 17619.31 |
| KXETH15M | 1946 | 20.5 | 48% | 79% (1889) | 83% (1894) | 89% (1921) | 92% (1935) | 0.123 | 0.084 | 71205.04 |
| KXHYPE15M | 1896 | 20.0 | 48% | 79% (1836) | 84% (1860) | 89% (1874) | 93% (1880) | 0.119 | 0.079 | 16519.92 |
| KXNEAR15M | 1896 | 20.0 | 47% | 79% (1845) | 83% (1863) | 88% (1879) | 92% (1884) | 0.120 | 0.084 | 10731.29 |
| KXSOL15M | 1895 | 20.0 | 48% | 79% (1835) | 84% (1862) | 88% (1869) | 90% (1875) | 0.117 | 0.087 | 30622.08 |
| KXXRP15M | 1895 | 20.0 | 50% | 78% (1855) | 83% (1846) | 87% (1872) | 92% (1880) | 0.120 | 0.089 | 59862.97 |
| KXZEC15M | 1894 | 20.0 | 49% | 80% (1840) | 82% (1855) | 88% (1876) | 92% (1878) | 0.124 | 0.082 | 9316.21 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (922) | 49% (1022) | 46% / 48% | 44% / 50% |
| KXBNB15M | 50% (954) | 48% (989) | 53% / 44% | 47% / 52% |
| KXDOGE15M | 46% (941) | 50% (1002) | 47% / 48% | 45% / 53% |
| KXETH15M | 45% (940) | 52% (1002) | 46% / 52% | 44% / 51% |
| KXHYPE15M | 48% (912) | 49% (980) | 50% / 48% | 46% / 50% |
| KXNEAR15M | 46% (890) | 48% (1002) | 47% / 45% | 44% / 51% |
| KXSOL15M | 45% (905) | 51% (986) | 46% / 50% | 44% / 51% |
| KXXRP15M | 47% (940) | 53% (951) | 48% / 53% | 46% / 52% |
| KXZEC15M | 47% (919) | 50% (971) | 47% / 48% | 46% / 53% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 600 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 299 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 242 | 47% | 50c | -3c |
| KXBTC15M | 60-80c | 242 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 565 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 656 | 7% | 7c | +0c |
| KXBNB15M | 20-40c | 242 | 31% | 29c | +2c |
| KXBNB15M | 40-60c | 204 | 49% | 51c | -2c |
| KXBNB15M | 60-80c | 233 | 71% | 70c | +1c |
| KXBNB15M | 80-100c | 612 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 642 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 240 | 28% | 30c | -2c |
| KXDOGE15M | 40-60c | 208 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 233 | 66% | 71c | -5c |
| KXDOGE15M | 80-100c | 624 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 635 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 245 | 30% | 29c | +1c |
| KXETH15M | 40-60c | 222 | 48% | 50c | -2c |
| KXETH15M | 60-80c | 255 | 68% | 70c | -3c |
| KXETH15M | 80-100c | 589 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 633 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 228 | 26% | 29c | -3c |
| KXHYPE15M | 40-60c | 202 | 50% | 49c | +1c |
| KXHYPE15M | 60-80c | 218 | 68% | 70c | -2c |
| KXHYPE15M | 80-100c | 615 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 628 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 257 | 32% | 29c | +3c |
| KXNEAR15M | 40-60c | 208 | 42% | 50c | -8c |
| KXNEAR15M | 60-80c | 232 | 65% | 70c | -6c |
| KXNEAR15M | 80-100c | 571 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 622 | 6% | 7c | -0c |
| KXSOL15M | 20-40c | 253 | 28% | 29c | -0c |
| KXSOL15M | 40-60c | 191 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 242 | 67% | 70c | -3c |
| KXSOL15M | 80-100c | 587 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 629 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 216 | 34% | 30c | +4c |
| KXXRP15M | 40-60c | 224 | 54% | 49c | +4c |
| KXXRP15M | 60-80c | 230 | 68% | 71c | -2c |
| KXXRP15M | 80-100c | 596 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 605 | 7% | 7c | -0c |
| KXZEC15M | 20-40c | 240 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 228 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 206 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 615 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 684 | -10c (187) | +4c (209) | -10c / -1c | -10c / +11c |
| KXDOGE15M | 686 | -5c (185) | -1c (235) | -13c / -6c | +3c / +5c |
| KXETH15M | 722 | -6c (175) | +0c (202) | -3c / -2c | -8c / +3c |
| KXHYPE15M | 658 | -5c (214) | -0c (220) | -4c / -8c | -6c / +7c |
| KXNEAR15M | 704 | -5c (247) | +1c (229) | -2c / -4c | -9c / +5c |
| KXSOL15M | 689 | -5c (192) | +0c (207) | -4c / -4c | -6c / +5c |
| KXXRP15M | 679 | -2c (199) | +4c (220) | +4c / -3c | -7c / +11c |
| KXZEC15M | 680 | -4c (204) | -2c (236) | -4c / -8c | -5c / +5c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
