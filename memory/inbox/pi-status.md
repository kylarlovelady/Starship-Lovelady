# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 2 hours, 45 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 35 hours (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: caf9a7d 10 minutes ago: Kitchen screen Pi plan
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (764 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +782.41 over   87 rounds, wins 13%   (-52.51 over +4 rounds since last check)
            v_edge10_s100  +524.42 over   87 rounds, wins 13%   (-81.29 over +4 rounds since last check)
            v_x60222031  +174.38 over  538 rounds, wins 45%   (-27.74 over +4 rounds since last check)
            v_x64216772   +74.24 over  573 rounds, wins 53%   (-12.00 over +4 rounds since last check)
            v_x60222032   +43.47 over  538 rounds, wins 54%   (-12.00 over +4 rounds since last check)
            v_x40223631    +3.78 over  525 rounds, wins 53%   (-12.00 over +4 rounds since last check)
            v_snipe_all    +2.70 over  475 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  320 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -58.64 over  320 rounds, wins 59%   (-13.89 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 105.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
