
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
# ✅ General System Issues
grep -iE "error|fail|warn" /var/log/syslog | tail -n 10 2

# ✅ SSH Attempts
grep -iE "Accepted|Failed|authentication failure" /var/log/auth.log | tail -n 10 2

### Apache errors

tail -n 10 /var/log/apache2/error.log | grep -iE "error|warn|fail

#### Wordpress log 
wp-log=/var/www/html/wp-content/debug.log
tail -n 10 "$wp_log" | grep -iE "error|warn|notice "



