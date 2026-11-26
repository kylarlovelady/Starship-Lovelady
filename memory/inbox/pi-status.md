# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 4 hours, 12 minutes; temp 48.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 382477c 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 52 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1830 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 2 min ago
      OK    learn_report.json updated 3 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1714 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1559 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_snipe    -154.66 over 1715 rounds, wins 26%   (+0.19 over +4 rounds since last check)
            v_edge10_s100_dd  -222.03 over 1326 rounds, wins 13%   (-10.39 over +4 rounds since last check)
            v_x64216772  -363.89 over 1812 rounds, wins 55%   (-7.06 over +4 rounds since last check)
            v_hold_s10  -364.16 over 1559 rounds, wins 57%   (+8.10 over +4 rounds since last check)
            v_x60222032  -394.66 over 1777 rounds, wins 55%   (-7.06 over +4 rounds since last check)
            v_x40223631  -434.35 over 1764 rounds, wins 55%   (-7.06 over +4 rounds since last check)
            v_take25_s10  -484.92 over 1559 rounds, wins 67%   (-0.11 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 474.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
