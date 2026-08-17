import csv

def validate_ipv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False, "wrong number of octets"

    if any(not part.isdigit() for part in parts):
        return False, "non numeric octet"

    if any(not (0<= int(part) <=255) for part in parts):
        return False, "octet outside 0-255"

    return True, ""

rejected_iocs = []
observed_ips = set()
reason_counts = {}
source_reason_counts = {}

with open("observed_ips.txt") as file:
    for line in file:
        ip = line.strip()
        if not ip:
            continue
        is_valid, reason = validate_ipv4(ip)

        if is_valid:
            observed_ips.add(ip)
        else:
            rejected_iocs.append((ip, "observed_ips.txt", reason))
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
            source_reason_counts[("observed_ips.txt", reason)] = source_reason_counts.get(("observed_ips.txt", reason), 0) + 1

malicious_iocs = set()

with open("malicious_iocs.txt") as file:
    for line in file:
        ip = line.strip()
        if not ip:
            continue
        is_valid, reason = validate_ipv4(ip)
        if is_valid:
            malicious_iocs.add(ip)
        else:
            rejected_iocs.append((ip, "malicious_iocs.txt", reason))
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
            source_reason_counts[("malicious_iocs.txt", reason)] = source_reason_counts.get(("malicious_iocs.txt", reason), 0) +1
with open("ioc_report.csv", "w", newline="") as report:
    writer = csv.writer(report, lineterminator="\n")
    writer.writerow(["ip", "status"])

    for ip in sorted(
    observed_ips,
    key=lambda ip: tuple(map(int, ip.split(".")))
    ):
        if ip in malicious_iocs:
            writer.writerow([ip, "MATCH"])
        else:
            writer.writerow([ip, "NO MATCH"])

with open("rejected_iocs.csv", "w", newline="") as report:
    writer= csv.writer(report, lineterminator="\n")
    writer.writerow(["value", "source", "reason"])

    for record in rejected_iocs:
        writer.writerow(record)


with open("rejection_summary.csv", "w", newline="") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["reason", "count"])

    for reason, count in reason_counts.items():
        writer.writerow([reason, count])


with open("source_rejection_summary.csv", "w", newline="") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["source", "reason", "count", "status"])

    for ((source, reason), count) in sorted(
        source_reason_counts.items(),
        key=lambda item: item[1],
        reverse=True
    ):
       if count >= 3:
            status = "HIGH"
       else:
            status = "NORMAL"

       writer.writerow([source, reason, count, status])

