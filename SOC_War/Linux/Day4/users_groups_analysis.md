# Day 4 — Users, Groups, and Privilege Investigation

## Core Concepts

**User:** Individual account (person or service)
**Group:** Collection of users with shared permissions
**Primary Group:** User's default group (same name as user)
**Secondary Groups:** Additional groups user belongs to

## Dangerous Groups (SOC Priority)

| Group | Danger Level | Why |
|-------|--------------|-----|
| sudo | CRITICAL | Can run commands as root |
| adm | HIGH | Can read system logs (cover tracks) |
| dip | MEDIUM | Can configure network interfaces |
| lxd | MEDIUM | Container escape = privilege escalation |
| wheel | CRITICAL | Alternative sudo group (some systems) |

## Case Study: sysbackup Account

### Investigation Results
- **Groups:** sysbackup only (no sudo, adm, dip, lxd)
- **Cron jobs:** None found
- **Login history:** None in auth.log
- **Creation date:** Apr 3 (13 days post-install)
- **Shell:** /bin/bash (real login capable)

### Assessment
- Account exists but is completely inactive
- No privilege escalation capability
- No scheduled tasks
- **Suspicious:** Ghost account (exists but unused)
- **Possibility:** Dormant attacker persistence account OR legitimate unused service

### SOC Detection Strategy
Monitor for ANY activity (login, cron execution, group membership change).
Sudden activation = immediate escalation.

## Key Learning
Groups enable **privilege delegation at scale**. Attackers targeting group memberships get exponential access.
