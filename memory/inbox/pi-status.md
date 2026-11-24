# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 4 hours, 42 minutes; temp 46.1'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 5a01a28 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 4 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1720 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1579 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1424 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_snipe    -134.47 over 1580 rounds, wins 26%   (+0.21 over +2 rounds since last check)
            v_x64216772  -201.21 over 1677 rounds, wins 56%   (-10.15 over +2 rounds since last check)
            hold       -226.54 over 1780 rounds, wins 59%   (-21.44 over +2 rounds since last check)
            v_x60222032  -231.98 over 1642 rounds, wins 56%   (-10.15 over +2 rounds since last check)
            v_x40223631  -271.67 over 1629 rounds, wins 56%   (-10.15 over +2 rounds since last check)
            v_hold_s10  -296.58 over 1424 rounds, wins 58%   (-5.48 over +2 rounds since last check)
            v_x60222031  -300.52 over 1642 rounds, wins 46%   (-19.53 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 427.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
