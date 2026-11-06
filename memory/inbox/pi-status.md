# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 10 hours, 16 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 25 hours (healthy); homeassistant Up 19 hours

## Sync and schedule
- Pi repo copy at: 0eb349d 3 minutes ago: queue 057: liquidity v2 + owner page check
- last notes sync result: push failed (run tasks/pi_push_setup.sh)
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (9 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (307 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 8 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +581.76 over   68 rounds, wins 49%   (-38.29 over +4 rounds since last check)
            v_x60222031  +405.67 over   68 rounds, wins 53%   (-9.74 over +4 rounds since last check)
            v_x88221261  +332.04 over   75 rounds, wins 24%   (-29.39 over +4 rounds since last check)
            v_x16217721  +241.62 over   83 rounds, wins 31%   (-52.27 over +4 rounds since last check)
            v_x64216771  +226.64 over  103 rounds, wins 41%   (-55.29 over +4 rounds since last check)
            v_x80218932  +198.95 over   87 rounds, wins 51%   (-30.68 over +4 rounds since last check)
            v_x52220781  +182.88 over   79 rounds, wins 25%   (-13.97 over +4 rounds since last check)
            v_x64216772  +145.06 over  103 rounds, wins 50%   (-10.49 over +4 rounds since last check)
            v_x32221881  +144.57 over   67 rounds, wins 39%   (-59.92 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 7.4 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
