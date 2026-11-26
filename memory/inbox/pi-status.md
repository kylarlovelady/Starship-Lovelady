# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 5 hours, 42 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 57d1852 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 16:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 52 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1832 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 3 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1717 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1562 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd   -41.29 over 1329 rounds, wins 13%   (+180.74 over +3 rounds since last check)
            v_snipe    -139.83 over 1718 rounds, wins 26%   (+14.83 over +3 rounds since last check)
            v_x64216772  -365.99 over 1815 rounds, wins 55%   (-2.10 over +3 rounds since last check)
            v_hold_s10  -367.20 over 1562 rounds, wins 57%   (-3.04 over +3 rounds since last check)
            v_x60222032  -396.76 over 1780 rounds, wins 56%   (-2.10 over +3 rounds since last check)
            v_x40223631  -436.45 over 1767 rounds, wins 55%   (-2.10 over +3 rounds since last check)
            v_edge10_s100  -464.86 over 1329 rounds, wins 13%   (+215.14 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 476.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
