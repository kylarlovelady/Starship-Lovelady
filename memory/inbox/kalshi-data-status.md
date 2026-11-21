# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4360 rows
- history/candles.jsonl: 4360 rows
- history/btc1m.jsonl: 221 rows
- snapshots.jsonl: 19665 rows, last written 2026-11-21 04:11
- sim_windows.jsonl: 118865 rows, last written 2026-11-21 03:48
- calls.jsonl: 1493 rows, last written 2026-11-21 03:48
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 20 day files, ticks-20261102.jsonl.gz to ticks-20261121.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.3G; Pi disk: 197G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
