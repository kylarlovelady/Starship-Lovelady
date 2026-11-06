#!/bin/bash
# QUEUE-OK
# copy the navy (A) covers into the repo so Claude can send them to Kylar
cd ~/starship || exit 1
for t in process-operator lab-operator; do
  if [ -f ~/kdp-studio/books/$t-a/out/cover.pdf ]; then
    mkdir -p memory/inbox/kdp-preview/$t-a
    cp ~/kdp-studio/books/$t-a/out/cover.pdf memory/inbox/kdp-preview/$t-a/cover.pdf
    git add memory/inbox/kdp-preview/$t-a/cover.pdf
  else
    echo "missing $t-a cover"; ls ~/kdp-studio/books/ | head -20
  fi
done
git commit -q -m "KDP: navy covers" 2>&1 | tail -1
git pull -q --rebase --autostash 2>&1 | tail -1
git push -q 2>&1 | tail -1
ls -l memory/inbox/kdp-preview/*-a/cover.pdf
