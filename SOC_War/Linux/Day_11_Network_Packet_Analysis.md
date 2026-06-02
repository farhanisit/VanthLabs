# Linux Day 11 — Network & Packet Analysis

## Core Idea
Logs tell you what a system RECORDED about an event.
Packets are the event itself — the actual bytes on the wire.
Lowest-level ground truth an analyst can get.

## The Two Tools
tcpdump   = command-line capture (the microphone)
Wireshark = GUI analysis (reading the recording deeply)
Common workflow: capture with tcpdump -> open .pcap in Wireshark.

## Key tcpdump Flags
-i <iface>   which interface to listen on
-n           don't resolve names (raw IPs/ports)
-w file.pcap write capture to file
-r file.pcap read capture back
-A           show payload as ASCII
port N       filter: only traffic on port N
timeout N    stop after N seconds

## The TCP Three-Way Handshake (know cold)
[S]     SYN     "can we talk?"
[S.]    SYN-ACK "yes, you?"
[.]     ACK     "confirmed"
No SYN-ACK back = service down, filtered, or blocked.
Repeated SYNs with no reply = port scan / firewall block signature.

## Plaintext vs Encrypted
Port 80  (HTTP)  -> -A shows GET / HTTP/1.1, headers, full page = open postcard
Port 443 (HTTPS) -> -A shows gibberish = armored box

## SNI — The One Thing HTTPS Leaks
TLS Client Hello must name the destination site BEFORE encryption starts.
So even on HTTPS, a network observer sees:
- destination IP
- domain name (via SNI)
- timing and data volume
But NOT the content.
HTTPS hides the conversation. It does not hide WHO you talked to.

## What Analysts Hunt For in Packets
- Plaintext creds over HTTP/FTP/Telnet = immediate exposure
- DNS queries to weird domains = C2 / DNS tunneling
- Beaconing: tiny packets to one external IP at fixed intervals
- Big outbound transfers = exfiltration
- Repeated SYNs with no reply = port scan
- TLS to unexpected IPs on 443

## Failed Connection Pattern
IPv4 SYNs firing repeatedly with no SYN-ACK = connection refused or filtered.
System retries, then falls back (e.g. IPv6).
On a real incident: SYNs to port 445 with no reply = SMB blocked.

## Live Captures Done
day11_first.pcap - HTTPS session to example.com (25 packets, TLS visible)
day11_http.pcap  - HTTP session to neverssl.com (plaintext GET + full HTML)

## Key Learnings (Day 11)
1. curl creates traffic. tcpdump records it. .pcap saves it.
2. TCP handshake is always first — three packets before any data.
3. Port 443 = encrypted payload (gibberish with -A).
4. Port 80 = readable payload (GET, headers, HTML with -A).
5. SNI leaks the domain even inside TLS — metadata is never truly hidden.
6. Absent SYN-ACK is data — tells you the port is closed or filtered.
