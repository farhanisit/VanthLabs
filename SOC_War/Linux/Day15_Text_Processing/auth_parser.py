#!/usr/bin/env python3
"""
auth_parser.py
Day 15 - Python mirrors of awk/sed/cut log analysis commands.
Run from the Day15_Text_Processing directory with auth_sample.log present.
"""

from collections import Counter

LOG_FILE = "auth_sample.log"

# MIRROR 1: awk '/Failed password/ {print $9, $11}'
# Extract username and IP from failed login lines
print("=== Failed Login Attempts (user + IP) ===")
with open(LOG_FILE) as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            if len(parts) > 10:
                print(parts[8], parts[10])

# MIRROR 2: awk '/Failed password/ {print $11}' | sort | uniq -c | sort -rn
# Ranked IP count - brute force detection
print("\n=== Ranked IPs by Failed Attempt Count ===")
ips = []
with open(LOG_FILE) as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            if len(parts) > 10:
                ips.append(parts[10])

for ip, count in Counter(ips).most_common():
    print(f"{count:>3}  {ip}")

# MIRROR 3: awk '/Failed password/ {print $9,$11}' | sort | uniq -c | sort -rn
# Ranked user+IP pairs
print("\n=== Ranked User+IP Pairs by Failed Attempt Count ===")
pairs = []
with open(LOG_FILE) as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            if len(parts) > 10:
                pairs.append(f"{parts[8]} {parts[10]}")

for pair, count in Counter(pairs).most_common():
    print(f"{count:>3}  {pair}")

# MIRROR 4: sed '/Accepted/d'
# Suppress accepted login lines
print("\n=== Lines with Accepted Removed ===")
with open(LOG_FILE) as f:
    for line in f:
        if "Accepted" not in line:
            print(line.strip())

# MIRROR 5: sed -n '/IP/p'
# Print only lines matching a specific IP
TARGET_IP = "185.220.101.47"
print(f"\n=== All Activity from {TARGET_IP} ===")
with open(LOG_FILE) as f:
    for line in f:
        if TARGET_IP in line:
            print(line.strip())
