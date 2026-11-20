# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4264 rows
- history/candles.jsonl: 4264 rows
- history/btc1m.jsonl: 216 rows
- snapshots.jsonl: 18840 rows, last written 2026-11-20 04:11
- sim_windows.jsonl: 112131 rows, last written 2026-11-20 03:48
- calls.jsonl: 1430 rows, last written 2026-11-20 03:32
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 19 day files, ticks-20261102.jsonl.gz to ticks-20261120.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.1G; Pi disk: 197G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
