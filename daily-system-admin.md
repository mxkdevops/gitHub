
## 🛡️ 1. Check for Suspicious Hidden Files
Hidden files start with a . — but we’ll look for anything unusual outside the normal patterns.
```bash
find /home/ubuntu -type f -name ".*" ! -name ".bash*" ! -name ".profile" ! -name ".sudo_as_admin_successful" ! -name ".cache" ! -name ".local" ! -name ".ssh" -ls
```
🔎 This finds hidden files that are not typical dotfiles.

## 🛠️ 2. Check for Files with SetUID or SetGID (security-sensitive)
```bash
find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -l {} \; 2>/dev/null
```
🔍 This finds any files with setuid or setgid permissions, often used in privilege escalation.

## 🧪 3. Check for Suspicious Processes
```bash
ps aux --sort=-%mem | head -n 15
```
🔎 Lists the top memory-using processes — good for spotting rogue behavior.

## 🔍 4. Look for Strange Cron Jobs
```bash
crontab -l
sudo ls -la /etc/cron*
```
🔎 See if anything unfamiliar is scheduled.


## 🧰 5. Run Rootkit Check (Install chkrootkit)
Install and run chkrootkit:

```bash
sudo apt update && sudo apt install chkrootkit -y
sudo chkrootkit
```
📦 This tool scans for known rootkits.

## 🧰 6. Run rkhunter (Rootkit Hunter)
Another rootkit tool:

```bash
sudo apt install rkhunter -y
sudo rkhunter --update
sudo rkhunter --check
```
