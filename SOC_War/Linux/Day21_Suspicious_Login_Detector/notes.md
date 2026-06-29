# Linux Part 2 — Day 21: Suspicious Login Detector

## The Pattern
Not just "many failures" — specifically: an IP that fails
3+ times AND later succeeds for the same IP. That combination
means credentials were eventually guessed/cracked correctly,
not just noise from a failed attacker who gave up.

## Threshold Discussion
FAIL_THRESHOLD = 3 is a tuned judgment call, not an absolute
truth. 1-2 failures is normal human error (typos). 3+ is where
most real detection systems draw the line between "mistake"
and "automated/malicious guessing."

Known limitation: a 2-failures-then-success pattern would be
MISSED by this threshold. This is a deliberate tradeoff, not
an oversight -- lowering the threshold to catch that case would
flood output with false positives from normal typos. Documented
here as a tunable parameter (FAIL_THRESHOLD sits at the top of
the script specifically so it can be adjusted without touching
the detection logic).

## Why Not Just Count Failures Globally
Counting all "Failed password" lines across the whole file
tells you THAT failures happened, not WHICH IP succeeded after
failing. Per-IP tracking is required because the response
action (block/isolate) needs a specific IP, not a vague
"something bad happened somewhere" signal.

## Why a Dictionary for Failures, a List for Successes
fail_counts needs a NUMBER per IP (how many times) -- that's
what a dictionary is for: key -> value.
accepted_ips only needs a YES/NO per IP (did it ever succeed) --
no count needed, so a simple list is enough. Using a dictionary
for accepted_ips would have been valid but unnecessarily complex
for what the data actually requires.

## Single Pass vs Two Passes
Checked for "Failed password" and "Accepted password" inside
the SAME loop, not two separate loops reading the file twice.
Real auth.log files can be very large -- reading once and
checking multiple conditions per line is the correct approach,
not re-opening/re-scanning the file for each pattern.

## Dictionary Counting Pattern
fail_counts[ip] = fail_counts.get(ip, 0) + 1

.get(ip, 0) looks up ip in the dictionary; if not found yet,
returns 0 instead of crashing. Add 1, store back under the
same key. First time: 0+1=1. Second time: 1+1=2. Per-IP
running tally, same concept as awk's count[$9]++.

## Real Mistakes Made and Fixed
- Tried building a single global if-condition counting all
  failures/successes across the file rather than per-IP --
  caught this myself by tracing through what the data would
  actually need to look like for the response action to work
- Used dictionary .get() syntax on accepted_ips after declaring
  it as a list -- lists don't have .get(), would have crashed.
  Fixed by switching to .append() to match the list type
- Typo: accpeted_ips vs accepted_ips -- inconsistent naming
  would have caused a NameError
- Extra stray ")" after fail_counts[ip] in the final if condition
- print() needed to convey BOTH the failure count AND the
  success outcome -- first draft only mentioned failures,
  missed stating the IP also got Accepted

## Final Output
Alert: 45.33.32.156, failed: 3 then succeeded
Alert: 185.220.101.47, failed: 3 then succeeded

Both IPs in the test log correctly flagged -- matches the
known capstone-style pattern from the WKSTN-04/mlopez scenario,
now detected automatically rather than read by eye.
