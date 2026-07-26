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
