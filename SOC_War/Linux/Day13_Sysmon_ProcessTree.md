
# Linux Day 13 — Sysmon & Process-Tree Hunting



## Core Idea

Logs tell you WHAT happened. Process trees tell you HOW.

A process doesn't just exist — it was spawned by something.

That parent-child relationship is the attack story written

in the OS itself.



## Why Sysmon

Windows native logs (EID 4688) give process creation but

miss detail. Sysmon adds:

- ParentImage  (what spawned it)

- CommandLine  (full command with arguments)

- Hashes       (file integrity)

- Network connections per process

Difference: "cmd.exe ran" vs "Word spawned PowerShell

which downloaded a payload."



## Key Sysmon EIDs

EID 1  — Process Create (ParentImage, CommandLine, Hashes)

EID 3  — Network Connection (process making outbound connection)

EID 11 — File Create

EID 13 — Registry value set (persistence)

EID 22 — DNS Query (which process asked for what domain)



## The Hunt Question

"Does this parent make sense for this child?"

If no → investigate. That's the entire Sysmon hunting reflex.



## Malicious Parent-Child Pairs

winword.exe    → powershell.exe     SUSPICIOUS

excel.exe      → cmd.exe            SUSPICIOUS

outlook.exe    → wscript.exe        SUSPICIOUS

mshta.exe      → powershell.exe     SUSPICIOUS (LOLBin)

cmd.exe        → whoami.exe         POST-EXPLOITATION

cmd.exe        → net.exe            DISCOVERY



## Legitimate Pairs (baseline)

explorer.exe   → chrome.exe         NORMAL

services.exe   → svchost.exe        NORMAL

wininit.exe    → lsass.exe          NORMAL

(lsass spawned by anything else = CRITICAL)



## LOLBins

Attackers abuse Windows' own binaries to avoid dropping tools:

powershell.exe, cmd.exe, mshta.exe, wscript.exe,

certutil.exe, regsvr32.exe

Detection = wrong parent + suspicious CommandLine args.



## Live Investigation — jsmith Chain

Five Sysmon events, 19 seconds, one user account (CORP\jsmith).



EID 1  [08:14:22]  WINWORD.EXE → powershell.exe

                   CommandLine: -nop -w hidden -enc JABj...

                   Wrong parent + Base64-encoded payload

                   = Initial Access (malicious macro) → Execution



EID 3  [08:14:23]  powershell.exe → 185.220.101.47:4444

                   Known-bad IP (185.220.101.x = C2 range)

                   Port 4444 = classic Metasploit reverse shell

                   = C2 established. Attacker has live access.



EID 1  [08:14:31]  powershell.exe → cmd.exe

                   whoami && net user && ipconfig

                   = Discovery (host fingerprinting)



EID 1  [08:14:35]  cmd.exe → net.exe

                   net user /domain

                   = Discovery (domain/AD enumeration)



EID 22 [08:14:41]  powershell.exe DNS query

                   fileserver01.corp.local

                   = Lateral Movement (next target identified)



NOTE: No persistence event (EID 13/11) present in this chain.

Do not import stages not evidenced in the logs.



19-second span = scripted/automated behaviour, not manual typing.



## 5-Layer Classification

Pattern:  Malicious Office macro → encoded PowerShell →

          reverse shell to 185.220.101.47:4444 → automated

          host/domain discovery → fileserver targeting.

          Full post-exploitation chain, one account, 19 seconds.



Type:     Scripted post-exploitation. Likely Metasploit or

          pre-built payload via phishing doc. LOLBin abuse

          (PowerShell, cmd, net).



Stage:    Initial Access → Execution → C2 → Discovery

          → Lateral Movement (preparation)



Severity: CRITICAL. Active reverse shell = live attacker access.

          Domain recon complete. Fileserver01 targeted.

          Clock is running.



Action:   Document all five events in full detail. Preserve

          (imaging IS preservation — before anything else).

          Recommend isolation of jsmith's workstation.

          Escalate to L2/L3 immediately. Do NOT kill the C2

          channel or block the IP unilaterally — L2/L3 decides

          containment timing. They may watch the live channel

          to scope the full compromise before cutting.



## Intelligence Argument — Why L2 May Keep C2 Open

Killing immediately: attacker loses access, but you lose

visibility. Attacker burns infrastructure, rebuilds elsewhere.

Monitoring: watch commands in real time, identify other

compromised hosts on same channel, log full C2 infrastructure,

close on your terms. Every second is a trade-off — L2/L3

owns that decision, never L1.

