# CAD kit: describe a part, get print files and a 3D view

Pure Node (no installs). `csg.mjs` is a small solid-modelling kernel (union, subtract, intersect, boxes, cylinders, extruded outlines).

1. Copy `example-part.mjs`, change the numbers or shapes.
2. `node --stack-size=30000 my-part.mjs` writes `stl/*.stl` (watertight, ready for a slicer).
3. `node view.mjs out.html stl/a.stl stl/b.stl` writes a self-contained 3D page you can open or publish.
4. Check fits by intersecting parts: `a.and(b)` should have ~0 volume (see `../kitchen-screen-case/v6/verify.mjs`).

Worked example with doors, hinges and vents: `hardware/kitchen-screen-case/v6/`.
Pi toolbox (manifold3d + trimesh in `~/cad-venv`, queued as `tasks/queue/099-cad-setup.sh`) is the Python route for heavier shapes.
