import csv
observed_ips = set()

with open("observed_ips.txt") as file:
    for line in file:
        observed_ips.add(line.strip())

malicious_iocs = set()

with open("malicious_iocs.txt") as file:
    for line in file:
        malicious_iocs.add(line.strip())

with open("ioc_report.csv", "w", newline="") as report:
    writer = csv.writer(report)
    writer.writerow(["ip", "status"])

    for ip in observed_ips:
        if ip in malicious_iocs:
            writer.writerow([ip, "MATCH"])
        else:
            writer.writerow([ip, "NO MATCH"])
