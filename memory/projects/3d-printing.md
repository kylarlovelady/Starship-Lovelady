# 3D printing
- Printer: Bambu Lab P1S, with a smart plug and a camera, a smoke detector in the room, someone almost always home.
- Idea: describe a part, Claude designs it in CAD, it prints; sell on Etsy and make custom parts. Wants the Pi and dashboard connected to run it nonstop.
- To check: Bambu connection options (LAN mode, cloud, Home Assistant integration); starting a print remotely from the Pi; auto-clearing prints is hardware-dependent, verify what is safe before running unattended.
- Safety plan: a Home Assistant rule that cuts the printer's smart plug and sends a phone alert on smoke or bad air. An air quality monitor is not a certified fire alarm: keep a real smoke detector and use the monitor as an extra trigger. Kylar to send a photo of his air quality monitor (model unknown); confirm the smoke detector is visible to Home Assistant.

- 2026-11-06 (Kylar by voice): filaments on hand are PLA and a hard black one he thinks is ASA (unconfirmed, check the spool label). Use ASA for anything in the truck (PLA softens in a hot cab); PLA only for test prints. Printer is the enclosed P1S.
