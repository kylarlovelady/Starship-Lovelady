#!/bin/bash
# QUEUE-OK
# liquidity by second, counting only seconds that have a book row; then check the KDP owner-page build
python3 ~/starship/tasks/liq_by_second.py 2>&1 | tail -30
echo "=== owner page"
cd ~/kdp-studio && ~/kdp-studio/.venv/bin/python -c "import pypdf; print('pypdf', pypdf.__version__)" 2>&1 | tail -1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_owner.py process-operator-a 2>&1 | tail -8
ls -l ~/kdp-studio/books/process-operator-a/out/ 2>&1
