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
