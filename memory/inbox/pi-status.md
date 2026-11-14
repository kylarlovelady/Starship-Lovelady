# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 9 hours, 15 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 21%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 4 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: aea5153 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1042 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1877.36 over  385 rounds, wins 14%   (-142.20 over +4 rounds since last check)
            v_edge10_s100_dd  +851.93 over  385 rounds, wins 14%   (-44.47 over +4 rounds since last check)
            v_x64216772  +117.46 over  871 rounds, wins 56%   (+20.59 over +4 rounds since last check)
            v_x60222032   +86.69 over  836 rounds, wins 57%   (+20.59 over +4 rounds since last check)
            v_x40223631   +47.00 over  823 rounds, wins 56%   (+20.59 over +4 rounds since last check)
            v_snipe_all    +2.70 over  773 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222031    +0.78 over  836 rounds, wins 45%   (+3.33 over +4 rounds since last check)
            v_hold_s5    +0.00 over  618 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x12229262   -21.70 over  815 rounds, wins 56%   (+43.34 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 183.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
