# How to Install Chocolatey on Windows

## Step 1: Open PowerShell as Administrator

- Press the `Win` key, type **PowerShell**
- Right-click **Windows PowerShell** and select **Run as administrator**

## Step 2: Set Execution Policy

Run this command to allow script execution temporarily:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
```
## Step 3: Install Chocolatey
Run the following command to download and install Chocolatey:

```powershell
iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex
```
## Step 4: Verify Installation
Close and reopen PowerShell, then check the installed version:
```bash
choco --version
```
### To install application using chocolaty 

```bash
choco install git -y
choco install python
choco upgrade awscli
choco list --localonly  # list installed packages
choco uninstall nodejs
```
