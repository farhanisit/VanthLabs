# Day 5 — Sudo Deep Dive and Escalation Detection

## What is Sudo?

Sudo = "Super User Do"
- Allows regular users to run commands as root
- Requires authentication (password or key)
- All attempts logged to /var/log/auth.log
- Every sudo attempt is a potential escalation indicator

## Sudo vs Root Access

Sudo:
- Temporary, specific commands only
- Fully logged in auth.log
- High traceability (user + command visible)
- Easy to detect

Root:
- Permanent, unrestricted access
- Partially logged
- Low traceability (harder to trace)
- Hard to detect

## Successful Sudo Execution

Log entry shows: user, TTY, working directory, target user, command executed
Session opens as root, executes command, then closes session
All timestamps recorded

## Failed Sudo Attempts

Log shows: "unknown user" or "permission denied" or "not in sudoers"
No COMMAND field (command never executed)
Still logged for detection

## SOC Detection Strategy

Red Flags:
- Sudo to access /etc/shadow (steal password hashes)
- Sudo to modify /etc/sudoers (grant persistent access)
- Sudo to create new users (backdoor creation)
- Failed attempts followed by successful escalation

Normal Activity:
- Admins using sudo regularly
- Service accounts with sudo for specific tasks
- Scheduled sudo in cron jobs

## The Escalation Chain

1. Initial access (user compromised)
2. Check sudo access: sudo -l
3. Escalate via sudo if allowed
4. Achieve root access
5. Hide tracks or establish persistence

## Key Learning

Sudo is the bridge between user and root.
Detecting sudo misuse = detecting escalation BEFORE root is achieved.
Post-root, detection becomes forensics, not prevention.
