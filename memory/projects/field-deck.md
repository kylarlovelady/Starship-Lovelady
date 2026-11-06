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

## Decisions from the voice chat (2026-11-06, Kylar)
- Use: mostly at work and in the truck, away from home; wants it rugged, tough and cool, with a doomsday backup role. Daily core: Linux terminal + mesh link home. Everything else bolts on later ("electronic Swiss Army knife" that grows).
- Mesh goal: home (West Columbia) to work (Clute), road 20 miles, straight line probably 13 to 15. Flat coastal land is good for radio; the weak end is a radio low inside a steel plant. Put the work radio high (window, roof, pole). Node on the plant's own tower only with the employer's permission. Never tie into the plant's own radios or antennas.
- Form: handheld core printed in ASA (P1S) that lifts out of an aluminium briefcase with foam bays for modules. Case should double as a Faraday case (metal case + foam + conductive/copper tape at the seam; test by sealing a phone or radio inside and trying to reach it). Signals do not work from inside it, so the core comes out to be used.
- Version 1 core: Note 20 Ultra, Meshtastic radio, GPS, weather sensor (BME280), 10,000 to 20,000 mAh power bank (heat-tolerant, not baking on the dash), spare antenna port and one empty bay.
- Power ideas: wall charger; truck 12 V via a fused step-down converter (Kylar thinks he owns an adjustable supply with alligator clips, maybe DeWalt: photo it, set and meter the voltage before connecting the phone); DeWalt 20 V pack via a clip-on USB adapter (quick) or a fused DIY mount with a buck converter (later).
- Costs (rough, unchecked, said aloud): core + case + home radio $150 to $350; with a few modules $300 to $600; everything $600 to $1,000.

## Module list (all wanted, add one at a time)
Sensors: Geiger counter board with USB or Bluetooth (Kylar especially wants it), air quality (particulates + gas), temperature/humidity/pressure, thermal camera, laser distance, magnetometer, light, sound level. Phone already has GPS, accelerometer, gyro, compass, barometer, light, proximity, cameras, NFC.
Transmit/test tools (own gear and learning only): sub-GHz radio (CC1101), infrared send/learn, NFC/RFID read/write own tags, SDR dongle (listen-only unless licensed), ESP32 Wi-Fi/Bluetooth analyzer, logic analyzer, USB serial adapter, Pico/ESP32 as a USB keyboard tool for own computers, Nmap-type scanners on own network. Not built: jammers, cloning other people's cards or key fobs, attacking networks he does not own.

## Doomsday kit (needs Kylar's go-ahead to buy; low priority, unlikely event, keep spending small)
- Spare Meshtastic radios, one at home and one in the truck, each sealed in its own metal can (ammo can or galvanized can with a tight lid, cardboard or foam inside), switched off and with the antenna detached (an attached antenna carries a pulse in).
- A couple of simple whip/dipole antennas per location plus spare coax, stored in the same can; a high antenna at home with a backup stored with the spare radio.
- Small solar panel + battery per radio, stored in the cage; a spare DeWalt pack in the cage.
- Spare Pi with a copy of the memory card, a small drive with a backup of the memory notes, a hand-crank or solar radio.
- Test routine every few months: unseal, power on, message between the two radios, seal again.
- A whole house cannot practically be a Faraday cage; long wires (power, internet, antenna cables) carry the surge. Protect small items in cans instead, unplug during storms. Surge protectors only help against lightning-type surges. Faraday bags are the weakest; metal cans with solid lid contact are the cheap choice; many "Faraday safe" claims are untested. Check any cage with the call/radio test.

## Repair and scavenge plan
- Likely EMP damage is protection diodes, regulators, sometimes a chip; replacing caps/diodes is learnable, replacing a fried processor needs the same chip plus its software. Best plan: working spares in the cage; scavenge simple parts (diodes, resistors, caps, regulators) from dead devices.
- Learn in order: soldering (through-hole, then surface mount; temperature-controlled iron, flux, wick, tweezers), reading a board, multimeter (continuity, voltage, shorts), later hot air station + cheap microscope. Practice on the pile of old electronics (see parts-inventory.md).
- Offline electronics dictionary on the phone: a library of datasheets, component references and repair guides (PDFs, Kiwix). No known offline app that identifies a chip from a camera photo; identification is by reading the part number. With internet, Kylar sends photos to Claude.
- Starter list item pending Kylar's yes: a basic soldering kit.

## Offline brain (later project)
See projects/offline-brain.md.

## Open questions for Kylar
- Exact model number (Settings > About phone).
- (answered by voice) Range target: home to work, 20 road miles.
- (answered by voice) 3D printer: Bambu P1S; filament PLA + a black one he thinks is ASA (check spool label).
- What kind of "mag chargers" (MagSafe-style, magnetic cables)?
- Separate doomsday radios or built into the Note? Undecided (the phone shares the same pulse risk; separate is safer).
- Does the case also hold the DeWalt battery and the alligator-clip supply?
- Want the ham (technician) license added as a stage after the Meshtastic radios? Legal way to bigger antennas, more power and emergency comms; multiple-choice test.
