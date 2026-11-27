# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 4928 rows
- history/candles.jsonl: 4928 rows
- history/btc1m.jsonl: 250 rows
- snapshots.jsonl: 24178 rows, last written 2026-11-27 04:13
- sim_windows.jsonl: 158541 rows, last written 2026-11-27 04:02
- calls.jsonl: 1861 rows, last written 2026-11-27 04:02
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 26 day files, ticks-20261102.jsonl.gz to ticks-20261127.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 3.1G; Pi disk: 195G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
