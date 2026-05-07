# 🧠 Vanth Command Vault (Phase 1)

Your ritual grimoire of every command that matters.
Structured by real intent, not random syntax.

---

## 🔐 Permissions

### `chmod 755`
- **Meaning**: User = rwx, Group = rx, Others = rx
- **Used for**: Making a file executable by everyone, but writable only by the owner.
- **Example**: `chmod 755 log_cleaner.sh`

### `chmod 700`
- **Meaning**: User = rwx, Group = -, Others = -
- **Used for**: Private scripts only you should run.
- **Example**: `chmod 700 personal_diary.sh`

### `chown`
- **Used for**: Changing file owner.
- **Example**: `sudo chown farhanahmed script.sh`

---

## 📂 Navigation

### `cd`, `pushd`, `popd`
- **`cd`**: Change directory
- **`pushd` / `popd`**: Stack-based movement
- **Use Case**: Teleport between folders during scripts

---

## 🔧 File Manipulation

### `touch`, `cat`, `nano`, `echo`
- **`touch`**: Create a file
- **`cat`**: View contents
- **`nano`**: Edit inline
- **`echo "txt" > file`**: Write to a file

---

## 🔎 Content Extraction

### `cut`, `tr`, `awk`, `sed`
- **`cut -d ':' -f1 file.txt`**: Extract first field
- **`tr '[:upper:]' '[:lower:]'`**: Lowercase transform
- **`awk -F ':' '{print $1, $3}' file.txt`**: Smart extraction
- **`sed 's/old/new/' file.txt`**: Stream substitution

---

## 🧪 Automation Tips

### `chmod +x script.sh`
- **Why**: Makes script executable so it can be run with `./script.sh`

### `umask`
- **Shows**: Default permissions mask for new files

---

> 📓 Add new entries every time you hit a real-world case, mistake, or insight.
