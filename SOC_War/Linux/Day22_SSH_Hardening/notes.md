# Linux Part 2 — Day 22: SSH Hardening

## Plain English
Default SSH config allows password auth, doesn't limit root
login behavior, and has no rate limiting on failed attempts.
Every scenario investigated this session (Day 9 beacon, the
WKSTN-04 capstone, login_detector.py) exploited exactly this
default, unhardened configuration. Hardening closes that gap.

## Config File
/etc/ssh/sshd_config
Edit: sudo nano /etc/ssh/sshd_config
Apply: sudo systemctl restart ssh

## Changes Made

PermitRootLogin prohibit-password
Root can ONLY log in via SSH key, never password. Chose
prohibit-password over a full "no" deliberately: keeps an
emergency access path open via key while still closing the
actual attack vector (brute-forcing root's password). A full
"no" is simpler but removes emergency access entirely -- valid
for a single-user lab, less realistic for production thinking.

MaxAuthTries 3
Limits failed attempts per CONNECTION before it drops. Doesn't
stop reconnecting and trying again, but slows rapid-fire
brute forcing within one session.

PasswordAuthentication no
Disables password login entirely -- key-based only. This is
the single biggest hardening step: makes the exact brute-force
pattern from login_detector.py (and the WKSTN-04 capstone)
structurally impossible, because there's no password to guess.
Config comment confirmed the real reason: disables tunneled
clear-text passwords over the wire, not just brute force
resistance.

## Why Key-Based Auth Is Structurally Stronger
Password = something you KNOW -- guessable, brute-forceable,
           phishable, reused across sites.
SSH key  = something you HAVE -- private key file, mathematically
           paired with a public key on the server. Effectively
           impossible to brute force given the keyspace size.
           Private key never leaves the local machine.

This matches the Day 19 finding directly: journalctl showed
"Accepted publickey for ubuntu" for the Multipass connection --
already key-based before any hardening was applied today.

## Safety Procedure Followed (critical -- prevents lockout)
1. Verified authorized_keys existed BEFORE disabling password
   auth (ls -la ~/.ssh/ -- confirmed correct permissions, 600)
2. Tested config syntax BEFORE applying:
   sudo sshd -t
   Empty output = valid syntax, safe to restart
3. Kept original session open while testing the change in a
   SEPARATE fresh connection -- if the new config had locked
   access out, the original session would still be alive to
   revert it
4. Verified service status after restart:
   sudo systemctl status ssh
   Confirmed "active (running)" -- noted systemd automatically
   re-ran sshd -t as ExecStartPre before starting the service,
   a built-in safety net independent of the manual test
5. Verified actual access from a genuinely NEW connection
   (multipass shell vanth-lab in a second terminal) -- proved
   the hardening didn't lock out real access, not just that
   the service was technically running

## Key Danger Flagged Before Editing
Disabling PasswordAuthentication WITHOUT first confirming a
working SSH key exists can lock you out of the machine entirely.
This is why step 1 (verifying authorized_keys) happened before
any config edit, not after.

## Deferred to a Future Session
AllowUsers <username> -- whitelist specific usernames, reject
everyone else before reaching a password/key prompt at all.
Deliberately skipped today to test changes incrementally
rather than changing everything at once and risking multiple
hidden failure points together.

## AllowUsers Addition (LNX-025, completed separately)
Added to /etc/ssh/sshd_config:
AllowUsers ubuntu

Whitelist control — only listed usernames may SSH in at all.
Everyone else rejected BEFORE reaching the key/password stage.
Fails closed. Shrinks attack surface from "every user on the
box" to "only named users."

Pre-change check: confirmed login username with `whoami`
(ubuntu) — the account that MUST be whitelisted or lockout
occurs on restart. AllowUsers whitelists by username, not key,
so the critical pre-check is the username, not key existence.

Verified: config syntax tested (sudo sshd -t) before restart,
fresh connection confirmed after restart.
