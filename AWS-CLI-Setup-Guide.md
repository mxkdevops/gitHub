
# AWS CLI Full Setup Guide

## 1. What is AWS CLI?

AWS CLI (Command Line Interface) is a unified tool to manage AWS services from your terminal or command prompt. You can control multiple AWS services and automate tasks using scripts.

---

## 2. Prerequisites

- A **supported OS**: Windows, macOS, or Linux
- An **AWS account** with IAM user access (with programmatic access enabled)

---

## 3. Install AWS CLI

### Windows

1. Download the AWS CLI MSI installer from the [AWS CLI official page](https://aws.amazon.com/cli/).
2. Run the installer and follow the prompts.
3. Verify installation:

```bash
aws --version
```
### macOS
Using Homebrew:
```bash
brew install awscli
```
Verify installation:
```bash
aws --version
```
### Linux 
Using bundled installer:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
## 4. Configure AWS CLI
Run this command to configure your credentials and default region:
```bash
aws configure
```
You will be prompted for:
- AWS Access Key ID: (from your IAM user)
- AWS Secret Access Key: (from your IAM user)
- Default region name: (e.g., us-east-1, eu-west-1)
- Default output format: (json, text, table — json is common)

## 5. Using Multiple Profiles (For Multiple AWS Accounts)
You can configure multiple profiles using:
```bash
aws configure --profile profile_name
aws configure --profile dev-account
```
Use a profile when running commands:
```bash
aws s3 ls --profile dev-account
```
## 6. Secure Your Credentials
- Never commit your ~/.aws/credentials file to Git or share it.
-  Use IAM roles for EC2 instances or AWS services where possible to avoid hardcoding credentials.
- Rotate keys regularly and delete unused keys.
- Store keys in secure password managers if needed.

## 7. Verify Your Configuration
Check the configured profiles and credentials:
```
cat ~/.aws/credentials
cat ~/.aws/config
Test a simple AWS CLI command:

bash
Copy
Edit
aws s3 ls
8. Useful AWS CLI Commands to Get Started
List all S3 buckets:

bash
Copy
Edit
aws s3 ls
Describe running EC2 instances:

bash
Copy
Edit
aws ec2 describe-instances --filters Name=instance-state-name,Values=running
List IAM users:

bash
Copy
Edit
aws iam list-users
9. Automate AWS CLI Commands
You can create Bash or PowerShell scripts to automate repetitive AWS tasks, e.g., starting/stopping instances, uploading files to S3, or checking billing.

10. Troubleshooting
If aws command not found, ensure your PATH includes the AWS CLI installation directory.

Update AWS CLI to the latest version regularly.

Check AWS CLI documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

11. Additional Resources
AWS CLI Official Docs: https://docs.aws.amazon.com/cli/

AWS IAM User Guide: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html




