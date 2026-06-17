# Security+ SY0-701 — Day 007 Consolidation (Recovery Day)
## Lessons 029–031

---

## Cold Recall Audit — Repair

| Wrong | Correct |
|---|---|
| DNS query proves successful connection | DNS query = lookup/intent only; connection log = actual contact; process log = what caused it |

All other recall items passed clean: 21=FTP, 22=SSH, 25=SMTP, 53=DNS, 445=SMB, 3389=RDP, SMTP/POP3/IMAP roles, DNS tunneling, encrypt/hash/encode, HTTPS limits.

---

## Lesson 029: Threat Actors and Motivations

**Core idea:** Threat actor = who attacks. Motivation = why they attack.

| Threat actor | Motivation/trait |
|---|---|
| Nation-state | Espionage, long-term, high resources |
| Organized crime | Financial gain |
| Hacktivist | Ideology, political/social cause |
| Insider threat | Trusted access misused |
| Competitor | Business advantage |
| Script kiddie | Low skill, public tools |
| Shadow IT | Unauthorized employee tools |
| Terrorist | Fear, disruption, ideological violence |

**Final memory line:** Money = organized crime. Cause = hacktivist. Espionage = nation-state.

---

## Lesson 030: Malware Types I

**Core idea:** Malware type = behavior of the malicious software.

| Type | Behavior |
|---|---|
| Virus | Attaches to files/programs, spreads when executed |
| Worm | Self-replicates across networks, no user action needed |
| Trojan | Pretends to be legitimate, hides malicious behavior |
| Ransomware | Encrypts/locks data, demands payment |

**Final memory line:** Virus attaches. Worm spreads itself. Trojan pretends. Ransomware locks and demands payment.

**Noted for later:** Spyware, Keylogger, Rootkit, Logic bomb, Backdoor, Bot/Botnet, Cryptominer, Fileless malware, Adware.

---

## Lesson 031: Malware Types II

**Core idea:** Identified by what they do.

| Type | Behavior |
|---|---|
| Spyware | Secretly monitors activity / collects info |
| Keylogger | Records keystrokes |
| Rootkit | Hides malware, maintains stealthy privileged access |
| Logic bomb | Activates when a specific condition is met |

**Final memory line:** Spyware watches. Keylogger records typing. Rootkit hides. Logic bomb waits for a trigger.

---

## The Bigger Chain (New Connection Today)
Threat actor → motivation → attack method/malware → impact/risk

Example: Organized crime → financial gain → ransomware → hospital outage/data loss

**SOC log tells:**
- One host scanning many internal systems → possible worm
- Many files rapidly encrypted/renamed → possible ransomware
- Fake installer spawning suspicious process → possible Trojan
- Keystroke capture behavior → possible keylogger
- Hidden process/privileged stealth → possible rootkit
- Condition-based deletion → possible logic bomb

---

## Three Things to Remember Tomorrow

1. DNS query = lookup/intent; connection log = actual contact
2. Threat actor = who attacks; motivation = why they attack
3. Virus attaches, worm spreads, Trojan pretends, ransomware locks

Bonus: Spyware watches, keylogger records typing, rootkit hides, logic bomb waits for a trigger.

---

## Recovery Day Note

Health was off today; session still completed three lessons. Repair principle: on recovery days, one clean lesson or consolidation is enough — three is not the expectation going forward.

---

## Day 007 Scores

| Item | Score |
|---|---|
| Cold Recall Audit | Passed with repair |
| Lesson 029 | 3/3 |
| Lesson 030 | 3/3 |
| Lesson 031 | 3/3 |
| Total | 9/9 |

---

## Next Session

Cold recall audit first — non-negotiable
032: Malware Types III — Backdoor, Botnet, Cryptominer, Fileless Malware
