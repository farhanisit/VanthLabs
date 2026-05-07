# 🔪 CLI Ritual #019 – The Hidden Layer

**Date:** 2025-05-18  
**Focus:** `ls -a`, hidden files, dotfiles, du usage with wildcards

---

## 🔧 Commands Practiced

```bash
touch .vanth_shadow
mkdir .vanth_hideout

ls               # Doesn’t show hidden
ls -a            # Shows . and ..
ls -A            # Shows all hidden, excludes . and ..
ls -alh          # Full listing, human readable

du -sh .vanth_*  # Size of all files/dirs starting with .vanth_

rm .vanth_shadow
rm -r .vanth_hideout

