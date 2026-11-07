# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 23 hours, 15 minutes; temp 38.4'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 23 hours; whisper Up 23 hours (healthy); piper Up 23 hours (healthy); pihole Up 23 hours (healthy); homeassistant Up 23 hours

## Sync and schedule
- Pi repo copy at: 8245ee2 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (422 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 18 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +334.96 over  191 rounds, wins 22%   (-20.99 over +4 rounds since last check)
            v_x96220861  +278.59 over  184 rounds, wins 39%   (-35.53 over +4 rounds since last check)
            v_x64216772  +175.11 over  219 rounds, wins 45%   (-10.24 over +4 rounds since last check)
            v_x60222031  +152.17 over  184 rounds, wins 39%   (-40.03 over +4 rounds since last check)
            v_x60222032  +144.34 over  184 rounds, wins 46%   (-10.24 over +4 rounds since last check)
            v_x40223631  +104.65 over  171 rounds, wins 43%   (-10.24 over +4 rounds since last check)
            v_x12229262   +96.54 over  163 rounds, wins 40%   (-23.73 over +4 rounds since last check)
            v_x40223632   +82.53 over  171 rounds, wins 46%   (+7.88 over +4 rounds since last check)
            v_x64216771   +48.58 over  219 rounds, wins 36%   (-22.62 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 5.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
