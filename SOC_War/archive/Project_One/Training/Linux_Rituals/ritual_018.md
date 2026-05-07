# 🔪 CLI Ritual #018 – Permission Magic & Ownership Control

**Date:** 2025-05-17  
**Focus:** `chmod`, `umask`, `stat`, `ls -l`, `rm`, permission logic

---

## 🔧 Commands Practiced

```bash
touch permission_test.txt
ls -l permission_test.txt

chmod 755 permission_test.txt
chmod u-w permission_test.txt
chmod 744 permission_test.txt

umask 077 == Meaning 0 permissions for the user; all perms for the group and others respectively.

stat permission_test.txt == to get the complete details of the permissions related.

Vanth Note: UMASK Logic
Default File Permission: 666 (rw-rw-rw-)

Default Directory Permission: 777 (rwxrwxrwx)

umask subtracts from these

umask	File Result	Meaning
022	644	I write, others read
077	600	Only I can read/write
002	664	Group writable (collab
