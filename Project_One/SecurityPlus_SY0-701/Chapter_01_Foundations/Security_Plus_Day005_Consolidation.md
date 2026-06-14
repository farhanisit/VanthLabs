# Security+ SY0-701 — Day 005 Consolidation
## Lessons 021–025

---

## Lesson 021: Certificate Problems

**Core idea:** Certificate problem = browser cannot fully trust or validate the certificate.

| Problem | Meaning |
|---|---|
| Expired | Validity date has passed |
| Revoked | Cancelled before expiry |
| Self-signed | Not issued by trusted CA |
| Name mismatch | Cert name does not match domain |
| Untrusted CA | Issuer not trusted by browser/system |

**Exam trap:** Self-signed certs are not always malicious — used in labs/internal systems. HTTPS does not mean the website is safe.

**Final memory line:** Certificate problem = browser cannot fully trust the site's digital ID.

---

## Lesson 022: Secure Protocols Intro

**Core idea:** Secure protocols protect data in transit.

| Insecure | Secure |
|---|---|
| HTTP | HTTPS |
| FTP | SFTP / FTPS |
| Telnet | SSH |
| LDAP | LDAPS |
| SNMPv1/v2 | SNMPv3 |

**Final memory line:** Secure protocols protect data in transit.

---

## Lesson 023: TLS / HTTPS

**Core idea:** HTTPS = HTTP + TLS

| Term | Meaning |
|---|---|
| HTTP | Web traffic, no encryption, port 80 |
| HTTPS | Secure web traffic, port 443 |
| TLS | Protects data in transit |

**TLS provides:** Confidentiality + Integrity + Authentication

**Major exam trap:** HTTPS means the connection is encrypted and certificate was accepted. A phishing site can still use HTTPS.

**Final memory line:** HTTPS = HTTP + TLS.

---

## Lesson 024: Common Ports and Protocols

**Core idea:** Ports tell you what service is probably running.

| Port | Protocol |
|---|---|
| 21 | FTP |
| 22 | SSH / SFTP |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

**SOC angles:**
- External IP → port 3389 = RDP exposure
- Many failed logins port 22 = SSH brute force
- Port 445 across internal machines = SMB / lateral movement

**Final memory line:** Ports tell you what service is probably running.

---

## Lesson 025: DNS Basics

**Core idea:** DNS = internet phonebook.

| Record | Meaning |
|---|---|
| A | Domain to IPv4 |
| AAAA | Domain to IPv6 |
| MX | Mail server for domain |
| CNAME | Alias to another domain |

**Port:** 53

**Exam pattern:** Can reach IP but not domain name = DNS issue.

**SOC angle:** DNS queries to suspicious domains may indicate malware/C2. Not every DNS query is malicious.

**Final memory line:** DNS = internet phonebook.

---

## Mixed Review — Lessons 001–025

**Score: 7/7**

| Question topic | Answer |
|---|---|
| Logged in but access denied | Authorization |
| Salt + hash comparison | Password verification without plaintext |
| Vendor update authenticity + integrity | Digital signature |
| Port 3389 | RDP |
| HTTPS phishing site | Encrypted connection, still malicious |
| Unapproved firewall change | Change management failure |
| Internet-facing database | Exposure |
| Serious legal/patient-care damage | Impact |

---

## Day 005 Scores

| Lesson | Score |
|---|---|
| 021 | 3/3 |
| 022 | 3/3 |
| 023 | 3/3 |
| 024 | 3/3 |
| 025 | 3/3 |
| Mixed Review | 7/7 |
| **Total** | **22/22** |

---

## Next Session
026: Email Protocols — SMTP, POP3, IMAP

027: SMB and RDP from a Security Perspective

028: DNS Security Issues Intro
