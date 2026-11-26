# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 17 hours, 26 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 343e1b3 14 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (37 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 51 of the last 96 rounds were settled by Kalshi and logged
      STUCK +0 new written lessons since the last check (1802 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1681 rounds, wins 0%   (+0.00 over +0 rounds since last check)
            v_hold_s5    +0.00 over 1526 rounds, wins 0%   (+0.00 over +0 rounds since last check)
            v_edge10_s100_dd   -66.20 over 1293 rounds, wins 13%   (+0.00 over +0 rounds since last check)
            v_snipe    -166.52 over 1682 rounds, wins 25%   (+0.00 over +0 rounds since last check)
            v_x64216772  -380.27 over 1779 rounds, wins 55%   (+0.00 over +0 rounds since last check)
            v_hold_s10  -383.74 over 1526 rounds, wins 57%   (+0.00 over +0 rounds since last check)
            v_edge10_s100  -395.17 over 1293 rounds, wins 13%   (+0.00 over +0 rounds since last check)
            v_x60222032  -411.04 over 1744 rounds, wins 56%   (+0.00 over +0 rounds since last check)
            v_x40223631  -450.73 over 1731 rounds, wins 55%   (+0.00 over +0 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 464.1 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
