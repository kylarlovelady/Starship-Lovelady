# Starship Field Deck (Galaxy Note 20 Ultra in a multi-tool case)

Owner idea (Kylar, 2026-11-06): use the old Galaxy Note 20 Ultra (AT&T, holds a charge) as the screen, memory and storage of a multipurpose tool in a case, with a Linux terminal, a mesh radio for off-grid ("doomsday") messaging, a link to the Pi when away from Wi-Fi/cell, and Flipper-Zero-style radios and sensors in the case.

## Facts and limits (researched 2026-11-06)
- Model number not checked yet. US AT&T Note 20 Ultra (SM-N986U) has a locked bootloader, so no replacing Android; run Linux inside Android with Termux + Termux-X11 (project github.com/pdone/linux-android, fork of mayukh4/linux-android; no root; needs 64-bit, 3 GB+ RAM). International models may be unlockable but have poor Linux support.
- Mesh: Meshtastic LoRa radio pairs with the phone by Bluetooth; text only; range about a few miles in town; needs a second radio on the Pi to message it. No internet or cell needed.
- Phone has one USB-C port: use a powered hub, and Bluetooth for the mesh radio.
- Each radio needs its own antenna for its band; never transmit without it.
- Legal: use on Kylar's own gear only; no cloning other people's cards, no jamming.

## Plan
1. Terminal: Tailscale + Starship page (http://loveladymainaihub.taild703ca.ts.net:8095) + Termux Linux desktop.
2. Mesh: two Meshtastic radios (one at the Pi), range test, small "status" text bridge on the Pi.
3. Case: 3D-printed cradle with SMA antenna ports and module bays.
4. Modules: sub-GHz (CC1101), NFC (PN532), IR, GPS and weather sensors on an ESP32/Pico.

## Open questions for Kylar
- Exact model number (Settings > About phone).
- How far must the mesh link reach (home, truck, work, camping)?
- 3D printer available?
