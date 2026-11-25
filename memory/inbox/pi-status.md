# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 6 hours, 42 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 99e7600 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 59 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1724 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1586 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1431 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -144.91 over 1587 rounds, wins 26%   (+0.00 over +3 rounds since last check)
            v_x64216772  -199.17 over 1684 rounds, wins 56%   (+11.17 over +3 rounds since last check)
            hold       -228.83 over 1787 rounds, wins 59%   (+24.52 over +3 rounds since last check)
            v_x60222032  -229.94 over 1649 rounds, wins 56%   (+11.17 over +3 rounds since last check)
            v_x40223631  -269.63 over 1636 rounds, wins 56%   (+11.17 over +3 rounds since last check)
            v_hold_s10  -305.19 over 1431 rounds, wins 58%   (-4.16 over +3 rounds since last check)
            v_x60222031  -310.29 over 1649 rounds, wins 46%   (+27.68 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 429.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
