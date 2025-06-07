### UFW command to open port 222
```bash
sudo ufw status numbered
sudo ufw delete 2

sudo ufw allow 2222/tcp
```
### Blocking IP address
```bash
sudo ufw deny from 167.71.46.247
```

## Best Practices for a Hardened SSH Setup (AWS/Linux)
```bash
sudo nano rotate_ssh_port.sh
chmod +x rotate_ssh_port.sh
sudo ./rotate_ssh_port.sh
```
### ✅ Auto-Rotates SSH Port
- Picks a random port in a safe range (e.g., 2000–65000)
- Updates /etc/ssh/sshd_config
- Updates UFW and Lightsail firewall (manually if needed)
- Restarts the SSH service
- Logs the new port locally
- Schedule this script via cron to run weekly or monthly
- Email the new port to your admin inbox
- Save the last 5 ports in a log and prevent reuse

### 🔐 SSH Hardening Checklist
Area	Recommendation
- 🔑 Authentication	Use SSH key-based login only (disable password login)
- 📦 Port	Change default port from 22 to a non-standard port (e.g., 2222, 54321)
- 🔁 Protocol	Use SSH Protocol 2 (Protocol 1 is insecure)
- 🔒 Root login	Disable root login over SSH (PermitRootLogin no)
- 👥 Users	Allow only specific users (AllowUsers youruser)
- 🔌 Idle connections	Disconnect idle sessions automatically
- 📛 Banners	Display legal warning banner (/etc/issue.net)
- 🔥 Firewall	Use UFW to allow only required ports (e.g., SSH, HTTP, HTTPS)
- 📉 Rate limiting	Use fail2ban to ban IPs with failed login attempts
- 📊 Logging	Enable SSHD logging (monitor with journalctl -u ssh)
- 🧪 Testing	Always keep a separate SSH session open when making changes



###  1. Lightsail Networking (cloud firewall)
- Blocked ports will never reach your server.
- Even if SSH is listening, if port 2222 is not allowed in Lightsail, it’s inaccessible.

###  2. UFW or iptables (OS firewall)
- If UFW is enabled and port 2222 is not allowed, the server will drop the traffic.
- Even if Lightsail allows it, and SSH is listening, Linux itself will block it.

####  UFW example
```bash

sudo ufw allow 2222/tcp
sudo ufw status
```
#### iptables example
```bash
sudo iptables -A INPUT -p tcp --dport 2222 -j ACCEPT
```
### 3. SSH Config (/etc/ssh/sshd_config)
- This sets what port SSHD listens on.
- If SSH isn’t told to listen on 2222, nothing will respond, even if firewalls allow it.

### 🔁 How They Work Together (must all align)
Let’s say you want SSH on port 2222:

### Step	Description	Command or Setting
✅ Cloud allows	Open port 2222 in Lightsail Networking	Lightsail → Networking → Add firewall rule for TCP 2222
✅ OS allows	Let traffic through UFW or iptables	sudo ufw allow 2222/tcp or iptables rule
✅ Service listens	SSH daemon listens on 2222	Edit /etc/ssh/sshd_config and set Port 2222
