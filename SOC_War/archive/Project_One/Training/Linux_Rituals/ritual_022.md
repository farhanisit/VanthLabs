### ⚙️ Ritual 022 – AWK: The Field Whisperer

**Theme:** Field-based text parsing  
**Tools:** `awk`  
**Core Commands:**
- `awk '{ print $1 }' filename.txt` → Print first field
- `awk -F ":" '$3 >= 501 { print $1, $3, $6, $7 }' /etc/passwd` → Filter users by UID
- `awk '/Failed password/ { print $(NF-5), $(NF-3) }' file` → Extract usernames + IPs from logs

**Case Studies:**
1. **Rogue User Tracker** – Extract human users from passwd
2. **Lost Log Entry Hunter** – Search logs for suspicious logins (timestamp + IP logic)

**Takeaway:**  
`awk` reads between the lines — it’s not just text processing, it’s **digital forensic surgery**.

awk '{ print $1 }' filename.txt                  # Print first field
awk -F ":" '$3 >= 501 { print $1, $3, $6, $7 }' /etc/passwd  # Filter users by UID
awk '/Failed password/ { print $(NF-5), $(NF-3) }' file      # Extract login fail info

Scenario 1: The Rogue User Tracker
🔍 Goal: Identify local users with UIDs ≥ 501
🎯 Use Case: Finding unauthorized human accounts on macOS or Linux
📂 Test File: Simulated /etc/passwd → passwd_clone.txt
📌 Command Used:

awk -F ":" '$3 >= 501 { print $1, $3, $6, $7 }' passwd_clone.txt
🎯 Follow-up Audit Idea:
Check if any of them have UID 0 (root-level privilege)

awk -F ":" '$3 == 0 { print $1 }' passwd_clone.txt
🧠 Scenario 2: The Lost Log Entry Hunter
🔍 Goal: Investigate a suspicious login at 03:21 AM
🎯 Use Case: Log forensics to detect failed or malicious login attempts
📂 Test File: fake_auth.log
📌 Command Used:

awk '$3 ~ /^03:21/ && /Failed password/ { print $(NF-5), $(NF-3) }' fake_auth.log
🧠 Field Breakdown:

$3 → Timestamp
$(NF-5) → Username
$(NF-3) → IP Address
🎯 Result: Pinpointed attackers and timestamp-specific anomalies without using external tools.

🧾 Takeaway:
awk is not just a command — it’s a field-based logic engine.
It’s what you reach for when:
grep can’t filter by column
cut can’t handle conditions
And you're on the hunt for patterns and structure.
This ritual laid the groundwork for automated CLI auditing, log parsing, and data shaping workflows — to be weaponized in weekend mini-projects using both Bash and Python.
