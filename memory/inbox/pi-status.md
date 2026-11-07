# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 6 hours, 15 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 30 hours; whisper Up 30 hours (healthy); piper Up 30 hours (healthy); pihole Up 30 hours (healthy); homeassistant Up 30 hours

## Sync and schedule
- Pi repo copy at: ae6341d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (450 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 20 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +331.90 over  212 rounds, wins 43%   (+62.69 over +4 rounds since last check)
            v_x96220861  +290.16 over  212 rounds, wins 40%   (+11.31 over +4 rounds since last check)
            v_x88221261  +171.44 over  219 rounds, wins 23%   (-5.45 over +4 rounds since last check)
            v_x64216772  +132.28 over  247 rounds, wins 46%   (-7.54 over +4 rounds since last check)
            v_x60222032  +101.51 over  212 rounds, wins 47%   (-7.54 over +4 rounds since last check)
            v_x40223632   +83.16 over  199 rounds, wins 45%   (+31.03 over +4 rounds since last check)
            v_x40223631   +61.82 over  199 rounds, wins 44%   (-7.54 over +4 rounds since last check)
            v_x12229262   +35.91 over  191 rounds, wins 42%   (-13.46 over +4 rounds since last check)
            v_snipe_all    +2.70 over  149 rounds, wins 1%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 12.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
