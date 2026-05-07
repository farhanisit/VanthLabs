# 🔪 CLI Ritual #017 – Directory Manipulation & File Movement

**Date:** 2025-05-17  
**Focus:** `mkdir`, `mv`, `cp`, `rm`, `rmdir`, `find`

---

## 🔧 Commands Practiced

```bash
mkdir test_arena
cd test_arena

touch alpha.txt beta.txt gamma.txt
mkdir chaos_zone backup_zone

mv *.txt chaos_zone/
cp chaos_zone/*.txt backup_zone/
rm chaos_zone/beta.txt
rm -r backup_zone/

find . -name "*.txt"

