## 🔧 STEP : Configure Jail for Apache
```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```
Reload fail2ban
```bash
sudo fail2ban-client reload
sudo fail2ban-client status apache-badbots
sudo systemctl restart fail2ban
```
You should now see it monitoring /var/log/apache2/access.log and ready to ban any IPs matching those bot user agents.
```bash
sudo tail -f /var/log/apache2/access.log
sudo tail -n 50 /var/log/fail2ban.log
```


Full jail example:
```bash
[apache-badbots]
enabled = true
port    = http,https
filter  = apache-badbots
logpath = /var/log/apache2/access.log
maxretry = 1
bantime = 86400
findtime = 600
action = ufw[port=http, protocol=tcp]
```
✅ 4. Check Fail2Ban Status
Check all jails:

bash
Copy
Edit
sudo fail2ban-client status
You should now see apache-badbots listed.

Then:

bash
Copy
Edit
sudo fail2ban-client status apache-badbots
### 🧪 Optional: Simulate a Bad Bot to Test
You can simulate a bad bot by manually adding a fake line to the Apache access log:
```bash
echo '123.123.123.123 - - [08/Jun/2025:10:23:00 +0000] "GET / HTTP/1.1" 200 2326 "-" "Jorgee"' | 
```

