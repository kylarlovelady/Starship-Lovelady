# Kalshi AI (BTC 15-minute markets)
Updated 2026-11-04. Details and code: markets/PLAN.md. Imported from Hub Notes.

## Status
- PRACTICE (fake) money only; live mode OFF. Kalshi account connected (Ed25519 key on the Pi, read+trade only, no transfers); the API location verification must be redone weekly (current one expires Nov 9).
- Service `market-agent` (collector.py), restart only when collector.py changes (bump line-2 "# vN restart" marker). Data ~/market-data. Live View http://loveladymainaihub.taild703ca.ts.net:8095/live.html . Cron: crew-update, market-lab (every 3 h), supervisor hourly (runs innovate.py).
- Honest findings: no signal or strategy has beaten price plus fees. 24 h review (Nov 4): `run` lost $548, nearly all from $25-100 bets (1 win in 12); bets under $25 roughly break-even. After the $50 cap went in (Nov 4 afternoon) the 8 h loss was only $40. Opposite-side tests (mood/flow flip) lost more than the normal versions. Break-even needs roughly 55-57% right; goal is 55%+.
- Next: let it run; review 12 h in the morning (`python3 ~/starship/markets/review.py 12`). A strategy needs about 40+ positive rounds before it earns bigger bets.

## Standing rules (Kylar's)
- BTC only for now. Nothing is retired: no strategy or signal is taken off the table; test them side by side and trust evidence.
- Hard rules only: $5 minimum bet; no selling a winner for a few cents (need about $5 profit after fees). Loss cut is flexible: depends on bet size, time left, distance to target; small bets can ride. $50 per-round cap until a strategy proves itself.
- On practice money the agent is very driven to learn: constant experiments, cuts losers quickly, backs winners, always explores something new, logs what changed and why. On live: no experimenting, only what has the best proven record. Aggression dial and loss floor are Kylar's.
- Money tiers (Kylar's plan): about $20 real first; about $500 later; bigger bets near $1,000, only after profit is shown at the lower tier. Kalshi's own limits are a backstop. Practice wallet auto-refills to $1,000.
- Every signal is graded individually. Ratings: Kylar's 13 plus Claude's 9 for unrated ones; weight = rating x evidence. Signals include order book, momentum, whales, big trades, news, Fear & Greed, funding, support/resistance, separate trends (15m/1h/4h/24h/7d), blockchain flow ideas.
- Learn from hindsight after every round: compare what it did with the best move, write the lesson, change a setting only if it beats the old one on unseen rounds after fees; keep a plain-English change log and old values.
- Everything must be visible in the Live View: what it is testing, the reactions it tries, and how it wins.

## Kylar's trading style (his words, Nov 3)
- Uses the hour trend: if BTC was very high an hour ago and is far lower now and still falling, it will come back, but not when. Watch the speed: while it falls fast, wait. When it is still falling but slowing, buy the OPPOSITE side (payout 4x-10x). Hold while the new move is fast; when it slows, watch; SELL on the first tick the other way (slowdown is a warning, the turn is the trigger). Only in the first half of the 15 minutes. Check distance to target against time left (about $80 away with 8-10 minutes left is a rough guess only, tune from data). Bet big on real setups, not many small bets.
- The agent must look every second, not every 5 seconds.
- Live checklist before going live: chip shows live; balance matches Kalshi; aggression low and biggest bet small (about $5) for the first session; loss floor set by Kylar; API verification not expired; kill switch and End session known.

## Parked
- More agents on other markets (options, stocks, commodities) only after the Kalshi agent shows a real edge; share the method, not the bets. Other coins on hold. Mempool tracker for big transfers only.

## Done
(Finished items go here with the date, newest first. Never delete.)
