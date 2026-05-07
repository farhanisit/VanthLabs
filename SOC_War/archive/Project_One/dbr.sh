#!/bin/bash

echo "⚔️ Entering Battle Mode: Project_ONE ⚔️"
echo "📜 Today's Journal:"
cd ~/VanthLabs/Project_ONE/Logs

# Auto-create today's log if missing
today=$(date +%Y-%m-%d).md
if [ ! -f "$today" ]; then
    echo "✅ What I Did:" > "$today"
    echo "" >> "$today"
    echo "- " >> "$today"
    echo "" >> "$today"
    echo "❓ What Blocked Me:" >> "$today"
    echo "" >> "$today"
    echo "- " >> "$today"
    echo "" >> "$today"
    echo "⚡ What I Learned/Felt:" >> "$today"
    echo "" >> "$today"
    echo "- " >> "$today"
    echo "" >> "$today"
    echo "🎯 Tomorrow’s Target:" >> "$today"
    echo "" >> "$today"
    echo "- " >> "$today"
fi

# Open today's log automatically
nano "$today"

