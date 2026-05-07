#!/bin/bash

# Set today's date
TODAY=$(date +%Y-%m-%d)

# Define log filename
LOG_FILE="Logs/${TODAY}.md"

# Check if file already exists
if [ -f "$LOG_FILE" ]; then
    echo "Log for today already exists: $LOG_FILE"
else
    echo "Creating new log: $LOG_FILE"
    cat << EOF > "$LOG_FILE"
# 📜 Daily Log - $TODAY

✅ **What I Did:**  
- 

❓ **What Blocked Me:**  
- 

⚡ **What I Learned/Felt:**  
- 

🎯 **Tomorrow’s Target:**  
- 

🛡️ **Warden's Note:**  
- 
EOF
    echo "Log created successfully!"
fi

# Open it immediately with nano (or VS Code if you prefer)
nano "$LOG_FILE"

