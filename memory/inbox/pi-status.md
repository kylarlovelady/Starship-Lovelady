# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 18 hours, 15 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 26 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 0f7f0bf 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (734 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd +1147.72 over   55 rounds, wins 15%   (+157.20 over +4 rounds since last check)
            v_edge10_s100 +1118.85 over   55 rounds, wins 15%   (+157.20 over +4 rounds since last check)
            v_x60222031  +225.22 over  506 rounds, wins 46%   (-37.07 over +4 rounds since last check)
            v_x64216772   +90.65 over  541 rounds, wins 53%   (-15.98 over +4 rounds since last check)
            v_x60222032   +59.88 over  506 rounds, wins 54%   (-15.98 over +4 rounds since last check)
            v_x40223631   +20.19 over  493 rounds, wins 53%   (-15.98 over +4 rounds since last check)
            v_snipe_all    +2.70 over  443 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  288 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x96220861   -24.51 over  506 rounds, wins 44%   (-24.28 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 96.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
