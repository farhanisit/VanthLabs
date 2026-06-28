from collections import Counter

ips = []
with open("auth_sample.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ips.append(parts[10])

print(Counter(ips).most_common())
