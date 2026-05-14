# Rule #10 — C2 Beaconing Detection (T1001, T1071)

## Threat Summary
Detects active Command & Control (C2) communication when a compromised system regularly "calls home" to attacker's server to receive commands and exfiltrate data.

## Detection Logic
Pattern: Multiple connections from same internal IP to same external IP at regular intervals (≤10 minutes apart, ≥10 connections over 60+ minutes).

## SPL Query
index=main
| stats count, latest(_time) as latest_time, earliest(_time) as earliest_time by src_ip, dest_ip
| where count >= 10
| eval duration=latest_time-earliest_time
| eval interval=duration/count
| where interval < 600

## Alert Configuration
- **Trigger:** Number of Results > 10
- **Schedule:** Hourly
- **Action:** Send email alert
- **Severity:** Critical

## MITRE ATT&CK Mapping
- **T1001** - Obfuscated Files or Information
- **T1071** - Application Layer Protocol
- **T1041** - Exfiltration Over C2 Channel

## Indicators of Compromise
- Same src_ip and dest_ip across multiple events
- Consistent time intervals (~5 minutes)
- Sustained activity (60+ minutes)
- External destination IP

## False Positive Considerations
- Legitimate polling services
- Cloud sync services
- VPN reconnection attempts

## Response Actions
1. Block dest_ip at firewall immediately
2. Isolate src_ip system from network
3. Investigate data exfiltration
4. Capture network traffic
5. Check for other C2 patterns

## Test Data
13 events: 192.168.1.100 → 203.0.113.50 every 5 minutes.
