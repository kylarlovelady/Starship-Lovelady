# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3224 rows
- history/candles.jsonl: 3224 rows
- history/btc1m.jsonl: 163 rows
- snapshots.jsonl: 8521 rows, last written 2026-11-09 04:11
- sim_windows.jsonl: 29328 rows, last written 2026-11-09 04:00
- calls.jsonl: 619 rows, last written 2026-11-09 04:00
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 8 day files, ticks-20261102.jsonl.gz to ticks-20261109.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 763M; Pi disk: 201G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
