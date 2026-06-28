# Linux Part 2 — Day 20: Python Log Parsing (Built From Scratch)

## Plain English
Every parser follows the same shape: open the file, loop
through lines, check a condition, act on matches, summarise
at the end. awk does this in one line; Python spells out
each step explicitly.

## Built Piece by Piece

### Piece 1 — open and loop
with open("auth_sample.log") as f:
    for line in f:
        print(line)

"with" auto-closes the file safely, no need for f.close().
First run printed double-spaced output — every line already
ends in \n, and print() adds its own \n on top. Fixed with
line.strip() to remove the trailing newline before printing.

split() vs strip():
strip()  = removes whitespace/newline from string edges
split()  = breaks a string into a LIST of word pieces

### Piece 2 — filtering
if "Failed password" in line:
    print(line.strip())

### Piece 3 — field extraction
parts = line.split()
print(parts[8], parts[10])

Real mistakes made and fixed:
- Tried $8, $10 (awk/bash syntax) instead of parts[8], parts[10]
  -- cross-tool syntax leak, awk thinking bleeding into Python
- TabError: inconsistent tabs and spaces in indentation
  -- nano mixed tab key and space key across edits, Python
     requires ONE consistent indentation style throughout

### Piece 4 — counting
from collections import Counter
ips = []
... inside the if-block:
    ips.append(parts[10])
... outside the loop entirely (left margin, no indent):
print(Counter(ips).most_common())

Real mistakes made and fixed:
- print(ips.append([])) -- wrapped append() in print AND
  appended an empty list instead of the IP. append() returns
  None always; it modifies the list in place silently.
- Forgot to remove print() from inside the loop after adding
  the Counter line -- caused 6 growing snapshots of the
  Counter recalculating fresh every iteration instead of one
  final summary. Fixed by moving print() fully outside the
  "with" block (left margin, zero indentation).

## Final Script
from collections import Counter

ips = []
with open("auth_sample.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ips.append(parts[10])

print(Counter(ips).most_common())

## Output
[('45.33.32.156', 3), ('185.220.101.47', 3)]

Matches awk '/Failed password/ {print $11}' | sort | uniq -c
exactly -- same result, different tool, fully built and
debugged from a blank file rather than copied.

## Indentation Rule (Python's core structural law)
Any line ending in : (if, for, while, with, def) demands an
indented block directly beneath it. Indentation depth is
not cosmetic -- it defines what's inside vs outside a block.
Code at the same indentation as "with" runs once, after
everything inside it finishes. Code indented inside a loop
runs every single iteration.
