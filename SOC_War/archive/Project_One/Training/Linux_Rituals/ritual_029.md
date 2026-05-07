📜 ritual_029.md — Tracing the Pulse of the Network
🗓 Date: 2025-07-18
🧠 Mode: Practical Execution
🧭 Ritual Title: Tracing the Pulse of the Network
🧰 Tools: ping, traceroute, mtr
🌐 Path: ~/VanthLabs/Project_One/Artifacts/Networking/Rituals/ritual_029.md

⚔️ Objective:
To trace, diagnose, and compare packet travel paths across two different network interfaces — JioFiber (IPv6) and DSL WiFi (IPv4) — using the CLI tools ping, traceroute, and mtr.

🔧 Commands Practiced:
bash
Copy
Edit
ping google.com
traceroute google.com
sudo mtr google.com
🔍 Key Observations:
✅ Network 1 — JioFiber (IPv6)
IP Format: 2409:... → IPv6

Path Length: 13 hops

Final Hop: dell1s20-in-x0e.1e100.net

No packet loss

Latency Avg: ~45ms

Clean and consistent, minor jitter at last hop

Some intermediate hops didn’t respond (ICMP filtered) — expected

✅ Network 2 — DSL WiFi (IPv4)
IP Format: 192.168.1.15 → IPv4 (Private)

Path Length: 8 hops

Final Hop: dell1s09-in-f14.1e100.net

No packet loss

Latency spike at Hop 4 (~96.7ms) with high jitter (StDev = 32.1ms)

Overall faster early hops, shorter route

Clean resolution, but potential congestion at ISP edge

📈 Outcome:
Understood hop-by-hop breakdown of packet journey

Visually verified protocol switch (IPv6 → IPv4)

Saw practical effects of ICMP filtering and routing bottlenecks

Regained CLI groove and system-level observation clarity

🔁 Summary Table:
🔍 Topic	Tools Used	Core Insight
Network Path Diagnostics	ping, traceroute, mtr	Identify connection status, trace route, visualize latency & packet loss live
Protocol Observation	N/A	Detected and compared behavior over IPv6 vs IPv4 networks

🧠 Final Notes:
Felt like returning home. The hum of the terminal, the green pulse of mtr, and the whisper of raw hops reminded me why Project ONE is sacred.


