Ritual_031.md (Final Log)
# Ritual 031 — Port & Process Vision

**Date:** 2025-08-22  
**Mode:** Active CLI (Investigation Drill)  
**Location:** ~/VanthLabs/Project_One/Training/Linux_Rituals/

---

## Command of the Day
```bash
|_________sudo lsof -nP -iTCP -sTCP:LISTEN | head -10_________|

Key Findings

rapportd (PID 427) → Apple Bluetooth/Handoff daemon, listening on 52352 (IPv4+IPv6).

ControlCenter (PID 507) → AirPlay/Screen sharing services, listening on 5000/7000.

logioptio (PID 971) → Logitech Options daemon, local config service on 59869.

adb (PID 1091) → Android Debug Bridge, bound to localhost:5037.

Reflection

The Warden now sees the gates of his own fortress.
Not all doors are opened by enemies; some are opened by his own keepers (Bluetooth, AirPlay, peripherals).
The lesson: to defend, first you must know which gates exist.
Today, the vision cleared — tomorrow, the hunt begins.
