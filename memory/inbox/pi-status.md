# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 19 hours, 53 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 14 seconds; whisper Up 44 hours (healthy); piper Up 44 hours (healthy); pihole Up 44 hours (healthy); homeassistant Up 44 hours

## Sync and schedule
- Pi repo copy at: 1de7021 5 minutes ago: Heal task queue lock held by the Jarvis mic switch
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (0 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 23:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (506 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250  +411.77 over   50 rounds, wins 68%   (+199.80 over +4 rounds since last check)
            v_hold_s500  +368.10 over   50 rounds, wins 68%   (+398.78 over +4 rounds since last check)
            v_x96220861  +277.38 over  268 rounds, wins 41%   (+22.02 over +4 rounds since last check)
            v_hold_s100  +272.27 over   50 rounds, wins 68%   (+80.59 over +4 rounds since last check)
            v_x60222031  +263.69 over  268 rounds, wins 43%   (+21.41 over +4 rounds since last check)
            v_hold_after60  +190.76 over   50 rounds, wins 70%   (+16.16 over +4 rounds since last check)
            v_hold_s50  +163.05 over   50 rounds, wins 68%   (+40.70 over +4 rounds since last check)
            v_hold_after120  +142.61 over   50 rounds, wins 64%   (+12.71 over +4 rounds since last check)
            v_x64216772  +132.25 over  303 rounds, wins 49%   (+8.30 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 26.5 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
