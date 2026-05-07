#!/bin/bash
#!/bin/bash

DATE=$1
NUM=$(date -j -f "%Y-%m-%d" "$DATE" +"%d" 2>/dev/null)

if [[ $? -ne 0 ]]; then
    echo "Invalid date format. Use YYYY-MM-DD"
    exit 1
fi

PADDED=$(printf "%03d" "$NUM")
FILE=~/VanthLabs/Project_One/Training/Linux_Rituals/ritual_${PADDED}.md

if [[ -f "$FILE" ]]; then
    nano "$FILE"
else
    echo "No ritual found for $DATE → $FILE"
fi

DATE=$1
FILE=~/VanthLabs/Project_One/Training/Linux_Rituals/ritual_$(date -j -f "%Y-%m-%d" "$DATE" +"%d").md

if [[ -f "$FILE" ]]; then
    nano "$FILE"
else
    echo "No ritual found for $DATE → $FILE"
fi

