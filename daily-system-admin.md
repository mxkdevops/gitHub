#### 20th June 

```bash
grep "WP_DEBUG already defined" /var/log/apache2/error.log
grep "define('WP_DEBUG" /var/www/html/wp-config.php

✅ Fix It Now
Edit /var/www/html/wp-config.php and wrap each define like this:
sudo nano /var/www/html/wp-config.php


if (!defined('WP_DEBUG')) {
    define('WP_DEBUG', true);
}

if (!defined('WP_DEBUG_LOG')) {
    define('WP_DEBUG_LOG', true);
}

if (!defined('WP_DEBUG_DISPLAY')) {
    define('WP_DEBUG_DISPLAY', false);
}

grep "define('WP_DEBUG" /var/www/html/wp-config.php
sudo tail -f /var/log/apache2/error.log

```




### 14 th june 2025 at 07:50 am 







#### 6th June 2025 12;14 pm 
```bash
sudo ufw deny from 167.71.46.247
```
#### Create a Custom MOTD script 
```bash
sudo nano /etc/update-motd.d/99-custom
sudo chmod +x /etc/update-motd.d/99-custom
run-parts /etc/update-motd.d/
```

```bash
#!/bin/bash

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   🚀 Welcome to MKCloudAI Server     ║"
echo "╠══════════════════════════════════════╣"
echo "║ 🔒 Secured Ubuntu Server - DevOps    ║"
echo "║ 🕒 Uptime: $(uptime -p)              ║"
echo "║ 💡 Tip: Keep your system updated!    ║"
echo "╚══════════════════════════════════════╝"
echo ""

echo "🌐 Hostname: $(hostname)"
echo "🕒 Uptime: $(uptime -p)"
echo "💾 Disk Usage: $(df -h / | awk 'NR==2 {print $5 " used"}')"
echo "🧠 Memory Usage: $(free -m | awk '/Mem:/ {printf("%.1f%% used\n", $3/$2*100)}')"
echo ""

```
### 🧠 Final Goal:
### Add the following to /etc/update-motd.d/99-custom:

- 🚨 Alert if disk usage > 80%
- ☁️ AWS EC2 instance metadata
- 📅 Show any upcoming cron jobs (like daily/weekly tasks)








### 🧠 Top 20 Daily Tasks for a System Admin / Engineer (Technical List)
### Code of the Day 
Edit /etc/ssh/sshd_config and change: port 2222 # 
```bash
sudo nano /etc/ssh/sshd_config
CHnage ssh port from 22 to 2222
Disable password :PasswordAuthentication no
No Root login : PermitRootLogin no
sudo systemctl restart sshd
```


#### 🔧 1. Check System Health
```bash
uptime
top or htop
vmstat 1 5
```
#### 🧠 2. Monitor Disk Usage
```bash
df -h
du -sh /var/*
```
#### 🧩 3. Check Running Services
```bash
systemctl status
systemctl list-units --type=service
```
#### 🔐 4. Review SSH Logins & Failed Attempts
```bash
last -a
sudo journalctl -u ssh

sudo cat /var/log/auth.log | grep 'Failed'
```
#### 📦 5. Check for Package Updates
```bash
sudo apt update && apt list --upgradable
```
#### 📋 6. Monitor System Logs
```bash
sudo journalctl -xe
sudo tail -f /var/log/syslog
sudo tail -f /var/log/messages
```
#### 💥 7. Analyze System Errors
```bash
dmesg | less
sudo cat /var/log/kern.log
```
#### 🚀 8. Monitor System Performance
```bash
top, htop
iotop
free -m
```
#### 🌐 9. Check Network Status
```bash
ip a
ss -tulnp
ping 8.8.8.8
```
#### 🛡️ 10. Verify Firewall Rules
```bash
sudo ufw status
iptables -L -n -v
```
#### 📊 11. Check Disk I/O and Performance Bottlenecks
```bash
iostat
iotop
```
#### 📁 12. Monitor File System Changes (Security & Integrity)
```bash
auditd, inotify-tools, or AIDE
```
#### 🛠️ 13. Manage User Accounts & Access
```bash
sudo useradd / usermod / userdel
sudo passwd
groups username
```
#### 🔐 14. Rotate and Backup Logs
```bash
logrotate
tar / rsync / scp for backups
```
#### ☁️ 15. Monitor Cloud Resources (AWS CLI / Azure CLI)
```bash
aws ec2 describe-instances
aws s3 ls
aws cloudwatch get-metric-data
```
#### 📡 16. Check Scheduled Jobs
```bash
crontab -l
ls -la /etc/cron*
```
#### 📌 17. Apply Security Patches
```bash
sudo apt upgrade --with-new-pkgs
unattended-upgrades (automated)
```
#### 🛠️ 18. Restart or Reload Services
```bash
sudo systemctl restart nginx
sudo systemctl reload sshd
```
#### 🧾 19. Review Configuration Changes (Git or Diff Tools)
```bash
diff /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
git diff (if infra tracked)
```
#### 🔁 20. Test Automated Scripts or Backups
```bash
bash /scripts/daily-backup.sh
systemctl status backup.timer
```

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
## 7. all-in-one security check script: run-security-check.sh

```bash
#!/bin/bash

echo "=== [1] Suspicious Hidden Files in /home/ubuntu ==="
find /home/ubuntu -type f -name ".*" \
  ! -name ".bash*" \
  ! -name ".profile" \
  ! -name ".sudo_as_admin_successful" \
  ! -name ".cache" \
  ! -name ".local" \
  ! -name ".ssh" -ls

echo -e "\n=== [2] SetUID/SetGID Files System-wide ==="
find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -l {} \; 2>/dev/null

echo -e "\n=== [3] Top 15 Memory-Consuming Processes ==="
ps aux --sort=-%mem | head -n 15

echo -e "\n=== [4] User Crontab Entries ==="
crontab -l

echo -e "\n=== [5] System Cron Jobs ==="
sudo ls -la /etc/cron*
sudo cat /etc/crontab 2>/dev/null

echo -e "\n=== [6] chkrootkit: Installing and Scanning ==="
sudo apt update && sudo apt install -y chkrootkit
sudo chkrootkit

echo -e "\n=== [7] rkhunter: Installing and Scanning ==="
sudo apt install -y rkhunter
sudo rkhunter --update
sudo rkhunter --check

echo -e "\n✅ Security check complete. Please review the output for any suspicious activity."


```
## ▶️ How to Use:
Save the script:
```bash
nano run-security-check.sh
```
Paste the code above, then save and exit.

Make it executable:
```
chmod +x run-security-check.sh
```
Run it:
```bash
./run-security-check.sh
```
