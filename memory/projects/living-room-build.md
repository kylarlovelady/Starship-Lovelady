# Living room build: one compact powerhouse PC + wall touchscreen + calendar + minimal wiring
Started 2026-11-07 (Kylar by voice, from a photo of the living room). Owner: Kylar. Status: idea / planning. Nothing bought. Details come later; this is the high-level list.

## The room (Kylar's photo, 11-07)
- LIGHT GREEN (kitchen pass-through, where the KEYS holder is): NEW touch-screen Pi panel with good speakers. Family control panel only: screensaver, cameras, lights and Home Assistant devices. Not where Kylar works on the Pi.
- DARK GREEN (wall above the white tower): digital calendar goes here. DARK BLUE: the digital calendar.
- LIGHT BLUE: the current white tall PC connected to the TV (it is a tower, not a fridge). Likely to be sold or moved after the new build.
- PURPLE: current non-touch Pi screen; moves somewhere else when the new touch screen is up. PINK: the Pi in its box.
- RED (cubby on the right of the TV stand): where the new computer goes. It must fit this cubby: MEASURE width, height, depth and airflow clearance (open back/sides?) before buying anything.
- Kylar works on the Pi from his phone and from the big TV connected to the new computer.

## Rules agreed
- The Pi stays on its OWN power and its own cable (small supply, ideally a battery backup), so it keeps running when the big PC updates or restarts. It can sit inside the big case on its own shelf, in its own Pironman case, as a separate box. "The Pi needs to be always running and hardened" (see HARDEN THE PI in todo.md).
- Pi stays the always-on brain; the PC is the muscle (local AI, big jobs). Hailo chip stays on the Pi for cameras (it cannot run language or speech models); the PC's graphics card runs the models.
- Kylar wants top-notch RAM, graphics card and CPU so there is no ceiling later; good storage up front, more added over time. Budget not yet given (his monthly limit is under $100); stage the build if needed.
- Build it from separate parts in a case with a window, lights and fans: aluminum look, black or white, compact.

## Research 2026-11-07 (web; prices move daily, re-check before buying)
- RAM is the big shock: DDR5 prices are up several hundred percent in a year because AI is soaking up supply. A 128 GB DDR5 listing tracker (updated Nov 6) shows a median of about $34 per GB (about $4,300 for 128 GB), range $395 (one oddball single 128 GB stick) to $7,355; 4-month high and still rising (+5% over 90 days). Other reports list a 128 GB kit at $3,399 to $4,199 and 32 GB at about $480. DDR4 128 GB is far cheaper (about $195 to $1,000 by listing) but needs an older platform. Suggestion: buy 64 GB now (board with 4 slots so it can grow), add more when prices fall; do not pay 128 GB prices unless a model needs it.
- Graphics card is where local AI is decided (video memory, not speed): 24 GB handles 34B-class models and tight 70B; 32 GB (RTX 5090, about $2,000+, 575 W, wants 1000 W+ PSU) handles 70B at high compression; 2 used RTX 3090s (about $700-900 each, 48 GB total) is the best value for big models but needs a roomy case and x8/x8 board. RTX 4090 24 GB about $1,500-2,000. Single card, compact case: RTX 5090 or a used 3090/4090 are the realistic choices. (Sources undated snapshots; check prices.)
- Case candidates seen (all inside what a big GPU needs, 335 mm+ GPU length): Phanteks Evolv Shift 2 (anodized aluminum panels, glass version about $110, fits big GPUs; closest to "aluminum + window"), Fractal Design Terra (aluminum shell and wood trim, about $180, no glass mentioned, 322 mm GPU), NZXT H3 Flow (steel, glass side, about $79, 35 L, up to 377 mm GPUs, 4-slot cards), Cooler Master NR200P Max (glass/mesh, 336 mm). None checked against Kylar's cubby yet. Lian Li and Hyte options to look at once the cubby size is known.
- Power: 1000 W+ ATX 3.1 supply with the native 12V-2x6 cable for a 5090; two intake and two exhaust fans minimum; plan airflow for the cubby (open back or vented sides, no sealed cabinet).
- Wiring: use power over Ethernet (PoE). One Cat6 cable per spot (wall touchscreen, calendar, later a camera or speaker) from one PoE switch, with a PoE splitter or a PoE-powered panel at the far end. For running cable in walls: Cat6 (use in-wall rated CM/CL2 cable), fish tape or glow rods, stud finder, low-voltage mounting brackets (old-work), wall plates with keystone jacks or brush plates, drywall saw. Safety: stay away from mains wiring in the walls, do not run network cable alongside it, check for studs and fire blocks, and consider an electrician or low-voltage installer for any in-wall work Kylar is unsure about.

## Kitchen/living room screen plan 2026-11-08 (Kylar)
- Screen he already owns: GeekPi 10.1 in, 1024x600 IPS, capacitive touch, built-in dual speakers (bought Oct 16). Touch does not work now: these panels need a separate USB cable from the computer for touch (HDMI carries picture and sound only). First check: is a USB cable running to the panel's touch port?
- Goal: mount where the KEYS holder is, as few cords as possible. Wire route over the doorway (photo) is long; studs may force an attic run.
- Plan A (no wall/attic run): small Pi behind the panel on Wi-Fi, one short power cable to a kitchen outlet, touch and HDMI are short cables inside the mount. Screen shows the Starship/dashboard from the main Pi over the network.
- Plan B: one Cat6 with PoE to a splitter behind the panel (power and network in one cable).
- Truly wireless is not possible for a lit screen (it needs power); closest is Wi-Fi plus one power cable.
- Speakers: panel speakers first; pebble speakers (check if USB is power only; Pi 5 has no headphone jack so a USB audio dongle is needed) on a shelf later. Jarvis answers and chimes go to the panel or pebbles; music routes to the Lovesac via Music Assistant plus a small network streamer or Bluetooth (later step).
- Needed from Kylar: is there an outlet near the key holder; pebble speaker model; which cables came with the screen.

- 2026-11-08: Kylar owns 3x Raspberry Pi Zero 2 W (ordered Oct 16, for the other rooms); one can drive the kitchen screen. Limits: 512 MB RAM (animated Starship scene will be slow; use a light page), one micro-USB data port (touch plus pebbles needs a hub), mini-HDMI. Pebble speakers are USB-A only.

- 2026-11-08: Case draft for the kitchen screen in hardware/kitchen-screen-case/ (kitchen_screen_case.scad parametric, blueprint.png). Two ASA parts (frame + back with Pi pod), vents bottom-in/top-out, wall keyholes, 247 x 154 mm, 19.4 mm slab, 43.4 mm at the pod. NOT test-compiled (no OpenSCAD here); dimensions assumed until Kylar measures the screen.
- Parts cart (11-08): SANOOV Pi 5 4GB kit, Pi 27W supply, SanDisk 64GB, Alvin's micro-HDMI cable, SUNGUY 2-pack USB-A to USB-C 1 ft; VHB tape already owned.

## Open questions for Kylar
1. Cubby measurements (width, height, depth, clearance) and whether the back/sides are open.
2. Budget for stage 1 (case, PSU, board, CPU, 64 GB RAM, starter NVMe) and for the graphics card.
3. The TikTok compact computers he liked (names/screenshots), to compare against a self-build.
4. Fully offline AI wanted? Which models? (decides VRAM)
5. Touch-screen size and brand preferences; whether the calendar is a store-bought smart display.
6. Where the Pi box sits (inside the case on its own shelf vs next to it) and whether it shares the new drive storage.

## Next steps
- [ ] Kylar: measure the cubby; send TikTok models.
- [ ] Claude: price-check a 2-3 option parts list against the cubby; compare with a ready-made compact machine; cable and PoE shopping list for the wall spots.
- [ ] Add this as a house project (and later its own room) on the Starship.

## Done
(nothing yet)

- 2026-11-08 case v2: real screen data (235x142x8; all ports on one short edge; ONE USB-C 'Touch & Power', full-size HDMI-IN, 3.5mm audio out; speakers on the rear top; M2.5 mounting points near the corners). Case now 277x154 mm, 20.2 mm slab, 44.2 mm at the pod, with a 30 mm cable bay on the port side, screen held by 4 M2.5 posts, speaker sound slots in the top rim. Only ONE USB cable is needed (2nd SUNGUY is spare). Hole positions are estimates from the diagram; not compiled in OpenSCAD yet.
