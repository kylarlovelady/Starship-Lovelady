#!/bin/bash
# QUEUE-OK
# copy the Process Operator C and E covers into the repo so Claude can send them to Kylar
cd ~/starship || exit 1
for k in c e; do
  mkdir -p memory/inbox/kdp-preview/process-operator-$k
  cp ~/kdp-studio/books/process-operator-$k/out/cover.pdf memory/inbox/kdp-preview/process-operator-$k/cover.pdf
  git add memory/inbox/kdp-preview/process-operator-$k/cover.pdf
done
git commit -q -m "KDP: Process Operator C and E covers" 2>&1 | tail -1
git pull -q --rebase --autostash 2>&1 | tail -1
git push -q 2>&1 | tail -1
