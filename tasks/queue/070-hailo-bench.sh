#!/bin/bash
# QUEUE-OK
# run a 5 second speed test of the AI chip with an object-detection model made for it
timeout 60 hailortcli benchmark --time-to-run 5 /usr/share/hailo-models/yolov6n_h8.hef 2>&1 | tail -10
echo "== temp"; hailortcli measure-power --help >/dev/null 2>&1; hailortcli fw-control chip-temp 2>&1 | tail -3
