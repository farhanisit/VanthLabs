# Security+ SY0-701 — Day 006 Consolidation
## Lessons 026–028

---

## Cold Recall Audit — Repairs

| Wrong | Correct |
|---|---|
| 22 = FTP | 21 = FTP, 22 = SSH/SFTP |
| Encoding = "guising with random Base64" | Encoding = reformatting data, not real security |
| Hesitated on internal SMB vs external RDP risk | External RDP = higher concern |

---

## Lesson 026: Email Protocols

**Core idea:** Three protocols, three jobs.

| Protocol | Job | Port |
|---|---|---|
| SMTP | Sends email | 25 |
| POP3 | Downloads email | 110 (secure: 995) |
| IMAP | Syncs email across devices | 143 (secure: 993) |

**Final memory line:** SMTP sends. POP3 downloads. IMAP syncs.

---

## Lesson 027: SMB and RDP

**Core idea:** Know the port, know the risk.

| Protocol | Job | Port | SOC note |
|---|---|---|---|
| SMB | Windows file sharing | 445 | Internal traffic may be normal |
| RDP | Remote desktop access | 3389 | External exposure = high risk |

**SOC distinction:**
- Internal workstation to file server port 445 = possibly normal
- External host to internal server port 3389 = suspicious, commonly attacked

**Attack context for RDP:** Brute force, credential attacks, initial access, ransomware entry.

**Final memory line:** 445 internal can be normal. 3389 exposed externally is risky.

---

## Lesson 028: DNS Security Issues

**Core idea:** DNS can be abused, not just used.

| Abuse type | What happens |
|---|---|
| DNS poisoning/spoofing | Domain resolves to attacker-controlled IP |
| DNS tunneling | Hidden data inside DNS queries/responses |
| Malware/C2 lookup | Infected host queries domain to find command-and-control server |

**Critical SOC distinction:**
- DNS query = name resolution attempt only
- Does NOT confirm successful connection
- To confirm: check DNS response + connection logs + destination IP + process + domain reputation + timing

**Exam question:** Many DNS queries to long random subdomains under same suspicious domain = DNS tunneling

**Final memory line:** DNS query = tried to resolve. Connection logs = actually connected.

---

## Three Things to Remember Tomorrow

1. 21 = FTP, 22 = SSH/SFTP
2. SMTP sends, POP3 downloads, IMAP syncs
3. DNS query = resolution attempt only; connection logs prove actual connection

---

## Day 006 Scores

| Item | Score |
|---|---|
| Cold Recall Audit | Passed with minor repairs |
| Lesson 026 | 3/3 |
| Lesson 027 | 3/3 |
| Lesson 028 | 3/3 |
| Total | 9/9 |

---

## Next Session

Cold recall audit first — non-negotiable
029: Threat Actors and Motivations
