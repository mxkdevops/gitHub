## 1. Lightsail Networking (cloud firewall)
Blocked ports will never reach your server.
Even if SSH is listening, if port 2222 is not allowed in Lightsail, it’s inaccessible.

## 2. UFW or iptables (OS firewall)
If UFW is enabled and port 2222 is not allowed, the server will drop the traffic.
Even if Lightsail allows it, and SSH is listening, Linux itself will block it.

####  UFW example
sudo ufw allow 2222/tcp
sudo ufw status
#### iptables example
sudo iptables -A INPUT -p tcp --dport 2222 -j ACCEPT

### 3. SSH Config (/etc/ssh/sshd_config)
This sets what port SSHD listens on.
If SSH isn’t told to listen on 2222, nothing will respond, even if firewalls allow it.

### 🔁 How They Work Together (must all align)
Let’s say you want SSH on port 2222:

Step	Description	Command or Setting
✅ Cloud allows	Open port 2222 in Lightsail Networking	Lightsail → Networking → Add firewall rule for TCP 2222
✅ OS allows	Let traffic through UFW or iptables	sudo ufw allow 2222/tcp or iptables rule
✅ Service listens	SSH daemon listens on 2222	Edit /etc/ssh/sshd_config and set Port 2222
