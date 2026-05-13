# Day 3 — File Permissions and Security Boundaries

## Core Concept
Permissions enforce **least privilege** — only authorized users can access specific resources.

## The Three Permissions
- **Read (r)** = View file contents / List directory contents
- **Write (w)** = Modify file / Create/Delete files in directory
- **Execute (x)** = Run file as program / Enter/Traverse directory

## Critical Files Analysis

### /etc/passwd (644: rw-r--r--)
- Owner: read + write (can modify user database)
- Group: read only (legitimate users need usernames)
- Others: read only (same reason)
- **Why 644?** Only root modifies, others just read

### /etc/shadow (600: rw-------)
- Owner: read + write (root updates password hashes)
- Group: nothing (password hashes = crown jewels)
- Others: nothing (absolutely no exposure)
- **Why 600?** Maximum secrecy, only root touches

### /etc/sudoers (440: r--r-----)
- Owner: read only (only visudo can modify, not direct write)
- Group: read only (admins can audit, not modify)
- Others: nothing
- **Why read-only?** Prevents accidental corruption

## The Attacker Model
- Non-root users: **Permissions STOP them**
- Root users: **Permissions are suggestions** (root can chmod anything)

## SOC Implication
Detect privilege escalation **before** it succeeds. Once root is achieved, permissions can't help.

## Key Learning
Permissions are **fail-secure by default** — restrictive permissions cause inconvenience. Open permissions cause breaches.
