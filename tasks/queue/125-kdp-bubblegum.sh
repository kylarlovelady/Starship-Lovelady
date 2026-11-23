#!/bin/bash
# QUEUE-OK
# Build the two new KDP colours (H bubblegum pink with white lettering) for every title; copy cover + interior + preview into memory/inbox/kdp-preview.
nohup bash -c '
cd ~/kdp-studio
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py h > ~/kdp-build-h.log 2>&1
slugs=""; for t in process-operator lab-operator; do for k in h; do slugs="$slugs $t-$k"; done; done
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_owner.py $slugs >> ~/kdp-build-h.log 2>&1
cd ~/starship
for k in $slugs; do
  o=memory/inbox/kdp-preview/$k; mkdir -p $o
  cp ~/kdp-studio/books/$k/out/cover.pdf $o/cover.pdf; cp ~/kdp-studio/books/$k/out/interior.pdf $o/interior.pdf
  PYTHONPATH=$HOME/kdp-studio ~/kdp-studio/.venv/bin/python -c "import engine,sys; engine.png(sys.argv[1], sys.argv[2], 1, 60)" ~/kdp-studio/books/$k/out/cover.pdf $o/cover >> ~/kdp-build-h.log 2>&1
  PYTHONPATH=$HOME/kdp-studio ~/kdp-studio/.venv/bin/python -c "import engine,sys; engine.png(sys.argv[1], sys.argv[2], 120, 90)" ~/kdp-studio/books/$k/out/interior.pdf $o/last-page >> ~/kdp-build-h.log 2>&1
done
git add -f memory/inbox/kdp-preview
git commit -q -m "KDP: bubblegum pink covers

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git pull -q --rebase --autostash; git push -q
echo done >> ~/kdp-build-h.log
' > /dev/null 2>&1 &
echo "KDP black-gold + pink build started in the background (log ~/kdp-build-h.log)"
