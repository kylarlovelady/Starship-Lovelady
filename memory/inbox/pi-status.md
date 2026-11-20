# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 12 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 9c044b6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1448 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +723.78 over  876 rounds, wins 12%   (-41.96 over +3 rounds since last check)
            v_edge10_s100_dd  +412.13 over  876 rounds, wins 12%   (-10.37 over +3 rounds since last check)
            v_x60222031  +145.23 over 1327 rounds, wins 47%   (-25.64 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1264 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1109 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s250_wild   -11.65 over  340 rounds, wins 62%   (-187.94 over +3 rounds since last check)
            v_x64216772   -20.70 over 1362 rounds, wins 58%   (+12.23 over +3 rounds since last check)
            v_x60222032   -51.47 over 1327 rounds, wins 59%   (+12.23 over +3 rounds since last check)
            v_x40223631   -91.16 over 1314 rounds, wins 58%   (+12.23 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 326.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
