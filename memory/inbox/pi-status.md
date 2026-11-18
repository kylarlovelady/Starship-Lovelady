# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 5 days, 5 hours, 45 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 10 days; whisper Up 12 days (healthy); piper Up 12 days (healthy); pihole Up 8 days (healthy); homeassistant Up 12 days

## Sync and schedule
- Pi repo copy at: 483a870 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    68 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1315 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1962.01 over  181 rounds, wins 65%   (+672.22 over +4 rounds since last check)
            v_edge10_s100  +792.69 over  717 rounds, wins 12%   (-52.18 over +4 rounds since last check)
            v_edge10_s100_dd  +741.32 over  717 rounds, wins 12%   (-20.39 over +4 rounds since last check)
            v_x60222031   +81.50 over 1168 rounds, wins 47%   (+201.75 over +4 rounds since last check)
            v_x64216772   +65.65 over 1203 rounds, wins 58%   (+6.03 over +4 rounds since last check)
            v_x60222032   +34.88 over 1168 rounds, wins 59%   (+6.03 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1105 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  950 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    -4.81 over 1155 rounds, wins 58%   (+6.03 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 276.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
