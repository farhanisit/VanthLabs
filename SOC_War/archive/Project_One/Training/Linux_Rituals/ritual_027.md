# CLI Ritual #028 – Guardians of the Node (macOS Edition)

**Codename**: "Guardians of the Node"  
**Date**: 30 May 2025  
**Focus**: Port Scanning, Socket Surveillance, Process Mapping  
**Mode**: Blue Team Resurrection  
**OS**: macOS

---

## 🎭 Command Archetypes:

| Tool      | Role           | Purpose                                  |
|-----------|----------------|------------------------------------------|
| `lsof`    | Detective      | Who's using what ports                   |
| `netstat` | Grandpa        | Legacy but wise network insights         |
| `tcp6`    | Phantom        | IPv6-only tunnels detection              |

---

## 🔍 Key Commands (macOS-Compatible)

### 1. Show active TCP listeners

sudo lsof -iTCP -sTCP:LISTEN -n -P

2. Show process using specific port (e.g., 22)

sudo lsof -i :22
3. Show established connections

sudo lsof -i | grep ESTABLISHED
4. Netstat-based listener check

netstat -anv | grep LISTEN
5. IPv6 socket check (phantom scan)

netstat -an | grep tcp6
🔐 Takeaways:
ss is unavailable on macOS; fallback to lsof and netstat

Listening services must be traced to PIDs and verified

IPv6 connections often go unnoticed — always scan for them

Blue Team mindset = know every tunnel into your node
