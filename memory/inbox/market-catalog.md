# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-06 15:37. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 1092486.94 | 0.4200 / 0.4300 | 75678.86 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 10930.19 | 0.2000 / 0.2100 | 692.29 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.01 | 0.0100 / 0.0800 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 15452.05 | 0.1200 / 0.1300 | 0.072597 | CF Benchmarks |
| KXETH15M | ETH 15 min | 43281.44 | 0.2800 / 0.2900 | 2225.24 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 7288.24 | 0.1600 / 0.1800 | 78.2803 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 5675.07 | 0.3900 / 0.4100 | 3.7048 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 22798.40 | 0.2700 / 0.3000 | 89.8 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 31757.74 | 0.1700 / 0.1900 | 1.1753 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 18209.29 | 0.0540 / 0.0630 | 1332.0894 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 4:45 PM EST on Nov 6, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 4:30 PM EST on November 6, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1328 | 14.0 | 48% | 77% (1273) | 80% (1297) | 86% (1297) | 90% (1312) | 0.135 | 0.099 | 1092486.94 |
| KXBNB15M | 1328 | 14.0 | 49% | 80% (1283) | 85% (1293) | 89% (1308) | 91% (1322) | 0.116 | 0.083 | 10930.19 |
| KXDOGE15M | 1328 | 14.0 | 48% | 79% (1291) | 84% (1301) | 89% (1308) | 92% (1320) | 0.115 | 0.082 | 15452.05 |
| KXETH15M | 1328 | 14.0 | 49% | 79% (1285) | 82% (1290) | 88% (1312) | 92% (1320) | 0.127 | 0.087 | 43281.44 |
| KXHYPE15M | 1141 | 12.0 | 49% | 79% (1111) | 85% (1122) | 89% (1127) | 92% (1130) | 0.118 | 0.080 | 7288.24 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (631) | 49% (694) | 47% / 47% | 46% / 51% |
| KXBNB15M | 52% (650) | 46% (675) | 52% / 44% | 51% / 49% |
| KXDOGE15M | 48% (643) | 49% (682) | 47% / 48% | 48% / 49% |
| KXETH15M | 45% (645) | 52% (680) | 45% / 50% | 45% / 54% |
| KXHYPE15M | 50% (558) | 48% (580) | 51% / 47% | 49% / 50% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 396 | 10% | 8c | +2c |
| KXBTC15M | 20-40c | 220 | 27% | 29c | -2c |
| KXBTC15M | 40-60c | 170 | 45% | 50c | -4c |
| KXBTC15M | 60-80c | 160 | 62% | 70c | -8c |
| KXBTC15M | 80-100c | 382 | 93% | 93c | -0c |
| KXBNB15M | 0-20c | 446 | 8% | 7c | +1c |
| KXBNB15M | 20-40c | 168 | 27% | 28c | -1c |
| KXBNB15M | 40-60c | 142 | 47% | 51c | -4c |
| KXBNB15M | 60-80c | 153 | 73% | 70c | +3c |
| KXBNB15M | 80-100c | 419 | 93% | 93c | -0c |
| KXDOGE15M | 0-20c | 423 | 7% | 7c | -1c |
| KXDOGE15M | 20-40c | 165 | 24% | 30c | -6c |
| KXDOGE15M | 40-60c | 147 | 48% | 50c | -2c |
| KXDOGE15M | 60-80c | 169 | 64% | 71c | -7c |
| KXDOGE15M | 80-100c | 424 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 424 | 8% | 7c | +0c |
| KXETH15M | 20-40c | 174 | 32% | 29c | +2c |
| KXETH15M | 40-60c | 153 | 46% | 49c | -4c |
| KXETH15M | 60-80c | 175 | 69% | 70c | -2c |
| KXETH15M | 80-100c | 402 | 92% | 93c | -2c |
| KXHYPE15M | 0-20c | 369 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 143 | 26% | 29c | -4c |
| KXHYPE15M | 40-60c | 115 | 49% | 50c | -1c |
| KXHYPE15M | 60-80c | 142 | 72% | 70c | +2c |
| KXHYPE15M | 80-100c | 372 | 91% | 93c | -2c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 466 | -11c (122) | +5c (154) | -13c / -3c | -9c / +12c |
| KXDOGE15M | 484 | -7c (124) | -2c (170) | -16c / -6c | -1c / +4c |
| KXETH15M | 501 | -7c (112) | +1c (143) | -8c / -4c | -6c / +4c |
| KXHYPE15M | 403 | -2c (133) | -1c (142) | -2c / -9c | -2c / +6c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
