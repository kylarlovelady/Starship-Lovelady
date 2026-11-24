# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 12 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 15f3eba 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1710 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1568 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1413 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -141.69 over 1569 rounds, wins 26%   (+0.00 over +3 rounds since last check)
            hold       -209.99 over 1769 rounds, wins 59%   (+2.88 over +3 rounds since last check)
            v_x64216772  -215.73 over 1666 rounds, wins 56%   (-19.24 over +3 rounds since last check)
            v_x60222032  -246.50 over 1631 rounds, wins 56%   (-19.24 over +3 rounds since last check)
            v_x40223631  -286.19 over 1618 rounds, wins 56%   (-19.24 over +3 rounds since last check)
            v_hold_s10  -297.40 over 1413 rounds, wins 58%   (-2.62 over +3 rounds since last check)
            v_take25_s10  -392.45 over 1413 rounds, wins 69%   (-2.62 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 422.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
