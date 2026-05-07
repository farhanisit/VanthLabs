# Ritual 033 — Closing Gates

**Date:** 2025-08-23  
**Mode:** Active CLI (Defense Drill)  
**Location:** ~/VanthLabs/Project_One/Training/Linux_Rituals/

---

## Actions
- Recon: found `logioptio` (PID 971) listening on port 59869.  
- Mistaken attempt: `kill 59869` (failed, port ≠ PID).  
- Corrected: `kill 971` (process terminated).  
- Verified with `lsof` → gate closed, no longer listening.  

---

## Reflection
The Warden learned the difference between process IDs and ports.  
A Sentinel must strike the process, not the shadow.  
The Logitech daemon was silenced, the port sealed.  
Control means not just seeing gates, but choosing which to close.  

---

## Tag
**#Defense #Ports #Sentinel**

