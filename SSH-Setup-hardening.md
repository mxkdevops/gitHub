# 🔐 SSH Setup, Hardening, and Multi-User Key Management (EC2 / Lightsail)

## ✅ Step-by-Step SSH Setup (EC2 or Lightsail)

1. **Launch Instance**
   - EC2: Select AMI, create/download key pair (`.pem`), allow SSH (port 22) in Security Group.
   - Lightsail: Download the SSH key from the interface or use browser-based terminal.

2. **Move SSH Key to Secure Folder**
   ```bash
   mkdir -p ~/.ssh
   mv ~/Downloads/your-key.pem ~/.ssh/
   chmod 400 ~/.ssh/your-key.pem
```
3.Connect to Instance
```bash
ssh -i ~/.ssh/your-key.pem ec2-user@<public-ip>   # Amazon Linux
ssh -i ~/.ssh/your-key.pem ubuntu@<public-ip>     # Ubuntu
```
4.Optional: SSH Config Entry
Add to ~/.ssh/config:
```bash
Host myserver
  HostName <public-ip>
  User ec2-user
  IdentityFile ~/.ssh/your-key.pem
```
5.Login Using Alias

ssh myserver
## 🔐 SSH Hardening (via sshd_config)
Backup sshd_config
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```
Edit Configuration
```bash
sudo nano /etc/ssh/sshd_config
```
8. Recommended Changes
```bash
Port 2222
PermitRootLogin no
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM yes
AllowUsers ec2-user
```
9.Restart SSH
```bash
sudo systemctl restart sshd
```
Update Security Group
Allow new SSH port (e.g. 2222)
Remove port 22 if desired

## 🚨 Common SSH Issues
Issue	Cause / Fix
- Permission denied (publickey)	Wrong username or .pem permissions (use chmod 400)
- Connection timed out	Port 22/2222 blocked or no public IP
- Locked out after config change	Use EC2 Session Manager or Lightsail console
- Host key verification failed	Remove old entry from ~/.ssh/known_hosts
- Slow login	Add UseDNS no to sshd_config

## 🧩 One-Liner SSH Hardening Script
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak && sudo sed -i '/^#Port /c\Port 2222' /etc/ssh/sshd_config && sudo sed -i '/^#PermitRootLogin /c\PermitRootLogin no' /etc/ssh/sshd_config && sudo sed -i '/^#PasswordAuthentication /c\PasswordAuthentication no' /etc/ssh/sshd_config && echo -e '\nAllowUsers ec2-user\nUseDNS no' | sudo tee -a /etc/ssh/sshd_config && sudo systemctl restart sshd
```
⚠️ Ensure port 2222 is allowed before applying this!

## 🔐 Public Key Location on Server
Remote authorized keys live in:
```bash
/home/<username>/.ssh/authorized_keys
When you launch EC2 or Lightsail, AWS auto-injects the .pem public key here for the default user.
```
## 🔄 Script to Manage Multiple Users' SSH Keys
```bash
#!/bin/bash

# Usage: sudo ./manage_ssh_keys.sh username1:pubkey1.pub username2:pubkey2.pub ...

set -e

echo "🔐 Managing SSH keys..."

for entry in "$@"; do
    IFS=':' read -r username pubkey <<< "$entry"

    if [[ -z "$username" || -z "$pubkey" || ! -f "$pubkey" ]]; then
        echo "❌ Invalid input: $entry"
        continue
    fi

    echo "📦 Processing user: $username"

    if ! id "$username" &>/dev/null; then
        sudo useradd -m -s /bin/bash "$username"
        echo "✅ Created user $username"
    fi

    ssh_dir="/home/$username/.ssh"
    mkdir -p "$ssh_dir"
    chmod 700 "$ssh_dir"
    chown "$username:$username" "$ssh_dir"

    cat "$pubkey" >> "$ssh_dir/authorized_keys"
    chmod 600 "$ssh_dir/authorized_keys"
    chown "$username:$username" "$ssh_dir/authorized_keys"

    echo "🔑 Added key for $username"
done

echo "✅ All SSH keys managed successfully."
```
Example:
```bash
sudo ./manage_ssh_keys.sh alice:alice.pub bob:bob.pub
```
## 🔒 SSH Best Practices
-Disable PasswordAuthentication

-Use non-root users only

-Limit users via AllowUsers

-Use non-default port (e.g., 2222)

-Monitor /var/log/auth.log or /var/log/secure
