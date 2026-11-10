# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 21 hours, 45 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 6 hours (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 6712e04 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 50 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (656 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1995.58 over  204 rounds, wins 61%   (-1034.60 over +4 rounds since last check)
            v_hold_s250  +941.03 over  204 rounds, wins 61%   (-517.63 over +4 rounds since last check)
            v_hold_s100  +376.17 over  204 rounds, wins 61%   (-207.74 over +4 rounds since last check)
            v_hold_s50  +200.71 over  204 rounds, wins 61%   (-103.96 over +4 rounds since last check)
            v_x60222031  +141.25 over  422 rounds, wins 46%   (-48.45 over +4 rounds since last check)
            v_x64216772  +126.96 over  457 rounds, wins 53%   (-11.33 over +4 rounds since last check)
            v_x60222032   +96.19 over  422 rounds, wins 54%   (-11.33 over +4 rounds since last check)
            v_hold_s25   +94.85 over  204 rounds, wins 61%   (-52.41 over +4 rounds since last check)
            v_x40223631   +56.50 over  409 rounds, wins 52%   (-11.33 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 76.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
