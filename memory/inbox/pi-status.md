# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 8 hours, 12 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 0b214b6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 6 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 59 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1729 total)
      OK    entry_stats.json updated 11 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1592 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1437 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -146.90 over 1593 rounds, wins 26%   (-5.68 over +3 rounds since last check)
            v_x64216772  -198.12 over 1690 rounds, wins 56%   (+4.65 over +3 rounds since last check)
            v_x60222032  -228.89 over 1655 rounds, wins 56%   (+4.65 over +3 rounds since last check)
            v_x40223631  -268.58 over 1642 rounds, wins 56%   (+4.65 over +3 rounds since last check)
            v_hold_s10  -306.40 over 1437 rounds, wins 58%   (+4.34 over +3 rounds since last check)
            v_edge10_s100_dd  -325.34 over 1204 rounds, wins 13%   (+142.33 over +3 rounds since last check)
            hold       -326.30 over 1793 rounds, wins 58%   (-28.06 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 430.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
