# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 14 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 3 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: ab3de18 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 13 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (974 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1308.86 over  310 rounds, wins 14%   (-84.54 over +4 rounds since last check)
            v_edge10_s100_dd  +753.54 over  310 rounds, wins 14%   (-20.96 over +4 rounds since last check)
            v_x64216772   +97.17 over  796 rounds, wins 56%   (-2.00 over +4 rounds since last check)
            v_x60222032   +66.40 over  761 rounds, wins 56%   (-2.00 over +4 rounds since last check)
            v_x40223631   +26.71 over  748 rounds, wins 56%   (-2.00 over +4 rounds since last check)
            v_snipe_all    +2.70 over  698 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  543 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -64.20 over  543 rounds, wins 60%   (-11.81 over +4 rounds since last check)
            v_snipe    -106.17 over  699 rounds, wins 30%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 164.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
