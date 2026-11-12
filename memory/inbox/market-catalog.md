# Kalshi 15-minute crypto series: catalogue and predictability

Generated 2026-11-12 04:40. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds).

## Catalogue (what exists right now; volume = contracts traded so far in the open round)

| series | title | open round volume | bid / ask now | strike | resolves on |
|---|---|---|---|---|---|
| KXBTC15M | BTC 15 min | 777053.39 | 0.2200 / 0.2300 | 73479.74 | CF Benchmarks |
| KXADA15M | Cardano 15 Minute | - | - / - | - | CF Benchmarks |
| KXBCH15M | Bitcoin Cash 15 Minute | - | - / - | - | CF Benchmarks |
| KXBNB15M | BNB 15 min | 9628.63 | 0.0200 / 0.0300 | 673.57 | CF Benchmarks |
| KXCRYPTOCOMP15M | Crypto Comparison 15 minute | - | - / - | - | CF Benchmarks |
| KXCRYPTOLEAD15M | Coin Race 15 minutes | 0.00 | 0.0000 / 0.0200 | - | CF Benchmarks |
| KXDOGE15M | DOGE 15 min | 12615.81 | 0.0560 / 0.0570 | 0.067308 | CF Benchmarks |
| KXETH15M | ETH 15 min | 58706.38 | 0.7900 / 0.8000 | 2047.05 | CF Benchmarks |
| KXHYPE15M | HYPE 15 min | 9198.90 | 0.3600 / 0.3800 | 71.7495 | CF Benchmarks |
| KXNEAR15M | NEAR 15m | 6418.09 | 0.0160 / 0.0170 | 3.5141 | CF Benchmarks |
| KXSOL15M | SOL 15 min | 21403.37 | 0.0440 / 0.0450 | 83.2958 | CF Benchmarks |
| KXTON15M | TON 15m | - | - / - | - | CF Benchmarks |
| KXXRP15M | XRP 15 min | 29605.99 | 0.0100 / 0.0110 | 1.0547 | CF Benchmarks |
| KXZEC15M | Zcash 15min | 10193.95 | 0.0350 / 0.0360 | 993.7902 | CF Benchmarks |

Rule text on a BTC round (Kalshi): If the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:45 AM EST on Nov 12, 2026 is at least the simple average of the sixty seconds of CF Benchmarks' BRTI before 5:30 AM EST on November 12, 2026, then the market resolves to Yes.

Multi-outcome series (KXCRYPTOCOMP15M, KXCRYPTOLEAD15M) are listed but not analysed here.

## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)

| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |
|---|---|---|---|---|---|---|---|---|---|---|
| KXBTC15M | 1852 | 19.5 | 48% | 78% (1781) | 81% (1805) | 87% (1816) | 91% (1830) | 0.130 | 0.095 | 777053.39 |
| KXBNB15M | 1851 | 19.5 | 49% | 79% (1792) | 84% (1805) | 89% (1820) | 92% (1840) | 0.116 | 0.083 | 9628.63 |
| KXDOGE15M | 1851 | 19.5 | 49% | 80% (1803) | 85% (1810) | 89% (1830) | 92% (1837) | 0.111 | 0.079 | 12615.81 |
| KXETH15M | 1850 | 19.5 | 48% | 79% (1796) | 83% (1800) | 89% (1827) | 92% (1839) | 0.123 | 0.085 | 58706.38 |
| KXHYPE15M | 1800 | 19.0 | 48% | 79% (1747) | 84% (1765) | 89% (1778) | 92% (1784) | 0.119 | 0.079 | 9198.90 |
| KXNEAR15M | 1800 | 19.0 | 47% | 79% (1752) | 83% (1769) | 88% (1784) | 92% (1788) | 0.120 | 0.084 | 6418.09 |
| KXSOL15M | 1799 | 19.0 | 48% | 79% (1741) | 85% (1768) | 88% (1777) | 90% (1780) | 0.117 | 0.087 | 21403.37 |
| KXXRP15M | 1799 | 19.0 | 50% | 78% (1762) | 83% (1752) | 88% (1778) | 92% (1784) | 0.120 | 0.088 | 29605.99 |
| KXZEC15M | 1798 | 19.0 | 49% | 80% (1748) | 83% (1761) | 89% (1780) | 92% (1786) | 0.123 | 0.080 | 10193.95 |

## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)

| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |
|---|---|---|---|---|
| KXBTC15M | 46% (884) | 50% (964) | 47% / 48% | 45% / 51% |
| KXBNB15M | 50% (910) | 48% (937) | 53% / 44% | 48% / 52% |
| KXDOGE15M | 46% (896) | 50% (951) | 47% / 48% | 46% / 52% |
| KXETH15M | 45% (895) | 52% (951) | 46% / 52% | 44% / 51% |
| KXHYPE15M | 48% (864) | 48% (932) | 49% / 48% | 47% / 48% |
| KXNEAR15M | 45% (844) | 48% (952) | 47% / 46% | 44% / 50% |
| KXSOL15M | 45% (857) | 50% (938) | 46% / 50% | 44% / 51% |
| KXXRP15M | 47% (890) | 52% (905) | 48% / 53% | 46% / 52% |
| KXZEC15M | 47% (874) | 50% (920) | 48% / 48% | 47% / 52% |

## Calibration at 5 minutes out (did the price mean what it said?)

| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |
|---|---|---|---|---|---|
| KXBTC15M | 0-20c | 561 | 9% | 8c | +1c |
| KXBTC15M | 20-40c | 284 | 26% | 29c | -3c |
| KXBTC15M | 40-60c | 233 | 45% | 50c | -4c |
| KXBTC15M | 60-80c | 234 | 65% | 70c | -5c |
| KXBTC15M | 80-100c | 540 | 93% | 93c | +0c |
| KXBNB15M | 0-20c | 616 | 7% | 7c | -0c |
| KXBNB15M | 20-40c | 231 | 32% | 29c | +3c |
| KXBNB15M | 40-60c | 196 | 47% | 51c | -3c |
| KXBNB15M | 60-80c | 223 | 72% | 71c | +2c |
| KXBNB15M | 80-100c | 585 | 93% | 93c | -1c |
| KXDOGE15M | 0-20c | 607 | 6% | 7c | -1c |
| KXDOGE15M | 20-40c | 228 | 26% | 29c | -3c |
| KXDOGE15M | 40-60c | 199 | 49% | 50c | -1c |
| KXDOGE15M | 60-80c | 225 | 66% | 71c | -5c |
| KXDOGE15M | 80-100c | 592 | 94% | 93c | +1c |
| KXETH15M | 0-20c | 597 | 7% | 7c | +0c |
| KXETH15M | 20-40c | 237 | 29% | 29c | -0c |
| KXETH15M | 40-60c | 213 | 48% | 50c | -1c |
| KXETH15M | 60-80c | 236 | 68% | 71c | -2c |
| KXETH15M | 80-100c | 567 | 92% | 93c | -1c |
| KXHYPE15M | 0-20c | 598 | 7% | 7c | +0c |
| KXHYPE15M | 20-40c | 216 | 25% | 29c | -4c |
| KXHYPE15M | 40-60c | 193 | 50% | 49c | +1c |
| KXHYPE15M | 60-80c | 205 | 67% | 70c | -3c |
| KXHYPE15M | 80-100c | 588 | 91% | 93c | -2c |
| KXNEAR15M | 0-20c | 593 | 6% | 7c | -1c |
| KXNEAR15M | 20-40c | 244 | 32% | 29c | +2c |
| KXNEAR15M | 40-60c | 193 | 41% | 50c | -9c |
| KXNEAR15M | 60-80c | 225 | 64% | 70c | -6c |
| KXNEAR15M | 80-100c | 545 | 93% | 93c | +0c |
| KXSOL15M | 0-20c | 586 | 6% | 7c | -0c |
| KXSOL15M | 20-40c | 243 | 27% | 29c | -2c |
| KXSOL15M | 40-60c | 182 | 46% | 50c | -4c |
| KXSOL15M | 60-80c | 228 | 67% | 70c | -3c |
| KXSOL15M | 80-100c | 560 | 93% | 93c | -1c |
| KXXRP15M | 0-20c | 595 | 6% | 7c | -1c |
| KXXRP15M | 20-40c | 203 | 33% | 30c | +3c |
| KXXRP15M | 40-60c | 213 | 53% | 49c | +3c |
| KXXRP15M | 60-80c | 221 | 67% | 71c | -3c |
| KXXRP15M | 80-100c | 567 | 93% | 93c | +0c |
| KXZEC15M | 0-20c | 573 | 7% | 7c | -1c |
| KXZEC15M | 20-40c | 224 | 29% | 29c | -0c |
| KXZEC15M | 40-60c | 219 | 51% | 50c | +1c |
| KXZEC15M | 60-80c | 192 | 63% | 71c | -8c |
| KXZEC15M | 80-100c | 590 | 92% | 93c | -1c |

## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)

| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |
|---|---|---|---|---|---|
| KXBNB15M | 654 | -11c (180) | +4c (202) | -10c / -1c | -12c / +11c |
| KXDOGE15M | 656 | -5c (178) | -0c (223) | -12c / -6c | +0c / +6c |
| KXETH15M | 686 | -6c (167) | +0c (190) | -4c / -0c | -8c / +0c |
| KXHYPE15M | 623 | -6c (206) | -0c (205) | -3c / -9c | -9c / +9c |
| KXNEAR15M | 669 | -6c (237) | +1c (214) | -3c / -4c | -9c / +5c |
| KXSOL15M | 656 | -4c (184) | -0c (194) | -2c / -5c | -7c / +6c |
| KXXRP15M | 646 | -2c (192) | +3c (207) | +4c / -4c | -7c / +11c |
| KXZEC15M | 640 | -5c (194) | -1c (217) | -6c / -9c | -4c / +7c |

## How to read this

- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.
- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.
- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.
- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.
- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on.
