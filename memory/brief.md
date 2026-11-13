# Morning brief, Fri 2026-11-13 (written 6:20 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (42 C), disk 11% full, nothing failed, up over a week. Notes sync worked (last one 6:00 am).
- Kalshi practice agent: running, live trading OFF, practice money only. The "only bet on a big edge" wallet v_edge10_s100 is +$1,604 over 265 rounds (it was +$1,873 at 173 rounds, so it has slipped) and wins only 15% of rounds: still a lottery shape, not a proven edge. Its throttled twin is +$896. Last 24 hours, "hold to the end" strategies were slightly positive (+$144 over 80 rounds); sell-early strategies were mostly negative. Nothing here is proven.
- Home Jarvis: wake-up bar still 0.8. 2 wake-ups in the last 24 hours, both empty. No change needed.
- Phone Jarvis: no chats for about 153 hours (idle, not broken), no errors. Average time to first words is 1.8 s. No new Jarvis notes to file.
- Hub screen: background library server is running on the Pi; no photos uploaded yet.
- Pi-hole is up; its stats stay blank until it gets its password.

## What is broken or needs a look
- Kalshi API key expired Nov 9 and is not renewed (4 days). The practice agent does not need it; the real-fills file does.
- The Kalshi forward-test review (due Wed Nov 11) is still not done (2 days late). Claude does it next.
- Home mic clips still end too short, so Jarvis can wait too long for you to finish. Needs a test at home.
- Stalled over 3 days, both waiting on you: Kalshi key, and the KDP re-upload of the 4 new Process Operator covers and interior.

## What you need to do (phone friendly)
1. Tell me "start Kalshi key" when you have a few minutes; I will walk you through it one step at a time.
2. When you can: upload the 4 new Process Operator covers and interior to KDP.
(On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
Kalshi forward-test review (round counts, pick winners, retire losers), then the new API key with you, then the kitchen Pi first boot with you at home.
