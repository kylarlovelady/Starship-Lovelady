# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3792 rows
- history/candles.jsonl: 3792 rows
- history/btc1m.jsonl: 192 rows
- snapshots.jsonl: 14402 rows, last written 2026-11-15 04:12
- sim_windows.jsonl: 75184 rows, last written 2026-11-15 04:02
- calls.jsonl: 1092 rows, last written 2026-11-15 04:02
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 14 day files, ticks-20261102.jsonl.gz to ticks-20261115.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.5G; Pi disk: 198G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
