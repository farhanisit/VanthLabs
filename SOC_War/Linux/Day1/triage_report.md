# Day 1 — SSH Brute Force Triage

## Attack Summary
- Source IP: 203.8.113.45
- Window: 08:16:12 – 08:21:26 (5m 14s)
- Failed attempts: 17
- Ports used: 5
- Compromised account: analyst

## Commands Used
- grep "Failed password" auth.log | wc -l
- grep "Failed password" auth.log | awk '{print $9}' | sort | uniq -c | sort -rn
- grep "Failed password" auth.log | awk '{print $1,$2,$3}' | head -1 && tail -1

## Key Finding
Automated SSH brute force. Username enumeration followed by password spray.
Analyst account compromised after 5 failed attempts.
