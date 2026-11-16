# Morning brief, Mon 2026-11-16 (written 6:20 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (42.8 C), disk 12% full, nothing failed. Notes sync worked (last one 6:00 am).
- Good news: the stuck job queue is fixed (your pkill worked). The Kalshi forward-test review ran at 3:55 am. Result: the big-stake practice wallets lose money; only the tiny-stake hold is slightly positive. Nothing is proven either way.
- Kalshi practice agent: running, live trading OFF, practice money only. The "only bet on a big edge" wallet v_edge10_s100 is +$817 over 537 rounds (was +$926), still winning only 12% of rounds, so it is a lottery shape, not a proven edge. A new "wild day" test wallet was added overnight.
- KDP: black-and-gold and rose-pink covers were built for both titles. The upload list is in memory/inbox/kdp-ready.
- Home Jarvis: 2 empty wake-ups in 24 hours, 13 of 13 false in the last week. The 0.8 wake bar stays.
- Phone Jarvis: idle about 225 hours, no errors, first words in 1.8 s. No new Jarvis notes to file.

## What is broken or needs a look
- One Pi job (queue 122, checks the new wild-day test) was refused because it lacks the approval line the runner requires. I did not add it myself, since that line is the approval gate. Tell me to approve 122 and the next Claude chat will add it.
- Kalshi API key expired Nov 9 and is still not renewed (7 days). The practice agent does not need it; the real-fills file does.
- KDP re-upload of the 4 Process Operator covers and interior has waited on you for 7 days.
- Pi-hole stats stay blank until it gets its password. Home mic clips still end too short; needs a test at home.

## What you need to do (phone friendly)
1. When you have a few minutes, tell me "start Kalshi key" and I will walk you through it one step at a time.
2. When you can, upload the new KDP covers and interior (list: memory/inbox/kdp-ready).
(Later, on the Pi: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
The wild-day check (queue 122) once approved, then the new Kalshi API key with you, then the kitchen Pi first boot with you at home.
