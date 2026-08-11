## Analyst Problem

The tool compares IP addresses observed in the environment against a known-malicious IOC list.

It then produces a structured CSV report showing which observed IPs matched and which did not, so the result can be reviewed, opened in Excel, or attached to a ticket.


## Input Data

- `observed_ips.txt` contains IP addresses observed in the network or environment.
- `malicious_iocs.txt` contains IP addresses from the known-malicious IOC list.


## Core Logic

After loading both files, the script compares each observed IP against the malicious IOC set.

For every observed IP, it checks whether the IP is present in `malicious_iocs`.

It then writes either `MATCH` or `NO MATCH` into the CSV report for that IP.


## Why Sets Were Used

Dictionaries store key-value pairs, but this tool only needs collections of unique IP values.

Sets are suitable because they keep unique values and make membership checks such as `if ip in malicious_iocs` straightforward.


## Important Methods

- `set()` creates an empty set that stores unique values.
- `.add()` inserts one value into an existing set.
- `.strip()` removes leading and trailing whitespace, including newline characters.
- `writer.writerow()` writes one row to the CSV file.


## Weakness Identified

The main difficulty was converting the analyst requirement into Python structure without seeing the finished code first.

I also needed reinforcement on indentation levels, the difference between `=` and `.add()`, and how each block ends before the next stage begins.


## LNX-031 — Rejected IOC Audit Log

The IOC checker now preserves malformed input instead of silently discarding it.

Invalid entries are stored in `rejected_iocs` as tuples containing:

- rejected value
- source file
- rejection reason

A second report, `rejected_iocs.csv`, is generated with:

value,source,reason

Testing confirmed that malformed values from both observed_ips.txt and malicious_iocs.txt were rejected before IOC processing and recorded with the correct source.

Final design:

valid input   → IOC comparison → ioc_report.csv
invalid input → audit record   → rejected_iocs.csv

Main lesson: validation protects the processing pipeline, while audit logging preserves analyst visibility and supports troubleshooting.


## LNX-032 — Specific IPv4 Rejection Reasons

- Changed the validator from Boolean-only output to:
  (validity, reason)
- Added precise rejection reasons:
  wrong number of octets
  non numeric octet
  octet outside 0-255
- Unpacked the returned tuple using:
  is_valid, reason = validate_ipv4(ip)
- Used the returned reason in rejected_iocs.csv
- Added:
  if not ip:
      continue
  to skip blank input lines

## LNX-033 — Rejection Reason Summary

- Used a dictionary to store reason → count.
- .get(reason, 0) safely handles a missing key.
- reason_counts[reason] = reason_counts.get(reason, 0) + 1 increments the count.
- .items() gives both dictionary key and value.
- rejection_summary.csv stores the final reason/count summary.
