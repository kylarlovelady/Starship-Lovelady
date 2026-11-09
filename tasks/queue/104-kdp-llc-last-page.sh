#!/bin/bash
# QUEUE-OK
# Rebuild all KDP books: no "Lovelady LLC" on the back cover, small imprint on the last interior page. Copies cover, interior and last-page preview into the repo.
nohup bash -c '
cd ~/kdp-studio
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py > ~/kdp-build-llc.log 2>&1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_owner.py >> ~/kdp-build-llc.log 2>&1
cd ~/starship
for k in process-operator-a process-operator-b process-operator-c process-operator-e lab-operator-a lab-operator-b lab-operator-c lab-operator-e; do
  o=memory/inbox/kdp-preview/$k; mkdir -p $o
  cp ~/kdp-studio/books/$k/out/cover.pdf $o/cover.pdf; cp ~/kdp-studio/books/$k/out/interior.pdf $o/interior.pdf
  PYTHONPATH=$HOME/kdp-studio ~/kdp-studio/.venv/bin/python -c "import engine,sys; engine.png(sys.argv[1], sys.argv[2], 120, 90)" ~/kdp-studio/books/$k/out/interior.pdf $o/last-page >> ~/kdp-build-llc.log 2>&1
  PYTHONPATH=$HOME/kdp-studio ~/kdp-studio/.venv/bin/python -c "import engine,sys; engine.png(sys.argv[1], sys.argv[2], 1, 60)" ~/kdp-studio/books/$k/out/cover.pdf $o/cover >> ~/kdp-build-llc.log 2>&1
done
git add -f memory/inbox/kdp-preview
git commit -q -m "KDP: LLC off back cover, small on last page

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git pull -q --rebase --autostash; git push -q
echo done >> ~/kdp-build-llc.log
' > /dev/null 2>&1 &
echo "KDP rebuild started in the background"
