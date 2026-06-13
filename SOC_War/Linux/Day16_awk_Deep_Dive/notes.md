# Linux Part 2 — Day 16: awk Deep Dive

## Plain English
awk is a line-by-line processor. For every line it asks:
does this match my pattern? If yes, run the action.
Day 15: extract and filter. Day 16: count, calculate, summarise.

## Skeleton
awk '
  BEGIN   { runs once before reading        }
  /pattern/ { runs for every matching line  }
  END     { runs once after all lines read  }
' filename

## New Syntax
count++           increment by 1
count[$9]++       increment counter keyed by field 9 value
count[$9" "$11]++ key by "user IP" string (space-separated)
total++           simple total counter
NR                current line number
NF                number of fields in current line
for (x in arr)    loop through array keys

## Goals Built This Session

### Goal 1 — Total count
awk '
  BEGIN { print "=== Failed Login Count ===" }
  /Failed password/ { count++ }
  END { print "Total:", count }
' auth_sample.log

### Goal 2 — Count per user
awk '
  BEGIN { print "Failed Logins" }
  /Failed password/ { count[$9]++ }
  END { for (user in count) print "User:", user, "Count:", count[user] }
' auth_sample.log

### Goal 3 — Full analyst summary
awk '
  BEGIN { print "=== Failed Login Summary ===" }
  /Failed password/ { count[$9" "$11]++; total++ }
  END {
    for (user in count)
      print "User:", user, "Failures:", count[user]
    print "Total failed logins:", total
  }
' auth_sample.log

## Key Corrections
count[9]   = literal key "9" (wrong)
count[$9]  = value of field 9 as key (correct)

for loop without braces owns only the NEXT single statement.
Print total OUTSIDE the for loop or it repeats every iteration.

count[$9,$11]   = internal separator, no space in output
count[$9" "$11] = explicit space in key string, readable output

## Python Mirror
count[$9]++ = count[parts[8]] = count.get(parts[8], 0) + 1
for (user in count) = for user, val in Counter(ips).items()
