#!/bin/bash
# QUEUE-OK
# raise the home Jarvis wake sensitivity threshold 0.7 -> 0.8 (14 of 21 wake-ups in 7 days were false, 6 of them at 2-4 AM); restores 0.7 automatically if the wake service does not come back
bash ~/starship/tasks/jarvis_tune.sh 0.8 "14 of 21 wake-ups in 7 days were false (6 at 2-4 AM when nobody was talking)"
docker ps --format '{{.Names}} {{.Status}}' | grep -i wake
systemctl is-active hub-satellite
