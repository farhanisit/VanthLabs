# Linux Part 2 — Day 18: find + xargs

## Plain English
awk/sed/cut work on file CONTENT. find works on the
FILESYSTEM ITSELF — locating files by name, type, age,
size, owner, permissions. The persistence-hunter's tool.

## Skeleton
find [WHERE] [CONDITION] [ACTION]
WHERE = starting directory (. or ~ or /)
CONDITION = -name, -type, -mtime, -size, -perm, -user
ACTION = -print (default), -delete, -exec

## Key Conditions
-name "pattern"   filename match (case-sensitive)
-type f           files only
-type d           directories only
-mtime -1         modified in last 1 day
-mtime +7         modified MORE than 7 days ago
-size +10M        larger than 10MB
-perm 777         exact permission match

## Lab Findings

find . -name "*.log"
Found two files: ./auth_sample.log and
./VanthLabs/SOC_War/labs/auth.log (recurses subdirectories)

find . d -name "*.log"  <- MISTAKE
"d" without a dash is read as a SECOND SEARCH PATH, not a
condition. find tried to search a nonexistent path "d" and
threw an error, but still searched "." correctly.
Conditions always need a dash: -type d, not bare d.

find . -type d -name "*.log"
Correctly returns EMPTY — asking for directories named
*.log, which don't exist. Files aren't directories.

find . -mtime -1 -name "*.log"
Returned empty initially — file was ~18 days old, not
modified in the last 1 day. Widened to -mtime -18 to find
the actual boundary. Empty output from a time condition
often means the condition is correct, not broken.

## -exec vs xargs

find . -type f -name "*.log" -exec wc -l {} \;
{}  = placeholder for each matched file
\;  = ends the -exec command
Runs wc -l ONCE PER FILE, separately. No combined total.

find . -type f -name "*.log" | xargs wc -l
Batches all matched files into ONE wc -l call.
wc sees multiple files at once and adds a TOTAL line
automatically — this only happens with xargs, not -exec.

Output comparison:
-exec:  10 ./auth_sample.log
        347 ./VanthLabs/SOC_War/labs/auth.log
xargs:  10 ./auth_sample.log
        347 ./VanthLabs/SOC_War/labs/auth.log
        357 total   <- xargs-only behavior

## Decision Rule
-exec = safer for destructive/order-sensitive per-file actions
xargs = better for bulk operations needing combined output
