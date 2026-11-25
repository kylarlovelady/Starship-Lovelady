# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 42 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 69a0f24 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 25 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 56 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1767 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1637 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1482 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -160.08 over 1638 rounds, wins 26%   (+1.18 over +3 rounds since last check)
            v_x64216772  -208.38 over 1735 rounds, wins 56%   (+1.14 over +3 rounds since last check)
            v_x60222032  -239.15 over 1700 rounds, wins 56%   (+1.14 over +3 rounds since last check)
            v_edge10_s100_dd  -268.36 over 1249 rounds, wins 13%   (+0.00 over +3 rounds since last check)
            v_x40223631  -278.84 over 1687 rounds, wins 56%   (+1.14 over +3 rounds since last check)
            v_hold_s10  -335.21 over 1482 rounds, wins 57%   (+2.34 over +3 rounds since last check)
            v_edge10_s100  -373.00 over 1249 rounds, wins 13%   (+0.00 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 447.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
