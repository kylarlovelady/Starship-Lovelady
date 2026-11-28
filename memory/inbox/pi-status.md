# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 2 days, 9 hours, 42 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 9 days (healthy); piper Up 9 days (healthy); pihole Up 9 days (healthy); homeassistant Up 9 days

## Sync and schedule
- Pi repo copy at: f5e177d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 27 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 56 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1897 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 1 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +309.05 over 1407 rounds, wins 14%   (+61.24 over +2 rounds since last check)
            v_snipe_all    +2.70 over 1795 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1640 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_edge10_s100    -7.83 over 1407 rounds, wins 14%   (+31.52 over +2 rounds since last check)
            v_snipe    -141.13 over 1796 rounds, wins 26%   (+9.85 over +2 rounds since last check)
            v_hold_s10  -376.75 over 1640 rounds, wins 57%   (+1.14 over +2 rounds since last check)
            v_x64216772  -395.11 over 1893 rounds, wins 55%   (+12.94 over +2 rounds since last check)
            v_x60222032  -425.88 over 1858 rounds, wins 55%   (+12.94 over +2 rounds since last check)
            v_x40223631  -467.61 over 1845 rounds, wins 55%   (+12.94 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 504.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
