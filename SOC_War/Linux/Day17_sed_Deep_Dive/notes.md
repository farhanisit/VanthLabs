# Linux Part 2 — Day 17: sed Deep Dive

## Plain English
sed = stream editor. Reads line by line, transforms on the fly.
Never modifies the original file unless -i is used.
-i is dangerous on investigation evidence — always work on copies.

## Skeleton
sed 'COMMAND' filename
sed -n 'COMMAND' filename   (-n suppresses default output)

## Commands

### Substitution
sed 's/old/new/' file        replace first match per line
sed 's/old/new/g' file       replace ALL matches per line
sed 's/Failed/ALERT: Failed/g' auth.log   log enrichment

### Delete
sed '/pattern/d' file        delete matching lines
WARNING: does not guarantee only failures remain.
Other line types (pam, sudo, cron) will still appear.

### Print (always use with -n)
sed -n '/pattern/p' file     print only matching lines
-n mutes everything, p unmutes matches — always use as a pair.

Without -n:
sed '/pattern/p' file = every line once + matching lines twice

### Ranges
sed -n '3,7p' file           print lines 3 to 7
sed -n '/start/,/end/p' file print from pattern to pattern

Pattern ranges RESET and REPEAT — every time the start
pattern appears again a new range opens. This means:
/Failed/,/Accepted/ extracts EVERY attack window in the file,
not just the first one. Useful for brute-force detection.

## Key Insight — Field Shifting
When sed enriches a line by adding words, field numbers shift.
sed 's/Failed/ALERT: Failed/g' adds one word = shifts all
fields right by one. Always re-verify field numbers after
enrichment before piping to awk.

Command to verify after enrichment:
sed 's/Failed/ALERT: Failed/g' auth.log | awk '/ALERT: Failed/ {for (i=1; i<=NF; i++) print i, $i; exit}'

## Two-Tool Pipeline
sed 's/Failed/ALERT: Failed/g' auth.log | awk '
  BEGIN { print "=== Failed Login Summary ===" }
  /ALERT: Failed/ { count[$10" "$12]++; total++ }
  END {
    for (user in count)
      print user, count[user]
    print "Total failed logins:", total
  }
'

sed enriches → pipe → awk summarises
Do NOT pass filename to awk when reading from pipe.

## Python Mirrors
sed 's/old/new/g'     = line.replace("old", "new")
sed '/pattern/d'      = [l for l in f if "pattern" not in l]
sed -n '/pattern/p'   = [l for l in f if "pattern" in l]
