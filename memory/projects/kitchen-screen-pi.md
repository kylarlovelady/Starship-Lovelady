# Kitchen screen Pi (the new Pi 5 behind the GeekPi 10.1" touch screen)

Started 2026-11-11 (Kylar at work, has the new Pi, SD card and parts). Status: preparing the SD card. It is a thin client: it only shows the main Pi's pages; the brains stay on LoveladyMainAiHub.

## Plan
1. SD card (Raspberry Pi Imager on his desktop): Raspberry Pi OS (64-bit) with desktop (same Debian 13 as the main Pi). In Imager's OS customisation: hostname (suggested kitchen-screen), his username and a password (not stored here), home Wi-Fi name and password, country US, time zone America/Chicago, keyboard US, SSH on with password login.
2. First boot at home (one step at a time with Claude): find the Pi on the network, SSH in, update.
3. Join Tailscale so it reaches loveladymainaihub.taild703ca.ts.net like his phone does (sign-in link in a browser; no keys in the repo).
4. Chromium kiosk at login, full screen, pointing at the Starship page (main Pi :8095) or the Hub (:8081/hub); screen never sleeps, touch works, no cursor.
5. Later: screensaver, cameras, Home Assistant lights panel (living room build in buy-list.md), speakers.

## Progress 2026-11-11
- 11:15 first boot done on the screen at work (the Imager user and Wi-Fi settings did NOT carry over, so Kylar created the user in the first-run wizard and put the Pi on his phone hotspot). Desktop is up and touch works. Next: run hardware/kitchen-screen/setup.sh (SSH on, no blanking, Tailscale join, Chromium kiosk to the Hub at :8081/hub; change URL on line 6 to switch pages). Software updates and the home Wi-Fi are still to do at home.

## What the screen is (Kylar, 2026-11-11 12:50)
- The main Pi at home (LoveladyMainAiHub) has no screen of its own. This GeekPi screen IS its screen, now driven by the new Pi (LoveladyMainAiHubSCREEN), so the screen can sit away from the main Pi and still control it. The new Pi's Tailscale address is about 100.77.212.2 (Kylar's phone alias `screen` on the main Pi).
- Requirements: (1) flip the display 180 degrees (wires face the wall) and the touch must flip too; (2) touch keyboard on demand, the page must resize so nothing hides behind it; (3) a way back to the desktop; (4) see the Starship page. Plan: windowed Chromium (not full-screen kiosk) via hardware/kitchen-screen/windowed.sh, Desktop icons Starship (:8095) and Hub (:8081/hub), rotation through Pi menu > Preferences > Screen Configuration (touch mapped there too), keyboard button on the panel (squeekboard).
- Side effect seen 11-11 12:44: Kylar ran pkill chromium on the MAIN Pi, closing its old home-screen kiosk; check it is not needed.

## Next step
- 2026-11-11 08:00 Step 1 DONE: SD card written with Imager (Pi OS 64-bit Trixie, hostname LoveladyMainAiHubSCREEN (Kylar chose it; reachable as loveladymainaihubscreen.local), user kylarlovelady, Central time, home Wi-Fi, SSH password login on, Pi Connect off). Next: card into the new Pi, assemble with the screen, power on at home (home Wi-Fi), then find it and SSH in (step 2 above).

## Done
(nothing yet)
