# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 5024 rows
- history/candles.jsonl: 5024 rows
- history/btc1m.jsonl: 255 rows
- snapshots.jsonl: 24872 rows, last written 2026-11-28 04:13
- sim_windows.jsonl: 164183 rows, last written 2026-11-28 03:47
- calls.jsonl: 1914 rows, last written 2026-11-28 03:47
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 27 day files, ticks-20261102.jsonl.gz to ticks-20261128.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 3.2G; Pi disk: 195G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
