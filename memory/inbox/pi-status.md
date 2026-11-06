# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 13 hours, 34 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 61%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 29 hours (healthy); homeassistant Up 23 hours

## Sync and schedule
- Pi repo copy at: b954619 3 minutes ago: queue 066: more diagnostics
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (27 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (319 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 4 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +542.15 over   80 rounds, wins 45%   (-13.02 over +4 rounds since last check)
            v_x60222031  +458.97 over   80 rounds, wins 50%   (+8.26 over +4 rounds since last check)
            v_x88221261  +311.91 over   87 rounds, wins 22%   (-7.07 over +4 rounds since last check)
            v_x80218932  +193.36 over   99 rounds, wins 47%   (+0.94 over +4 rounds since last check)
            v_x64216771  +192.26 over  115 rounds, wins 38%   (-5.58 over +4 rounds since last check)
            v_x52220781  +186.89 over   91 rounds, wins 24%   (-12.50 over +4 rounds since last check)
            v_x16217721  +147.57 over   95 rounds, wins 29%   (+6.08 over +4 rounds since last check)
            v_x64216772  +142.01 over  115 rounds, wins 48%   (-3.72 over +4 rounds since last check)
            v_x24220781  +136.64 over   83 rounds, wins 48%   (+0.94 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 10.7 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
