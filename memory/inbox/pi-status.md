# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 45 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 9 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 60daabc 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 03:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 52 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (668 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1505.36 over  216 rounds, wins 62%   (+473.95 over +4 rounds since last check)
            v_hold_s250  +699.29 over  216 rounds, wins 62%   (+240.91 over +4 rounds since last check)
            v_hold_s100  +284.03 over  216 rounds, wins 62%   (+100.98 over +4 rounds since last check)
            v_hold_s50  +157.98 over  216 rounds, wins 62%   (+54.66 over +4 rounds since last check)
            v_x64216772  +118.33 over  469 rounds, wins 53%   (+3.57 over +4 rounds since last check)
            v_x60222031   +88.95 over  434 rounds, wins 45%   (+18.11 over +4 rounds since last check)
            v_x60222032   +87.56 over  434 rounds, wins 54%   (+3.57 over +4 rounds since last check)
            v_hold_s25   +76.72 over  216 rounds, wins 62%   (+31.02 over +4 rounds since last check)
            v_x40223631   +47.87 over  421 rounds, wins 52%   (+3.57 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 79.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
