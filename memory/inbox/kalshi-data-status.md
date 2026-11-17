# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3984 rows
- history/candles.jsonl: 3984 rows
- history/btc1m.jsonl: 202 rows
- snapshots.jsonl: 16257 rows, last written 2026-11-17 04:13
- sim_windows.jsonl: 90928 rows, last written 2026-11-17 04:02
- calls.jsonl: 1233 rows, last written 2026-11-17 03:46
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 16 day files, ticks-20261102.jsonl.gz to ticks-20261117.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.7G; Pi disk: 197G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
