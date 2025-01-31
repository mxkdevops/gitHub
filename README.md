# gitHub
# 1. Install the Required Tools

Before starting, make sure you have the following installed:
Git: Download and install it from git-scm.com
VS Code: Install it from code.visualstudio.com
GitHub Account: Create one at github.com

# 2. Set Up a Local Repository in Windows Using VS Code

#### Open VS Code
### Initialize a Git Repository

Open a folder where you want to store your project (e.g., C:\Users\YourName\Documents\MyProject).

#### Open VS Code, go to Terminal → New Terminal, and run:

```base
git init

```
This initializes a local repository inside your folder.

### Check Git Version and Path

```base
git --version
```
### Check Git Version and Path
```base
where.exe git
```
### Configure Git (First-Time Setup)
#### Set your name and email (for commits):

```bash
git config --global user.name "Mohammad"
git config --global user.email "mxkdevops.com"

```
###  Create or Add Files
Create a new file (e.g., index.html or README.md) inside your project folder.
### Add and Commit Files
```bash
git status
```
### Add all files to staging:
```bash
git add .
```

### Commit the changes:
```bash
git commit -m "Initial commit"
```

## Push the Local Repository to GitHub
###  A. Using HTTPS
### Create a Repository on GitHub

Go to GitHub, click New Repository, name it, and click Create.
Copy the HTTPS link from GitHub (e.g.,https://github.com/mxkdevops/blue-bengal-website.git)).

### Connect the Local Repository
####  Run the following command in the VS Code terminal
```bash
git remote add origin https://github.com/mxkdevops/blue-bengal-website.git

```
### Verify the repote URL
```bash
git remote -v
```
###Push to github 
```bash
git push -u origin main
```
It will ask for your GitHub username and password.

## Using SSH (More Secure)
### Generate an SSH Key (If You Haven't Already)

### Open Git Bash and run:
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```
Press Enter multiple times to accept the default location (C:\Users\YourName\.ssh\id_rsa).

### Add the SSH Key to GitHub
```bash
cat ~/.ssh/id_rsa.pub
```

### Go to GitHub → Settings → SSH and GPG keys → New SSH Key, then paste the key.
### Test the SSH Connection

```bash
ssh -T git@github.com
```
### If successful, you’ll see:
``
Hi YourUsername! You've successfully authenticated.
Connect and Push Using SSH
``
Add the remote repository using SSH:
sh
Copy
Edit
git remote add origin git@github.com:YourUsername/MyProject.git
Push changes:
sh
Copy
Edit
git push -u origin main



### Saving Changes (Commit)
### Publish to GitHub 
### Make Changes to Remote GitHub File (Commit & Push)
### Sync Changes from GitHub to Local File (Pull)
### Staging, i.e., Choosing Changes to Commit (Stage)
