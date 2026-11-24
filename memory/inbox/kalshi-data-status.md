# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4648 rows
- history/candles.jsonl: 4648 rows
- history/btc1m.jsonl: 235 rows
- snapshots.jsonl: 22005 rows, last written 2026-11-24 04:10
- sim_windows.jsonl: 140068 rows, last written 2026-11-24 03:47
- calls.jsonl: 1691 rows, last written 2026-11-24 03:47
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 23 day files, ticks-20261102.jsonl.gz to ticks-20261124.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.7G; Pi disk: 196G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
