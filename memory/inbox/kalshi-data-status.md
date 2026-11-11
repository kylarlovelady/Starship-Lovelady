# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3416 rows
- history/candles.jsonl: 3416 rows
- history/btc1m.jsonl: 173 rows
- snapshots.jsonl: 10298 rows, last written 2026-11-11 04:12
- sim_windows.jsonl: 42514 rows, last written 2026-11-11 04:00
- calls.jsonl: 760 rows, last written 2026-11-11 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 10 day files, ticks-20261102.jsonl.gz to ticks-20261111.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 963M; Pi disk: 200G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
