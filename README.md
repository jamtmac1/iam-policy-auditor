# iam-policy-auditor
Script to audit AWS IAM roles and policies
A Python-based command-line tool that analyzes IAM roles and policies in your AWS account to identify common security misconfigurations and privilege escalation risks.
This project simulates core functionality used by security engineers, cloud auditors, and DevOps teams to enforce least privilege and improve AWS account security.

## Features
- Lists all IAM roles in your AWS account
- Analyzes both inline and managed policies
- Flags:
  - Wildcard permissions (e.g. `"Action": "*"` or `"s3:*"`)
  - Privilege escalation risks (e.g. `iam:PassRole`, `iam:AttachUserPolicy`)
- Outputs flagged actions by role
- Easily extendable and CLI-ready


## Why This Exists

This tool is part of my cloud engineering development journey and focuses on:

- IAM policy structure and risk modeling
- Automating cloud audits with Python and boto3
- Building real-world, security-first DevOps tooling


## How It Works

1. Connects to your AWS account using your default AWS CLI credentials
2. Pulls all IAM roles using `boto3`
3. For each role:
   - Checks all attached and inline policies
   - Looks for dangerous actions or excessive permissions
4. Prints issues found in a readable format


## Example Risk Checks

- `"Action": "*"`  
- `"Resource": "*"`  
- `iam:PassRole`  
- `iam:CreateAccessKey`  
- `iam:AttachUserPolicy`



## Requirements

- Python 3.x
- AWS credentials configured (`aws configure`)
- boto3 (Install with `pip install boto3`)


## Usage

```bash
python iam_auditor.py
