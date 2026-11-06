#!/bin/bash
# QUEUE-OK
# build the orchid purple (scheme e) covers and interiors in the background, add the refined owner page, copy the Process Operator cover and preview into the repo
nohup bash -c '
cd ~/kdp-studio
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py e > ~/kdp-build-e.log 2>&1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_owner.py process-operator-e lab-operator-e >> ~/kdp-build-e.log 2>&1
cd ~/starship
for k in process-operator-e lab-operator-e; do mkdir -p memory/inbox/kdp-preview/$k; cp ~/kdp-studio/books/$k/out/cover.pdf memory/inbox/kdp-preview/$k/cover.pdf; git add memory/inbox/kdp-preview/$k; done
git add -f memory/inbox/kdp-preview
git commit -q -m "KDP: orchid purple covers (scheme e)" 
git pull -q --rebase --autostash
git push -q
echo done >> ~/kdp-build-e.log
' > /dev/null 2>&1 &
echo "orchid build started in the background"
