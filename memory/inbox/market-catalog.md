# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-16 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1043358.69 | 0.5500 / 0.5600 | 64526.92 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 10689.53 | 0.5100 / 0.5400 | 590.88 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.01 | 0.1600 / 0.2300 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 8031.85 | 0.6700 / 0.6800 | 0.05854 | CF Benchmarks |
| KXETH15M | ETH 15 min | 46259.18 | 0.6200 / 0.6300 | 1805.39 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 10386.14 | 0.6300 / 0.6600 | 67.3188 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 4941.59 | 0.5300 / 0.5500 | 3.1852 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 21331.34 | 0.7900 / 0.8000 | 71.3303 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 34858.30 | 0.7900 / 0.8000 | 0.9501 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 11433.06 | 0.7000 / 0.7100 | 891.605 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 16, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 16, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2236 | 23.5 | 47% | 78% (2152) | 82% (2180) | 87% (2194) | 91% (2211) | 0.128 | 0.093 | 1043358.69 |
| KXBNB15M | 2235 | 23.5 | 49% | 79% (2164) | 84% (2177) | 89% (2201) | 92% (2220) | 0.120 | 0.085 | 10689.53 |
| KXDOGE15M | 2235 | 23.5 | 48% | 79% (2179) | 84% (2187) | 89% (2205) | 92% (2219) | 0.113 | 0.081 | 8031.85 |
| KXETH15M | 2234 | 23.5 | 48% | 79% (2167) | 83% (2175) | 89% (2206) | 92% (2222) | 0.123 | 0.084 | 46259.18 |
| KXHYPE15M | 2184 | 23.0 | 48% | 79% (2117) | 84% (2136) | 89% (2155) | 92% (2164) | 0.120 | 0.082 | 10386.14 |
| KXNEAR15M | 2184 | 23.0 | 47% | 79% (2127) | 83% (2146) | 88% (2164) | 92% (2168) | 0.121 | 0.083 | 4941.59 |
| KXSOL15M | 2183 | 23.0 | 47% | 79% (2119) | 84% (2146) | 88% (2155) | 91% (2162) | 0.118 | 0.086 | 21331.34 |
| KXXRP15M | 2183 | 23.0 | 49% | 79% (2132) | 84% (2129) | 88% (2157) | 92% (2168) | 0.118 | 0.088 | 34858.30 |
| KXZEC15M | 2182 | 23.0 | 49% | 80% (2121) | 82% (2139) | 88% (2160) | 92% (2164) | 0.125 | 0.084 | 11433.06 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1058) | 49% (1174) | 47% / 49% | 45% / 49% |
| KXBNB15M | 49% (1086) | 48% (1145) | 53% / 46% | 46% / 50% |
| KXDOGE15M | 46% (1074) | 50% (1157) | 48% / 49% | 43% / 51% |
| KXETH15M | 45% (1075) | 51% (1155) | 47% / 52% | 44% / 50% |
| KXHYPE15M | 48% (1050) | 49% (1130) | 49% / 48% | 46% / 49% |
| KXNEAR15M | 46% (1025) | 48% (1155) | 47% / 46% | 45% / 49% |
| KXSOL15M | 45% (1032) | 50% (1147) | 45% / 50% | 45% / 49% |
| KXXRP15M | 48% (1070) | 51% (1109) | 48% / 54% | 47% / 48% |
| KXZEC15M | 47% (1059) | 50% (1119) | 49% / 48% | 45% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 700 | 9% | 8c | +2c |
| KXBTC15M | 20-40c | 334 | 24% | 29c | -5c |
| KXBTC15M | 40-60c | 282 | 49% | 49c | -1c |
| KXBTC15M | 60-80c | 273 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 647 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 756 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 279 | 29% | 29c | +0c |
| KXBNB15M | 40-60c | 244 | 49% | 50c | -1c |
| KXBNB15M | 60-80c | 264 | 70% | 71c | -0c |
| KXBNB15M | 80-100c | 692 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 746 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 278 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 232 | 47% | 50c | -3c |
| KXDOGE15M | 60-80c | 270 | 65% | 70c | -6c |
| KXDOGE15M | 80-100c | 709 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 742 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 282 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 253 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 286 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 671 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 733 | 8% | 7c | +0c |
| KXHYPE15M | 20-40c | 267 | 26% | 29c | -3c |
| KXHYPE15M | 40-60c | 234 | 50% | 50c | +1c |
| KXHYPE15M | 60-80c | 249 | 68% | 70c | -2c |
| KXHYPE15M | 80-100c | 701 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 729 | 6% | 8c | -1c |
| KXNEAR15M | 20-40c | 302 | 33% | 30c | +3c |
| KXNEAR15M | 40-60c | 232 | 42% | 50c | -7c |
| KXNEAR15M | 60-80c | 269 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 652 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 722 | 6% | 7c | -1c |
| KXSOL15M | 20-40c | 294 | 30% | 29c | +1c |
| KXSOL15M | 40-60c | 222 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 274 | 66% | 70c | -4c |
| KXSOL15M | 80-100c | 671 | 92% | 93c | -1c |
| KXXRP15M | 0-20c | 729 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 253 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 254 | 51% | 50c | +1c |
| KXXRP15M | 60-80c | 253 | 68% | 71c | -2c |
| KXXRP15M | 80-100c | 694 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 706 | 8% | 7c | +0c |
| KXZEC15M | 20-40c | 278 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 255 | 51% | 50c | +0c |
| KXZEC15M | 60-80c | 242 | 64% | 71c | -8c |
| KXZEC15M | 80-100c | 701 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 792 | -10c (210) | +3c (231) | -11c / +2c | -8c / +5c |
| KXDOGE15M | 785 | -5c (209) | -1c (260) | -9c / -5c | -2c / +4c |
| KXETH15M | 821 | -5c (198) | +1c (220) | -5c / -1c | -6c / +3c |
| KXHYPE15M | 760 | -4c (240) | -1c (256) | -2c / -5c | -5c / +3c |
| KXNEAR15M | 811 | -5c (276) | +3c (267) | -2c / -3c | -8c / +8c |
| KXSOL15M | 796 | -7c (218) | +0c (234) | -3c / -3c | -10c / +4c |
| KXXRP15M | 771 | -3c (221) | +2c (253) | +3c / -1c | -8c / +6c |
| KXZEC15M | 782 | -6c (228) | -1c (273) | -1c / -2c | -10c / -1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
