# 🔪 CLI Ritual #016 – The WordCounter Blade

**Date:** 2025-05-17  
**Focus:** `wc`, `tee`, `grep`, pipelines

---

## 🔧 Commands Practiced

```bash
wc -l countme.txt
wc -w countme.txt
wc -c countme.txt
wc countme.txt

wc -l countme.txt | tee line_report.log
grep "vanth" countme.txt | wc -l | tee vanth_line_count.txt

