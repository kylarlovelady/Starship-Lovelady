# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 10 hours, 42 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 2e9fc69 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 50 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1842 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1730 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1575 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  -151.09 over 1342 rounds, wins 13%   (-50.85 over +3 rounds since last check)
            v_snipe    -158.82 over 1731 rounds, wins 26%   (-10.03 over +3 rounds since last check)
            v_hold_s10  -378.29 over 1575 rounds, wins 57%   (+3.96 over +3 rounds since last check)
            v_x64216772  -400.47 over 1828 rounds, wins 55%   (+5.84 over +3 rounds since last check)
            v_x60222032  -431.24 over 1793 rounds, wins 55%   (+5.84 over +3 rounds since last check)
            v_x40223631  -470.93 over 1780 rounds, wins 55%   (+5.84 over +3 rounds since last check)
            v_take25_s10  -487.59 over 1575 rounds, wins 67%   (+3.96 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 481.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
