
```bash
- Even though it's from AWS, this activity is clearly unauthorized scanning:
sudo ufw insert 1 deny from 3.140.191.144 comment 'Nmap scan from AWS EC2'

Optionally log it:
echo "$(date) - Blocked AWS IP 3.140.191.144 after Nmap scan" | sudo tee -a /var/log/security_incidents.log

✅ 1. Check total number of SSH failures:
sudo grep "Failed password" /var/log/auth.log | wc -l

✅ 2. See all recent logins (successful & failed):
last -a | head -20

✅ 3. Search rotated logs (auth.log.1 or gzipped):
sudo zgrep "Failed password" /var/log/auth.log.*

✅ 4. Confirm fail2ban is actively protecting SSH
sudo fail2ban-client status sshd

✅ 5. Open the file in a code editor or terminal:
 sudo nano /var/www/html/wp-config.php

✅ 6. RUn 

grep "define('WP_DEBUG" /var/www/html/wp-config.php
🔍 7. Check Apache Error Log (Live)
sudo tail -f /var/log/apache2/error.log

🔍 8. Search for Past WP_DEBUG Errors
grep "WP_DEBUG already defined" /var/log/apache2/error.log

📦 9. Bonus: Confirm no duplicate WP_DEBUG in config
grep "define('WP_DEBUG" /var/www/html/wp-config.php
✅ 10. Check Disk Usage
df -h
✅ 11. Check Memory and Swap
free -h
✅ 12. Check CPU and Top Processes
top -o %CPU

✅ 13. Check Apache Service Status
sudo systemctl status apache2

✅ 14 If inactive or failed:
journalctl -xe | grep apache2

✅ 15. Check MySQL/MariaDB (if using local DB)
udo systemctl status mysql

✅ 16 Test DB login:
mysql -u wpuser -p

✅ 17. View Apache Error Log (recent lines)
sudo tail -n 50 /var/log/apache2/error.log

✅ 18. Check Syslog for Kernel / System Errors
sudo tail -n 50 /var/log/syslog

✅ 19. Check WordPress File Permissions (Basic Audit)
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;

✅ 20. Check for Open Ports (Apache, SSH, etc.)
sudo ss -tuln

✅ 21. Check UFW (Firewall) Rules
sudo ufw status verbose
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable

✅ 22. Check Running WordPress Cron Jobs
grep DISABLE_WP_CRON /var/www/html/wp-config.php

✅ 23 disabled, then server must have real cron:
crontab -l

✅ 24. Check Active Connections (DDoS or Bot Hits)
sudo netstat -an | grep :80 | wc -l

✅ 25.and for top IPs:
sudo netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head

✅ 26. Check Auto Updates (Security Patches)
sudo cat /etc/apt/apt.conf.d/20auto-upgrades

✅ 27. Apache Access Log — Check Traffic Patterns
sudo tail -n 100 /var/log/apache2/access.log
📌 Look for: spikes from one IP, 404 floods, bots, vulnerability scanners.

✅ 28. Syslog — Hardware & Kernel Issues
sudo grep -i error /var/log/syslog | tail -n 50
📌 Look for: disk errors, OOM killer, service restarts, etc

✅ 29. Auth Log — Security Breaches or Failed Logins
sudo grep "Failed password" /var/log/auth.log | tail -n 20
📌 Look for: brute force attempts, failed logins.

✅ 30. Backup Files
sudo tar -czvf /home/ubuntu/wp-site-backup-$(date +%F).tar.gz /var/www/html

✅ 31. Backup Database
mysqldump -u wpuser -p wordpressdb > /home/ubuntu/wp-db-backup-$(date +%F).sql
📌 Both backups go to /home/ubuntu. Secure and copy them.

🔁 32: Transfer Files (SCP Example)
scp -i /path/to/key.pem ubuntu@<EC2-IP>:/home/ubuntu/wp-site-backup-2025-06-20.tar.gz .

✅ 33. Apache Virtual Host
sudo nano /etc/apache2/sites-available/000-default.conf

✅ 34 Change/add:
ServerName yourdomain.com
DocumentRoot /var/www/html
sudo systemctl reload apache2

✅ 35. PHP Settings (e.g., upload size)
sudo nano /etc/php/8.1/apache2/php.ini
upload_max_filesize = 32M
post_max_size = 64M

✅ 36 Create a Git Repository (For WordPress Version Control)
cd /var/www/html
sudo git init
sudo git add .
sudo git commit -m "Initial WordPress commit"

✅ 37 Set file ownership back to www-data:
sudo chown -R www-data:www-data /var/www/html

✅ 38 Install & Configure Software (Fail2ban for SSH Protection)
sudo apt update
sudo apt install fail2ban -y

✅ 39 Create config:
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
Edit jail config:
sudo nano /etc/fail2ban/jail.local
[sshd]
enabled = true






```
