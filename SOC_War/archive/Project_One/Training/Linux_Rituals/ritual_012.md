---

## ⚙️ CLI Ritual #012 – Redirection & Output Control

**Date:** 2025-05-16  
**Focus:** `>`, `>>`, `2>`, `2>&1`, `/dev/null`

**Commands Practiced:**
- `echo "..." > file.txt` → overwrite
- `echo "..." >> file.txt` → append
- `command > file.txt` → capture stdout
- `command 2> file.txt` → capture stderr
- `command > file.txt 2>&1` → merge all output
- `command > /dev/null 2>&1` → complete silence

**Use Cases:**
- Script logs
- Silencing cron job noise
- Keeping outputs clean
- Capturing errors separately

**Vanth Insight:**
In Unix, everything is a voice. Redirecting output is not just redirection — it’s **discipline**. Control signal. Kill noise. This is real-world operator work.


