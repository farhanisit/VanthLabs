# 🧙 CLI Ritual #021 – The Signal Caster

**Date:** 2025-05-19  
**Focus:** Process management using signals (`kill`, `ps`, `jobs`, `nice`, etc.)

---

## 🔧 Commands Practiced

```bash
# View all processes
ps aux

# Find a Python process
ps aux | grep python

# Simulate a long process
sleep 9999 &

# List background jobs
jobs

# Pause and resume jobs
kill -STOP %1
kill -CONT %1

# Kill softly
kill -15 %1

# Kill forcefully
kill -9 %1

# Start a process with lower priority
nice -n 10 python3 my_script.py

# Adjust priority of existing process
renice +10 -p <PID>
```

---

## 🧠 Vanth Notes

* `kill -15` is graceful; `kill -9` is ruthless.
* `%1` refers to the first job listed via `jobs`.
* `STOP`/`CONT` = freeze and unfreeze time — literally.
* `nice` and `renice` manage **CPU hunger** like a boss.
* `ps aux | grep something` is your digital sonar.

---

## 🔍 Case Study: The Python Rogue

> Situation: A Python script is misbehaving on a remote machine.

You:
```bash
ps aux | grep python
kill -15 <PID>          # Ask it to exit
kill -STOP <PID>        # Freeze if not cooperating
renice +10 -p <PID>     # Calm it down
kill -9 <PID>           # If all else fails, execute
```

Silent. Tactical. Professional.

---

## ✅ Ritual Complete

📁 File Path:
```bash
~/VanthLabs/Project_One/Training/Linux_Rituals/ritual_021.md
```

You now command **running processes** like a system sorcerer.  
The terminal listens. The OS obeys.  
Vanth moves onward.

