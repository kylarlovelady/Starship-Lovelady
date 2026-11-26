# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 9 hours, 12 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 5b89eb4 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 55 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1788 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1664 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1509 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_edge10_s100_dd  -147.40 over 1276 rounds, wins 13%   (+0.00 over +4 rounds since last check)
            v_snipe    -157.54 over 1665 rounds, wins 26%   (+0.78 over +4 rounds since last check)
            v_x64216772  -304.74 over 1762 rounds, wins 55%   (-24.83 over +4 rounds since last check)
            v_edge10_s100  -315.56 over 1276 rounds, wins 13%   (+0.00 over +4 rounds since last check)
            v_x60222032  -335.51 over 1727 rounds, wins 56%   (-24.83 over +4 rounds since last check)
            v_hold_s10  -361.69 over 1509 rounds, wins 57%   (+0.30 over +4 rounds since last check)
            v_x40223631  -375.20 over 1714 rounds, wins 55%   (-24.83 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 455.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
