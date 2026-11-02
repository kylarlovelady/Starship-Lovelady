# Short commands for typing on a phone. Loaded from ~/.bashrc.
alias mcheck='~/crew-update.sh >/dev/null 2>&1; python3 ~/starship/markets/check.py'   # health check of the market agent
alias mlog='journalctl -u market-agent -n 30 --no-pager'                                # last lines of its log
alias mrestart='sudo systemctl restart market-agent && echo restarted'
alias mstop='sudo systemctl stop market-agent && echo stopped'
alias mstart='sudo systemctl start market-agent && echo started'
alias mupdate='~/crew-update.sh && echo updated'                                         # pull the newest version now
alias hub='systemctl list-units "hub*" --no-pager | head -20; sudo docker ps --format "{{.Names}} {{.Status}}"'  # are the hub services up
alias shortcuts='grep -h "^alias" ~/starship/markets/shortcuts.sh | cut -d"=" -f1 | sed "s/alias /  /"'
alias mrun='~/crew-update.sh >/dev/null 2>&1; echo "----- about to run -----"; cat ~/starship/tasks/run.sh; echo "------------------------"; read -p "Run this? (y/n) " a; [ "$a" = y ] && bash ~/starship/tasks/run.sh'   # runs the task Claude queued, after showing it to you
