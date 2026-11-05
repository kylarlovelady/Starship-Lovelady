# Kalshi AI (BTC 15-minute markets)
Updated 2026-11-04. Details and code: markets/PLAN.md. Imported from Hub Notes.

## Status
- PRACTICE (fake) money only; live mode OFF. Kalshi account connected (Ed25519 key on the Pi, read+trade only, no transfers); the API location verification must be redone weekly (current one expires Nov 9).
- Service `market-agent` (collector.py), restart only when collector.py changes (bump line-2 "# vN restart" marker). Data ~/market-data. Live View http://loveladymainaihub.taild703ca.ts.net:8095/live.html . Cron: crew-update, market-lab (every 3 h), supervisor hourly (runs innovate.py).
- Honest findings: no signal or strategy has beaten price plus fees. 24 h review (Nov 4): `run` lost $548, nearly all from $25-100 bets (1 win in 12); bets under $25 roughly break-even. After the $50 cap went in (Nov 4 afternoon) the 8 h loss was only $40. Opposite-side tests (mood/flow flip) lost more than the normal versions. Break-even needs roughly 55-57% right; goal is 55%+.
- Next: let it run; review 12 h in the morning (`python3 ~/starship/markets/review.py 12`). A strategy needs about 40+ positive rounds before it earns bigger bets.

- Data (2026-11-05): `bash ~/starship/tasks/kalshi_data_sync.sh install` makes a daily 4:10 am pull of 30 days of rounds/prices/Bitcoin minutes plus your real fills, and writes memory/inbox/kalshi-data-status.md (coverage). Per-second recordings and practice logs already run continuously. Mission 2 (betting help) formally starts after Jarvis is complete (roadmap.md); data keeps collecting now.


## Review 2026-11-05 02:30 (Claude, from review.py 12 h and 24 h plus learned files on the Pi)
- No signal has a clear edge. Graded accuracy (n, right%, 95% range): momentum 193, 57.0, 46.9-65.6 (best, but cannot be told from 50%); levels 52.2; trend_1h 51.9; funding 51.3; fng 51.2; trend_h 51.0; book 50.3; bigtrades 48.1; trend_w 48.1; news 48.0; trend_4h 48.0; trend_7d 47.9; trend_24h 47.3; whales 41.5 (worst, so far). Baseline loses about 4-5% per dollar staked, the cost of trading (patterns.json train -4.9%, test -4.4%).
- 24 h (71 rounds): run -$393, hold -$536, mood -$600, swing -$584, trend -$363, signals -$195. 12 h (28 rounds) was about break-even for the old strategies: the loss came from Wed daytime (hour 08: -$182 in 3 rounds) and the 21:30-23:30 streak (6 losses in a row), then Thu 00:30-01:45 won 5 of 6. Variance is huge at 15-minute rounds.
- The ~40 "v_x..." variants made by innovate.py show +$55 to +$254 over 10-24 rounds in the last 12 h. Do NOT trust yet: many variants, small samples, same hours, same lucky stretch (several show the identical +$75.77 for the same 4 rounds). Need forward testing on unseen rounds.
- Consistent across windows: stakes over $25 lose, under $25 about break-even (run, 24 h: $25-100: 19 rounds -$389; under $25: 35 rounds -$4). The $50 cap IS holding (max staked $49.83 per round over 14 h; the "$96" in the review text is a sum of adds). Early sells hurt (-$65 on 8 sells); agent auto-disabled its take-profit rules ("every tested take-profit rule did worse than holding" over 190 rounds). Cut-tight -$262, trailing -$98, adds -$327 over 24 h. Flip versions of mood/flow lost -$366/-$394, so reversing them is not an edge.
- Timing: cheapest winning-side price comes about 3:06-4:44 into a round; the agent's first bet is about 1:32-2:08 in and pays 9-15 cents above that cheapest point; 45% of first bets are on the winning side (58% money-weighted in the last 12 h, 38% in 24 h).
- Biggest lever found: COST, not prediction. Holding to settlement pays no sell fee and no second spread; maker (resting) entries could cut the entry fee and spread; both can be tested in the simulator without any edge in prediction. Resting orders are not built yet (see PLAN.md "later stage").
- Recommended (waiting for Kylar's go): (1) cap 50 -> 25 until a strategy wins on unseen rounds; (2) hold-to-settlement as the default for the run, no early odds-sells or tight cuts, keep a cut only for big adverse moves; (3) forward-test the best variants (promote only on t >= 2 over rounds they did not see) and count how many variants were tried; (4) build a maker-entry test in the sim; (5) keep logging, review daily from memory/inbox/kalshi-digest.md.

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

## Going live (Kylar, 2026-11-05)
- Plan: yes, he will go live with real money and wants to watch it grow while learning to read trends. He has gone live before and it worked, but the agent could not use the option Kalshi offers after each trade to take profits over time (Kylar's description; Claude to look up exactly which Kalshi order option this is, e.g. a resting sell order, and add it to the agent).
- API key: works now; a new one is due around Nov 9 (Kylar unsure what is needed). Claude to check the Kalshi API notice and give exact steps before Nov 8. Keys never go in this repo.
- Live stays OFF until Kylar says. Hard rules unchanged ($5 min bet, no selling a winner without $5 profit after fees).

## Parked
- More agents on other markets (options, stocks, commodities) only after the Kalshi agent shows a real edge; share the method, not the bets. Other coins on hold. Mempool tracker for big transfers only.

## Done
(Finished items go here with the date, newest first. Never delete.)
