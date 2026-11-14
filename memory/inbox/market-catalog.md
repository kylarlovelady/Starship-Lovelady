# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-14 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1154349.97 | 0.4400 / 0.4500 | 67203.8 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 23820.89 | 0.9400 / 0.9420 | 618.13 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 28.01 | 0.6900 / 0.8000 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 24970.72 | 0.8800 / 0.8900 | 0.062883 | CF Benchmarks |
| KXETH15M | ETH 15 min | 61732.39 | 0.5400 / 0.5500 | 1907.1 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 29180.18 | 0.2200 / 0.2500 | 69.3151 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 16507.65 | 0.5500 / 0.5600 | 3.3307 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 27284.71 | 0.5000 / 0.5200 | 75.7347 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 40198.81 | 0.7900 / 0.8100 | 0.99 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 24226.35 | 0.9360 / 0.9410 | 902.9962 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 14, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 14, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2044 | 21.5 | 48% | 77% (1963) | 81% (1994) | 87% (2005) | 91% (2021) | 0.129 | 0.095 | 1154349.97 |
| KXBNB15M | 2043 | 21.5 | 49% | 79% (1977) | 84% (1993) | 89% (2009) | 92% (2030) | 0.118 | 0.083 | 23820.89 |
| KXDOGE15M | 2043 | 21.5 | 48% | 79% (1991) | 84% (1998) | 89% (2016) | 92% (2027) | 0.112 | 0.080 | 24970.72 |
| KXETH15M | 2042 | 21.5 | 49% | 79% (1984) | 83% (1988) | 89% (2017) | 92% (2030) | 0.121 | 0.083 | 61732.39 |
| KXHYPE15M | 1992 | 21.0 | 48% | 79% (1930) | 84% (1952) | 89% (1968) | 93% (1974) | 0.119 | 0.079 | 29180.18 |
| KXNEAR15M | 1992 | 21.0 | 47% | 79% (1938) | 83% (1956) | 89% (1974) | 92% (1979) | 0.120 | 0.083 | 16507.65 |
| KXSOL15M | 1991 | 21.0 | 48% | 79% (1930) | 84% (1957) | 88% (1965) | 90% (1971) | 0.117 | 0.086 | 27284.71 |
| KXXRP15M | 1991 | 21.0 | 50% | 79% (1946) | 84% (1941) | 88% (1968) | 92% (1976) | 0.119 | 0.088 | 40198.81 |
| KXZEC15M | 1990 | 21.0 | 49% | 80% (1932) | 83% (1950) | 89% (1972) | 92% (1973) | 0.123 | 0.081 | 24226.35 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (970) | 49% (1070) | 47% / 48% | 45% / 50% |
| KXBNB15M | 50% (1002) | 48% (1037) | 53% / 45% | 48% / 51% |
| KXDOGE15M | 46% (989) | 50% (1050) | 47% / 48% | 45% / 53% |
| KXETH15M | 45% (990) | 52% (1048) | 46% / 53% | 44% / 51% |
| KXHYPE15M | 48% (960) | 49% (1028) | 50% / 48% | 45% / 50% |
| KXNEAR15M | 46% (935) | 48% (1053) | 46% / 45% | 45% / 50% |
| KXSOL15M | 45% (949) | 50% (1038) | 46% / 50% | 45% / 50% |
| KXXRP15M | 47% (986) | 52% (1001) | 49% / 53% | 46% / 50% |
| KXZEC15M | 47% (969) | 51% (1017) | 49% / 48% | 45% / 53% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 628 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 312 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 255 | 48% | 50c | -2c |
| KXBTC15M | 60-80c | 256 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 593 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 685 | 7% | 7c | +0c |
| KXBNB15M | 20-40c | 254 | 30% | 29c | +1c |
| KXBNB15M | 40-60c | 214 | 49% | 51c | -1c |
| KXBNB15M | 60-80c | 248 | 71% | 71c | +0c |
| KXBNB15M | 80-100c | 642 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 671 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 254 | 28% | 29c | -2c |
| KXDOGE15M | 40-60c | 217 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 246 | 65% | 71c | -6c |
| KXDOGE15M | 80-100c | 655 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 664 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 257 | 30% | 29c | +1c |
| KXETH15M | 40-60c | 231 | 47% | 50c | -2c |
| KXETH15M | 60-80c | 267 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 623 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 663 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 240 | 26% | 29c | -4c |
| KXHYPE15M | 40-60c | 213 | 50% | 50c | +1c |
| KXHYPE15M | 60-80c | 229 | 68% | 70c | -2c |
| KXHYPE15M | 80-100c | 647 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 656 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 274 | 32% | 29c | +3c |
| KXNEAR15M | 40-60c | 215 | 41% | 50c | -9c |
| KXNEAR15M | 60-80c | 247 | 64% | 70c | -6c |
| KXNEAR15M | 80-100c | 600 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 654 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 265 | 29% | 29c | -0c |
| KXSOL15M | 40-60c | 201 | 45% | 50c | -5c |
| KXSOL15M | 60-80c | 250 | 66% | 70c | -4c |
| KXSOL15M | 80-100c | 621 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 661 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 225 | 33% | 30c | +3c |
| KXXRP15M | 40-60c | 236 | 53% | 50c | +3c |
| KXXRP15M | 60-80c | 237 | 69% | 71c | -2c |
| KXXRP15M | 80-100c | 632 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 639 | 7% | 7c | -0c |
| KXZEC15M | 20-40c | 251 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 236 | 50% | 50c | +0c |
| KXZEC15M | 60-80c | 215 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 649 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 721 | -9c (193) | +4c (217) | -10c / +1c | -8c / +8c |
| KXDOGE15M | 722 | -5c (192) | -0c (245) | -13c / -6c | +2c / +6c |
| KXETH15M | 755 | -6c (180) | +1c (208) | -3c / -2c | -8c / +3c |
| KXHYPE15M | 692 | -4c (224) | -0c (229) | -4c / -6c | -4c / +6c |
| KXNEAR15M | 743 | -5c (260) | +1c (241) | -3c / -4c | -8c / +6c |
| KXSOL15M | 719 | -5c (201) | +0c (215) | -4c / -3c | -6c / +4c |
| KXXRP15M | 707 | -2c (205) | +4c (230) | +4c / -3c | -8c / +11c |
| KXZEC15M | 708 | -5c (210) | -1c (243) | -3c / -7c | -7c / +4c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
