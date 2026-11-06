# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 hour, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 30%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up About an hour; whisper Up About an hour (healthy); piper Up About an hour (healthy); pihole Up About an hour (healthy); homeassistant Up About an hour

## Sync and schedule
- Pi repo copy at: 23a06b8 8 minutes ago: Note 20 Ultra plan
- last notes sync result: remove the file manually to continue.
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (335 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +491.21 over   96 rounds, wins 43%   (+1.92 over +4 rounds since last check)
            v_x60222031  +447.94 over   96 rounds, wins 46%   (+2.36 over +4 rounds since last check)
            v_x88221261  +292.16 over  103 rounds, wins 21%   (-9.66 over +4 rounds since last check)
            v_x64216771  +230.72 over  131 rounds, wins 37%   (+127.97 over +4 rounds since last check)
            v_x80218932  +153.92 over  115 rounds, wins 44%   (-17.98 over +4 rounds since last check)
            v_x64216772  +152.80 over  131 rounds, wins 47%   (+1.79 over +4 rounds since last check)
            v_x52220781  +125.74 over  107 rounds, wins 23%   (-28.35 over +4 rounds since last check)
            v_x60222032  +122.03 over   96 rounds, wins 49%   (+1.79 over +4 rounds since last check)
            v_x24220781   +97.20 over   99 rounds, wins 44%   (-17.98 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 14.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
