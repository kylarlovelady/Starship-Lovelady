# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4832 rows
- history/candles.jsonl: 4832 rows
- history/btc1m.jsonl: 245 rows
- snapshots.jsonl: 23470 rows, last written 2026-11-26 04:11
- sim_windows.jsonl: 152171 rows, last written 2026-11-26 01:48
- calls.jsonl: 1802 rows, last written 2026-11-26 01:48
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 25 day files, ticks-20261102.jsonl.gz to ticks-20261126.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.9G; Pi disk: 196G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
