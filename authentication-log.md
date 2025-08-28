
```bash
sudo grep "maximum authentication attempts" /var/log/auth.log
sudo grep "Too many authentication failures" /var/log/auth.log
sudo grep "invalid user admin" /var/log/auth.log
sudo grep "session opened" /var/log/auth.log
sudo grep "invalid user" /var/log/auth.log
sudo grep "sudo" /var/log/auth.log
sudo grep "Failed password" /var/log/auth.log
sudo grep "Accepted password" /var/log/auth.log


```
###  ✅ General System Issues
```bash
#### System Errors
grep -iE "error|fail|warn" /var/log/syslog | tail -n 10

####  SSH Attempts
grep -iE "Accepted|Failed|authentication failure" /var/log/auth.log | tail -n 10

#### ✅ Apache Errors
grep -iE "error|warn|fail" /var/log/apache2/error.log | tail -n 10

#### Wordpress log 
wp_log=/var/www/html/wp-content/debug.log
tail -n 10 "$wp_log" | grep -iE "error|warn|notice"
```
# SSH password logins (rare if you use keys)
sudo grep "Accepted password" /var/log/auth.log

# SSH key logins (most common in hardened setups)
sudo grep "Accepted publickey" /var/log/auth.log

# PAM session opened (covers ssh + sudo + su)
sudo grep "session opened" /var/log/auth.log


