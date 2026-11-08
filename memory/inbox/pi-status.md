# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 5 hours, 45 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 10 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: dfd3eea 23 minutes ago: Starship: remove stray agents at door and conference chairs, remove candle over screen saver board
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (541 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500  +363.66 over   86 rounds, wins 64%   (-1145.65 over +4 rounds since last check)
            v_hold_s250  +287.00 over   86 rounds, wins 64%   (-645.64 over +4 rounds since last check)
            v_x96220861  +276.85 over  304 rounds, wins 43%   (-3.13 over +4 rounds since last check)
            v_x60222031  +273.52 over  304 rounds, wins 45%   (-38.06 over +4 rounds since last check)
            v_hold_s100  +125.50 over   86 rounds, wins 64%   (-295.23 over +4 rounds since last check)
            v_x64216772  +120.02 over  339 rounds, wins 50%   (-16.66 over +4 rounds since last check)
            v_hold_after60  +101.26 over   86 rounds, wins 66%   (-43.87 over +4 rounds since last check)
            v_x60222032   +89.25 over  304 rounds, wins 51%   (-16.66 over +4 rounds since last check)
            v_hold_s50   +81.58 over   86 rounds, wins 64%   (-145.44 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 36.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
