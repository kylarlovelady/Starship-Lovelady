# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 10 hours, 12 minutes; temp 47.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 174039a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 56 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1791 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 9 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1667 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1512 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -167.94 over 1668 rounds, wins 26%   (-10.40 over +3 rounds since last check)
            v_edge10_s100_dd  -214.45 over 1279 rounds, wins 13%   (-67.05 over +3 rounds since last check)
            v_x64216772  -335.11 over 1765 rounds, wins 55%   (-30.37 over +3 rounds since last check)
            v_x60222032  -365.88 over 1730 rounds, wins 56%   (-30.37 over +3 rounds since last check)
            v_hold_s10  -371.22 over 1512 rounds, wins 57%   (-9.53 over +3 rounds since last check)
            v_x40223631  -405.57 over 1717 rounds, wins 55%   (-30.37 over +3 rounds since last check)
            v_take25_s10  -434.70 over 1512 rounds, wins 68%   (-1.88 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 456.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
