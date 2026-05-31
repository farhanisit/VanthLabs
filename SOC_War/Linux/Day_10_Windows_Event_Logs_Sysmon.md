# Linux Day 10 — Windows Event Logs & Sysmon

## Core Idea
On Linux you read auth.log, syslog, cron (plain text).
On Windows, telemetry lives in EVENT LOGS — structured and ID-numbered.
Same skeleton as Linux logging, different skin.

## Two Sources of Windows Telemetry

1. Native Windows Event Logs (built in, always on)
   - Channels: Security, System, Application
   - Numeric Event IDs (4624, 4625, 7045 ...)
   - Limited: weak parent-child, often no command line, no hashes.

2. Sysmon (Sysinternals, installed separately, configurable)
   - Own channel: Microsoft-Windows-Sysmon/Operational
   - Rich: command line, file hashes, ParentImage, per-process
     network connections, process GUIDs.
   - = telemetry amplifier.

## KEYSTONE WARNING
Native Event IDs and Sysmon Event IDs are TWO DIFFERENT schemes.
  Native process creation = Event ID 4688 (Security log)
  Sysmon process creation = Event ID 1   (Sysmon log)
Same event, different log, different number. Never mix them.

## Key Native Security Event IDs
  4624  Successful logon
  4625  Failed logon            <- brute force lives here
  4634 / 4647  Logoff
  4663  Object access (a file/object was touched)
  4672  Special privileges assigned (admin-level logon)
  4688  Process creation (native; weaker than Sysmon EID 1)
  4698  Scheduled task created  <- persistence
  4720  User account created    <- persistence / backdoor user
  4732  Member added to a security group  <- privilege change
  7045  Service installed (System log)    <- lateral movement / persistence

## Logon Types (the field that gives 4624/4625 meaning)
  Type 2   Interactive (physical console)
  Type 3   Network (SMB / file share)   <- LATERAL MOVEMENT
  Type 10  RemoteInteractive (RDP)
A logon event means little until you read its TYPE.

## Key Sysmon Event IDs
  1    Process creation (Image, ParentImage, CommandLine, hashes)
  3    Network connection (src/dest IP, dest port)
  11   File created
  12/13 Registry modified

## Internal vs External IP (daily reflex)
  10.x.x.x , 172.16-31.x.x , 192.168.x.x = INTERNAL
  Everything else = EXTERNAL.

---

## Worked Rep — Reading a Chain (suspicious -> confirmed)

Events (one server, one night):
  03:14:02 | 4624 | Type 3 | svc_backup  | from WKSTN-42 (10.0.0.88)
  03:14:47 | 4720 | svc_backup2 created BY svc_backup
  03:15:10 | 4732 | svc_backup2 ADDED to Administrators by svc_backup
  03:15:58 | 4624 | Type 3 | svc_backup2 | from WKSTN-42 (10.0.0.88)
  03:16:30 | 4663 | svc_backup2 accessed \\FILESERVER\Finance\payroll_2026.xlsx

Reading:
- 4624 alone = INCONCLUSIVE (backup acct, internal IP, 3 AM = could be a real job).
- 4720 = SUSPICIOUS (role mismatch: service accounts don't create accounts).
- 4732 = THE PINPOINT. Service account grants its sockpuppet ADMIN.
  No benign twin exists for this. Confirmation of malice happens HERE.
- 4624 (svc_backup2) and 4663 = the attacker USING the access = IMPACT, not proof.

## Two Findings, Not One
- PROOF of malice: 4732 @ 03:15:10 (privilege escalation).
- IMPACT / scope: 4663 @ 03:16:30 (payroll data accessed).
Report them separately — one proves the case, one sizes the damage.
(Same principle as the db-prod-01 incident report.)

Verdict (flat phrasing):
"Confirmed malicious. Privilege escalation confirmed at 4732 (03:15:10);
finance data accessed at 4663 (03:16:30). One internal host, 2.5-minute chain.
Escalate immediately, scope the payroll exposure."

## Key Learnings (Day 10)
1. Windows telemetry = Event IDs in channels; same flow as Linux logs.
2. Native EID != Sysmon EID. Know which log you're reading.
3. A logon (4624/4625) is meaningless until you read the Logon Type. Type 3 = network = lateral movement.
4. ROLE MISMATCH = clean suspicion signal (account acting outside its function).
5. Privilege escalation (e.g. 4732) is usually where SUSPICION becomes CONFIRMATION.
6. "Confirmed" and "suspicious" don't stack. Once confirmed, it's confirmed malicious.
7. Proof and impact are separate findings.
