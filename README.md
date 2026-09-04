# CloudShield Enterprise

> **Enterprise Cloud & Web Security Assessment Platform**

CloudShield Enterprise is a Flask-based cybersecurity platform designed to bring website security assessment, Azure cloud security assessment, centralized findings management, risk scoring, recommendations, dashboards, and security reporting into a single application.

The project is designed as a **BTech final-year cybersecurity project** and follows a modular architecture so additional cloud providers, scanners, and security capabilities can be integrated later.

---

## Table of Contents

- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Modules](#project-modules)
- [Security Assessment Workflow](#security-assessment-workflow)
- [Azure Security Assessment](#azure-security-assessment)
- [Findings Engine](#findings-engine)
- [Risk and Security Score](#risk-and-security-score)
- [Reporting](#reporting)
- [Dashboard](#dashboard)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Azure Configuration](#azure-configuration)
- [Database](#database)
- [Git and GitHub](#git-and-github)
- [Security Considerations](#security-considerations)
- [Testing](#testing)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Academic Project Information](#academic-project-information)
- [License](#license)

---

## Overview

CloudShield Enterprise provides a centralized interface for performing security assessments and managing their results.

The platform currently combines two primary assessment paths:

### 1. Website Security Assessment

The basic scanner evaluates a web target and can provide information related to:

- Website analysis
- HTTP security headers
- SSL/TLS
- DNS
- WHOIS
- Technology detection
- Open ports
- Security findings
- Recommendations

### 2. Azure Cloud Security Assessment

The Azure Basic Security Scanner connects to Microsoft Azure and evaluates the available Azure environment information.

The Azure assessment includes:

- Resource Groups
- Virtual Machines
- Virtual Networks
- Subnets
- Network Security Groups
- Network Interfaces
- Key Vaults
- Microsoft Defender information
- Security findings
- Risk assessment
- Security score
- Recommendations
- Azure-specific reporting

The Azure scanner is intentionally scoped as a **basic Azure security assessment** rather than a complete replacement for enterprise cloud security products.

---

# Project Objectives

The primary objectives of CloudShield Enterprise are:

1. Build a centralized cybersecurity assessment platform.
2. Provide a web-based security assessment workflow.
3. Analyze website security configuration.
4. Integrate Azure cloud security assessment.
5. Centralize security findings.
6. Assign severity to findings.
7. Calculate security risk.
8. Generate security scores.
9. Provide remediation recommendations.
10. Generate professional security reports.
11. Provide a dashboard for security visibility.
12. Maintain scan and asset history.
13. Create a modular foundation for future security integrations.

---

# Key Features

## Authentication

- User registration
- User login
- Password hashing
- Logout
- Protected application routes

## Dashboard

The dashboard provides centralized visibility into:

- Projects
- Assets
- Scans
- Findings
- Security status
- Cloud/security information
- Recent activity
- Security metrics

## Project Management

- Create projects
- View projects
- Edit projects
- Delete projects
- Associate assets and scans with projects

## Asset Management

Assets can be associated with projects and security assessments.

Examples include:

- Website targets
- Azure subscriptions
- Cloud resources

## Website Scanner

The basic scanner supports security assessment areas such as:

- HTTP security headers
- SSL/TLS
- DNS
- WHOIS
- Technology detection
- Port information
- Website analysis

## Findings Management

Security findings are centralized through the findings engine.

Each finding can contain information such as:

- Title
- Severity
- Description
- Recommendation
- Evidence
- CVSS
- CWE
- OWASP information
- Reference
- Status
- Asset
- Scan

## Azure Security Scanner

The Azure scanner collects and analyzes cloud information including:

- Resource Groups
- Virtual Machines
- Virtual Networks
- Subnets
- Network Security Groups
- Network Interfaces
- Key Vaults
- Microsoft Defender information

## Risk Assessment

Findings are passed through the risk engine to determine an overall risk level.

## Security Score

The security assessment produces a security score that can be displayed on dashboards and reports.

## Recommendations

The platform generates remediation recommendations from detected security findings.

## Reporting

CloudShield Enterprise supports report generation for security assessments.

Normal website reports contain website-oriented sections.

Azure reports contain Azure-specific sections.

---

# Architecture

CloudShield Enterprise follows a modular Flask architecture.

```text
                    CloudShield Enterprise
                              |
             +----------------+----------------+
             |                                 |
       Web Security                      Cloud Security
             |                                 |
      Basic Scanner                    Azure Scanner
             |                                 |
             +----------------+----------------+
                              |
                       Findings Engine
                              |
                +-------------+-------------+
                |             |             |
              Risk          Score      Recommendations
                |             |             |
                +-------------+-------------+
                              |
                         Reporting
                              |
                    +---------+---------+
                    |                   |
                 Dashboard           PDF/JSON
```

---

# Security Assessment Workflow

The general assessment workflow is:

```text
Target / Cloud
      |
      v
Scanner
      |
      v
Inventory / Assessment Data
      |
      v
Analyzer
      |
      v
Security Findings
      |
      v
Findings Engine
      |
      v
Risk Assessment
      |
      v
Security Score
      |
      v
Recommendations
      |
      v
Dashboard / Reports
```

---

# Azure Security Assessment

The Azure scanner is designed around the following pipeline:

```text
Azure Authentication
        |
        v
Azure Resource Inventory
        |
        +---- Resource Groups
        |
        +---- Virtual Machines
        |
        +---- Virtual Networks
        |
        +---- Subnets
        |
        +---- Network Security Groups
        |
        +---- Network Interfaces
        |
        +---- Key Vaults
        |
        +---- Defender
        |
        v
Azure Analyzer
        |
        v
Security Findings
        |
        v
Risk Engine
        |
        v
Security Score
        |
        v
Recommendations
        |
        v
Azure Report
```

## Azure Network Assessment

The network component can inspect information such as:

- Virtual networks
- Subnets
- Network Security Groups
- Security rules
- Network interfaces
- IP configuration
- Network exposure

Security rules can contain information such as:

- Rule name
- Priority
- Direction
- Allow/Deny
- Protocol
- Source
- Source port
- Destination
- Destination port

## Virtual Machine Assessment

The Azure assessment can collect VM information such as:

- VM name
- Resource group
- Location
- Operating system
- Size
- Network interfaces
- Public exposure information

## Key Vault Assessment

The scanner inventories Key Vault resources and provides the collected information to the security analysis pipeline.

## Microsoft Defender

The Azure security pipeline includes Microsoft Defender information such as:

- Secure score
- Alerts
- Recommendations

These results can contribute to the security assessment and findings.

---

# Findings Engine

The findings engine provides a common security finding model across assessment types.

A finding can contain:

```text
Finding
├── ID
├── Title
├── Severity
├── Description
├── Recommendation
├── Evidence
├── CVSS
├── CWE
├── OWASP
├── Reference
├── Status
├── Asset
└── Scan
```

This allows findings from the Azure scanner to be connected to the same application-wide findings pipeline used by the rest of CloudShield Enterprise.

---

# Risk and Security Score

The assessment pipeline calculates:

```text
Findings
   |
   v
Risk Engine
   |
   v
Risk Level
   |
   v
Security Score
```

Typical severity categories include:

- Critical
- High
- Medium
- Low
- Info

The final score and risk level are surfaced through the dashboard and reports.

> The exact score is produced by the application's implemented scoring engine; it should not be interpreted as an official Microsoft Azure security score unless explicitly identified as such.

---

# Reporting

CloudShield Enterprise uses different report sections depending on the assessment type.

## Website Report

Normal/basic website reports can contain:

```text
Cover
Executive Summary
Website Analysis
Security Headers
SSL/TLS
DNS
WHOIS
Technology
Ports
Findings
Recommendations
Appendix
Raw Output
```

## Azure Cloud Report

Azure reports can contain:

```text
Cover
Executive Summary
Cloud Security Assessment
Security Score
Risk Level
Azure Resource Inventory
Resource Groups
Virtual Machines
Virtual Networks
Subnets
Network Security Groups
Network Interfaces
Key Vaults
Microsoft Defender
Cloud Security Findings
Cloud Recommendations
Azure Inventory Details
Findings
Recommendations
Appendix
Raw Output
```

The PDF generator detects whether the scan is a cloud/Azure assessment and selects the appropriate report sections.

---

# Dashboard

The dashboard is the central monitoring interface of CloudShield Enterprise.

It can present:

- Project statistics
- Asset information
- Deployment information
- Scan information
- Findings
- Security scores
- Risk information
- Cloud information
- Recent activity
- System status

The Azure dashboard can expose the results of the Azure security assessment without requiring users to inspect raw Azure API output.

---

# Project Modules

The major application areas include:

```text
app/
├── auth/
├── dashboard/
├── projects/
├── assets/
├── findings/
├── scanner/
├── cloud/
├── analytics/
├── reports/
├── monitoring/
├── settings/
├── models/
├── services/
├── api/
├── templates/
├── static/
└── extensions.py
```

The exact project tree can evolve as modules are added or reorganized.

---

# Project Structure

A representative structure is:

```text
CloudShield-Enterprise/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── projects/
│   ├── assets/
│   ├── findings/
│   ├── scanner/
│   │   └── services/
│   ├── cloud/
│   │   └── azure/
│   │       ├── security/
│   │       ├── network.py
│   │       ├── defender.py
│   │       ├── keyvault.py
│   │       ├── virtual_machines.py
│   │       ├── resource_groups.py
│   │       ├── analyzer.py
│   │       ├── risk.py
│   │       ├── score.py
│   │       ├── recommendations.py
│   │       └── report.py
│   ├── analytics/
│   ├── reports/
│   ├── models/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── extensions.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Technology Stack

## Backend

- Python
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate

## Database

Development can use:

- SQLite

Production can use:

- PostgreSQL

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap
- Jinja2

## Cloud

Azure integration uses the Microsoft Azure Python SDK / management libraries.

## Security Tooling

Depending on the configured scanner modules, the platform can integrate security tools and utilities such as:

- Nmap
- Nikto
- WhatWeb
- Nuclei
- WAFW00F
- testssl.sh
- dnsrecon
- subfinder

Not every external tool is required for the currently completed Basic Azure scope.

## Reporting

- ReportLab
- JSON
- CSV/export functionality where implemented

---

# Requirements

Recommended environment:

- Python 3.11+ compatible environment
- pip
- Git
- Microsoft Azure account for Azure scanning
- Appropriate Azure permissions for the resources being assessed

For Windows PowerShell:

```powershell
python --version
pip --version
```

---

# Installation

## 1. Clone the repository

```powershell
git clone https://github.com/sam29sahil/CloudShield-Enterprise.git
cd CloudShield-Enterprise
```

## 2. Create a virtual environment

```powershell
python -m venv venv
```

## 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If dependencies are being installed manually during development, install the packages listed by the application's import errors and then update `requirements.txt`.

## 5. Configure environment variables

Create:

```text
.env
```

Example:

```env
SECRET_KEY=replace-with-a-random-secret
DATABASE_URL=sqlite:///cloudshield.db
```

Azure variables should be configured according to the authentication method implemented in the project.

**Never commit real secrets to GitHub.**

---

# Configuration

The application configuration is managed through the project's Flask configuration.

Typical configuration areas include:

```text
Flask
Database
Secret Key
Azure
Mail
Security
Application settings
```

For production deployments:

- Use a strong random secret key.
- Use PostgreSQL where appropriate.
- Store secrets in environment variables or a secret manager.
- Disable Flask debug mode.
- Use HTTPS.
- Restrict cloud credentials to the minimum required permissions.

---

# Running the Application

Activate the virtual environment first.

```powershell
.\venv\Scripts\Activate.ps1
```

Then:

```powershell
python run.py
```

The Flask development server should start.

Open the local application URL shown by Flask in the terminal.

---

# Azure Configuration

The Azure scanner requires valid Azure authentication and appropriate permissions.

Before running an Azure assessment, verify:

1. Azure credentials are available.
2. The subscription is accessible.
3. The application has permission to read the required Azure resources.
4. Required Azure management packages are installed.
5. The selected subscription is correct.

The scanner is intended for authorized Azure environments only.

---

# Database

CloudShield Enterprise uses database models for application data such as:

- Users
- Projects
- Assets
- Security scans
- Findings
- Reports
- Notifications

Database migrations should be used when the project's model schema changes.

Typical development commands may include:

```powershell
flask db migrate -m "description"
flask db upgrade
```

Use the migration workflow appropriate to the current project configuration.

---

# Git and GitHub

Initialize Git if the project is not already a repository:

```powershell
git init
```

Set the remote:

```powershell
git remote add origin https://github.com/sam29sahil/CloudShield-Enterprise.git
```

Check:

```powershell
git remote -v
```

Create the main branch:

```powershell
git branch -M main
```

Stage:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Initial CloudShield Enterprise release"
```

Push:

```powershell
git push -u origin main
```

---

# Security Considerations

CloudShield Enterprise is a security assessment platform and should itself be operated securely.

## Never expose secrets

Do not commit:

```text
.env
Azure credentials
Passwords
API keys
Private keys
Production database credentials
```

## Authorization

Only scan systems and cloud resources for which you have explicit authorization.

## Azure permissions

Use least-privilege Azure permissions.

The scanner should not receive unnecessary write permissions when read-only assessment is sufficient.

## Production deployment

For production:

- Disable debug mode.
- Use HTTPS.
- Use a production WSGI server.
- Protect the database.
- Protect environment variables.
- Restrict administrative access.
- Rotate credentials when necessary.
- Monitor application logs.

---

# Testing

Before a release, perform at least the following checks.

## Python syntax

```powershell
python -m py_compile app\scanner\services\report_builder.py
python -m py_compile app\scanner\services\report_generator.py
python -m py_compile app\cloud\azure\security_service.py
```

## Application startup

```powershell
python run.py
```

## Website scan

Verify:

```text
Website scan
    ↓
Findings
    ↓
Risk
    ↓
Score
    ↓
Report
```

## Azure scan

Verify:

```text
Azure authentication
    ↓
Inventory
    ↓
Analysis
    ↓
Findings
    ↓
Risk
    ↓
Score
    ↓
Recommendations
    ↓
Dashboard
    ↓
PDF
```

## PDF verification

Verify that:

### Website scan

Uses:

- Website Analysis
- Headers
- SSL
- DNS
- WHOIS
- Technology
- Ports

### Azure scan

Uses:

- Azure Security Assessment
- Azure inventory
- Defender
- Cloud findings
- Cloud recommendations

---

# Limitations

The current Azure implementation is a **Basic Azure Security Assessment**.

It should not be described as:

- A complete Azure Security Center replacement
- A complete Microsoft Defender for Cloud replacement
- A full enterprise CSPM product
- A full penetration-testing platform
- A complete compliance auditing platform

The scanner evaluates the Azure data and security checks implemented by CloudShield Enterprise.

Coverage can vary depending on:

- Azure permissions
- Available resources
- SDK/API availability
- Scanner implementation
- Subscription configuration

---

# Future Enhancements

Potential future versions can include:

## Cloud

- AWS security assessment
- Google Cloud security assessment
- Multi-subscription Azure assessment
- Multi-account cloud assessment
- Cloud compliance frameworks
- CIS benchmark mapping
- Continuous cloud monitoring

## Security

- Advanced CSPM
- Vulnerability correlation
- Threat intelligence
- Attack-path analysis
- Security posture history
- Automated remediation

## Reporting

- Advanced PDF templates
- Executive reports
- Compliance reports
- Scheduled reports
- Report comparison
- Historical trend analysis

## Platform

- REST API expansion
- Background scan workers
- Job queues
- Notification integrations
- Email alerts
- SIEM integration
- SOC/XDR integration

These are future enhancements and are not required for the current Basic Azure scope.

---

# Academic Project Information

## Project Name

**CloudShield Enterprise**

## Project Type

**BTech Final-Year Cybersecurity Project**

## Domain

**Cybersecurity / Cloud Security / Web Security**

## Primary Goal

To develop a centralized security assessment platform capable of analyzing website and Azure cloud security information and presenting the results through findings, risk scores, recommendations, dashboards, and reports.

## Major Learning Areas

The project demonstrates practical knowledge of:

- Python
- Flask
- Web application development
- Database management
- Authentication
- Cybersecurity assessment
- Vulnerability/finding management
- Cloud security
- Azure SDK integration
- Risk analysis
- Security scoring
- Report generation
- Git/GitHub
- Software architecture

---

# Project Status

## CloudShield Enterprise v1

**Status: Completed for the defined project scope**

Completed core areas include:

- Authentication
- Dashboard
- Projects
- Assets
- Website security scanner
- Findings engine
- Risk engine
- Security scoring
- Recommendations
- Reporting
- Azure Basic Security Scanner
- Azure inventory
- Azure network assessment
- Azure VM assessment
- Key Vault inventory
- Defender information
- Azure findings integration
- Azure-specific reporting
- Cloud-aware PDF reporting

The backend should be treated as **frozen for the v1 release** unless a bug or security issue requires a change.

---

# Responsible Use

CloudShield Enterprise is intended for **authorized security assessment and defensive security purposes**.

Only scan:

- Systems you own
- Cloud subscriptions you control
- Systems where you have explicit authorization to perform security testing

Do not use the platform to access, scan, disrupt, or test unauthorized systems.

---

# License

This project is an academic/personal cybersecurity project.

Add an appropriate open-source license before publicly distributing the project if required.

---

# Author

**Sahil Samyal**

BTech Student  
Cybersecurity Enthusiast

---

## Acknowledgement

CloudShield Enterprise was developed as a practical project to explore the integration of web security assessment, cloud security, security findings management, risk analysis, and security reporting into a unified platform.

---

# Deployment

## Local Development

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Copy `.env.example` to `.env` and set local values. The development server listens on `0.0.0.0:${PORT:-5000}`.

## Docker

```bash
docker build -t cloudshield-enterprise .
docker run --name cloudshield-enterprise --env-file .env -p 5000:5000 cloudshield-enterprise
```

## Docker Compose

```bash
docker compose up --build
```

Compose is for local development. Docker management/scanning routes require access to a Docker daemon; the web container does not mount a Docker socket by default.

## Render

Render is the recommended deployment target for this Flask web service. Connect the GitHub repository as a Docker Web Service, or use the included `render.yaml` Blueprint. The service uses:

```text
Gunicorn -> 0.0.0.0:$PORT -> Flask run:app -> application routes
```

Render settings:

- Runtime: Docker
- Dockerfile: `./Dockerfile`
- Health check path: `/health`
- Pre-deploy command: `flask --app run db upgrade`
- The Docker image uses one Gunicorn worker and a 300-second timeout for synchronous scanner requests.
- Set `DATABASE_URL` to a Render PostgreSQL connection string. Do not use SQLite for production persistence.
- Set `SECRET_KEY` to a long random value. The production app refuses to start without it.

After deployment, verify `/health`, login, registration, `/scanner/`, findings, PDF downloads, and Azure inventory.

## Environment Variables

Required in production:

```env
APP_ENV=production
FLASK_ENV=production
SECRET_KEY=generate-a-long-random-value
DATABASE_URL=postgresql://...
```

Optional integrations:

```env
AWS_REGION=ap-south-1
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
MAIL_SERVER=
MAIL_PORT=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_USE_TLS=True
MAIL_USE_SSL=False
AZURE_TENANT_ID=
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=
AZURE_SUBSCRIPTION_ID=
KUBECONFIG=
K8S_NAMESPACE=default
```

Azure production authentication uses the service-principal environment variables above. Azure CLI login is supported for local development only and is not required in Render.

## Persistence and Runtime Limitations

- Render web-service filesystems are ephemeral. Evidence uploads and CSV/JSON temporary exports do not persist across deploys or restarts.
- PDF reports are generated in memory and downloaded immediately.
- Use PostgreSQL for users, findings, scans, and application records.
- Persistent evidence/report history requires object storage or a persistent disk; this repository does not silently add that storage backend.
- Docker SDK features require a separate Docker-capable worker/service. Render should not be assumed to provide `/var/run/docker.sock`.
- External scanner binaries are not installed by the current image. Verify each tool is available before enabling tool-specific scans.
- Synchronous scans run in the web request and are bounded by the 300-second Gunicorn timeout. A background worker is a future option if scan duration or volume requires it.

## Azure Permissions

Basic subscription inventory uses read-only management APIs and normally requires the service principal to have the **Reader** role at subscription scope. Security-related APIs may additionally require **Security Reader** or service-specific read permissions. No Owner or Contributor permission is required by the inspected inventory code.

## Deployment Checklist

- [ ] GitHub repository contains no secrets
- [ ] `.env` is ignored and `.env.example` contains placeholders only
- [ ] Dockerfile builds and Gunicorn binds to `$PORT`
- [ ] `/health` returns HTTP 200
- [ ] Production `SECRET_KEY` is configured
- [ ] Render PostgreSQL is configured through `DATABASE_URL`
- [ ] `flask --app run db upgrade` succeeds
- [ ] Azure service principal and Reader permission are configured
- [ ] Authentication and registration tested
- [ ] Basic scanner, findings, and PDF tested
- [ ] Docker routes treated as unavailable unless a daemon-capable service is provided

## Deployment Alternatives

- **Render:** recommended for the existing Flask/Docker/Gunicorn architecture and simple PostgreSQL integration.
- **Railway:** workable alternative with similar environment and PostgreSQL configuration.
- **Fly.io:** workable when more control over networking and persistent volumes is required.
- **Azure App Service:** strong Azure integration, but requires more Azure-specific operational setup.
- **VPS:** most control, including a Docker daemon and persistent disks, but requires operating-system and security maintenance.

Vercel is not recommended for the complete application because synchronous security scans, Docker-daemon features, PDF/file workflows, and persistent server-side state do not match its serverless execution model. Use Render for the backend.

## Production Architecture

```text
GitHub
    -> Render Docker Web Service
    -> Gunicorn (one worker, PORT, 300s timeout)
    -> Flask application
    -> Render PostgreSQL
    -> Azure service principal (optional)

Docker scanning, if required:
    Flask API -> separate Docker-capable scanning worker/service
```

## Useful Commands

```bash
flask --app run db upgrade
gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 300 run:app
curl http://127.0.0.1:5000/health
```

Do not commit `.env`, database files, uploads, credentials, or private keys. Typical Git setup is:

```bash
git add Dockerfile docker-compose.yml .dockerignore .env.example config.py run.py render.yaml requirements.txt README.md app tests
git commit -m "Prepare CloudShield for Render deployment"
git push origin main
```
