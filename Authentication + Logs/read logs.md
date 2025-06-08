sudo cat /var/log/auth.log | grep "Failed\|Accepted\|sudo"
sudo journalctl _COMM=sshd -xe


## Understand auth mechanisms, read logs

### Password-Based Auth
/etc/passwd – User accounts
/etc/shadow – Encrypted passwords
pam_unix.so – PAM module for Unix auth

### Public Key Authentication (SSH)
Keys: ~/.ssh/id_rsa, ~/.ssh/authorized_keys
Daemon config: /etc/ssh/sshd_config
Example: PasswordAuthentication no, PubkeyAuthentication yes

### Multi-Factor Authentication (MFA)
TOTP via Google Authenticator
pam_google_authenticator.so

### PAM (Pluggable Authentication Modules)
Configs: /etc/pam.d/
Example: /etc/pam.d/sshd

### Centralized Auth (Advanced)
LDAP, Active Directory, Kerberos, SSO


