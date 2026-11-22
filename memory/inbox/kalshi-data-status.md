# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4456 rows
- history/candles.jsonl: 4456 rows
- history/btc1m.jsonl: 226 rows
- snapshots.jsonl: 20469 rows, last written 2026-11-22 04:13
- sim_windows.jsonl: 126691 rows, last written 2026-11-22 04:01
- calls.jsonl: 1566 rows, last written 2026-11-22 04:01
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 21 day files, ticks-20261102.jsonl.gz to ticks-20261122.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 2.4G; Pi disk: 196G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
