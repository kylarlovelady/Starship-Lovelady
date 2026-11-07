# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 22 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 22 hours; whisper Up 22 hours (healthy); piper Up 22 hours (healthy); pihole Up 22 hours (healthy); homeassistant Up 22 hours

## Sync and schedule
- Pi repo copy at: 66e3347 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (418 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +355.95 over  187 rounds, wins 22%   (+99.49 over +4 rounds since last check)
            v_x96220861  +314.12 over  180 rounds, wins 39%   (-54.19 over +4 rounds since last check)
            v_x60222031  +192.20 over  180 rounds, wins 39%   (-71.54 over +4 rounds since last check)
            v_x64216772  +185.35 over  215 rounds, wins 46%   (-16.84 over +4 rounds since last check)
            v_x60222032  +154.58 over  180 rounds, wins 47%   (-16.84 over +4 rounds since last check)
            v_x12229262  +120.27 over  159 rounds, wins 41%   (-53.50 over +4 rounds since last check)
            v_x40223631  +114.89 over  167 rounds, wins 43%   (-16.84 over +4 rounds since last check)
            v_x40223632   +74.65 over  167 rounds, wins 46%   (+41.59 over +4 rounds since last check)
            v_x64216771   +71.20 over  215 rounds, wins 36%   (-86.62 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 4.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
