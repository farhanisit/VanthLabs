#  THM: Linux Fundamentals Part 1 (Raw Notes)

##  INTRODUCTION
- Linux is an operating system (like Windows/macOS), but more **flexible** and **powerful** for servers and hacking.
- It's what powers the backbone of the internet.

---

## ️ APPLICATIONS OF LINUX
- Used in:
  - Web servers
  - ATMs
  - Checkout tills
  - Car infotainment systems
  - Routers, Smart TVs, etc.

---

##  ORIGIN OF "LINUX"
- Not a single OS — **umbrella term** for OSes based on UNIX
- It’s **open source**, meaning anyone can read, modify, or build on it
- Major distros: Ubuntu, Debian, CentOS, Arch, Kali

---

##  Vanth Reflection (Freeform)
Today I wasn’t trying to take perfect notes — I just showed up.  
That’s the hardest part. I wrote some lines, and in them, I found momentum.  
*“You do not rise to the level of your goals, you fall to the level of your systems.”* — yeah, James Clear said that, and now I’m here making mine.


---

## 🔍 Part 2: Grep & Find Training (May 14)

**Commands Practiced:**
- `grep "THM{" access.log` → searched for flag
- `grep "81.143.211.90" access.log` → filtered by IP
- `find . -name "crew.txt"` → searched by name
- `find . -name "*.txt"` → wildcard search (with quotes)
- `wc -l access.log` → counted lines

**Concepts Locked In:**
- grep = line filtering sniper
- find = recursive file locator
- wildcards need quoting in zsh
- THM labs simulate real-world server logs

**My Insight:**
Today felt like stepping into the backrooms of the internet.  
I wasn’t just reading commands — I was tracking visitors, reading bot trails, spotting digital footprints.  
I liked it. I want more of this.

---

# 🧠 TryHackMe – Linux Fundamentals Part 1 Notes

---

## ✅ Completion Log — Linux Fundamentals Part 1
**Timestamp:** $(date "+%Y-%m-%d %H:%M")

Vanth has completed the **final module** of *Linux Fundamentals Part 1* on TryHackMe. Currently reviewing the conclusion notes.

### 🧠 Key Operator Clarifications:

- & → Runs a command **in the background**
- && → Runs the **second command only if the first succeeds**
- > → **Overwrites** the file with new output
- >> → **Appends** to the file (adds to existing content)

This marks the closure of Part 1. Next step: plan for Linux Fundamentals Part 2 and more THM rooms tied to real-world attack surfaces.
