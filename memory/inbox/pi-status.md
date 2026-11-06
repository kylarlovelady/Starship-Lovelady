# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 30%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 minutes; whisper Up 3 minutes (healthy); piper Up 3 minutes (healthy); pihole Up 3 minutes (healthy); homeassistant Up 3 minutes

## Sync and schedule
- Pi repo copy at: 0ba3ebb 43 seconds ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (11 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 03:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    92 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (331 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +489.29 over   92 rounds, wins 43%   (-39.97 over +4 rounds since last check)
            v_x60222031  +445.58 over   92 rounds, wins 47%   (-7.53 over +4 rounds since last check)
            v_x88221261  +301.82 over   99 rounds, wins 22%   (+0.67 over +4 rounds since last check)
            v_x80218932  +171.90 over  111 rounds, wins 45%   (-30.25 over +4 rounds since last check)
            v_x52220781  +154.09 over  103 rounds, wins 24%   (-34.85 over +4 rounds since last check)
            v_x64216772  +151.01 over  127 rounds, wins 47%   (+21.81 over +4 rounds since last check)
            v_x60222032  +120.24 over   92 rounds, wins 50%   (+21.81 over +4 rounds since last check)
            v_x24220781  +115.18 over   95 rounds, wins 45%   (-30.25 over +4 rounds since last check)
            v_hold     +106.69 over  203 rounds, wins 42%   (-9.49 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 13.4 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
