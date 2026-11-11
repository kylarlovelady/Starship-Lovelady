# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 19 hours, 15 minutes; temp 37.8'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 27 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: f3ee22b 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (737 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 21 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd +1063.18 over   59 rounds, wins 14%   (-84.54 over +4 rounds since last check)
            v_edge10_s100 +1034.31 over   59 rounds, wins 14%   (-84.54 over +4 rounds since last check)
            v_x60222031  +210.94 over  510 rounds, wins 46%   (-14.28 over +4 rounds since last check)
            v_x64216772   +88.50 over  545 rounds, wins 53%   (-2.15 over +4 rounds since last check)
            v_x60222032   +57.73 over  510 rounds, wins 54%   (-2.15 over +4 rounds since last check)
            v_x40223631   +18.04 over  497 rounds, wins 53%   (-2.15 over +4 rounds since last check)
            v_snipe_all    +2.70 over  447 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  292 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -37.86 over  292 rounds, wins 60%   (-2.15 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 97.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
