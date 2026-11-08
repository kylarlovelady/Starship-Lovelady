# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 21 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up About an hour; whisper Up 45 hours (healthy); piper Up 45 hours (healthy); pihole Up 45 hours (healthy); homeassistant Up 45 hours

## Sync and schedule
- Pi repo copy at: a310604 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (510 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1311.26 over   54 rounds, wins 70%   (+943.16 over +4 rounds since last check)
            v_hold_s250  +884.87 over   54 rounds, wins 70%   (+473.10 over +4 rounds since last check)
            v_hold_s100  +464.01 over   54 rounds, wins 70%   (+191.74 over +4 rounds since last check)
            v_x96220861  +275.10 over  272 rounds, wins 42%   (-2.28 over +4 rounds since last check)
            v_x60222031  +265.60 over  272 rounds, wins 44%   (+1.91 over +4 rounds since last check)
            v_hold_s50  +260.84 over   54 rounds, wins 70%   (+97.79 over +4 rounds since last check)
            v_hold_after60  +199.30 over   54 rounds, wins 70%   (+8.54 over +4 rounds since last check)
            v_hold_after120  +150.20 over   54 rounds, wins 65%   (+7.59 over +4 rounds since last check)
            v_x64216772  +148.70 over  307 rounds, wins 50%   (+16.45 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 27.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
