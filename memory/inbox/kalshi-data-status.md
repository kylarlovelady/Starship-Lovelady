# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 2840 rows
- history/candles.jsonl: 2840 rows
- history/btc1m.jsonl: 144 rows
- snapshots.jsonl: 3535 rows, last written 2026-11-05 04:19
- sim_windows.jsonl: 2607 rows, last written 2026-11-05 04:15
- calls.jsonl: 240 rows, last written 2026-11-05 04:15
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 4 day files, ticks-20261102.jsonl.gz to ticks-20261105.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 204M; Pi disk: 202G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
