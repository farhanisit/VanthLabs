# Linux Part 2 — Day 15: Text Processing for SOC Logs
## Tools: cut, awk, sed

---

## The Core Problem
grep finds the LINE.
cut / awk / sed find the FIELD inside that line.

Sample log line:
Jun 08 06:41:12 WKSTN-04 sshd[2291]: Failed password for mlopez from 45.33.32.156 port 51890 ssh2

grep "Failed" → whole line
awk '$9, $11'  → mlopez 45.33.32.156

---

## RULE ZERO: Verify Fields Before Extracting
Never assume field numbers. Always inspect first.

Command:
awk '/Failed password/ {for (i=1; i<=NF; i++) print i, $i; exit}' auth.log

This prints each field with its number from the first matching line.
Verify, then extract.

---

## TOOL 1 — cut

Plain English:
Split a line by a fixed delimiter and print one piece.

Skeleton:
cut -d 'DELIMITER' -f FIELD_NUMBER filename

Visual:
cut        = the tool
-d ':'     = split wherever : appears
-f 1       = give me piece number 1
filename   = file to read

Simple example (/etc/passwd line):
root:x:0:0:root:/root:/bin/bash
  1  2 3 4  5     6      7

cut -d ':' -f 1 /etc/passwd
Output: root (username only)

SOC use case:
cut -d ':' -f 1 /etc/passwd   <- list all system usernames
                                  useful for user enumeration check

WARNING — cut breaks on variable spaces:
"Jun  8 06:41:17"  <- two spaces before 8
cut -d ' ' sees: Jun | empty | 8 | 06:41:17
Field 3 = 8, not the timestamp.
Use awk for syslog, not cut.

Rule: cut = clean fixed delimiters (: , | tab)
      awk = messy whitespace logs

Python mirror:
cut -d ':' -f 1  ≈  line.split(':')[0]

---

## TOOL 2 — awk

Plain English:
Read each line, split into fields, filter by pattern,
print selected fields or apply logic.

Skeleton:
awk 'PATTERN { ACTION }' FILE

Visual:
awk           = the tool
'/pattern/'   = which lines to match (optional)
{print $N}    = what to do — print field N
FILE          = file to read
$1,$2...      = field numbers (1-indexed)
$NF           = last field
$0            = entire line

Simple example:
echo "a b c d" | awk '{print $2}'
Output: b

SOC example:
awk '/Failed password/ {print $9, $11}' auth.log
Output: username and IP from every failed login line

Common mistakes:
WRONG: awk '/Failed password/ auth.log {print $11}'
       (filename inside the quotes — awk thinks it's part of the pattern)

WRONG: awk '/Failed password/ {print $11} auth.log
       (missing closing quote — shell waits forever with > prompt)

WRONG: awk '/Failed pasword/ {print $11}' auth.log
       (typo in pattern — silent empty output, no error)

CORRECT: awk '/Failed password/ {print $11}' auth.log

awk vs Python indexing:
awk $9  = Python parts[8]   (awk 1-indexed, Python 0-indexed)
awk $11 = Python parts[10]  (always subtract 1)

Python mirror:
with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            if len(parts) > 10:
                print(parts[8], parts[10])

---

## TOOL 3 — sed

Plain English:
Transform, substitute, delete, or selectively print lines.
Not a field extractor — a line editor.

Skeleton:
sed 'COMMAND' filename

Visual:
sed               = the tool
's/old/new/g'     = substitute old with new, all occurrences
'/pattern/d'      = delete lines matching pattern
'-n /pattern/p'   = print only lines matching pattern
                    (-n mutes everything, p unmutes matches)

Simple example:
echo "hello world" | sed 's/world/there/'
Output: hello there

SOC examples:
sed 's/Failed/ALERT: Failed/g' auth.log
→ enrich log lines before reporting

sed '/Accepted/d' auth.log
→ suppress accepted login lines
WARNING: does NOT guarantee only failures remain.
pam_unix, sudo, cron lines will still appear.
For only failures: grep "Failed password" auth.log

sed -n '/185.220.101.47/p' auth.log
→ print only lines from that IP

The -n / p pair:
-n = mute all output (silence everything)
p  = unmute only matching lines
Together = print only what matches, nothing else

Python mirror:
sed 's/old/new/g'     = line.replace("old", "new")
sed '/pattern/d'      = [l for l in f if "pattern" not in l]
sed -n '/pattern/p'   = [l for l in f if "pattern" in l]

---

## Brute Force Detection Chain

One-line analyst query:
awk '/Failed password/ {print $11}' auth.log | sort | uniq -c | sort -rn

Step by step:
awk '/Failed password/ {print $11}'  filter + extract IP
sort                                  group identical IPs together
uniq -c                               count each group
sort -rn                              rank highest count first

With username + IP:
awk '/Failed password/ {print $9, $11}' auth.log | sort | uniq -c | sort -rn

uniq -c counts identical complete lines.
{print $11}      groups by IP only
{print $9,$11}   groups by user+IP pair — different analyst question

---

## Notebook Card (physical notebook)
VERIFY: awk '/Failed password/ {for (i=1;i<=NF;i++) print i,$i; exit}' auth.log
cut  -d ':' -f 1        clean delimiters only
awk  '/pattern/ {print $N}'   filter then extract
sed  's/old/new/g'      replace all
sed  '/pattern/d'       delete matching lines
sed  -n '/pattern/p'    print only matching (-n mutes, p unmutes)
$NF=last field | $0=whole line
awk 1-indexed → Python 0-indexed (subtract 1)
line.split() not line.split(' ')
Always: if len(parts) > N before parts[N]
Chain: awk '/pattern/ {print $N}' file | sort | uniq -c | sort -rn
