#!/bin/bash

# === Vanth Log Generator ===

LOG_DIR=~/VanthLabs/Project_One/Logs
TODAY=$(date "+%Y-%m-%d")
LOG_FILE="$LOG_DIR/$TODAY.md"

mkdir -p "$LOG_DIR"

# === If log exists but is incomplete ===
if [[ -f "$LOG_FILE" ]]; then
  if grep -q "❓ What Blocked Me:" "$LOG_FILE" && ! grep -q "✅ LOG COMPLETE" "$LOG_FILE"; then
    echo "🟡 Log for today exists but is incomplete. Time to finish it, Warden."
    open "$LOG_FILE"
    exit 1
  fi

  echo "✅ Log for today already completed."
  exit 0
fi

# === Create new log ===
cat > "$LOG_FILE" <<EOF
✅ What I Did:

❓ What Blocked Me:

⚡ What I Learned/Felt:

🎯 Tomorrow’s Target:
EOF

echo "📓 New log for $TODAY created. Time to reflect, Warden."
open "$LOG_FILE"

