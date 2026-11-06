#!/bin/bash
# QUEUE-OK
# Rebuild all 8 notebooks without the white barcode box (published without an ISBN, so KDP prints no barcode).
cd ~/kdp-studio || exit 1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py 2>&1 | grep -E "FAIL|==|sheet" | head -20
ls -la ~/kdp-studio/books/process-operator-a/out/*.pdf ~/kdp-studio/books/lab-operator-a/out/*.pdf
