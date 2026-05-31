# SOC Deep Revision 01 — Meridian Logistics Case (Lessons 7-14 integrated)

## Purpose
Single live case run end-to-end to prove Lessons 7-14 are one workflow,
not eight separate topics. Fresh scenario (stolen-credential account takeover).

## The Case
Account m.reyes flagged by impossible-travel:
- 08:55 logon from Mumbai (198.51.100.20) -> CONFIRMED corporate VPN = the REAL user
- 09:08 logon from Lagos (203.0.113.40)   -> unsanctioned, no travel on record

Lagos session telemetry:
  09:08 | 4624 Type 10 (RDP) | m.reyes | first-try success, NO failures
  09:09 | 4625 x6 | spray vs m.reyes/admin/svc_sql/root/administrator/backup (FAILED)
  09:14 | 4624 Type 3 | m.reyes -> FILE-02 (10.0.0.52)  (lateral movement, succeeded)
  09:15 | 4663 | m.reyes accessed \\FILE-02\HR\salaries\

## Workflow Walked
- L8 (TP/FP): impossible travel = HIGH false-positive pattern (VPN/proxy egress).
  Verdict starts INCONCLUSIVE until egress resolved. Don't jump to "compromised."
- Egress check: Mumbai = benign VPN; Lagos = hostile. Split the two sessions.
- L8 on Lagos session: CONFIRMED malicious. Pinpoint = 09:09 privileged spray
  (no benign twin for a user spraying root/admin).
- L10 (correlation): impossible travel was the ONLY thing that caught a
  credentialed login that otherwise looked perfect.
- Attack type: CREDENTIAL THEFT (stolen creds), NOT brute/dictionary.
  Tell: failures present = guessing; FIRST-TRY success = stolen credentials.
- Key pattern: privilege escalation FAILED, but breach SUCCEEDED via the
  account's OWN existing access (lateral move to FILE-02).

## L11 Containment (in order)
0. PRESERVE evidence first (step zero, non-negotiable) — capture session + logs
   before altering state, or forensics is contaminated.
1. Block 203.0.113.40 at perimeter (reversible, breaks nothing legitimate).
2. Disable m.reyes + force password reset — credential is burned; brief
   inconvenience to the real user is ACCEPTABLE after a confirmed takeover.
3. DO NOT eradicate/clean FILE-02 (above L1 + destroys evidence).
4. Escalate to L2 with facts.

## L13 Brief (proof vs impact, flat)
Confirmed account takeover via stolen creds (high confidence). First-try Lagos
logon while real user on Mumbai VPN; surfaced by impossible-travel correlation.
PROOF: first-try credentialed logon + failed priv-esc spray (09:09).
IMPACT: lateral move to FILE-02 (09:14) via own access; HR salary data accessed (09:15).
CONTAINMENT: evidence preserved; IP blocked; account disabled + reset.
ASK L2: scope HR exposure, check for other compromised accounts, find theft vector.

## Reflexes Locked
1. Impossible travel != compromise. It's a prompt to check egress.
2. Walk all four L8 layers to EARN the verdict, don't land on it by feel.
3. Failures present = guessing; first-try success = stolen credentials.
4. Escalation can FAIL while the breach SUCCEEDS via existing access.
5. Containment step zero = preserve. Always.
6. Proof line and impact line are separate findings.
7. Don't confirm + suspicious in the same breath; once confirmed, it's confirmed.
