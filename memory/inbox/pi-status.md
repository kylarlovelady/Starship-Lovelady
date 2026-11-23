# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 12 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 8a3b1db 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 23 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    64 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1649 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1500 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1345 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -88.66 over 1598 rounds, wins 57%   (-7.81 over +4 rounds since last check)
            v_x60222032  -119.43 over 1563 rounds, wins 57%   (-7.81 over +4 rounds since last check)
            v_snipe    -148.81 over 1501 rounds, wins 26%   (-9.49 over +4 rounds since last check)
            v_x40223631  -159.12 over 1550 rounds, wins 57%   (-7.81 over +4 rounds since last check)
            hold       -244.17 over 1701 rounds, wins 58%   (-29.10 over +4 rounds since last check)
            v_x60222031  -251.75 over 1563 rounds, wins 46%   (-71.09 over +4 rounds since last check)
            v_hold_s10  -275.89 over 1345 rounds, wins 59%   (-4.45 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 398.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
