# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-18 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1147952.91 | 0.0230 / 0.0240 | 64292.56 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 15635.58 | 0.0140 / 0.0170 | 589.58 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 28.07 | 0.1800 / 0.2800 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 19919.88 | 0.1500 / 0.1700 | 0.059373 | CF Benchmarks |
| KXETH15M | ETH 15 min | 73866.75 | 0.0170 / 0.0180 | 1804.3 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 32730.16 | 0.0390 / 0.0430 | 68.5362 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 25628.69 | 0.9780 / 0.9790 | 3.3204 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 42836.98 | 0.2600 / 0.2700 | 74.6198 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 38564.33 | 0.1500 / 0.1600 | 0.9972 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 34076.14 | 0.4200 / 0.4300 | 937.0421 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 18, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 18, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 2428 | 25.5 | 47% | 78% (2342) | 82% (2370) | 88% (2386) | 91% (2403) | 0.128 | 0.092 | 1147952.91 |
| KXBNB15M | 2427 | 25.5 | 49% | 79% (2351) | 84% (2367) | 89% (2391) | 92% (2410) | 0.120 | 0.083 | 15635.58 |
| KXDOGE15M | 2427 | 25.5 | 48% | 79% (2366) | 84% (2374) | 89% (2392) | 92% (2409) | 0.115 | 0.082 | 19919.88 |
| KXETH15M | 2426 | 25.5 | 48% | 79% (2355) | 83% (2363) | 89% (2396) | 92% (2410) | 0.122 | 0.084 | 73866.75 |
| KXHYPE15M | 2376 | 25.0 | 48% | 79% (2305) | 84% (2320) | 89% (2345) | 92% (2353) | 0.122 | 0.082 | 32730.16 |
| KXNEAR15M | 2376 | 25.0 | 47% | 79% (2314) | 83% (2336) | 88% (2354) | 92% (2358) | 0.120 | 0.083 | 25628.69 |
| KXSOL15M | 2375 | 25.0 | 48% | 79% (2303) | 84% (2336) | 88% (2347) | 91% (2350) | 0.118 | 0.085 | 42836.98 |
| KXXRP15M | 2375 | 25.0 | 50% | 79% (2321) | 84% (2316) | 88% (2347) | 92% (2358) | 0.118 | 0.088 | 38564.33 |
| KXZEC15M | 2374 | 25.0 | 49% | 80% (2308) | 82% (2328) | 88% (2347) | 92% (2353) | 0.126 | 0.083 | 34076.14 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (1148) | 49% (1276) | 47% / 48% | 45% / 50% |
| KXBNB15M | 49% (1180) | 48% (1243) | 53% / 46% | 45% / 51% |
| KXDOGE15M | 46% (1166) | 50% (1257) | 48% / 49% | 43% / 52% |
| KXETH15M | 45% (1169) | 51% (1253) | 46% / 52% | 45% / 50% |
| KXHYPE15M | 48% (1146) | 49% (1226) | 49% / 48% | 46% / 50% |
| KXNEAR15M | 46% (1122) | 48% (1250) | 46% / 47% | 45% / 50% |
| KXSOL15M | 45% (1132) | 50% (1239) | 46% / 50% | 45% / 50% |
| KXXRP15M | 48% (1174) | 51% (1197) | 49% / 54% | 47% / 49% |
| KXZEC15M | 46% (1152) | 51% (1218) | 50% / 49% | 43% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 761 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 368 | 25% | 29c | -4c |
| KXBTC15M | 40-60c | 301 | 49% | 50c | -1c |
| KXBTC15M | 60-80c | 297 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 701 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 814 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 313 | 29% | 29c | +0c |
| KXBNB15M | 40-60c | 262 | 48% | 50c | -2c |
| KXBNB15M | 60-80c | 287 | 70% | 71c | -1c |
| KXBNB15M | 80-100c | 751 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 805 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 305 | 28% | 29c | -1c |
| KXDOGE15M | 40-60c | 257 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 288 | 65% | 70c | -6c |
| KXDOGE15M | 80-100c | 772 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 805 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 316 | 32% | 29c | +3c |
| KXETH15M | 40-60c | 265 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 308 | 70% | 70c | -1c |
| KXETH15M | 80-100c | 732 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 796 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 296 | 26% | 29c | -3c |
| KXHYPE15M | 40-60c | 255 | 50% | 50c | +1c |
| KXHYPE15M | 60-80c | 265 | 67% | 70c | -3c |
| KXHYPE15M | 80-100c | 764 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 796 | 7% | 7c | -1c |
| KXNEAR15M | 20-40c | 325 | 32% | 29c | +3c |
| KXNEAR15M | 40-60c | 242 | 43% | 50c | -7c |
| KXNEAR15M | 60-80c | 299 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 714 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 786 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 321 | 29% | 29c | -0c |
| KXSOL15M | 40-60c | 236 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 294 | 67% | 70c | -3c |
| KXSOL15M | 80-100c | 738 | 93% | 93c | -1c |
| KXXRP15M | 0-20c | 791 | 7% | 7c | -0c |
| KXXRP15M | 20-40c | 279 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 274 | 52% | 50c | +3c |
| KXXRP15M | 60-80c | 273 | 67% | 71c | -3c |
| KXXRP15M | 80-100c | 758 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 771 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 298 | 29% | 29c | +0c |
| KXZEC15M | 40-60c | 278 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 266 | 64% | 71c | -8c |
| KXZEC15M | 80-100c | 761 | 92% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 867 | -10c (225) | +3c (256) | -10c / +3c | -9c / +3c |
| KXDOGE15M | 855 | -4c (222) | -0c (288) | -8c / -3c | -1c / +3c |
| KXETH15M | 889 | -3c (211) | +2c (241) | -5c / +1c | -2c / +2c |
| KXHYPE15M | 827 | -5c (260) | -1c (281) | -2c / -5c | -8c / +3c |
| KXNEAR15M | 874 | -4c (299) | +2c (288) | -3c / -2c | -5c / +6c |
| KXSOL15M | 857 | -7c (232) | -0c (258) | -2c / -3c | -11c / +3c |
| KXXRP15M | 837 | -2c (239) | +2c (283) | +4c / +1c | -8c / +3c |
| KXZEC15M | 849 | -6c (244) | -0c (299) | -3c / -0c | -10c / -1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
