# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 21 hours, 0 minutes; temp 38.4'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 12 hours (healthy); homeassistant Up 6 hours

## Sync and schedule
- Pi repo copy at: 73001bc 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (251 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x44219232  +253.55 over   35 rounds, wins 49%   (+36.19 over +4 rounds since last check)
            v_x8220761  +228.38 over   36 rounds, wins 47%   (+55.17 over +4 rounds since last check)
            v_x219212  +193.27 over   43 rounds, wins 44%   (+36.19 over +4 rounds since last check)
            v_x44219231  +140.44 over   35 rounds, wins 43%   (+36.19 over +4 rounds since last check)
            v_x16217722  +135.06 over   27 rounds, wins 52%   (+104.71 over +4 rounds since last check)
            v_x72222452  +122.28 over   36 rounds, wins 42%   (+36.19 over +4 rounds since last check)
            v_x80218932  +120.80 over   31 rounds, wins 58%   (+30.77 over +4 rounds since last check)
            v_x88221261  +101.69 over   19 rounds, wins 42%   (-14.91 over +4 rounds since last check)
            v_x88221262   +94.50 over   19 rounds, wins 58%   (+36.19 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 2.1 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
