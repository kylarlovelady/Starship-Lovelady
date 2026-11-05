# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 18 hours, 30 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 58%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 10 hours (healthy); homeassistant Up 4 hours

## Sync and schedule
- Pi repo copy at: fa47c78 29 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (243 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x8220761  +169.39 over   28 rounds, wins 43%   (-63.54 over +4 rounds since last check)
            v_x44219232  +149.20 over   27 rounds, wins 41%   (-70.11 over +4 rounds since last check)
            v_x80218932  +113.65 over   23 rounds, wins 57%   (+9.06 over +4 rounds since last check)
            v_x219212   +88.92 over   35 rounds, wins 37%   (-73.81 over +4 rounds since last check)
            v_x44219231   +87.49 over   27 rounds, wins 37%   (-66.02 over +4 rounds since last check)
            v_x16217722   +73.13 over   19 rounds, wins 53%   (-9.94 over +4 rounds since last check)
            v_x72222452   +69.33 over   28 rounds, wins 36%   (-66.02 over +4 rounds since last check)
            v_x24220781   +56.93 over    7 rounds, wins 86%   (+9.06 over +4 rounds since last check)
            v_x64216772   +45.13 over   39 rounds, wins 46%   (+14.36 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 19; errors: 0; ignored blips: 5; last activity: 0 min ago
- hang-ups: you ended it x7, quiet x2
- time to first words: avg 1.9s, slowest 4.2s over 18 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
