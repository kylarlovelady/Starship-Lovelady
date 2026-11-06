#!/bin/bash
# QUEUE-OK
# run the board builder and the crew report once, then check the Starship page files and the projects rows
cd ~/starship && python3 tasks/projects_board.py 2>&1 | head -4
python3 tasks/crew_report.py 2>&1 | tail -2
cmp ~/starship/index.html ~/crew-web/index.html && echo "page copy: same as repo"
python3 -c "import json;d=json.load(open('/home/kylarlovelady/crew-web/hub-extra.json'));print('projects rows in served json:',len(d.get('projects',[])))"
curl -s -m 5 -o /dev/null -w "page %{http_code} %{size_download}b\n" http://100.105.140.126:8095/
