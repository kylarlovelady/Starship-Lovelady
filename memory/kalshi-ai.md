# Kalshi AI (practice money only, live mode OFF)
Updated 2026-11-04. Details: markets/PLAN.md.
- BTC 15-minute markets only. Service `market-agent` (collector.py). Restart only when collector.py changes (bump the "# vN restart" marker on line 2). Data in ~/market-data. Live View: http://loveladymainaihub.taild703ca.ts.net:8095/live.html
- Rules: nothing is retired (all strategies and signals stay eligible); hard rules only: $5 minimum bet and no selling a winner unless profit is at least $5 after fees; loss cuts are flexible (size, time left, distance to target). $50 per-round cap until a strategy proves itself.
- Findings: no signal has clearly beaten price plus fees. 24 h review: `run` lost $548, almost all from $25-100 bets (1 win in 12); bets under $25 about break-even. After the cap (2026-11-04 afternoon): 8 h loss only $40.
- Next: let it run overnight; review 12 h in the morning. A strategy needs 40+ rounds positive before it earns bigger bets.
- Cron: crew-update, market-lab (every 3 h), supervisor hourly (runs innovate.py).
