# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 21 hours, 12 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: c69de76 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1761 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1629 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1474 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -161.26 over 1630 rounds, wins 26%   (+0.00 over +3 rounds since last check)
            v_x64216772  -179.08 over 1727 rounds, wins 56%   (+2.65 over +3 rounds since last check)
            v_x60222032  -209.85 over 1692 rounds, wins 56%   (+2.65 over +3 rounds since last check)
            v_x40223631  -249.54 over 1679 rounds, wins 56%   (+2.65 over +3 rounds since last check)
            v_edge10_s100_dd  -257.85 over 1241 rounds, wins 13%   (-54.93 over +3 rounds since last check)
            v_hold_s10  -321.04 over 1474 rounds, wins 57%   (+0.78 over +3 rounds since last check)
            v_edge10_s100  -330.64 over 1241 rounds, wins 13%   (-24.54 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 443.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
