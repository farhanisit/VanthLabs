# Linux Part 2 — Day 24: Capstone Investigation

## Evidence Package
Host: PROD-LX-07 | User: sysadmin | Date: 2026-07-05
Three sources: auth.log, tcpdump, Sysmon

## Unified Timeline

02:14:33-36  auth.log   4 failed SSH attempts in 4 seconds
                         Automated brute force — sequential ports
                         Stage: Initial Access (attempted)

02:14:37     auth.log   Accepted password for sysadmin
                         5th attempt success = automated tool
                         Stage: Initial Access (achieved)

02:14:37-38  pcap       SSH data exchange — payload delivered
                         Stage: Execution

02:14:38     Sysmon     sshd.exe → cmd.exe (wrong parent)
             EID 1      whoami && net user && ipconfig
                         Stage: Discovery (host)

02:14:45     Sysmon     cmd.exe → net.exe
             EID 1      net user /domain — AD enumeration
                         Stage: Discovery (domain)

02:14:52     auth.log   sudo /bin/bash — ROOT SHELL obtained
                         Full system ownership
                         Stage: Privilege Escalation

02:14:52     pcap       10.0.0.15:4444 → 91.92.251.103:9001
                         Victim calls out — reverse shell
                         Stage: C2

02:14:52     Sysmon     cmd.exe → 91.92.251.103:9001
             EID 3      Confirms C2 — same channel as pcap

02:14:55     Sysmon     cmd.exe creates C:\Windows\Temp\svch0st.exe
             EID 11     Disguised binary (zero not 'o') dropped
                         Stage: Persistence (setup)

02:14:58     Sysmon     svch0st.exe sets Run registry key
             EID 13     HKLM\...\Run\WindowsUpdate — survives reboot
                         Named to blend in with legitimate updates
                         Stage: Persistence (locked)

02:15:01     auth.log   SSH disconnect — attacker left
                         C2 and persistence remain active

Total elapsed: 28 seconds. Fully automated.

## Full Attack Chain
Initial Access (brute force SSH) → Execution →
Discovery (host + domain) → C2 (reverse shell) →
Privilege Escalation (sudo root shell) →
Persistence (dropped binary + Run registry key)

## 5-Layer Classification
Pattern:  Automated SSH brute force → password success →
          sshd→cmd wrong parent → domain recon → reverse
          shell C2 4444→9001 → root shell → svch0st.exe
          dropped → Run registry persistence. 28 seconds.

Type:     Automated credential attack with post-exploitation
          toolkit. LOLBin abuse (cmd, net). Registry Run key
          persistence. Disguised payload (svch0st.exe).

Stage:    Initial Access → Execution → Discovery →
          C2 → Privilege Escalation → Persistence

Severity: CRITICAL. Root shell obtained. C2 active after
          SSH disconnect. Persistence survives reboot.
          sysadmin account compromised, domain recon complete.

Action:   PRESERVE FIRST (image before anything else).
          Document all events. Recommend isolating PROD-LX-07.
          Escalate to L2/L3 immediately. Do NOT kill C2
          unilaterally. Flag svch0st.exe hash for TI lookup.

## L2 Escalation Brief
Automated SSH brute force against sysadmin on PROD-LX-07
succeeded on 5th attempt at 02:14:37. Root shell obtained
via sudo /bin/bash. Reverse shell C2 active on 4444→9001.
Disguised binary svch0st.exe dropped and set to run at
startup via registry Run key. Full chain in 28 seconds.

C2 remains active post-disconnect. Persistence survives
reboot. Domain recon complete, blast radius unknown.

Image PROD-LX-07 before intervention. Recommend isolation.
L2/L3 to determine C2 containment timing.

## Part 2 Tools That Would Catch This
ss -tnp             spot active C2 (4444→9001, cmd.exe owner)
journalctl -u ssh   surface brute force + success sequence
find /tmp -mtime -1 catch recently dropped files
sha256sum           hash svch0st.exe, compare against TI feed
login_detector.py   automated brute-force-then-success detection
awk + sort + uniq   surface offending IP with failure count
