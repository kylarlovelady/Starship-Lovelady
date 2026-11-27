# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-27 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1749941.97 | 0.1200 / 0.1300 | 61612.75 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 21172.53 | 0.5000 / 0.5100 | 563.64 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 81.73 | 0.5900 / 0.6900 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 23539.34 | 0.8900 / 0.9000 | 0.05856 | CF Benchmarks |
| KXETH15M | ETH 15 min | 113755.81 | 0.3000 / 0.3100 | 1727.87 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 13730.97 | 0.9420 / 0.9440 | 65.7486 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 13323.23 | 0.9610 / 0.9640 | 3.1239 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 68535.93 | 0.2200 / 0.2300 | 73.3747 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 40852.69 | 0.9480 / 0.9490 | 0.9809 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 8372.11 | 0.2400 / 0.2500 | 756.1858 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 27, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 27, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 3276 | 34.5 | 47% | 78% (3163) | 82% (3195) | 87% (3219) | 91% (3243) | 0.128 | 0.092 | 1749941.97 |
| KXBNB15M | 3275 | 34.5 | 49% | 79% (3179) | 84% (3196) | 89% (3226) | 92% (3246) | 0.121 | 0.082 | 21172.53 |
| KXDOGE15M | 3275 | 34.5 | 49% | 79% (3196) | 83% (3203) | 89% (3223) | 92% (3248) | 0.119 | 0.084 | 23539.34 |
| KXETH15M | 3274 | 34.5 | 49% | 78% (3184) | 82% (3193) | 88% (3238) | 92% (3250) | 0.125 | 0.086 | 113755.81 |
| KXHYPE15M | 3224 | 34.0 | 48% | 79% (3123) | 84% (3149) | 89% (3181) | 92% (3193) | 0.122 | 0.082 | 13730.97 |
| KXNEAR15M | 3224 | 34.0 | 47% | 79% (3139) | 83% (3168) | 88% (3191) | 92% (3198) | 0.121 | 0.084 | 13323.23 |
| KXSOL15M | 3223 | 34.0 | 48% | 79% (3122) | 84% (3165) | 88% (3188) | 91% (3192) | 0.121 | 0.086 | 68535.93 |
| KXXRP15M | 3223 | 34.0 | 49% | 79% (3145) | 83% (3143) | 88% (3182) | 92% (3195) | 0.122 | 0.087 | 40852.69 |
| KXZEC15M | 3222 | 34.0 | 48% | 80% (3134) | 82% (3160) | 88% (3187) | 92% (3195) | 0.125 | 0.082 | 8372.11 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 45% (1544) | 49% (1726) | 46% / 50% | 45% / 48% |
| KXBNB15M | 49% (1594) | 48% (1675) | 51% / 47% | 47% / 49% |
| KXDOGE15M | 47% (1595) | 50% (1674) | 47% / 49% | 48% / 51% |
| KXETH15M | 46% (1590) | 51% (1678) | 45% / 52% | 47% / 50% |
| KXHYPE15M | 48% (1558) | 49% (1660) | 49% / 48% | 48% / 49% |
| KXNEAR15M | 46% (1522) | 48% (1696) | 46% / 48% | 46% / 49% |
| KXSOL15M | 47% (1549) | 50% (1668) | 46% / 50% | 48% / 49% |
| KXXRP15M | 48% (1588) | 51% (1629) | 47% / 53% | 49% / 49% |
| KXZEC15M | 47% (1556) | 50% (1660) | 48% / 50% | 46% / 50% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 1019 | 8% | 8c | +1c |
| KXBTC15M | 20-40c | 493 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 402 | 48% | 50c | -2c |
| KXBTC15M | 60-80c | 423 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 939 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 1083 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 425 | 29% | 29c | -0c |
| KXBNB15M | 40-60c | 362 | 49% | 50c | -1c |
| KXBNB15M | 60-80c | 405 | 69% | 70c | -1c |
| KXBNB15M | 80-100c | 1000 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 1057 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 422 | 30% | 29c | +1c |
| KXDOGE15M | 40-60c | 362 | 51% | 50c | +1c |
| KXDOGE15M | 60-80c | 422 | 66% | 70c | -4c |
| KXDOGE15M | 80-100c | 1012 | 93% | 93c | +1c |
| KXETH15M | 0-20c | 1059 | 8% | 7c | +1c |
| KXETH15M | 20-40c | 438 | 32% | 29c | +4c |
| KXETH15M | 40-60c | 366 | 46% | 50c | -4c |
| KXETH15M | 60-80c | 438 | 68% | 71c | -3c |
| KXETH15M | 80-100c | 973 | 93% | 93c | -0c |
| KXHYPE15M | 0-20c | 1066 | 8% | 7c | +1c |
| KXHYPE15M | 20-40c | 413 | 28% | 29c | -2c |
| KXHYPE15M | 40-60c | 353 | 48% | 49c | -2c |
| KXHYPE15M | 60-80c | 377 | 69% | 70c | -1c |
| KXHYPE15M | 80-100c | 1015 | 92% | 93c | -1c |
| KXNEAR15M | 0-20c | 1070 | 7% | 8c | -1c |
| KXNEAR15M | 20-40c | 439 | 31% | 29c | +1c |
| KXNEAR15M | 40-60c | 340 | 44% | 50c | -6c |
| KXNEAR15M | 60-80c | 394 | 65% | 70c | -5c |
| KXNEAR15M | 80-100c | 981 | 93% | 93c | -0c |
| KXSOL15M | 0-20c | 1042 | 7% | 7c | -0c |
| KXSOL15M | 20-40c | 441 | 28% | 28c | -0c |
| KXSOL15M | 40-60c | 338 | 48% | 50c | -2c |
| KXSOL15M | 60-80c | 401 | 66% | 70c | -5c |
| KXSOL15M | 80-100c | 1001 | 93% | 93c | -0c |
| KXXRP15M | 0-20c | 1056 | 7% | 7c | +0c |
| KXXRP15M | 20-40c | 388 | 32% | 29c | +3c |
| KXXRP15M | 40-60c | 368 | 48% | 49c | -1c |
| KXXRP15M | 60-80c | 374 | 67% | 71c | -3c |
| KXXRP15M | 80-100c | 1037 | 93% | 93c | -0c |
| KXZEC15M | 0-20c | 1043 | 7% | 7c | +0c |
| KXZEC15M | 20-40c | 420 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 366 | 50% | 50c | -0c |
| KXZEC15M | 60-80c | 386 | 65% | 71c | -6c |
| KXZEC15M | 80-100c | 1007 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 1199 | -9c (306) | +3c (343) | -10c / +4c | -7c / +1c |
| KXDOGE15M | 1214 | -6c (327) | +3c (397) | -4c / -2c | -7c / +8c |
| KXETH15M | 1242 | -5c (303) | +3c (338) | -4c / -1c | -5c / +7c |
| KXHYPE15M | 1157 | -6c (367) | -1c (382) | -4c / -2c | -8c / +0c |
| KXNEAR15M | 1183 | -6c (399) | +1c (395) | -6c / +0c | -7c / +2c |
| KXSOL15M | 1189 | -7c (323) | -1c (361) | -3c / -1c | -12c / -1c |
| KXXRP15M | 1143 | -3c (327) | +0c (382) | -2c / +3c | -5c / -2c |
| KXZEC15M | 1180 | -7c (358) | +0c (405) | -4c / -0c | -10c / +1c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
