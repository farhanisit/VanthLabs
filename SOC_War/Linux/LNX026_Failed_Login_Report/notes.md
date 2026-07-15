# LNX-026 — Failed-Login Report Generator (CSV Output)

## SOC Automation Lab — Phase 2 opens here
Not "learn a command" anymore. Every session builds a script
that answers a real analyst question.

## The Analyst Question
"Give me a structured report of failed-login activity I can
hand to L2 — not raw log lines, but IP, failure count, and
whether it eventually succeeded, in a format I can attach
to a ticket."

## What's New vs login_detector.py (LNX-021)
Same detection logic. The change is the OUTPUT:
- login_detector.py PRINTED alerts to the screen
- login_report.py WRITES a structured CSV file instead
Detection stayed identical; output format changed from
terminal print to file write. That's the difference between
"I ran a script" and "here is a report."

## The csv Module
import csv
writer = csv.writer(file_object)   creates the writer
writer.writerow([col1, col2, ...]) writes one row
First writerow = the header (column names)

## File Modes (locked distinction)
"w" = write — overwrites the file fresh each run.
      Correct for a REPORT (want one clean file, one header).
"a" = append — adds to the end without erasing.
      Correct for a LOG (want accumulating history).
Running in "a" twice would duplicate header AND data.

## Real Mistakes Made and Fixed
- Nearly wrote output to "login_report.py" (the script itself)
  in "w" mode — would have ERASED the script and replaced it
  with CSV data. Caught before running. Lesson: with open(..,"w")
  always double-check the filename, "w" destroys what's there.
- IndentationError from mixed spaces/tabs when un-indenting the
  CSV block — same tab/space family issue as LNX-020. Fixed by
  retyping the block with consistent 4-space indents.
- CSV block was initially nested INSIDE the log-reading "with"
  block — should be at the left margin, a separate stage:
  read the log and close it, THEN write the report.

## Output Produced
ip,failure_count,succeeded
45.33.32.156,3,yes
185.220.101.47,3,yes

A real analyst deliverable — opens in Excel, attaches to a
ticket, hands to L2 as evidence.
