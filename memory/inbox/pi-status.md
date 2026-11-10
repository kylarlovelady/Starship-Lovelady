# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 14 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 22 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 78d2337 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    80 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (719 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +409.33 over   39 rounds, wins 8%   (-49.35 over +4 rounds since last check)
            v_edge10_s100  +380.46 over   39 rounds, wins 8%   (-49.35 over +4 rounds since last check)
            v_x60222031  +269.47 over  490 rounds, wins 46%   (-5.81 over +4 rounds since last check)
            v_x64216772  +104.18 over  525 rounds, wins 53%   (-4.46 over +4 rounds since last check)
            v_x60222032   +73.41 over  490 rounds, wins 54%   (-4.46 over +4 rounds since last check)
            v_x40223631   +33.72 over  477 rounds, wins 53%   (-4.46 over +4 rounds since last check)
            v_snipe_all    +2.70 over  427 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  272 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -26.59 over  272 rounds, wins 60%   (-4.37 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 92.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
