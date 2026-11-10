# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3320 rows
- history/candles.jsonl: 3320 rows
- history/btc1m.jsonl: 168 rows
- snapshots.jsonl: 9177 rows, last written 2026-11-10 04:10
- sim_windows.jsonl: 33924 rows, last written 2026-11-10 04:00
- calls.jsonl: 672 rows, last written 2026-11-10 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 9 day files, ticks-20261102.jsonl.gz to ticks-20261110.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 832M; Pi disk: 200G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
