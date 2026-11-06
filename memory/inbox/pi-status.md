# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 11 hours, 58 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 62%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 27 hours (healthy); homeassistant Up 21 hours

## Sync and schedule
- Pi repo copy at: 9809ccc 9 seconds ago: KDP: Process Operator C and E covers
- last notes sync result: push failed (run tasks/pi_push_setup.sh)
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (51 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (311 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +532.04 over   72 rounds, wins 46%   (-49.72 over +4 rounds since last check)
            v_x60222031  +397.32 over   72 rounds, wins 51%   (-8.35 over +4 rounds since last check)
            v_x88221261  +328.52 over   79 rounds, wins 24%   (-3.52 over +4 rounds since last check)
            v_x64216771  +211.15 over  107 rounds, wins 40%   (-15.49 over +4 rounds since last check)
            v_x80218932  +192.81 over   91 rounds, wins 49%   (-6.14 over +4 rounds since last check)
            v_x52220781  +179.36 over   83 rounds, wins 25%   (-3.52 over +4 rounds since last check)
            v_x16217721  +166.35 over   87 rounds, wins 30%   (-75.27 over +4 rounds since last check)
            v_x24220781  +136.09 over   75 rounds, wins 51%   (-6.14 over +4 rounds since last check)
            v_x64216772  +130.39 over  107 rounds, wins 49%   (-14.67 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 9.1 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
