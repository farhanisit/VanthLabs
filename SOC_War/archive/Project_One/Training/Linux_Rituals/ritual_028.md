
# 🕷️ Ritual 028 – The Packet Weaver (macOS Edition)

**Date:** 2025-06-08  
**Mode:** Practical  
**System:** macOS (Unix-based)

---

## 🎯 Objective
Establish foundational packet sniffing skillset using `tcpdump`, aligned with macOS interface logic. Prepare for Wireshark + Tshark rituals.

---

## 🧪 Commands Practiced

### 🔎 Interface Discovery
```
networksetup -listallhardwareports
ifconfig | grep -B2 "status: active"
ipconfig getifaddr en0  # To verify IP of Wi-Fi interface
```

### 🎯 Packet Capture (HTTPS)
```
sudo tcpdump -i en0 port 443
```

Observed:  
- Encrypted packets (TLS)  
- `len 0` or unreadable payloads due to SSL/TLS encryption  
- Capture working as expected on interface `en0`

### 💾 Save to File
```
sudo tcpdump -i en0 -w ~/Desktop/vanth_capture.pcap
```

---

## 🧠 Takeaways
- Encrypted traffic (HTTPS) will show metadata but not payloads  
- `tcpdump` is a CLI warrior tool — use it when GUI fails  
- Understanding interface names on macOS is critical (`en0`, `lo0`, `utun`)  
- `-w` creates .pcap file for GUI analysis in Wireshark  

---

## 🗂️ Alignment
This ritual enables:
- Network analysis
- SOC packet forensics
- Trigger lab eligibility (e.g., Bettercap, Suricata)

> “See the packet. Become the wire. Smell the breach.”  
— Prof MiAmor

