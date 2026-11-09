# Quiet payload drone (3D printed parts, good camera, thermal camera, Steam Deck ground station)

Added 2026-11-09 (Kylar by text). Status: idea. Nothing chosen or bought.

## What Kylar wants
- A drone that can carry a payload, and is quiet.
- Printed on his Bambu P1S where it makes sense.
- A good camera plus maybe a thermal camera.
- Controlled from his Steam Deck (LCD model, see steam-deck.md).

## Answers so far (Kylar, 2026-11-09 12:07)
- Purpose: fun (hobby, no business use, so Part 107 is not needed unless that changes).
- The Steam Deck IS the controller (sticks and triggers fly it), not just a screen. He would enjoy building a printed attachment for the Deck (for example a holder for the radio/telemetry module, antenna and video receiver, powered from the Deck's USB-C).
- Wants to fly low (not high) but FAR (2026-11-09 12:08). Claude notes (unconfirmed): long range design = efficient big slow props (also quiet), a large battery (Li-ion 21700 packs are common for long range), a light frame, and a long-range radio link (900 MHz class, for example ELRS 915 or a 900 MHz telemetry radio with a good antenna). Flying low shortens radio range because of trees, buildings and ground. Legal limit to check: US recreational rules require keeping the drone in visual line of sight (or using a visual observer when flying FPV), so "far" in practice means as far as he can see it, unless he gets an FAA waiver or goes the Part 107 route. Land and permission matter too (private property, no flying over people).
- Where: his grandma's 200-acre property (private land, owner's permission). 200 acres is about 0.8 square km, roughly 900 m on a side, so he needs about 1 to 1.5 km of radio range, which is modest. FAA rules still apply on private land (registration over 250 g, Remote ID, line of sight, check nearby airspace). Trees and hills may block sight and signal; check the terrain. Ask grandma about livestock, neighbours and power lines.
- Correction 2026-11-09 12:11: the property is THIN AND LONG, cabin at the very front, with quite a lot of trees. Kylar wants to fly to the very back. Claude math (unconfirmed): 200 acres is about 810,000 m2, so a strip 200 m wide is about 4 km long and 300 m wide about 2.7 km long. The back may be 2 to 4 km from the cabin, a lot more than the earlier 1-1.5 km estimate. Consequences: a round trip of 5 to 8 km needs about 20 to 30 minutes of flight; a long-range 900 MHz link (ELRS 915 class) is realistic over open ground but trees cut range a lot, so use a high antenna, test early, and have a failsafe; line of sight to the far end is unlikely from the cabin, so the practical plan is to move the launch point (truck, ATV) toward the middle or the back, or use a spotter. Next: ask Kylar for the property length and width (a satellite map screenshot works).
- Kylar (2026-11-09 12:13): a little over 2 miles from the cabin to the back (he thinks in miles; answer him in miles and feet). 2 miles is about 3.2 km. At 200 acres that makes the property about 800 ft wide. Round trip about 4.5 miles. The radio and battery plan should target 2.5 miles out with margin (about 3 miles), through trees.
- Budget: none set; Kylar knows it will be pricey and wants to save where he can. Payload: unknown, wants enough for all the cameras and attachments (2026-11-09 12:15).
- Claude's working target (unconfirmed, to be checked in research): payload about 1 kg (2.2 lb) covering a main camera on a small gimbal (about 200-400 g), a thermal module (about 50-150 g), a small companion computer, video transmitter and wiring (about 150-250 g), and some margin. Aircraft total maybe 4-6 lb with battery. A long-range, quiet build usually costs more in battery and motors than in the electronics; first rough budget guess about $1,500-3,500 (guess only, price check before buying). Save money by printing mounts, buying a proven flight controller and motors rather than a ready kit, and buying the thermal module last.
- Still unanswered (only if Kylar wants to say): payload weight and what it carries, budget, buy-a-frame vs design-own-frame.

## First ideas (Claude, unconfirmed; to research with current prices before buying)
- Quiet and lifting heavy pull in the same direction: large, slow-turning props on low-KV motors, more than four motors if needed, and a frame that keeps vibration down. Prop choice matters more for noise than anything else.
- Frame: carbon-fibre tubes for the arms, printed hubs, mounts and payload brackets (ASA or PETG-CF; PLA softens too easily). Print the camera and payload mounts first as they are the safest start.
- Flight controller: an ArduPilot-class board (open, supports payload, gimbal, return-to-home). Companion computer (a small Pi) can run the cameras.
- Deck as the controller (Claude, unconfirmed): in Desktop Mode, QGroundControl can map the Deck's sticks to a joystick and send them to an ArduPilot drone over a MAVLink telemetry radio link. This needs testing for lag and what the drone does when the link drops (set a safe failsafe: hover, then return home). A regular RC radio link as backup is the safer plan for the first flights.
- Ground station on the Steam Deck: Desktop Mode runs Linux flight-control apps (Mission Planner or QGroundControl); the Deck needs a telemetry link and a video link to the drone. Sticks on the Deck can be mapped as a joystick. A dedicated radio is the safer primary control; the Deck can be the screen and mission planner at first.
- Cameras: a stabilised main camera on a gimbal; a thermal module (small thermal cores exist for hobby use). Check resolution and frame rate versus price, and whether video can be sent live to the Deck.

## Rules to check before flying (not legal advice)
- In the US, FAA rules apply: registration over 250 g, Remote ID, keep line of sight, and a Part 107 licence if any flying is for business (for example selling photos or inspection work). Confirm current rules before the first flight.

## Questions for Kylar
- How much payload (grams or pounds) and what is it (camera gimbal only, or something to drop or carry)?
- What is it for (video, inspecting, the farm/coop, fun)?
- Budget, and whether he wants to buy a proven frame and print only add-ons, or design the frame himself.

## Next step
- PARKED by Kylar 2026-11-09 12:16: save for later, do not start the parts research until he asks.
- When he asks: - Kylar answers the questions; Claude researches parts and prices and drafts a staged plan: bench test one motor and prop for thrust and noise, then a small test frame, then the full build.

## Done
(nothing yet)
