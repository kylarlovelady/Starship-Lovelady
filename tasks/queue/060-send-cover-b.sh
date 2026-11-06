#!/bin/bash
# QUEUE-OK
# copy the Process Operator B (forest green) cover into the repo so Claude can send it to Kylar
cd ~/starship || exit 1
mkdir -p memory/inbox/kdp-preview/process-operator-b
cp ~/kdp-studio/books/process-operator-b/out/cover.pdf memory/inbox/kdp-preview/process-operator-b/cover.pdf
ls -l memory/inbox/kdp-preview/process-operator-b/cover.pdf
git add memory/inbox/kdp-preview/process-operator-b/cover.pdf
git commit -q -m "KDP: Process Operator B cover" 2>&1 | tail -1
git pull -q --rebase --autostash 2>&1 | tail -1
git push -q 2>&1 | tail -1
