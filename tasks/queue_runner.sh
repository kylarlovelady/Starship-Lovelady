#!/bin/bash
# Runs new scripts from tasks/queue/ once each (see tasks/queue/README.md). Cron every 3 minutes after the git pull.
# Install: bash ~/starship/tasks/queue_runner.sh install     Kill switch: touch ~/queue.off
if [ "$1" = "install" ]; then
  ( crontab -l 2>/dev/null | grep -v task-queue; echo "1-59/3 * * * * flock -n /tmp/queue.lock bash \$HOME/starship/tasks/queue_runner.sh >> \$HOME/queue.log 2>&1 # task-queue" ) | crontab -
  echo "Installed: the Pi checks the task queue every 3 minutes. Turn off any time with: touch ~/queue.off"; exit 0
fi
[ -f ~/queue.off ] && exit 0
cd ~/starship 2>/dev/null || exit 1
DONE=~/.queue_done; touch $DONE
RES=memory/inbox/queue-results.md; ran=0
BAD='rm +-[a-z]*r[a-z]* +(/|~|\$HOME)( |$)|mkfs|dd +.*of=/dev|shutdown|reboot|poweroff|passwd|ssh-keygen|curl[^|]*\|[^|]*sh|wget[^|]*\|[^|]*sh|keys\.env|market-data/env|\.ssh/|id_ed25519|chmod +-?[0-7]*777 +/|:\(\)\{'
for f in tasks/queue/*.sh; do
  [ -f "$f" ] || continue
  sum=$(sha256sum "$f" | cut -d' ' -f1); grep -q "$sum" $DONE && continue
  { echo; echo "## $(date '+%F %T') $f"; } >> $RES
  if [ "$(sed -n 1p "$f")" != "#!/bin/bash" ] || [ "$(sed -n 2p "$f")" != "# QUEUE-OK" ]; then echo "REFUSED: header must be '#!/bin/bash' then '# QUEUE-OK'" >> $RES
  elif grep -E -q "$BAD" "$f"; then echo "REFUSED: contains a command on the deny list" >> $RES
  elif grep -E -q '(^|[;&| ])sudo ' "$f"; then echo "REFUSED: sudo is not allowed in queue scripts" >> $RES
  else echo '```' >> $RES; ( timeout 300 bash "$f" 2>&1 | head -c 6000 ) >> $RES; echo "(exit ${PIPESTATUS[0]})" >> $RES; echo '```' >> $RES; fi
  echo "$sum $f" >> $DONE; ran=$((ran+1))
done
if [ $ran -gt 0 ]; then
  tail -c 30000 $RES > $RES.tmp && mv $RES.tmp $RES
  bash ~/starship/tasks/memory_sync.sh >/dev/null 2>&1 || true
  echo "$(date '+%F %T') ran $ran queue script(s)"
fi
