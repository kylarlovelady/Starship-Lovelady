# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 2936 rows
- history/candles.jsonl: 2936 rows
- history/btc1m.jsonl: 149 rows
- snapshots.jsonl: 4848 rows, last written 2026-11-06 04:11
- sim_windows.jsonl: 8064 rows, last written 2026-11-06 04:00
- calls.jsonl: 335 rows, last written 2026-11-06 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 5 day files, ticks-20261102.jsonl.gz to ticks-20261106.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 395M; Pi disk: 202G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
