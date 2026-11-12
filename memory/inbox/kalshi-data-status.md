# Kalshi data on the Pi (auto, counts only)

- history/rounds.jsonl: 3504 rows
- history/candles.jsonl: 3504 rows
- history/btc1m.jsonl: 178 rows
- snapshots.jsonl: 11386 rows, last written 2026-11-12 04:11
- sim_windows.jsonl: 50254 rows, last written 2026-11-12 02:03
- calls.jsonl: 844 rows, last written 2026-11-12 02:09
- live_orders.jsonl: 61 rows, last written 2026-11-02 23:32
- per-second recordings: 11 day files, ticks-20261102.jsonl.gz to ticks-20261112.jsonl
- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)
- market-data size: 1.1G; Pi disk: 199G free

Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files.
