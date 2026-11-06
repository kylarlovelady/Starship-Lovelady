# Kalshi 15-minute crypto markets (catalogue)

Kylar (2026-11-06): list all the 15-minute markets and see whether any are more predictable than BTC. Standing rule: BTC only for real trading; this file is data. Results of the comparison: memory/inbox/market-catalog.md (queue 083, about 30 min after it starts), summary goes under "Findings" below.

## Series found on Kalshi (probe 2026-11-06 14:04, queue 076)
| series | what it is | volume of the open round at the probe |
|---|---|---|
| KXBTC15M | Bitcoin up/down, settles on the average of the last 60 CF Benchmarks index prices vs the strike | about 967,000 |
| KXETH15M | Ethereum | about 16,500 |
| KXSOL15M | Solana | about 25,700 |
| KXXRP15M | XRP | about 15,600 |
| KXDOGE15M | Dogecoin | about 5,700 |
| KXBNB15M | BNB | not probed |
| KXZEC15M | Zcash | not probed |
| KXADA15M | Cardano | not probed |
| KXBCH15M | Bitcoin Cash | not probed |
| KXTON15M | TON | not probed |
| KXHYPE15M | HYPE | not probed |
| KXNEAR15M | NEAR | not probed |
| KXCRYPTOLEAD15M | Coin Race (which coin leads over 15 minutes; multi-outcome) | not probed |
| KXCRYPTOCOMP15M | Crypto Comparison (one coin vs another; multi-outcome) | not probed |
Also exist (no volume at the probe): hourly/daily BTC and ETH series (KXBTCD, KXETHD, KXBTC, KXETH).

## What "predictable" is measured as
Decided earlier (favourite wins more often, earlier), lower Brier score, memory between rounds, BTC leading the others, and mispricing (calibration gap). Thin markets are flagged: a $1,000 bet would move them.

## Findings (first run, 2026-11-06 15:16, last 3 days, 280 rounds per series; queue 083)
- Series with markets in the study: BTC, ETH, SOL, XRP, DOGE, BNB, HYPE, NEAR, ZEC. ADA, BCH and TON had no settled rounds (no trading). Coin Race and Crypto Comparison are multi-outcome (not analysed), almost no volume.
- Liquidity, open round volume at 15:16 (contracts so far in that round): BTC 123,327; DOGE 3,396; XRP 2,529; ETH 2,458; SOL 1,237; HYPE 503; BNB 387; ZEC 366; NEAR 117. BTC is 36 to 1,000 times deeper. A $1,000 bet on any other coin would move the price. (The spread and volume columns of the first run were not trustworthy; the nightly version dropped them.)
- DECIDED EARLIER: favourite right at 5 min: BTC 79%, XRP 81, NEAR 81, ZEC 81, ETH 82, DOGE 83, SOL 84, BNB 84, HYPE 85. Brier at 3 min (0 perfect, 0.25 coin flip): BTC 0.102 (least decided), XRP 0.095, SOL 0.096, ETH 0.090, HYPE 0.087, NEAR 0.086, BNB 0.083, DOGE 0.079, ZEC 0.076. So the alts are a little more predictable than BTC by 1 to 4 points. BUT their prices are well calibrated (80-100c bucket won 91 to 96% vs 92 to 94c): decided earlier does not mean mispriced.
- MEMORY: every series shows UP less likely after an UP round than after a DOWN round (BTC 45 vs 49, ETH 41 vs 49, XRP 44 vs 52, NEAR 45 vs 54, ZEC 49 vs 58). Not independent: all coins move with BTC, and one series has a standard error of about 6 points, so it is about 1 sample, not 9. Checked on the whole BTC history in queue 084 (about 2,800 rounds).
- LEAD/LAG: when BTC priced strongly UP at 5 min the alts' outcomes came in 13 to 19 cents BELOW their own price in 5 of 9 series; when BTC priced strongly DOWN, alts beat their own price by 7 to 27 cents in all 9. Same caveat: the same 50 to 70 rounds in every series; an alt that has not followed BTC may simply be mean-reverting. Needs many more days (the nightly run keeps adding).
- CALIBRATION: no clear persistent gap in any series; buckets of 30 to 100 rounds, gaps of up to 15c are noise. The 20-40c bucket won more than priced in 7 of 9 coins (+3 to +18c), same story as the BTC longshot idea that did not hold up.
- VERDICT so far: no coin is clearly more tradable than BTC. The alts resolve a bit earlier but are thin; nothing is provably mispriced. Keep collecting.

## Keeping it running (Kylar, voice 2026-11-06)
- tasks/series_catalog_daily.sh runs nightly at 4:40 am (installed by queue 084), caches every settled round in ~/market-data/history/series15m.jsonl (prices 10/7/5/3/2 minutes out, new rounds only) and rewrites inbox/market-catalog.md with older-half / newer-half columns for memory and lead/lag. First run backfills 14 days within its 40 minute budget; later nights add the newest rounds.
- Next: after about 7 to 14 days check whether any memory/lead-lag/calibration gap holds in BOTH halves; only then a bootstrap test and a small practice strategy.
