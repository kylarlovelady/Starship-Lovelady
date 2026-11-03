# Market agent plan (written 2026-11-03 so nothing gets forgotten)

Goal: a BTC 15-minute Kalshi agent that learns, from its own recorded data, what really wins. Practice money only until proven. Live mode stays OFF.

## Everything that must be tested, rated, tuned, and logged
1. **Signals, each graded alone** (never lumped): BTC speed, slowing, distance from target, 15m/1h/4h/24h/7d trends, Kalshi ticker speed, trade flow, Kalshi book imbalance, Coinbase book, exchange gaps, open interest, funding, liquidations, news, whales, big trades, fear & greed, support/resistance. Weight = Kylar's rating x evidence (grades.py -> signal_weights.json).
2. **Response to each signal** (separate from signal quality; must be learned and self-correcting): when to buy, which side (with or against), how much, hold, add to winners, when to cut a loss, when to sell a winner. Tested by lab.py, response.py, pairs.py, stops.py.
3. **Selling rules**: no hard timer; never sell for a few cents (need ~$3 or 2% after fees); cut losses instead of riding to the end; bank at target, trail the peak, sell when the move slows, or hold. Never buy and sell within seconds.
4. **Speed / bots**: lag.py (Kalshi vs BTC), Kalshi trade tape (ktrades) to see bots' behavior, resting orders and Kalshi Auto Sell (take-profit) as a later stage.
5. **Endgame**: settlement-average model in the last 60 s (endgame.py).
6. **Data logging**: per-second recorder; every lab rule tried goes to ~/market-data/lab_log.jsonl; trades log carries features.

## How a result earns trust
Chosen on older rounds, checked on newest rounds, t-stat, and still winning the next day. With ~100 per-second rounds (+~96/day) most findings are weak until data grows.

## Findings so far
No single signal beats price + fees on 1267 minute-level rounds. Trends carry no information. BTC speed and distance move price a few cents but net about break-even. Kalshi lags BTC 1-2c vs ~3.6c round-trip cost. Coach guardrails not yet proven.

## Running now vs next
Running: v5 agent (fresh scoreboard). Not yet running (needs restart on Kylar's go = v6): $3/2% min profit, 35% loss cut, Kalshi trade tape, split trends, weights from ratings, response-learning, promotion of lab winners to practice strategies.
Lab (read-only, runs overnight): `bash ~/starship/tasks/lab_setup.sh`.

## Open
Kylar to rate 9 signals (or "go with yours"); run pairs.py, endgame.py, stops.py; Kalshi API location check by Nov 9; confirm maker fee on first real fill.
