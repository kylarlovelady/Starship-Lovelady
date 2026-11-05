# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 6 hours, 51 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 22 hours (healthy); homeassistant Up 16 hours

## Sync and schedule
- Pi repo copy at: ea65791 4 minutes ago: KDP: match Kylar's approved look (flat lettering, fine grain, CAPS, thin double border), build 8 books (queue 045)
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (43 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (291 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +619.51 over   52 rounds, wins 56%   (-1.17 over +4 rounds since last check)
            v_x60222031  +446.19 over   52 rounds, wins 60%   (+17.94 over +4 rounds since last check)
            v_x88221261  +404.20 over   59 rounds, wins 29%   (-16.88 over +4 rounds since last check)
            v_x16217721  +397.88 over   67 rounds, wins 33%   (-81.46 over +4 rounds since last check)
            v_x64216771  +390.43 over   87 rounds, wins 45%   (-68.48 over +4 rounds since last check)
            v_x32221881  +331.83 over   51 rounds, wins 47%   (-60.42 over +4 rounds since last check)
            v_x52220781  +244.78 over   63 rounds, wins 30%   (+37.07 over +4 rounds since last check)
            v_x96220872  +239.74 over   52 rounds, wins 40%   (-44.13 over +4 rounds since last check)
            v_x80218932  +208.96 over   71 rounds, wins 54%   (-24.61 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 3.9 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
