### 🔄 Different Ways to Use or Distribute Keys
Method	Notes
✅ AWS Key Pair (.pem)	Download once → use with -i flag
✅ Manually Add Public Key	Paste into ~/.ssh/authorized_keys
✅ ssh-copy-id	Automates public key upload
✅ Ansible/Script	Automate adding public keys for multiple servers
✅ GitHub SSH Key	Share your public key to GitHub for repo access

### 🛠️ How Do You Generate SSH Keys?
✅ Method 1: Generate Locally
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Saves to: ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

✅ Method 2: Generate on AWS (EC2 key pair)
Go to AWS Console → EC2 → Key Pairs

AWS gives you a .pem file (your private key) — download and store safely.

The matching public key is injected into /home/ubuntu/.ssh/authorized_keys automatically when launching the instance.
### 📥 How to Copy Your Public Key to a Remote Server
✅ Manual (Paste the public key)
```bash
cat ~/.ssh/id_rsa.pub
```
Then paste the content into ~/.ssh/authorized_keys on the server.

✅ Use ssh-copy-id
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@your-server-ip
```
### 🧪 Test & Troubleshoot
#### 🔍 Permissions Matter!
~/.ssh folder: 700

authorized_keys: 600

id_rsa: 600

#### ❌ Common Issues
Issue	Fix
“Permission denied (publickey)”	Ensure .pem or key is correct, and server has your public key
“Bad permissions”	Fix with chmod 600 ~/.ssh/id_rsa
Wrong username	AWS: usually ubuntu or ec2-user, not root
