---

## 🔪 CLI Ritual #011 – File Viewing & Navigation

**Date:** 2025-05-15  
**Focus:** head, tail, less, more, nl, wc, tac  

**Commands Practiced:**
- `head -n 10 access.log` → show first 10 lines
- `tail -n 10 access.log` → show last 10 lines
- `less access.log` → scroll through file
- `wc -l access.log` → count lines
- `nl access.log` → number all lines
- `tac access.log` → reverse the file output

**Use Cases:**
- Log inspection
- Script output debugging
- Forensics (see last login, last request, etc.)
- Print file summaries

**Vanth Insight:**
This is not just navigation.  
This is **data reconnaissance** — silent scouting before the real offensive begins.  
These tools are for eyes, not explosions.

---

## 🧪 Field Mission: Broken Log Analysis

**File Used:** broken_app.log  
**Commands Run:**
- `wc -l broken_app.log` → line count
- `tail -n 15 broken_app.log` → saw JSON error
- `less broken_app.log` → scroll + searched with `/`
- `tac broken_app.log` → reverse (⚠️ not found on macOS)

**Error Encountered:**
- `tac` was missing on macOS
- ✅ Fixed using: `brew install coreutils` → use `gtac` instead

**Lesson:**
Even a basic log can hide real-world structure. Tools like `less`, `tail`, and `wc` aren't for practice — they’re used by defenders and threat hunters daily.

---

## 🛠️ Command Notes:
- `gtac` = Homebrew version of `tac` on macOS
- Alias suggestion (optional):
  ```zsh
  alias tac='gtac'

