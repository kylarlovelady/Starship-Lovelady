# Morning brief, Thu 2026-11-19 (written 6:20 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (43.9 C), disk 12% full, nothing failed. Notes sync worked (last one 6:00 am).
- The Pi restarted about 18 hours ago (it had been up 12 days). Everything came back by itself and nothing is failing, so I am treating it as a normal reboot.
- Kalshi practice agent: running, live trading OFF, practice money only. The "big edge only" wallet v_edge10_s100 is +$1,570 over 779 rounds (was +$845 over 708), winning 13%: still a lottery shape, unproven. The "wild day" wallet v_hold_s250_wild fell to +$721 over 243 rounds (was +$1,782 over 172), winning 62%. It has given back more than half its early profit, so its early number was luck-heavy.
- The daily Kalshi digest file came out empty this morning (header only). The supervisor report and data files are fine, so I used those. Not urgent.
- Phone Jarvis: idle about 297 hours, no errors, first words about 2.0 s. No new Jarvis notes to file.
- Home Jarvis: 5 empty wake-ups yesterday (08:00 to 16:00), 18 of 18 false in the last week, no real commands heard. Wake bar is still 0.8, and the mic is muted right now.

## What is broken or needs a look
- Nothing is down.
- Kalshi API key expired Nov 9 and is still not renewed (10 days). The practice agent does not need it; the real-fills file does.
- KDP re-upload of the 4 Process Operator covers and interior has waited on you for 10 days (list: memory/inbox/kdp-ready).
- Home Jarvis false wake-ups are above the "3 or more a day" line again; the 11-07 rule says to nudge the bar to 0.85. I did not touch the Pi. Tell me "raise it" and I will queue it.
- Pi-hole stats stay blank until it gets its password. Home mic clips still end too short; needs a test at home.

## What you need to do (phone friendly)
1. When you have a few minutes, tell me "start Kalshi key" and I will walk you through it one step at a time.
2. When you can, upload the new KDP covers and interior.
(Later, on the Pi: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
The new Kalshi API key with you, then the kitchen Pi first boot with you at home.
