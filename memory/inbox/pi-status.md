# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 hours, 42 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 hours; whisper Up 7 hours (healthy); piper Up 7 hours (healthy); pihole Up 7 hours (healthy); homeassistant Up 7 hours

## Sync and schedule
- Pi repo copy at: 97fe5fb 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    68 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1343 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 4 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1582.63 over  212 rounds, wins 63%   (-204.04 over +4 rounds since last check)
            v_edge10_s100 +1136.60 over  748 rounds, wins 12%   (+213.45 over +4 rounds since last check)
            v_edge10_s100_dd  +873.19 over  748 rounds, wins 12%   (+136.17 over +4 rounds since last check)
            v_x60222031  +240.03 over 1199 rounds, wins 47%   (+71.58 over +4 rounds since last check)
            v_x64216772   +40.20 over 1234 rounds, wins 58%   (+3.51 over +4 rounds since last check)
            v_x60222032    +9.43 over 1199 rounds, wins 59%   (+3.51 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1136 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  981 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631   -30.26 over 1186 rounds, wins 58%   (+3.51 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 285.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
