# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 23 hours, 42 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 24 hours; whisper Up 24 hours (healthy); piper Up 24 hours (healthy); pihole Up 24 hours (healthy); homeassistant Up 24 hours

## Sync and schedule
- Pi repo copy at: 76ae8fb 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    62 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1385 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1337.85 over  796 rounds, wins 12%   (+0.00 over +4 rounds since last check)
            v_hold_s250_wild +1082.26 over  260 rounds, wins 63%   (+7.65 over +4 rounds since last check)
            v_edge10_s100_dd  +832.04 over  796 rounds, wins 12%   (+0.00 over +4 rounds since last check)
            v_x60222031  +153.89 over 1247 rounds, wins 47%   (+8.98 over +4 rounds since last check)
            v_x64216772   +32.40 over 1282 rounds, wins 58%   (+10.78 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1184 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222032    +1.63 over 1247 rounds, wins 59%   (+10.78 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1029 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x12229262   -37.71 over 1226 rounds, wins 58%   (+18.67 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 302.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
