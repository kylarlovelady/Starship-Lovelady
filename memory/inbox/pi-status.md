# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 1 hour, 44 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 17 hours (healthy); homeassistant Up 11 hours

## Sync and schedule
- Pi repo copy at: 0433259 3 minutes ago: queue 020: more Kalshi analysis
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (37 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (271 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +512.30 over   39 rounds, wins 41%   (-13.50 over +4 rounds since last check)
            v_x96220861  +504.50 over   32 rounds, wins 66%   (+43.43 over +4 rounds since last check)
            v_x60222031  +421.16 over   32 rounds, wins 66%   (+40.64 over +4 rounds since last check)
            v_x52220781  +285.51 over   43 rounds, wins 33%   (-5.48 over +4 rounds since last check)
            v_x32221881  +242.44 over   31 rounds, wins 58%   (-147.17 over +4 rounds since last check)
            v_x64216771  +222.95 over   67 rounds, wins 48%   (-160.23 over +4 rounds since last check)
            v_x72222451  +204.08 over   56 rounds, wins 41%   (-5.31 over +4 rounds since last check)
            v_x28219981  +202.98 over   71 rounds, wins 45%   (-144.85 over +4 rounds since last check)
            v_x219211  +202.60 over   63 rounds, wins 41%   (-5.31 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 6.8 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
