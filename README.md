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


### Saving Changes (Commit)
### Publish to GitHub 
### Make Changes to Remote GitHub File (Commit & Push)
### Sync Changes from GitHub to Local File (Pull)
### Staging, i.e., Choosing Changes to Commit (Stage)
