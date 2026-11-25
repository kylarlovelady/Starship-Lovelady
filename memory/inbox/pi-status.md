# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 22 hours, 42 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 4f0032d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1763 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 18 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1632 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1477 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -161.26 over 1633 rounds, wins 26%   (+0.00 over +3 rounds since last check)
            v_x64216772  -189.13 over 1730 rounds, wins 56%   (-10.05 over +3 rounds since last check)
            v_x60222032  -219.90 over 1695 rounds, wins 56%   (-10.05 over +3 rounds since last check)
            v_edge10_s100_dd  -257.85 over 1244 rounds, wins 13%   (+0.00 over +3 rounds since last check)
            v_x40223631  -259.59 over 1682 rounds, wins 56%   (-10.05 over +3 rounds since last check)
            v_hold_s10  -326.59 over 1477 rounds, wins 57%   (-5.55 over +3 rounds since last check)
            v_edge10_s100  -330.64 over 1244 rounds, wins 13%   (+0.00 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 445.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
