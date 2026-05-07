
# ⚔️ CLI_RITUAL_024 — SUID Hunt: The Hidden Root Keys + /dev Abyss  
📅 Date: 2025-05-25  
🧠 Mode: Read-Only + Deep Exploration  
🎯 Phase: 1.5+ — Privilege Escalation Primer

---

## 🔍 01. Scenario / Real Trigger

> Started by learning how **SUID binaries** can allow privilege escalation.  
> Ended up opening the **/dev** directory as if it were a file using `cat ./dev`, and uncovered the raw chaotic guts of the OS — terminals, devices, random, and disk maps.

---

## 🧠 02. Commands Covered

| Command | Purpose | Note |
|--------|---------|------|
| `find / -perm -4000 2>/dev/null` | List all SUID files | Finds root-owned binaries with special permission |
| `ls -l /bin/bash` | Check if bash has SUID | Look for `rws` instead of `rwx` |
| `/bin/bash -p` | Run bash with preserved privileges | Used if bash has SUID |
| `cat ./dev` | Tried to read the /dev directory as a file | Unexpected output: hardware-level devices streamed out |
| `ls /dev` | Proper way to explore devices | Used to safely inspect device files |

---

## 🧠 03. Logic Checks

- SUID = gives you the *power of the file’s owner*  
- `/dev` = not a normal directory, but a **live wire** of system device files  
- `cat` is for reading **text files**, not binary virtual hardware entries

---

## 👣 04. Rehearsal Path (Next Session)

```bash
# Find SUID files
find / -perm -4000 2>/dev/null

# Check for SUID on bash
ls -l /bin/bash

# Try bash escalation if applicable
/bin/bash -p

# Explore devices safely
ls /dev

05. Case Reflections

In a real CTF or system audit, you could:
Abuse /usr/bin/python with SUID
Escalate via SUID bash
Use /dev/null or /dev/zero for script logic (e.g., discard logs or write infinite zeroes)
