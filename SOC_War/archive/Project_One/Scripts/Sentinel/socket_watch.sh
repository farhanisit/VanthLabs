#!/bin/bash

LOGFILE="$HOME/VanthLabs/Project_One/Logs/socket_report.log"
SUSPICIOUS_PORTS=(31337 4444 5555)

echo "[$(date)] Checking open ports..." >> "$LOGFILE"

# Scan open listening ports
lsof -nP -iTCP -sTCP:LISTEN | awk 'NR>1 {print $9}' | while read portInfo; do
    port=$(echo "$portInfo" | awk -F':' '{print $NF}')
    
    if [[ " ${SUSPICIOUS_PORTS[@]} " =~ " $port " ]]; then
        echo "[$(date)] ⚠️ ALERT: Suspicious port $port detected!" >> "$LOGFILE"
    fi
done

echo "[$(date)] Scan complete." >> "$LOGFILE"

#!/bin/bash

echo "TEST: script ran" >> $HOME/test_script.log

