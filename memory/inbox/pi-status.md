# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 1 hour, 45 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: db6f904 15 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (525 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1308.30 over   70 rounds, wins 67%   (+600.69 over +4 rounds since last check)
            v_hold_s250  +876.42 over   70 rounds, wins 67%   (+302.63 over +4 rounds since last check)
            v_hold_s100  +451.75 over   70 rounds, wins 67%   (+123.72 over +4 rounds since last check)
            v_x60222031  +273.57 over  288 rounds, wins 44%   (+42.25 over +4 rounds since last check)
            v_hold_s50  +247.40 over   70 rounds, wins 67%   (+64.34 over +4 rounds since last check)
            v_x96220861  +237.73 over  288 rounds, wins 42%   (+42.83 over +4 rounds since last check)
            v_hold_after60  +172.19 over   70 rounds, wins 69%   (-3.61 over +4 rounds since last check)
            v_hold_after120  +158.25 over   70 rounds, wins 67%   (-4.57 over +4 rounds since last check)
            v_x64216772  +135.30 over  323 rounds, wins 50%   (+11.67 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 32.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
