cheat_sheet_content = """
# 🕵️‍♂️ Network Forensics CLI Cheat Sheet — Project ONE Edition

## 🔍 LIST OPEN PORTS & LISTENING SERVICES

### 1. List all network connections with PID
sudo lsof -i

### 2. List only listening services on specific port
sudo lsof -nP -iTCP:80 -sTCP:LISTEN

### 3. List processes using HTTPS (port 443)
sudo lsof -nP -iTCP:443 -sTCP:ESTABLISHED

### 4. General netstat to view connections
netstat -an

### 5. Show listening ports and their owning processes (Linux)
sudo netstat -tulnp

### 6. On macOS, use `ss` equivalent (not available)
Use `lsof` or install `ss` via `brew install iproute2mac`

---

## 🌍 WHOIS & IP Analysis

### 7. Basic WHOIS lookup
whois <IP_ADDRESS>

### 8. Find which app is making connection to a remote IP
sudo lsof -i @<IP_ADDRESS>

---

## 🔒 Extra: Real-time Network Monitoring

### 9. Use `iftop` to monitor live bandwidth usage
sudo iftop

### 10. Use `nethogs` to view per-process network usage
sudo nethogs

---

## 🛠️ Bonus: Save lsof output to file
sudo lsof -nP -iTCP -sTCP:LISTEN > active_listeners.txt

---

## 📦 Location:
Saved under `~/VanthLabs/Project_One/Scripts/Network_CheatSheets/cli_network_forensics.md`
"""

# Define the save path again
base_dir = Path("/mnt/data/VanthLabs/Project_One/Scripts/Network_CheatSheets")
base_dir.mkdir(parents=True, exist_ok=True)
file_path = base_dir / "cli_network_forensics.md"

# Save the file
file_path.write_text(cheat_sheet_content)

file_path.name
Result
'cli_network_forensics.md'
