# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-15 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 881464.73 | 0.6700 / 0.6800 | 65437.14 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 15072.71 | 0.6200 / 0.6300 | 597.44 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 502.00 | 0.0000 / 0.1200 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 25723.86 | 0.8400 / 0.8600 | 0.058927 | CF Benchmarks |
| KXETH15M | ETH 15 min | 53844.29 | 0.4800 / 0.4900 | 1827.89 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 11627.87 | 0.8200 / 0.8600 | 67.9171 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 9251.33 | 0.8700 / 0.8800 | 3.1691 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 24006.25 | 0.9110 / 0.9120 | 71.8652 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 25508.50 | 0.7600 / 0.7700 | 0.9619 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 6830.55 | 0.8900 / 0.9040 | 908.5057 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 15, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 15, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2140 | 22.5 | 47% | 78% (2059) | 82% (2087) | 87% (2099) | 91% (2116) | 0.128 | 0.093 | 881464.73 |
| KXBNB15M | 2139 | 22.5 | 49% | 79% (2072) | 84% (2084) | 89% (2105) | 92% (2126) | 0.118 | 0.083 | 15072.71 |
| KXDOGE15M | 2139 | 22.5 | 48% | 79% (2084) | 84% (2092) | 89% (2111) | 92% (2123) | 0.113 | 0.080 | 25723.86 |
| KXETH15M | 2138 | 22.5 | 48% | 79% (2078) | 83% (2084) | 89% (2111) | 92% (2126) | 0.121 | 0.082 | 53844.29 |
| KXHYPE15M | 2088 | 22.0 | 48% | 79% (2021) | 84% (2045) | 89% (2061) | 92% (2069) | 0.118 | 0.080 | 11627.87 |
| KXNEAR15M | 2088 | 22.0 | 47% | 79% (2034) | 83% (2051) | 88% (2068) | 92% (2072) | 0.121 | 0.083 | 9251.33 |
| KXSOL15M | 2087 | 22.0 | 47% | 79% (2026) | 84% (2052) | 88% (2060) | 91% (2066) | 0.118 | 0.086 | 24006.25 |
| KXXRP15M | 2087 | 22.0 | 49% | 79% (2039) | 84% (2037) | 88% (2063) | 92% (2072) | 0.117 | 0.088 | 25508.50 |
| KXZEC15M | 2086 | 22.0 | 49% | 80% (2027) | 82% (2044) | 88% (2067) | 92% (2068) | 0.125 | 0.082 | 6830.55 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1008) | 49% (1128) | 47% / 48% | 45% / 49% |
| KXBNB15M | 50% (1042) | 47% (1093) | 53% / 44% | 47% / 51% |
| KXDOGE15M | 46% (1026) | 50% (1109) | 47% / 48% | 45% / 51% |
| KXETH15M | 45% (1028) | 51% (1106) | 46% / 52% | 44% / 50% |
| KXHYPE15M | 48% (1002) | 49% (1082) | 50% / 48% | 45% / 49% |
| KXNEAR15M | 46% (976) | 48% (1108) | 46% / 46% | 45% / 49% |
| KXSOL15M | 45% (987) | 50% (1096) | 45% / 50% | 45% / 49% |
| KXXRP15M | 48% (1025) | 51% (1058) | 48% / 54% | 47% / 48% |
| KXZEC15M | 47% (1011) | 50% (1071) | 49% / 48% | 44% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 669 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 322 | 25% | 29c | -5c |
| KXBTC15M | 40-60c | 270 | 49% | 50c | -1c |
| KXBTC15M | 60-80c | 265 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 614 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 728 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 266 | 30% | 29c | +1c |
| KXBNB15M | 40-60c | 230 | 49% | 50c | -2c |
| KXBNB15M | 60-80c | 253 | 71% | 70c | +1c |
| KXBNB15M | 80-100c | 662 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 713 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 267 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 223 | 47% | 50c | -3c |
| KXDOGE15M | 60-80c | 263 | 65% | 71c | -6c |
| KXDOGE15M | 80-100c | 673 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 708 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 272 | 31% | 29c | +2c |
| KXETH15M | 40-60c | 237 | 47% | 50c | -3c |
| KXETH15M | 60-80c | 280 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 641 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 703 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 253 | 25% | 29c | -4c |
| KXHYPE15M | 40-60c | 222 | 50% | 50c | +1c |
| KXHYPE15M | 60-80c | 240 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 670 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 697 | 6% | 8c | -1c |
| KXNEAR15M | 20-40c | 293 | 33% | 30c | +3c |
| KXNEAR15M | 40-60c | 225 | 42% | 50c | -7c |
| KXNEAR15M | 60-80c | 253 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 620 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 694 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 278 | 29% | 29c | +0c |
| KXSOL15M | 40-60c | 212 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 262 | 66% | 70c | -4c |
| KXSOL15M | 80-100c | 641 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 700 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 241 | 32% | 30c | +3c |
| KXXRP15M | 40-60c | 243 | 52% | 50c | +3c |
| KXXRP15M | 60-80c | 243 | 68% | 71c | -2c |
| KXXRP15M | 80-100c | 660 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 678 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 264 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 247 | 51% | 50c | +0c |
| KXZEC15M | 60-80c | 230 | 63% | 71c | -9c |
| KXZEC15M | 80-100c | 667 | 93% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 754 | -9c (201) | +3c (224) | -11c / +0c | -7c / +6c |
| KXDOGE15M | 758 | -5c (203) | -1c (255) | -10c / -6c | -1c / +5c |
| KXETH15M | 789 | -6c (190) | +1c (215) | -4c / -0c | -8c / +2c |
| KXHYPE15M | 725 | -4c (230) | -1c (245) | -2c / -6c | -6c / +5c |
| KXNEAR15M | 779 | -5c (270) | +3c (257) | -2c / -4c | -8c / +9c |
| KXSOL15M | 757 | -6c (211) | -0c (224) | -2c / -3c | -9c / +3c |
| KXXRP15M | 738 | -2c (212) | +3c (244) | +3c / -2c | -7c / +7c |
| KXZEC15M | 747 | -6c (219) | -1c (261) | -2c / -5c | -10c / +2c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
