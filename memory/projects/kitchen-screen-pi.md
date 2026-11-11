# Kitchen screen Pi (the new Pi 5 behind the GeekPi 10.1" touch screen)

Started 2026-11-11 (Kylar at work, has the new Pi, SD card and parts). Status: preparing the SD card. It is a thin client: it only shows the main Pi's pages; the brains stay on LoveladyMainAiHub.

## Plan
1. SD card (Raspberry Pi Imager on his desktop): Raspberry Pi OS (64-bit) with desktop (same Debian 13 as the main Pi). In Imager's OS customisation: hostname (suggested kitchen-screen), his username and a password (not stored here), home Wi-Fi name and password, country US, time zone America/Chicago, keyboard US, SSH on with password login.
2. First boot at home (one step at a time with Claude): find the Pi on the network, SSH in, update.
3. Join Tailscale so it reaches loveladymainaihub.taild703ca.ts.net like his phone does (sign-in link in a browser; no keys in the repo).
4. Chromium kiosk at login, full screen, pointing at the Starship page (main Pi :8095) or the Hub (:8081/hub); screen never sleeps, touch works, no cursor.
5. Later: screensaver, cameras, Home Assistant lights panel (living room build in buy-list.md), speakers.

## Next step
- Kylar writes the card and tells Claude when it is done.

## Done
(nothing yet)
