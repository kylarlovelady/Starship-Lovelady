# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 23 hours, 15 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 10 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 8 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: 57bdf42 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    73 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1301 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 8 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +2054.49 over  162 rounds, wins 64%   (+117.77 over +3 rounds since last check)
            v_edge10_s100  +966.51 over  698 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +812.73 over  698 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_x64216772   +59.60 over 1184 rounds, wins 58%   (+0.38 over +3 rounds since last check)
            v_x60222032   +28.83 over 1149 rounds, wins 59%   (+0.38 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1086 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  931 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -10.86 over 1136 rounds, wins 58%   (+0.38 over +3 rounds since last check)
            v_x12229262   -68.76 over 1128 rounds, wins 58%   (+8.08 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 269.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
