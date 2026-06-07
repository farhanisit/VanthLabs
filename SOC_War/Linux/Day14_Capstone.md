# Linux Day 14 — Capstone Investigation

## Evidence Package
Host: WKSTN-04 | User: CORP\mlopez | Date: 2026-06-06
Three sources: auth.log, tcpdump, Sysmon

## Unified Timeline

06:41:12–16  auth.log   Brute force SSH from 45.33.32.156
                         5 failed attempts, sequential source ports
                         Stage: Initial Access (attempted)

06:41:17     auth.log   Accepted password — SSH session opened
                         Repeated failures then success = weak/valid creds
                         Stage: Initial Access (achieved)

06:41:18–19  pcap       SSH data exchange — payload delivered
                         Stage: Execution (delivery over SSH)

06:41:19     Sysmon     sshd.exe → cmd.exe → encoded PowerShell
             EID 1      Wrong parent + Base64-encoded command
                         Stage: Execution

06:41:20     Sysmon     cmd.exe → powershell.exe, encoded command
             EID 1      Shell established, execution deepening
                         Stage: Execution

06:41:21     Sysmon     powershell.exe → net.exe
             EID 1      net user /domain — AD enumeration
                         Stage: Discovery

06:41:22     Sysmon     PowerShell sets IFEO registry key on svchost.exe
             EID 13     Process execution hijack — survives reboots
                         Stage: Persistence

06:41:22     pcap       192.168.1.14:4444 → 45.33.32.156:9001
                         Victim PowerShell phoning home
                         Repeated 512-byte payloads
                         Stage: C2

06:41:28     Sysmon     powershell.exe → 45.33.32.156:9001
             EID 3      C2 confirmed — same attacker IP
                         Stage: C2

Total elapsed: 16 seconds. Fully automated and scripted.

## Full Attack Chain
Initial Access (brute force SSH)
→ Execution (encoded PowerShell via sshd→cmd)
→ Discovery (net user /domain)
→ Persistence (IFEO registry hijack on svchost.exe)
→ C2 (reverse shell, victim phones home 4444→9001)

## 5-Layer Classification
Pattern:  Brute-force SSH success → encoded PowerShell via
          sshd→cmd → domain discovery → IFEO persistence on
          svchost.exe → reverse shell C2 to 45.33.32.156:9001.
          Full chain in 16 seconds, fully automated.

Type:     Scripted post-exploitation via SSH brute force.
          LOLBin abuse (cmd, PowerShell, net).
          IFEO hijack for persistent execution.

Stage:    Initial Access → Execution → Discovery
          → Persistence → C2

Severity: CRITICAL. Active C2 open. Persistence survives reboot.
          Domain recon complete. Lateral movement and exfil imminent.

Action:   Image WKSTN-04 before any intervention (imaging IS
          preservation). Isolate host. Escalate to L2/L3
          immediately. Do NOT kill C2 unilaterally — L2/L3
          determines containment timing.

## L2 Escalation Brief
Brute-force SSH from 45.33.32.156 against mlopez succeeded on
6th attempt at 06:41:17. Automated post-exploitation followed
immediately: encoded PowerShell via sshd→cmd, domain discovery,
IFEO persistence planted on svchost.exe (EID 13), reverse shell
C2 confirmed outbound to 45.33.32.156:9001. Full chain in 16 seconds.

Active C2 channel open. Persistence survives reboot. Lateral
movement and exfiltration risk is immediate.

Image WKSTN-04 before any intervention. Recommend host isolation.
L2/L3 to determine containment timing on live C2 channel.

## Key Corrections Noted (self-audit)
- Incrementing source ports = ephemeral ports, not port scanning
- -enc flag = Base64 encoding specifically, not base32/64
- pcap port 4444 outbound = C2 channel opening, not confirmed exfil
- EID 13 IFEO = process execution hijack, not DLL plant
- EID 3 direction = victim phoning attacker, not attacker to victim
