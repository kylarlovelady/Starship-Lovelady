# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 12 hours, 12 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 08f1d4b 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 23:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 57 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1796 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1674 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1519 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_edge10_s100_dd   -29.05 over 1286 rounds, wins 13%   (+152.24 over +4 rounds since last check)
            v_snipe    -166.82 over 1675 rounds, wins 25%   (+0.00 over +4 rounds since last check)
            v_edge10_s100  -273.79 over 1286 rounds, wins 13%   (+140.93 over +4 rounds since last check)
            v_x64216772  -341.68 over 1772 rounds, wins 55%   (-8.82 over +4 rounds since last check)
            v_x60222032  -372.45 over 1737 rounds, wins 56%   (-8.82 over +4 rounds since last check)
            v_hold_s10  -373.87 over 1519 rounds, wins 57%   (-4.01 over +4 rounds since last check)
            v_x40223631  -412.14 over 1724 rounds, wins 55%   (-8.82 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 458.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
