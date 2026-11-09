# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 23 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 27 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: abe7165 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    93 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (612 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +3270.76 over  158 rounds, wins 62%   (+1230.63 over +4 rounds since last check)
            v_hold_s250 +1612.59 over  158 rounds, wins 62%   (+616.59 over +4 rounds since last check)
            v_hold_s100  +639.19 over  158 rounds, wins 62%   (+248.20 over +4 rounds since last check)
            v_hold_s50  +326.76 over  158 rounds, wins 62%   (+125.71 over +4 rounds since last check)
            v_hold_s25  +152.93 over  158 rounds, wins 62%   (+64.05 over +4 rounds since last check)
            v_x60222031  +146.23 over  376 rounds, wins 45%   (-25.96 over +4 rounds since last check)
            v_hold_after120  +116.35 over  158 rounds, wins 63%   (+99.50 over +4 rounds since last check)
            v_take100  +103.82 over  158 rounds, wins 65%   (+26.05 over +4 rounds since last check)
            v_x64216772  +102.39 over  411 rounds, wins 52%   (+5.03 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 53.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
