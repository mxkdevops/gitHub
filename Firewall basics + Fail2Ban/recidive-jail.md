sudo ufw deny from 14.18.41.55

sudo nano /etc/fail2ban/jail.d/recidive.conf
[recidive]
enabled  = true
logpath  = /var/log/fail2ban.log
banaction = iptables-allports
bantime  = 1d
findtime = 1h
maxretry = 5
