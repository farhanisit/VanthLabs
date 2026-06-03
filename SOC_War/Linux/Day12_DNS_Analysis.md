# Linux Day 12 — DNS Analysis & DNS Tunneling (C2)

## Core Idea
DNS resolves names to IPs — the phonebook. Every connection starts
with a lookup unless cached. Day 11 gap: neverssl was cached, so no
DNS packet appeared. Today we forced fresh lookups and read them live.

## Lab Setup
- VM: vanth-lab. Captures written to ~/pcaps/ on the VM.
- Tools: tcpdump (capture), dig (force lookup).
- Capture cmd: sudo tcpdump -i any -n port 53 -w <file>
  -i any = all interfaces | -n = NO name resolution (stops tcpdump
  polluting its own DNS capture) | port 53 = DNS | -w = write pcap.

## Baseline (Normal) — dns_baseline.pcap
- One `dig example.org` = 4 packets.
- Two-hop resolution via systemd-resolved (127.0.0.53 stub):
    app -> 127.0.0.53 (lo)  ->  192.168.2.2 -> 192.168.2.1 (enp0s1)
    answer back the same path.
- Response 2/0/1 = 2 answers, resolved to two A records.
- tcpdump In/Out is from the INTERFACE perspective; lo direction
  labels are perspective-flipped (a quirk, not an anomaly).
- Note: this capture caught the full query/response pairs including
  the resolving 2/0/1 answer.

## Tunnel Pattern — dns_tunnel.pcap
- 10 dig queries, long random base64-ish subdomains, one base domain.
- 41 packets vs baseline's 4 = volume red flag.
- Every response 0/1/1 = ZERO answers (non-resolving) = transmitting,
  not looking up.

## DNS Tunneling — Detection Logic
Behavior -> telemetry -> logs -> query:
malware encodes data in subdomains -> floods port 53 with long
high-entropy queries to one domain -> pcap/DNS logs hold them ->
hunt on length + volume + entropy + resolution rate.

Hunt pivots:
1. Subdomain length (normal short / tunnel very long)
2. Distinct subdomains per registered domain (few vs hundreds)
3. Query volume per host (spike to one domain)
4. Resolution rate (tunnel mostly 0 answers / NXDOMAIN)
5. Entropy of label (random base64-ish = encoded data)

Field test: "Many unique high-entropy subdomains, one base domain,
barely resolving, high volume from one host" = DNS tunnel.

## 5-Layer Classification
- Pattern:  High-entropy subdomains, shared base domain, non-resolving.
- Type:     Covert channel / C2 communication (exfil via DNS).
- Stage:    C2 (and Exfiltration if data egressing).
- Severity: Critical — active covert channel = live compromise.
- Action:   Detect and DOCUMENT (imaging IS preservation — capture
            the pcap, record host/domain/volume/timestamps).
            RECOMMEND blocking the domain + isolating host.
            ESCALATE to L2/L3. L1 does NOT block/cut unilaterally —
            containment is L2/L3's call; they may watch first to scope.

## Locks Re-seated
- Imaging IS preservation (not two sequential steps).
- L1 RECOMMENDS the block, never pulls the trigger.
