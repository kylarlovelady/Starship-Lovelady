#!/bin/bash
# QUEUE-OK
# copy the new Process Operator A interior into the repo so Claude can send it to Kylar
cd ~/starship || exit 1
mkdir -p memory/inbox/kdp-preview/process-operator-a
cp ~/kdp-studio/books/process-operator-a/out/interior.pdf memory/inbox/kdp-preview/process-operator-a/interior.pdf
ls -l memory/inbox/kdp-preview/process-operator-a/interior.pdf
git add memory/inbox/kdp-preview/process-operator-a/interior.pdf
git commit -q -m "KDP: new Process Operator A interior (owner page)" 2>&1 | tail -1
git pull -q --rebase --autostash 2>&1 | tail -1
git push -q 2>&1 | tail -1
