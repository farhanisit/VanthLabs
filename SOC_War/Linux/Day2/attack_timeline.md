# Day 2 Part 2 — Attack Timeline and Privilege Analysis

## Attack Sequence (From auth.log)

1. **Brute Force Phase:** 17 failed attempts on analyst account
2. **Compromise:** Successful login as analyst (08:20:13)
3. **Privilege Check:** No sudo access available
4. **Outcome:** Attacker confined to analyst privileges

## Key Finding
- analyst account: NO sudo access
- Attacker could NOT escalate to root
- Persistence must be established as analyst-level user
- Next threat: SSH keys, cron jobs, hidden processes

## SOC Detection Points
- auth.log: Caught brute force + successful login
- sudoers check: Confirmed no escalation path
- Next step: Check for persistence mechanisms as analyst
