# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 4 hours, 19 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 19 hours (healthy); homeassistant Up 13 hours

## Sync and schedule
- Pi repo copy at: 26cbb2e 3 minutes ago: queue 036: recording only, auto rollback if unhealthy
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (12 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (283 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +595.42 over   44 rounds, wins 57%   (-24.70 over +4 rounds since last check)
            v_x16217721  +486.26 over   59 rounds, wins 36%   (-57.38 over +4 rounds since last check)
            v_x64216771  +443.77 over   79 rounds, wins 47%   (+31.94 over +4 rounds since last check)
            v_x88221261  +419.81 over   51 rounds, wins 31%   (-31.05 over +4 rounds since last check)
            v_x60222031  +379.36 over   44 rounds, wins 57%   (+16.08 over +4 rounds since last check)
            v_x32221881  +378.31 over   43 rounds, wins 51%   (+28.78 over +4 rounds since last check)
            v_x96220872  +233.55 over   44 rounds, wins 41%   (-18.33 over +4 rounds since last check)
            v_x52220781  +212.69 over   55 rounds, wins 31%   (-2.96 over +4 rounds since last check)
            v_x80218932  +203.02 over   63 rounds, wins 54%   (-10.19 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 1.4 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
