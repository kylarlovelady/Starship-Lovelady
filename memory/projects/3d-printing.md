# 3D printing
- Printer: Bambu Lab P1S, with a smart plug and a camera, a smoke detector in the room, someone almost always home.
- Idea: describe a part, Claude designs it in CAD, it prints; sell on Etsy and make custom parts. Wants the Pi and dashboard connected to run it nonstop.
- To check: Bambu connection options (LAN mode, cloud, Home Assistant integration); starting a print remotely from the Pi; auto-clearing prints is hardware-dependent, verify what is safe before running unattended.
- Safety plan: a Home Assistant rule that cuts the printer's smart plug and sends a phone alert on smoke or bad air. An air quality monitor is not a certified fire alarm: keep a real smoke detector and use the monitor as an extra trigger. Kylar to send a photo of his air quality monitor (model unknown); confirm the smoke detector is visible to Home Assistant.

- 2026-11-06 (Kylar by voice): filaments on hand are PLA and a hard black one he thinks is ASA (unconfirmed, check the spool label). Use ASA for anything in the truck (PLA softens in a hot cab); PLA only for test prints. Printer is the enclosed P1S.

## Kitchen screen case: print lessons and recipe (2026-11-09)
- Plate 1 (door A + left body half) failed at the hinge knuckles on the first print: the round barrels sit over empty space. Bambu Studio warned "floating cantilever" and the warning was right. Fix: supports ON. Settings picked 2026-11-09 03:45: Support tab, Enable support checked, Type tree, Threshold angle 30, "On build plate only" unchecked. Reslice, check Preview shows support under the barrels on both parts, then print.
- Base recipe (Bambu Lab P1S, textured PEI, PolyLite ASA, 0.4 mm stainless nozzle, profile 0.20mm Standard @BBL X1C): Wall loops 4, Sparse infill 20% Gyroid, Top/Bottom shell layers 4, Brim Outer brim only 5 mm, Timelapse Off. Dry the ASA first.
- Future: redesign hinge knuckles with 45 degree chamfered undersides so they print without supports (only if Kylar asks).

## Kitchen screen case v7: fixes needed after the first real build (Kylar by voice, 2026-11-09 night, last plate printing)
Kylar is making this first case work for himself; ALL of these must be fixed before it is sold to anyone. Do not redraw until he sends the measurements below.
1. Doors fall open: the faceplate screws are the only thing holding the doors shut and the tolerances are loose. Fix: a detent bump and notch on each door so it clicks and stays shut without the faceplate screws.
2. Doors wiggle: one hinge pin lets them rock. Fix: a second hinge point or a wider bearing, and tighter clearances.
3. Screen mounting does not work: the back-plate holes cannot be screwed through the screen. Kylar's idea (adopted): enlarge the holes in the posts the screen sits on so the screen's brass studs sit INSIDE them, then the faceplate screws clamp the screen down onto the studs.
4. Adapters and cables do not fit in the side bays: the plugs stick out up, down or back; he had to take a door off. Fix: use 180 degree (right-angle the other way) adapters so the cable runs back along the screen edge, and make BOTH bays wider so the case stays even (not lopsided). Redo the left bay around that.
5. Pi screws and posts: the screws that came with the Pi do not fit the holes, and with the Pi on the posts its tall USB and Ethernet ports hit the back of the screen. Kylar double-sided taped the Pi to the back of the screen for now. Fix: a printed Pi tray that rides on the back of the screen (preferred) or a shallow flat mount with port notches; check the screw size.
- Measurements I need from Kylar: (a) how far the HDMI adapter plus cable stick out from the screen edge (mm or inches); (b) brass stud diameter (about 5 mm?) with a close-up and tape measure; (c) height of the Pi's tallest port with the Pi flat on a table, in mm. Also photos or drawings of the adapters he will use.
- A 6:30 AM phone reminder holds the same list (set by voice).
