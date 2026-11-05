#!/bin/bash
# Gives the Pi permission to push notes to the repo (a deploy key for THIS repo only), then installs a 30-minute notes sync.
# Run 1: creates the key and prints it. Add it at GitHub (repo Settings > Deploy keys > Add deploy key, tick "Allow write access").
# Run 2 (same command): tests the connection and installs the cron job.
set -e
KEY=~/.ssh/starship_deploy
mkdir -p ~/.ssh; chmod 700 ~/.ssh
if [ ! -f $KEY ]; then
  ssh-keygen -t ed25519 -N "" -C "lovelady-ai-hub-notes" -f $KEY >/dev/null
  echo; echo "Key created. Copy EVERYTHING on the next line (starts with ssh-ed25519):"; echo
  cat $KEY.pub; echo
  echo "Now on GitHub: open the Starship-Lovelady repo > Settings > Deploy keys > Add deploy key."
  echo "Title: Pi notes. Paste the key. Tick 'Allow write access'. Add key. Then run this same command again."
  exit 0
fi
grep -q "Host github-starship" ~/.ssh/config 2>/dev/null || cat >> ~/.ssh/config <<CFG

Host github-starship
  HostName github.com
  User git
  IdentityFile $KEY
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
CFG
chmod 600 ~/.ssh/config
cd ~/starship
git remote set-url --push origin git@github-starship:kylarlovelady/Starship-Lovelady.git
git config pull.rebase true
git config user.name "Lovelady AI Hub"; git config user.email "hub@loveladymainaihub.local"
if ssh -T git@github-starship 2>&1 | grep -qi "successfully authenticated"; then
  echo "GitHub accepts the key."
else
  echo "GitHub did not accept the key yet. Check the deploy key was added with write access, then run this again."; exit 1
fi
( crontab -l 2>/dev/null | grep -v memory_sync; echo "*/30 * * * * bash \$HOME/starship/tasks/memory_sync.sh >> \$HOME/memory_sync.log 2>&1" ) | crontab -
echo "Installed. Notes sync every 30 minutes. Test now with: bash ~/starship/tasks/memory_sync.sh"
