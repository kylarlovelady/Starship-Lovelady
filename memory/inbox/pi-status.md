# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 19 hours, 12 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 19 hours; whisper Up 19 hours (healthy); piper Up 19 hours (healthy); pihole Up 19 hours (healthy); homeassistant Up 19 hours

## Sync and schedule
- Pi repo copy at: c17b617 12 minutes ago: Daily check 2026-11-19: brief, projects header, changelog
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 06:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 2 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1372 total)
      OK    entry_stats.json updated 7 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1579.68 over  782 rounds, wins 13%   (+9.91 over +3 rounds since last check)
            v_edge10_s100_dd  +927.39 over  782 rounds, wins 13%   (+2.38 over +3 rounds since last check)
            v_hold_s250_wild  +573.08 over  246 rounds, wins 62%   (-148.07 over +3 rounds since last check)
            v_x60222031  +213.52 over 1233 rounds, wins 47%   (-17.96 over +3 rounds since last check)
            v_x64216772   +16.53 over 1268 rounds, wins 58%   (-5.66 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1170 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1015 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032   -14.24 over 1233 rounds, wins 59%   (-5.66 over +3 rounds since last check)
            v_x12229262   -36.90 over 1212 rounds, wins 58%   (-12.39 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 297.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
