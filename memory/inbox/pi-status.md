# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 18 hours, 12 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 53ef152 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1753 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1620 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1465 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_snipe    -161.26 over 1621 rounds, wins 26%   (-10.37 over +4 rounds since last check)
            v_x64216772  -197.84 over 1718 rounds, wins 56%   (-18.52 over +4 rounds since last check)
            v_x60222032  -228.61 over 1683 rounds, wins 56%   (-18.52 over +4 rounds since last check)
            v_edge10_s100_dd  -233.31 over 1232 rounds, wins 13%   (+56.21 over +4 rounds since last check)
            v_x40223631  -268.30 over 1670 rounds, wins 56%   (-18.52 over +4 rounds since last check)
            v_hold_s10  -307.62 over 1465 rounds, wins 58%   (+2.15 over +4 rounds since last check)
            v_take25_s10  -379.52 over 1465 rounds, wins 68%   (+0.08 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 440.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
