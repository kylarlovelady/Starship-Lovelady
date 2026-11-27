# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 20 hours, 12 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 12b4092 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 27 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 56 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1867 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +109.39 over 1370 rounds, wins 14%   (+44.81 over +2 rounds since last check)
            v_snipe_all    +2.70 over 1758 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1603 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_edge10_s100   -89.88 over 1370 rounds, wins 14%   (+110.29 over +2 rounds since last check)
            v_snipe    -129.31 over 1759 rounds, wins 26%   (+15.69 over +2 rounds since last check)
            v_x64216772  -359.19 over 1856 rounds, wins 55%   (+3.46 over +2 rounds since last check)
            v_hold_s10  -377.87 over 1603 rounds, wins 57%   (-0.09 over +2 rounds since last check)
            v_x60222032  -389.96 over 1821 rounds, wins 55%   (+3.46 over +2 rounds since last check)
            v_x40223631  -431.69 over 1808 rounds, wins 55%   (+3.46 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 490.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
