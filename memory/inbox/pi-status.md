# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 2 hours, 15 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 4b8456c 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (529 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 9 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +297.34 over  292 rounds, wins 45%   (+23.77 over +4 rounds since last check)
            v_x96220861  +295.46 over  292 rounds, wins 42%   (+57.73 over +4 rounds since last check)
            v_hold_s250  +282.14 over   74 rounds, wins 64%   (-594.28 over +4 rounds since last check)
            v_hold_s500  +213.35 over   74 rounds, wins 64%   (-1094.95 over +4 rounds since last check)
            v_hold_s100  +156.99 over   74 rounds, wins 64%   (-294.76 over +4 rounds since last check)
            v_x64216772  +113.26 over  327 rounds, wins 50%   (-22.04 over +4 rounds since last check)
            v_hold_after120   +97.59 over   74 rounds, wins 64%   (-60.66 over +4 rounds since last check)
            v_hold_after60   +92.86 over   74 rounds, wins 65%   (-79.33 over +4 rounds since last check)
            v_hold_s50   +92.56 over   74 rounds, wins 64%   (-154.84 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 32.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
