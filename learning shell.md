### Shebang :Define script interpreter 
```bash
#!/bin/bash
```
This tells Linux: run this script using Bash, not Python or another shell.
✅ Why it matters: Always define the shell to ensure the right interpreter is used — avoids hidden bugs.

### 📝 Comments & Metadata

```bash
# SSH Port Rotator Script
# Author: mkcloudai.com
# Caution: Use with care to avoid locking yourself out!

```
Adding comments and metadata helps others (and future you) understand what this script does at a glance.
✅ Pro Tip: Always describe what a script does, especially for security tools. Future you will thank you.


### 📂 Define important variables
```bash
CONFIG="/etc/ssh/sshd_config"
LOG="/var/log/ssh_port_rotation.log"
PORT_RANGE_START=2000
PORT_RANGE_END=65000
```
✅ Why: Keeping config & constants at the top makes your code easier to manage and modify.
### 🎲 Generate a random port
```bash
NEW_PORT=$(shuf -i ${PORT_RANGE_START}-${PORT_RANGE_END} -n 1)
```
-shuf randomly picks a number in the given range.
-n 1 means “just one number.”
✅ Mindset: Think like an attacker — avoid predictable patterns. This helps evade port scanners that look for port 22.
### 🔍 Check if the port is already used
```bash
if ss -tuln | grep -q ":$NEW_PORT"; then
  echo "Port $NEW_PORT already in use. Try again."
  exit 1
fi
```
ss -tuln lists active ports.
grep -q silently checks if the port is already in use.
✅ Mindset: Always validate before making changes. Avoid blindly overwriting configs — prevent disasters.
### 📢 Inform user
```bash
echo "🔄 Changing SSH port to: $NEW_PORT"
```
User feedback matters. Good CLI tools communicate clearly what’s happening.
✅ Pro Tip: Clear output helps with debugging and makes scripts user-friendly.
### 📦 Backup ssh config
```bash
cp $CONFIG ${CONFIG}.bak
```
Always back up critical files before editing.
✅ Mindset: A good sysadmin never trusts a one-shot change. Backups = safety net.
### ✏️ Update the sshd_config with the new port
```bash
sed -i "/^Port /d" $CONFIG
echo "Port $NEW_PORT" >> $CONFIG
```
sed deletes any existing Port lines.
echo appends the new port to the file.
✅ Mindset: Make scripts idempotent — it should work the same every time you run it, without breaking things.
### update firewall (UFW)
```bash
ufw allow $NEW_PORT/tcp
ufw delete allow 22/tcp
```
Allow the new port.
Block the old default port 22.
✅ Pro Tip: Always sync firewall rules with config changes, or you’ll lock yourself out. 👀
## ♻️ Restart SSH
```bash
systemctl restart ssh
```
Applies the changes immediately.
✅ Mindset: Scripts should be complete — do not leave manual steps unless absolutely necessary.

### 🧾 Log the change
```bash
echo "$(date): SSH port changed to $NEW_PORT" >> $LOG
```
Tracks when and to what port the change happened.
✅ Good practice: Logging helps in troubleshooting, auditing, and rollback.
### ✅ Final user feedback
```bash
echo "✅ SSH port changed to $NEW_PORT"
echo "📌 Important: Next time connect with: ssh -p $NEW_PORT -i key.pem user@your-ip"
```
Clear, user-friendly output.
Tells the user what to do next to avoid confusion.
✅ Mindset: A good engineer thinks about the end-user experience, even in CLI tools.

Want to Go Pro?
Here’s how you could take this further:

📧Send new port to your email using mailx or sendmail
🔒 Add root-only permissions: chmod 700 to the script
🧪 Build a safe rollback mechanism (if new port fails, revert)
🔄 Run it monthly using cron
