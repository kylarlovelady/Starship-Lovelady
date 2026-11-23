# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4552 rows
- history/candles.jsonl: 4552 rows
- history/btc1m.jsonl: 231 rows
- snapshots.jsonl: 21245 rows, last written 2026-11-23 04:11
- sim_windows.jsonl: 133698 rows, last written 2026-11-23 03:47
- calls.jsonl: 1629 rows, last written 2026-11-23 03:47
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 22 day files, ticks-20261102.jsonl.gz to ticks-20261123.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.6G; Pi disk: 196G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
