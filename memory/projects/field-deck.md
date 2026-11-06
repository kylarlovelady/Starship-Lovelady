# Starship Field Deck (Galaxy Note 20 Ultra in a multi-tool case)

Owner idea (Kylar, 2026-11-06): use the old Galaxy Note 20 Ultra (AT&T, holds a charge) as the screen, memory and storage of a multipurpose tool in a case: Linux terminal, mesh radio for off-grid ("doomsday") messaging, a link to the Pi when away from Wi-Fi/cell, Flipper-Zero-style radios and sensors, and a cellular Wi-Fi module of his own. Goal range for the mesh link to the Pi: 25 miles, 50 would be great. Also wants to reuse his Alexa devices and collected electronics.

## Facts and limits (researched 2026-11-06)
- Model number not checked yet. US AT&T Note 20 Ultra (SM-N986U) has a locked bootloader, so no replacing Android; run Linux inside Android with Termux + Termux-X11 (github.com/pdone/linux-android, fork of mayukh4/linux-android; no root; needs 64-bit, 3 GB+ RAM). Remove Google apps only per user (ADB disable), never by hacks.
- Mesh: Meshtastic LoRa (US 902-928 MHz) pairs to the phone by Bluetooth; text only. 25 to 50 miles only works with line of sight and height at both ends (Pi node on a roof or mast with an outdoor antenna, a hilltop relay if needed). A ground-level truck or handheld will get far less. Do not add an RF amplifier (power limits).
- Phone has one USB-C port. The Note 20 Ultra supports Qi wireless charging, so a magnetic ring plate + charger coil in the case can charge it and free the USB-C port for the module hub.
- Each radio needs its own antenna for its band; never transmit without it.
- Legal: use on Kylar's own gear only; no cloning other people's cards, no jamming. Do not route around the employer's Wi-Fi filters; use his own data (LTE module with own SIM) instead.

## Plan
1. Terminal: Tailscale + Starship page (http://loveladymainaihub.taild703ca.ts.net:8095) + Termux Linux desktop.
2. Mesh: two Meshtastic radios, one at the Pi (put it high), range-test ladder 1, 5, 10, 25 miles; small "status" text bridge on the Pi.
3. Case: 3D-printed cradle, magnet/Qi charging, SMA antenna ports, module bays.
4. Modules: LTE Wi-Fi module with own data SIM (see projects/cell-booster.md), sub-GHz (CC1101), NFC (PN532), IR, GPS and weather sensors on an ESP32/Pico.
5. Parts: photo-identify the collected electronics, log them in projects/parts-inventory.md, pick what to reuse.

## Alexa devices (Echo Dot puck, Echo Show screen, Echo Dot)
- Echo Dot: Bluetooth speaker for the Pi, and speak Starship alerts if we add Home Assistant's Alexa notification integration (Home Assistant already runs on the Pi; check the integration still works before relying on it).
- Echo Show: wall display for the Starship page on the home Wi-Fi (local address, not Tailscale) if its browser opens it.
- They are locked down; no flashing plans. Mute the mics when not needed.

## Open questions for Kylar
- Exact model number (Settings > About phone).
- Terrain and where the 25 to 50 miles goes (work, a cabin, camping).
- 3D printer available?
- What kind of "mag chargers" (MagSafe-style, magnetic cables)?
