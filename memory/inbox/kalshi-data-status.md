# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4744 rows
- history/candles.jsonl: 4744 rows
- history/btc1m.jsonl: 240 rows
- snapshots.jsonl: 22745 rows, last written 2026-11-25 04:10
- sim_windows.jsonl: 146256 rows, last written 2026-11-25 04:00
- calls.jsonl: 1750 rows, last written 2026-11-25 03:47
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 24 day files, ticks-20261102.jsonl.gz to ticks-20261125.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.8G; Pi disk: 196G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
