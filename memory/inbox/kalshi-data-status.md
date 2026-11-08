# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3128 rows
- history/candles.jsonl: 3128 rows
- history/btc1m.jsonl: 159 rows
- snapshots.jsonl: 7341 rows, last written 2026-11-08 04:11
- sim_windows.jsonl: 21264 rows, last written 2026-11-08 04:01
- calls.jsonl: 525 rows, last written 2026-11-08 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 7 day files, ticks-20261102.jsonl.gz to ticks-20261108.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 661M; Pi disk: 201G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
