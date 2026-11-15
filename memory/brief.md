# Morning brief, Sun 2026-11-15 (written 6:20 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (42 C), disk 11% full, nothing failed, up over 9 days. Notes sync worked (last one 6:00 am).
- Kalshi practice agent: running, live trading OFF, practice money only. The "only bet on a big edge" wallet v_edge10_s100 dropped to +$926 over 449 rounds (it was +$2,124 over 357 rounds yesterday), still winning only 12% of rounds. That swing is what a lottery shape looks like; it is not a proven edge. Last 24 hours the best strategy was v_hold_s250_agree (+$755 over 73 rounds, 70% wins); most others lost.
- Home Jarvis: wake-up bar still 0.8. 1 empty wake-up in the last 24 hours, 15 of 17 false in the last week. No change needed today.
- Phone Jarvis: no chats for about 201 hours (idle, not broken), no errors. Average time to first words is 1.8 s. No new Jarvis notes to file.
- Pi-hole is up; its stats stay blank until it gets its password.

## What is broken or needs a look
- The Pi job queue has been stuck since Nov 11 (4 days). The Hub picture server holds the runner's lock, so the Kalshi forward-test review (queue 117) cannot run. Fix is one command, below.
- Kalshi API key expired Nov 9 and is not renewed (6 days). The practice agent does not need it; the real-fills file does.
- The Kalshi forward-test review (due Wed Nov 11) is now 4 days late because of the stuck queue.
- Home mic clips still end too short, so Jarvis can wait too long for you to finish. Needs a test at home.
- Stalled over 5 days, both waiting on you: Kalshi key, and the KDP re-upload of the 4 new Process Operator covers and interior.

## What you need to do (phone friendly)
1. On the Pi terminal paste: pkill -f hub2/media_server.py
   (the Pi restarts it within 3 minutes and the queue runs again)
2. Tell me "start Kalshi key" when you have a few minutes; I will walk you through it one step at a time.
(Later: upload the 4 new Process Operator covers and interior to KDP. On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
Kalshi forward-test review once the queue is free, then the new API key with you, then the kitchen Pi first boot with you at home.
