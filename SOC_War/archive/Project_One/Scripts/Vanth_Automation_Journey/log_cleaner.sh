#!/bin/bash
#!/bin/bash

# Check for dry run mode
DRY_RUN=false
if [[ "$1" == "--dry" ]]; then
  DRY_RUN=true
fi

LOG_DIR=~/VanthLabs/Project_ONE/Logs
OUTPUT=~/VanthLabs/Project_ONE/Artifacts/weekly_summary.md

# Begin summary file or simulate output
$DRY_RUN || echo "## ✅ Weekly Activity Summary" > "$OUTPUT"

# Process each markdown log from the last 7 days
find "$LOG_DIR" -name "*.md" -mtime -7 | sort | while read file; do
    if $DRY_RUN; then
        echo -e "\033[1;34m[DRY] Processing $(basename "$file")\033[0m"
        echo -e "\n### From $(basename "$file" .md):"
        sed -n '/^✅ What I Did:/,/^❓/p' "$file" | sed '$d'
    else
        echo -e "\033[1;34m[INFO] Processing $(basename "$file")\033[0m"
        echo -e "\n### From $(basename "$file" .md):" >> "$OUTPUT"
        sed -n '/^✅ What I Did:/,/^❓/p' "$file" | sed '$d' >> "$OUTPUT"
    fi
done

# Optional typo fix
$DRY_RUN || sed -i '' -e 's/recieve/receive/g' "$OUTPUT"

# Timestamp
$DRY_RUN || echo -e "\n---\n🕒 Generated on: $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT"

# Final message
if $DRY_RUN; then
    echo -e "\033[1;33m[DRY RUN] No file written. Preview only.\033[0m"
else
    echo -e "\033[1;32m[OK] Log cleaning complete. Summary saved to $OUTPUT\033[0m"
fi

