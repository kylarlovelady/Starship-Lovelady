# New Hub screen (glassy home dashboard on the kitchen/home touch screen)

Requested 2026-11-11 14:19 (Kylar). Status: design preview first, then wire to the Pi. The screen is the main Pi's display, driven by the new Pi (LoveladyMainAiHubSCREEN, see kitchen-screen-pi.md). The current Hub is ~/hub-dashboard on the main Pi (not in this repo; has a frosted clock bubble and a theme editor).

## What Kylar wants
1. Background that is easy to change: holiday themes, or pictures of the family.
2. Time and date, with a blurry, glossy, glassy bubble behind them so they are easy to read.
3. Mic mute / unmute button (Jarvis mic; rule: mic stays muted until Kylar says).
4. Control ALL Home Assistant devices from the screen: see, view, change, everything.
5. Every button, slider, keyboard and control looks like a glassy, clear, futuristic, iPhone-style dashboard. Real clean.
6. Double tap hides the top task bar (kiosk look); double tap again brings it back so he can close the Hub and do other things.
7. The touch keyboard pops up when needed; he never wants to connect a keyboard or mouse.

## Plan
- Build ONE page (hub2) that runs in demo mode with sample devices for the look, and in live mode on the Pi. Page never holds the Home Assistant token: the Pi serves a small proxy that adds it (token lives in ~/market-data/env or ~/voice-data/keys.env on the Pi, never in the repo).
- Double tap = browser fullscreen toggle (hides the panel); keyboard = squeekboard through the Chromium Wayland IME flag (already set in kitchen-screen/windowed.sh) plus an on-page keyboard button.
- Backgrounds: built-in holiday/seasonal sets plus family photos uploaded from his phone (stored on the Pi, not in the repo; this repo is public).
- Mic mute: probe how Jarvis mutes (hub-voice / hub-satellite) before wiring.
- Open questions for Kylar: which holidays first; which devices matter most on the main view; Sharee's input on the family photos.

## Next step
- Preview page (demo data) for Kylar to try on his phone; probe of the Pi (queue 110: HA device types, mic mute method); then wire live control.

## Done
(nothing yet)
