# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3888 rows
- history/candles.jsonl: 3888 rows
- history/btc1m.jsonl: 197 rows
- snapshots.jsonl: 15338 rows, last written 2026-11-16 04:12
- sim_windows.jsonl: 83104 rows, last written 2026-11-16 04:00
- calls.jsonl: 1168 rows, last written 2026-11-16 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 15 day files, ticks-20261102.jsonl.gz to ticks-20261116.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.6G; Pi disk: 197G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
