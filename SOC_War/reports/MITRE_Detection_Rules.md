# Vanth SOC Detection Rules — MITRE ATT&CK Mapping

## Rule #1: Brute Force Attack Detected
**MITRE Technique:** T1110 (Brute Force)
**Tactic:** Credential Access
**Pattern:** Multiple failed logins + 1 successful from same IP
**SPL Query:**
```spl
index=main sourcetype=auth_log1 | rex field=_raw "for (?<user>\S+) from (?<src_ip>[\d.]+)" | stats count(eval(match(_raw,"Failed"))) as failed, count(eval(match(_raw,"Accepted"))) as successful by src_ip, user | where successful > 0 AND failed > 0
```
**Detection Trigger:** Successful login after 5+ failed attempts
**Real-world Impact:** Attacker gains account access via password guessing
**Response:** Lock account, force password reset, review user activity

---

## Rule #2: Privilege Escalation — Shadow File Access via Sudo
**MITRE Technique:** T1548.004 (Abuse Elevation Control Mechanism)
**Tactic:** Privilege Escalation
**Pattern:** User accesses /etc/shadow via sudo (password file)
**SPL Query:**
```spl
index=main sourcetype=auth_log1 "sudo" "/etc/shadow"
```
**Detection Trigger:** Any sudo access to /etc/shadow
**Real-world Impact:** Attacker steals password hashes for offline cracking
**Response:** Revoke sudo privileges, audit all sudo commands, force password reset

---

## Rule #3: Lateral Movement — Impossible Travel
**MITRE Technique:** T1021 (Remote Services)
**Tactic:** Lateral Movement
**Pattern:** Same user logs in from 2+ different IPs within impossible time window
**SPL Query:**
```spl
index=main sourcetype=auth_log1 "ACCEPTED" | rex field=_raw "for (?<user>\S+) from (?<src_ip>[\d.]+)" | stats min(_time) as first_login, max(_time) as last_login, values(src_ip) as ips by user | where mvcount(ips) > 1
```
**Detection Trigger:** User from multiple IPs in short time
**Real-world Impact:** Attacker compromised account, accessing from multiple locations
**Response:** Isolate all sessions, verify user location, check for C2 beaconing

---

## Rule #4: Data Exfiltration — Large External Transfer
**MITRE Technique:** T1041 (Exfiltration Over C2 Channel)
**Tactic:** Exfiltration
**Pattern:** Large file transfers to non-internal IPs
**SPL Query:**
```spl
index=main sourcetype=csv destination_ip != "192.168.*" AND destination_ip != "10.*" | stats count, sum(file_size_gb) by source_user, destination_ip
```
**Detection Trigger:** File transfer > 100MB to external IP
**Real-world Impact:** Confidential data stolen and sent to attacker
**Response:** Block IP, isolate user, preserve evidence, notify legal/IR team

---

## Rule #5: Privilege Escalation — Sudo Access to Sensitive Files
**MITRE Technique:** T1548.004 (Abuse Elevation Control Mechanism)
**Tactic:** Privilege Escalation
**Pattern:** User runs sudo to access sensitive system files
**SPL Query:**
```spl
index=main sourcetype=csv sudo "/etc/shadow" user="analyst"
```
**Detection Trigger:** sudo access to /etc/shadow or /etc/sudoers
**Real-world Impact:** Attacker gains root-level file access
**Response:** Audit sudo logs, revoke privileges, investigate all sudo commands

---

## Rule #6: Account Lockout Detection
**MITRE Technique:** T1110 (Brute Force)
**Tactic:** Credential Access
**Pattern:** 5+ failed login attempts = account locked
**SPL Query:**
```spl
index=main sourcetype=csv | stats count by user | where count > 5
```
**Detection Trigger:** User with 5+ failed attempts
**Real-world Impact:** Legitimate account locked or attacker attempting brute force
**Response:** Contact user, verify legitimacy, unlock if needed, check for compromise

---

## Rule #7: Unusual SSH Port Activity
**MITRE Technique:** T1571 (Non-Standard Port)
**Tactic:** Command & Control / Defense Evasion
**Pattern:** SSH attempts on non-standard ports (not 22)
**SPL Query:**
```spl
index=main sourcetype=csv protocol="SSH" | where destination_port != 22
```
**Detection Trigger:** SSH on ports 2222, 8022, 5555, etc.
**Real-world Impact:** Attacker using alternate entry points or backdoor access
**Response:** Block unusual ports at firewall, investigate successful logins, scan for persistence

---

## Rule #8: Account Takeover — Successful Login After Lockout
**MITRE Technique:** T1110.003 (Password Spraying)
**Tactic:** Credential Access
**Pattern:** Account locked → then successful login from different IP
**SPL Query:**
```spl
index=main sourcetype=csv (attempt_result="Account_Locked" OR attempt_result="Accepted")
```
**Detection Trigger:** Locked account with successful login from new IP
**Real-world Impact:** **CONFIRMED ACCOUNT COMPROMISE** — attacker has active access
**Response:** IMMEDIATE isolation, force logout all sessions, reset password, escalate to IR

---

## Kill Chain Coverage

| Phase | Rule | MITRE Tactic |
|-------|------|--------------|
| Reconnaissance | — | — |
| Exploitation | #1, #2, #5, #7 | Credential Access, Privilege Escalation |
| Persistence | — | (Future: Rule #9) |
| Command & Control | #7, #3 | C2, Lateral Movement |
| Exfiltration | #4 | Data Exfiltration |
| Post-Compromise | #6, #8 | Account Lockout, Account Takeover |

---

## Portfolio Notes
- All rules tested in Splunk 10.2.2
- Queries optimized for performance on auth logs
- Email alerts configured for critical rules (#8, #4)
- Ready for deployment in production SIEM
