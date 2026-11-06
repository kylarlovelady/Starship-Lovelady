# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 8 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 hours; whisper Up 8 hours (healthy); piper Up 8 hours (healthy); pihole Up 8 hours (healthy); homeassistant Up 8 hours

## Sync and schedule
- Pi repo copy at: d4d22a2 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (363 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +383.54 over  124 rounds, wins 40%   (-45.59 over +4 rounds since last check)
            v_x60222031  +303.28 over  124 rounds, wins 40%   (-86.18 over +4 rounds since last check)
            v_x88221261  +253.06 over  131 rounds, wins 20%   (-7.79 over +4 rounds since last check)
            v_x64216771  +177.84 over  159 rounds, wins 36%   (-49.39 over +4 rounds since last check)
            v_x64216772  +111.37 over  159 rounds, wins 44%   (-17.83 over +4 rounds since last check)
            v_x52220781   +96.43 over  135 rounds, wins 21%   (+10.19 over +4 rounds since last check)
            v_x60222032   +80.60 over  124 rounds, wins 45%   (-17.83 over +4 rounds since last check)
            v_x36215122   +72.20 over  151 rounds, wins 17%   (-10.05 over +4 rounds since last check)
            v_x80218932   +62.76 over  143 rounds, wins 41%   (-40.08 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 21.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
