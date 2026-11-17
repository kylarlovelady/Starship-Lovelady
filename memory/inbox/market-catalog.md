# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-17 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1021607.81 | 0.6900 / 0.7000 | 64168.81 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 11720.04 | 0.4900 / 0.5200 | 587.97 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 21.19 | 0.3600 / 0.4100 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 8745.36 | 0.7900 / 0.8000 | 0.058473 | CF Benchmarks |
| KXETH15M | ETH 15 min | 49555.95 | 0.6400 / 0.6600 | 1793.17 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 19682.39 | 0.2500 / 0.2900 | 68.8469 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6212.63 | 0.8300 / 0.8500 | 3.1989 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 22903.15 | 0.8700 / 0.8900 | 72.283 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 38931.59 | 0.8800 / 0.9000 | 0.9557 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 19322.71 | 0.1500 / 0.1700 | 925.5942 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 17, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 17, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2332 | 24.5 | 47% | 78% (2247) | 82% (2276) | 87% (2290) | 91% (2307) | 0.128 | 0.093 | 1021607.81 |
| KXBNB15M | 2331 | 24.5 | 49% | 79% (2258) | 84% (2273) | 89% (2296) | 92% (2315) | 0.120 | 0.084 | 11720.04 |
| KXDOGE15M | 2331 | 24.5 | 48% | 79% (2274) | 84% (2280) | 89% (2298) | 92% (2314) | 0.115 | 0.082 | 8745.36 |
| KXETH15M | 2330 | 24.5 | 48% | 79% (2259) | 83% (2267) | 89% (2300) | 92% (2315) | 0.122 | 0.084 | 49555.95 |
| KXHYPE15M | 2280 | 24.0 | 48% | 79% (2212) | 84% (2228) | 89% (2250) | 92% (2258) | 0.121 | 0.083 | 19682.39 |
| KXNEAR15M | 2280 | 24.0 | 47% | 79% (2222) | 83% (2242) | 88% (2258) | 92% (2264) | 0.120 | 0.082 | 6212.63 |
| KXSOL15M | 2279 | 24.0 | 48% | 79% (2211) | 84% (2241) | 88% (2251) | 91% (2256) | 0.119 | 0.086 | 22903.15 |
| KXXRP15M | 2279 | 24.0 | 49% | 79% (2226) | 84% (2221) | 88% (2252) | 92% (2262) | 0.118 | 0.088 | 38931.59 |
| KXZEC15M | 2278 | 24.0 | 49% | 80% (2216) | 82% (2234) | 89% (2253) | 92% (2258) | 0.126 | 0.083 | 19322.71 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1106) | 49% (1222) | 47% / 49% | 45% / 49% |
| KXBNB15M | 49% (1133) | 48% (1194) | 53% / 46% | 46% / 50% |
| KXDOGE15M | 46% (1120) | 50% (1207) | 48% / 49% | 43% / 51% |
| KXETH15M | 45% (1118) | 51% (1208) | 47% / 52% | 44% / 49% |
| KXHYPE15M | 48% (1099) | 49% (1177) | 50% / 48% | 46% / 49% |
| KXNEAR15M | 46% (1071) | 48% (1205) | 47% / 47% | 44% / 50% |
| KXSOL15M | 45% (1083) | 50% (1192) | 46% / 50% | 45% / 49% |
| KXXRP15M | 48% (1122) | 51% (1153) | 49% / 54% | 47% / 48% |
| KXZEC15M | 47% (1105) | 50% (1169) | 49% / 49% | 44% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 731 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 354 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 291 | 49% | 49c | -0c |
| KXBTC15M | 60-80c | 283 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 673 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 784 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 296 | 29% | 29c | +0c |
| KXBNB15M | 40-60c | 254 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 276 | 70% | 71c | -0c |
| KXBNB15M | 80-100c | 721 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 777 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 290 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 245 | 49% | 50c | -2c |
| KXDOGE15M | 60-80c | 280 | 64% | 70c | -7c |
| KXDOGE15M | 80-100c | 739 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 777 | 7% | 7c | -0c |
| KXETH15M | 20-40c | 296 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 262 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 292 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 703 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 763 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 278 | 27% | 29c | -2c |
| KXHYPE15M | 40-60c | 244 | 50% | 50c | -0c |
| KXHYPE15M | 60-80c | 259 | 67% | 70c | -3c |
| KXHYPE15M | 80-100c | 736 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 760 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 314 | 32% | 29c | +3c |
| KXNEAR15M | 40-60c | 236 | 42% | 50c | -7c |
| KXNEAR15M | 60-80c | 289 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 681 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 753 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 310 | 29% | 29c | +1c |
| KXSOL15M | 40-60c | 230 | 47% | 50c | -4c |
| KXSOL15M | 60-80c | 280 | 66% | 70c | -4c |
| KXSOL15M | 80-100c | 706 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 760 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 265 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 266 | 52% | 50c | +2c |
| KXXRP15M | 60-80c | 262 | 68% | 71c | -3c |
| KXXRP15M | 80-100c | 726 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 737 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 288 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 266 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 254 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 733 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 831 | -10c (216) | +3c (246) | -10c / +3c | -10c / +3c |
| KXDOGE15M | 820 | -5c (216) | -0c (275) | -6c / -4c | -3c / +4c |
| KXETH15M | 850 | -5c (202) | +1c (231) | -4c / -1c | -6c / +4c |
| KXHYPE15M | 791 | -4c (250) | -1c (270) | -2c / -5c | -7c / +2c |
| KXNEAR15M | 847 | -5c (287) | +2c (282) | -3c / -3c | -7c / +7c |
| KXSOL15M | 826 | -7c (222) | -0c (249) | -2c / -3c | -12c / +3c |
| KXXRP15M | 804 | -3c (227) | +2c (271) | +4c / -1c | -9c / +5c |
| KXZEC15M | 815 | -6c (233) | -1c (289) | -2c / -1c | -11c / -1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
