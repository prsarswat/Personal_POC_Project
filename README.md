# ETL CI/CD Pipeline POC

## Overview

Demonstrates a Python-based ETL pipeline integrated with Jenkins via GitHub Codespaces—no local install required.

## How to Use

1. Push this repo to GitHub.
2. Open in GitHub Codespaces.
3. Codespace will install dependencies automatically.
4. Run Jenkins via Docker:
   ```bash
   docker run -d -p 8080:8080 \
     -v jenkins_home:/var/jenkins_home \
     jenkins/jenkins:lts
