# Cellular booster for a buddy (build it, do not buy one)
Added 2026-11-05 23:46 by Kylar: he wants to MAKE a cell signal booster for a friend instead of buying one.

## Status
idea. Nothing built. Open questions to ask Kylar: which carrier and phones, where the friend lives (house, truck, shop), how bad the signal is outside vs inside, and whether there is any signal at all outside.

## Important note on legality (US), so the design stays legal and does not hurt anyone
- A homemade AMPLIFIER (an active booster made from parts) is not allowed in the US: the FCC only permits consumer boosters that are certified and registered with the carrier, because a bad home-built amplifier can jam towers and knock out service (and 911 calls) for a whole area. Carriers can trace interference and fines are possible. Please do not build the active amplifier part.
- Passive builds (no amplification) are fine and often get most of the benefit when there is some signal outside.

- MEXICO (buddy lives there, asked 2026-11-05 23:56): not confirmed. Telecom equipment there must be homologated (IFT seal; the regulator IFT was replaced by a new telecom authority in 2025) and the cell frequencies are licensed to the carriers, so a homemade active amplifier is very likely not allowed there either (same interference risk). A web search did not find a rule specifically about boosters; Kylar or the buddy should ask the carrier (e.g. Telcel, AT&T Mexico) or check with the telecom regulator before building any amplifier. Passive antenna routes below stay the safe choice in both countries.

- 2026-11-06 00:00 Kylar wants the buddy's version to plug into a wall socket in his room and strengthen the weak signal, and believes that is legal in Mexico (unverified). Claude has not designed a homemade amplifier: a home-built repeater can oscillate (feedback between the two antennas) and jam the tower, which is a real hazard whatever the law says. Plan instead: build everything around an already-approved (homologated) amplifier module or kit: outdoor antenna, mast, cable, indoor antenna, enclosure, power, mounting. If Kylar has a source showing boosters are allowed in Mexico, add it here.

- 2026-11-06 00:02 Kylar: it must be ONE piece, no wires, plug into the wall. A one-box repeater (both antennas inside one housing) is the worst case for oscillation, so Claude proposed an equivalent one-piece build that is not a repeater: a plug-in cellular-to-Wi-Fi unit (certified LTE modem module + small computer + Wi-Fi, internal antennas, one enclosure, one power plug). It takes the weak cell signal and gives the buddy Wi-Fi internet (and Wi-Fi calling for his phone). Needs: bands for his carrier in Mexico, SIM/data plan, module choice. Waiting on Kylar's yes and the carrier/town/signal details.

## Legal DIY routes to look at first (Claude can detail the one Kylar picks)
1. Outdoor high-gain directional antenna (Yagi or panel) on a mast, pointed at the nearest tower, a low-loss coax run inside, and a cell phone/hotspot or a cellular router with external antenna ports. Making the antenna and mast is a real DIY job and legal.
2. Cellular router/hotspot with external antenna connectors (placed in the best spot, Wi-Fi inside the house) plus Wi-Fi calling on the phones.
3. Wi-Fi calling and a carrier femtocell/network extender (the carrier supplies it, often free if signal is poor).
4. If a real amplifier is needed: use a certified, registered booster kit; the friend can still get the DIY antenna and mast part cheaper than the kit's.
- Find the tower first: use the carrier tower map or an app with signal bars/band info (Kylar to pick the app); the antenna direction and band decide everything.

## BUILD PLAN: one-piece plug-in cellular Wi-Fi unit (Kylar said go, 2026-11-06 00:05)
Status: planned, parts not chosen until we know the buddy's carrier, town and signal.
- What it is: one enclosure, one wall plug, no wires out. LTE modem takes the weak cell signal, a small computer shares it as a Wi-Fi network in his room (not a repeater, nothing is retransmitted on cell frequencies).
- Parts (all certified/off-the-shelf, prices unchecked estimates about $90 to $150 total plus data plan): (1) Raspberry Pi Zero 2 W (built-in Wi-Fi, small, low power) or Pi 3A+/4 if more range is needed; (2) a global LTE Cat 4 module that covers the Mexican bands, e.g. Quectel EG25-G on a mini-PCIe-to-USB or Pi HAT board (Sixfab forum says EG25-G and Telit LE910C1-NF both work in Mexico); the exact bands must be confirmed against his carrier before buying (the 2016/2018 Xataka table lists Telcel and AT&T on B4 and Movistar on B2, but it is old and more bands are in use now); (3) two LTE antennas (main + diversity), small flat/internal ones, mounted inside the case against the window side; (4) 5 V 3 A power supply (or a USB-C wall adapter with the board built into the case); (5) microSD 16 GB+; (6) a SIM with a data plan from his carrier (unlocked modem, check the APN); (7) enclosure: 3D print it (ties into the 3D printing project) with an antenna window; optional OLED/LEDs for signal bars.
- Software (Raspberry Pi OS Lite + NetworkManager/ModemManager): modem shows up as a mobile broadband connection (set the carrier's APN), then a Wi-Fi hotspot on wlan0 sharing it (nmcli hotspot, or hostapd + dnsmasq with NAT); a small status script shows signal bars/band/data used; auto-reconnect watchdog; optional Wi-Fi calling on his phone over this Wi-Fi.
- Placement tip for the buddy: put it at the window on the side facing the tower; even one or two metres changes the signal a lot.
- Risks/notes: weak signal means slow data, it will not create signal that is not there; the modem's own antennas inside a plastic case are fine; keep the case ventilated. Check the SIM/plan allows tethering/hotspot sharing.
- Kylar to confirm: carrier, town, signal strength outside/inside, data plan (who pays), Wi-Fi network name/password for the room, budget.

## Order (Kylar, 2026-11-06 00:06): build unit #1 for HIMSELF first (US), then a second one for the buddy in Mexico
- Unit #1 needs: Kylar's carrier, where it will live (home / truck / shop), how weak the signal is there, what data plan the SIM will use (hotspot sharing must be allowed), and whether he wants the Pi 5 hub to host the Wi-Fi or a separate small Pi. US note: some carriers (Verizon, AT&T, T-Mobile) only accept devices/modems they have certified, so the module choice depends on his carrier; a global module like the EG25-G can work on some but not all (check the carrier's bands and approved-device list before buying).
- Unit #2 (Mexico): same design, module chosen for his carrier and Mexican approval.

## Next step
Ask Kylar the open questions above, check the friend's signal, then pick route 1, 2 or 3 and write the parts list and steps here (buy-list.md only if Kylar wants parts listed).

## Done
(nothing yet)
