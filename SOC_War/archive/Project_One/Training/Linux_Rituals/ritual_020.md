# 🔪 CLI Ritual #020 – The Archive Blade

**Date:** 2025-05-18  
**Focus:** `tar`, `gzip`, archive creation and extraction

---
tar packs files (like a box)

gzip compresses that box (vacuum seal)

tar -xzvf opens + unpacks it again

Watch the filenames: underscore ≠ dash — terminal is literal





## 🔧 Commands Practiced

```bash
# Step into arena
cd ~/VanthLabs/Project_One/Training/Linux_Rituals/test_arena
mkdir tar_test && cd tar_test

# Create files
echo "Vanth was here" > blade1.txt
echo "The logs are sacred" > blade2.txt
echo "May 18 — Ritual Complete" > blade3.txt

# Archive them into one .tar file
tar -cvf vanth_archive.tar *.txt

# Compress the tarball
gzip vanth_archive.tar  # → vanth_archive.tar.gz

# Extract the archive
tar -xzvf vanth_archive.tar.gz

