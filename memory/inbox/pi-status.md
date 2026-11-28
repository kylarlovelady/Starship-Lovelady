# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 2 days, 17 hours, 42 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 9 days (healthy); piper Up 9 days (healthy); pihole Up 9 days (healthy); homeassistant Up 9 days

## Sync and schedule
- Pi repo copy at: c0c6767 15 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 28 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 4 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 53 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1914 total)
      OK    entry_stats.json updated 9 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +601.75 over 1425 rounds, wins 14%   (+12.94 over +2 rounds since last check)
            v_edge10_s100  +332.26 over 1425 rounds, wins 14%   (+53.48 over +2 rounds since last check)
            v_snipe_all    +2.70 over 1813 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1658 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_snipe    -125.70 over 1814 rounds, wins 26%   (+12.94 over +2 rounds since last check)
            v_hold_s10  -372.83 over 1658 rounds, wins 56%   (+6.75 over +2 rounds since last check)
            v_x64216772  -387.08 over 1911 rounds, wins 55%   (+12.94 over +2 rounds since last check)
            v_x60222032  -417.85 over 1876 rounds, wins 55%   (+12.94 over +2 rounds since last check)
            v_x40223631  -459.58 over 1863 rounds, wins 55%   (+12.94 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 512.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
