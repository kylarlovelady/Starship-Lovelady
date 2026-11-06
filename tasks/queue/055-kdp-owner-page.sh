#!/bin/bash
# QUEUE-OK: refined owner page for the KDP interiors (small, letter-spaced, hairline fields)
cd ~/kdp-studio || exit 1
PY=~/kdp-studio/.venv/bin/python
$PY -c "import pypdf" 2>/dev/null || $PY -m pip install -q pypdf 2>&1 | tail -1
cd ~/starship && git pull -q --rebase --autostash 2>&1 | tail -1
cd ~/kdp-studio && $PY ~/starship/tasks/kdp_owner.py 2>&1 | tail -12
ls -l ~/kdp-studio/books/process-operator-a/out/
