# Task queue
Claude (or Kylar) drops a script here; the Pi runs it once and writes the output to `memory/inbox/queue-results.md`, so nobody has to copy and paste commands.
Rules (enforced by tasks/queue_runner.sh): file ends in `.sh`, first line is exactly `#!/bin/bash`, second line is `# QUEUE-OK`; runs as the normal user (no sudo), 5 minute limit, once per file content; scripts with dangerous commands are refused (rm -rf on / or ~, mkfs, dd to a disk, shutdown, reboot, passwd, ssh-keygen, curl|sh, anything reading keys.env or env files). Kill switch on the Pi: `touch ~/queue.off` (remove the file to resume).
Security: whoever can push to this repo can run these on the Pi, so keep 2-step login on GitHub. Results are public (the repo is public): scripts must not print keys, balances or personal data.

Warning (11-14): never start a background server from a queue script. It inherits the runner's flock and the queue then stops running anything (the Hub media server did this from queue 116). Start servers from crew-update.sh or a cron line instead.
