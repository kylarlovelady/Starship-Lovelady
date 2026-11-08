#!/bin/bash
# QUEUE-OK
# Sets up a free scripted-CAD toolbox on the Pi (no sudo): Python venv with manifold3d (solid 3D boolean engine), trimesh (STL check/export), numpy.
set -u
cd ~ || exit 1
python3 -m venv ~/cad-venv 2>&1 | tail -2
. ~/cad-venv/bin/activate
pip install --quiet --upgrade pip 2>&1 | tail -1
pip install --quiet manifold3d trimesh numpy 2>&1 | tail -3
python - <<'P'
import manifold3d, trimesh, numpy
print("manifold3d", manifold3d.__version__ if hasattr(manifold3d,"__version__") else "ok")
print("trimesh", trimesh.__version__, "numpy", numpy.__version__)
m = manifold3d.Manifold.cube([20,10,5], True) - manifold3d.Manifold.cylinder(10, 2, 2, 32)
print("boolean test volume", round(m.volume(),1), "genus", m.genus())
P
echo "openscad on this Pi: $(command -v openscad || echo not installed)"
echo "arch: $(uname -m); python: $(python3 --version)"
