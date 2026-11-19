# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 7 hours, 12 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 hours; whisper Up 7 hours (healthy); piper Up 7 hours (healthy); pihole Up 7 hours (healthy); homeassistant Up 7 hours

## Sync and schedule
- Pi repo copy at: dc54a3d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1346 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1449.80 over  215 rounds, wins 63%   (-132.83 over +3 rounds since last check)
            v_edge10_s100 +1181.50 over  751 rounds, wins 13%   (+44.90 over +3 rounds since last check)
            v_edge10_s100_dd  +884.34 over  751 rounds, wins 13%   (+11.15 over +3 rounds since last check)
            v_x60222031  +234.79 over 1202 rounds, wins 47%   (-5.24 over +3 rounds since last check)
            v_x64216772   +70.28 over 1237 rounds, wins 58%   (+30.08 over +3 rounds since last check)
            v_x60222032   +39.51 over 1202 rounds, wins 59%   (+30.08 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1139 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  984 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631    -0.18 over 1189 rounds, wins 58%   (+30.08 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 285.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
