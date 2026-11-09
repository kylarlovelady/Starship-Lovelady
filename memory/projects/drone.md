# Quiet payload drone (3D printed parts, good camera, thermal camera, Steam Deck ground station)

Added 2026-11-09 (Kylar by text). Status: idea. Nothing chosen or bought.

## What Kylar wants
- A drone that can carry a payload, and is quiet.
- Printed on his Bambu P1S where it makes sense.
- A good camera plus maybe a thermal camera.
- Controlled from his Steam Deck (LCD model, see steam-deck.md).

## First ideas (Claude, unconfirmed; to research with current prices before buying)
- Quiet and lifting heavy pull in the same direction: large, slow-turning props on low-KV motors, more than four motors if needed, and a frame that keeps vibration down. Prop choice matters more for noise than anything else.
- Frame: carbon-fibre tubes for the arms, printed hubs, mounts and payload brackets (ASA or PETG-CF; PLA softens too easily). Print the camera and payload mounts first as they are the safest start.
- Flight controller: an ArduPilot-class board (open, supports payload, gimbal, return-to-home). Companion computer (a small Pi) can run the cameras.
- Ground station on the Steam Deck: Desktop Mode runs Linux flight-control apps (Mission Planner or QGroundControl); the Deck needs a telemetry link and a video link to the drone. Sticks on the Deck can be mapped as a joystick. A dedicated radio is the safer primary control; the Deck can be the screen and mission planner at first.
- Cameras: a stabilised main camera on a gimbal; a thermal module (small thermal cores exist for hobby use). Check resolution and frame rate versus price, and whether video can be sent live to the Deck.

## Rules to check before flying (not legal advice)
- In the US, FAA rules apply: registration over 250 g, Remote ID, keep line of sight, and a Part 107 licence if any flying is for business (for example selling photos or inspection work). Confirm current rules before the first flight.

## Questions for Kylar
- How much payload (grams or pounds) and what is it (camera gimbal only, or something to drop or carry)?
- What is it for (video, inspecting, the farm/coop, fun)?
- Budget, and whether he wants to buy a proven frame and print only add-ons, or design the frame himself.

## Next step
- Kylar answers the questions; Claude researches parts and prices and drafts a staged plan: bench test one motor and prop for thrust and noise, then a small test frame, then the full build.

## Done
(nothing yet)
