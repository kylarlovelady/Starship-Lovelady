# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4168 rows
- history/candles.jsonl: 4168 rows
- history/btc1m.jsonl: 211 rows
- snapshots.jsonl: 17992 rows, last written 2026-11-19 04:13
- sim_windows.jsonl: 105124 rows, last written 2026-11-19 02:02
- calls.jsonl: 1367 rows, last written 2026-11-19 02:09
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 18 day files, ticks-20261102.jsonl.gz to ticks-20261119.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.9G; Pi disk: 197G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
