# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 15 hours, 45 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 4 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 2baefb6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 13 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (978 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1527.10 over  314 rounds, wins 14%   (+218.24 over +4 rounds since last check)
            v_edge10_s100_dd  +807.52 over  314 rounds, wins 14%   (+53.98 over +4 rounds since last check)
            v_x64216772  +111.71 over  800 rounds, wins 56%   (+14.54 over +4 rounds since last check)
            v_x60222032   +80.94 over  765 rounds, wins 56%   (+14.54 over +4 rounds since last check)
            v_x40223631   +41.25 over  752 rounds, wins 56%   (+14.54 over +4 rounds since last check)
            v_snipe_all    +2.70 over  702 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  547 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -60.60 over  547 rounds, wins 60%   (+3.60 over +4 rounds since last check)
            v_snipe    -102.55 over  703 rounds, wins 30%   (+3.62 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 166.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
