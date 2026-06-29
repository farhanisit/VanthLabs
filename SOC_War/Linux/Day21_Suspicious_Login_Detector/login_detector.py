FAIL_THRESHOLD = 3
fail_counts = {}
accepted_ips = []

with open("auth_sample.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[10]
            fail_counts[ip] = fail_counts.get(ip, 0) + 1
        if "Accepted password" in line:
            parts = line.split()
            ip = parts[10]
            accepted_ips.append(ip)

for ip in fail_counts:
    if fail_counts[ip] >= FAIL_THRESHOLD and ip in accepted_ips:
        print(f"Alert: {ip}, failed: {fail_counts[ip]} then succeeded")
