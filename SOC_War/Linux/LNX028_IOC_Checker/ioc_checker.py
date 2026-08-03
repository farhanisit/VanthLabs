import csv

def is_valid_ipv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False
    return all(
        part.isdigit() and 0 <= int(part) <= 255
        for part in parts
    )


rejected_iocs = []
observed_ips = set()

with open("observed_ips.txt") as file:
    for line in file:
        ip = line.strip()

        if is_valid_ipv4(ip):
            observed_ips.add(ip)
        else:
            rejected_iocs.append((ip, "observed_ips.txt", "invalid IPv4 format"))
malicious_iocs = set()

with open("malicious_iocs.txt") as file:
    for line in file:
        ip = line.strip()

        if is_valid_ipv4(ip):
            malicious_iocs.add(ip)
        else:
            rejected_iocs.append((ip, "malicious_iocs.txt", "invalid IPv4 format"))

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
