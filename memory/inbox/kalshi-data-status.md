# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3696 rows
- history/candles.jsonl: 3696 rows
- history/btc1m.jsonl: 187 rows
- snapshots.jsonl: 13436 rows, last written 2026-11-14 04:12
- sim_windows.jsonl: 66814 rows, last written 2026-11-14 04:00
- calls.jsonl: 1014 rows, last written 2026-11-14 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 13 day files, ticks-20261102.jsonl.gz to ticks-20261114.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.3G; Pi disk: 198G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
