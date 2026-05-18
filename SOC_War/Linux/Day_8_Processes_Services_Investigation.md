# Linux Day 8 — Processes, Services & System Behavior Investigation

## Objective
Investigate system for indicators of compromise through process analysis, network monitoring, persistence detection, and authentication review.

## Investigation Methodology

### Stage 1: Process Enumeration
**Command:** `ps aux`

**Findings:**
- Kernel processes: All standard (systemd, kthreadd, kworkers)
- User processes: SSH daemon, cron service, network services
- Assessment: No suspicious processes detected
- Red flags checked: Wrong user ownership, unusual parents, staging directories

### Stage 2: Network Connection Monitoring
**Command:** `sudo lsof -i`

**Findings:**
- SSH listening on port 22 (expected)
- systemd-resolve handling DNS (expected)
- systemd-network managing DHCP (expected)
- Current SSH session established from gateway
- Assessment: No C2 beaconing, no reverse shells, no unexpected listening ports
- Red flags checked: Unknown external connections, continuous beaconing, backdoor ports

### Stage 3: Persistence Mechanism Detection
**Commands:** 
- `sudo cat /var/spool/cron/crontabs/root`
- `sudo ls -la /etc/systemd/system/`

**Findings:**
- No cron jobs in root crontab
- All systemd services are standard/documented
- Regular cron jobs run every 5 minutes (system scheduled tasks, normal)
- Assessment: No backdoor persistence, no malicious services
- Red flags checked: Unauthorized cron jobs, custom systemd services, suspicious schedulers

### Stage 4: Authentication Log Review
**Command:** `sudo grep -E "sudo|Failed|Accepted" /var/log/auth.log | tail -30`

**Key Events:**
- 04:02:41 — SSH key authentication (expected)
- 04:04:14 — sudo mailcap installation (user activity)
- 04:08:45 — sudo net-tools installation (user activity)
- 04:19:03 — sudo bruteforce tool (user activity)
- 19:21:35 → 19:45:11 — Investigation commands (current session)
- 15-hour gap between 04:19 and 19:21 with NO suspicious activity

**Findings:**
- No failed SSH attempts from unknown IPs
- No unauthorized logins
- All sudo usage is from ubuntu user (expected)
- No lateral movement attempts
- Assessment: Authentication layer is secure
- Red flags checked: Failed logins, brute force attempts, privilege escalation abuse

### Stage 5: Temporary File System Inspection
**Command:** `sudo ls -la /tmp/`

**Findings:**
- snap-private-tmp (snap package isolation)
- systemd-private-* directories (service temporary storage)
- No suspicious files or scripts
- No staging artifacts
- Assessment: No malware or exploit staging detected

## Investigation Summary

Comprehensive system security investigation conducted across five stages:
1. ✅ Process execution analysis
2. ✅ Network connection monitoring
3. ✅ Persistence mechanism detection
4. ✅ Authentication log review
5. ✅ Temporary file system inspection

**Final Assessment:** No indicators of compromise (IOCs) detected. System is secure and uncompromised.

**Evidence:**
- Clean process list
- No malicious network activity
- No unauthorized persistence
- No authentication anomalies
- No staging artifacts

**Conclusion:** System assessed as SECURE. No further investigation required.

## Key Learnings (Day 8)

1. **Process investigation requires context** — What process? Who owns it? What spawned it?
2. **Network monitoring catches C2** — lsof -i reveals persistent connections
3. **Persistence lives in cron + systemd** — Always check both
4. **Auth logs tell the story** — Timeline is critical for attribution
5. **Temporary directories = staging ground** — Attackers leave artifacts in /tmp and /dev/shm
6. **Clean system shows NO red flags** — Absence of evidence is evidence of absence (in this case)

## Investigation Time
Total duration: 54 minutes
Stages completed: 5/5
Result: SECURE
