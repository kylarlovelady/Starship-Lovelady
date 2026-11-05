#!/bin/bash
# QUEUE-OK
# Copy the KDP studio code and the current book.json into the notes folder so Claude can read and test it (code only: no PIN, no settings).
D=~/starship/memory/inbox/kdp-studio-copy
mkdir -p $D && cd ~/kdp-studio || exit 1
cp -f engine.py app.py $D/
cp -f "$(ls -t books/*/book.json | head -1)" $D/book-current.json
cp -f "$(ls -t books-old-1026-0008/*/book.json | head -1)" $D/book-old.json
ls -la $D
