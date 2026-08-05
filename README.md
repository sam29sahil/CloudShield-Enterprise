# 🛡️ CloudShield Enterprise

> Enterprise Cybersecurity, Cloud Security and Infrastructure Management Platform built with Flask.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

CloudShield Enterprise is an enterprise-grade cybersecurity and cloud security platform developed using **Python**, **Flask**, and **Bootstrap**.

The platform centralizes cybersecurity operations into a single dashboard by combining:

- Vulnerability Assessment
- Asset Management
- Findings Management
- Docker Management
- Cloud Security
- Security Analytics
- Executive Reporting
- Notification Center
- PDF/CSV/JSON Reporting

CloudShield is designed as a modular security platform suitable for enterprise environments, educational projects, and cybersecurity research.

---

# 🎯 Objectives

The project aims to:

- Simplify vulnerability assessment
- Centralize security monitoring
- Improve asset visibility
- Provide executive-level reporting
- Integrate cloud security services
- Support Docker infrastructure management
- Deliver a professional enterprise dashboard

---

# ✨ Key Features

## 🔐 Authentication

- Secure Login
- User Registration
- Password Hashing
- Session Management
- Protected Routes

---

## 📊 Dashboard

- Security Overview
- Live Statistics
- Recent Activity
- Security Score
- Quick Navigation

---

## 🔍 Security Scanner

- Universal Scanner
- Basic Scanner
- Multiple Security Tools
- Scan History
- Detailed Scan Reports
- Security Score Calculation

---

## 🖥 Asset Management

- Add Assets
- Edit Assets
- Delete Assets
- Asset Categories
- Asset Tracking

---

## 🚨 Findings Management

- Security Findings
- Severity Classification
- Filtering
- Search
- Status Tracking

---

## 📈 Analytics

- Security Statistics
- Charts
- Severity Distribution
- Trends
- Top Assets
- Scanner Usage

---

## 📄 Reports

- PDF Reports
- CSV Export
- JSON Export
- Report Viewer
- Report Management

---

## 🔔 Notifications

- Scan Notifications
- Security Alerts
- Mark as Read
- Delete Notifications
- Global Notification Badge

---

## ⚙ Settings

CloudShield includes a centralized settings module for user preferences and application configuration.

Features:

- Profile Management
- Password Change
- Scanner Preferences
- Report Preferences
- Security Preferences
- System Information

---

## 🐳 Docker Management

The Docker module provides enterprise container management directly from the dashboard.

Features:

- Docker Dashboard
- Running Containers
- Container Details
- Container Logs
- Container Statistics
- Images
- Networks
- Volumes
- Start Container
- Stop Container
- Restart Container
- Remove Container

---

## ☁ Cloud Security

CloudShield integrates cloud security monitoring for Amazon Web Services (AWS).

Modules:

- AWS Dashboard
- EC2 Monitoring
- Amazon S3
- IAM
- Security Groups
- CloudTrail
- GuardDuty
- Inspector

Cloud services are designed to support real AWS accounts while also functioning gracefully when no AWS credentials are configured.

---

## 👨‍💼 Executive Dashboard

The Executive Dashboard provides high-level security insights for managers and decision-makers.

Includes:

- Security KPIs
- Executive Summary
- Security Trends
- Asset Overview
- Vulnerability Distribution
- Overall Security Score

---

## 🌐 REST API

CloudShield exposes REST APIs for integration with external tools.

Current API capabilities include:

- Dashboard Information
- Assets
- Reports
- Security Findings
- Scanner Data
- Notifications

The API is designed for future integration with automation platforms and SIEM solutions.

---

# 🛠 Technology Stack

## Backend

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-Migrate
- WTForms

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2
- Bootstrap Icons

---

## Database

Development

- SQLite

Production

- PostgreSQL

---

## Security Tools

- Nmap
- Custom Scanner Engine
- Docker SDK
- Boto3 (AWS)

---

## Cloud Services

- Amazon EC2
- Amazon S3
- IAM
- CloudTrail
- GuardDuty
- Inspector

---

## Infrastructure

- Docker
- Gunicorn
- Nginx
- Linux
- Windows

---

# 📁 Project Structure

```text
CloudShield/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── scanner/
│   ├── reports/
│   ├── analytics/
│   ├── findings/
│   ├── notifications/
│   ├── settings/
│   ├── assets/
│   ├── cloud/
│   ├── docker/
│   ├── executive/
│   ├── api/
│   ├── templates/
│   ├── static/
│   └── models/
│
├── docs/
├── migrations/
├── instance/
├── requirements.txt
├── run.py
└── README.md
```

---

# 🏗 Application Architecture

```
                    Users
                      │
                      ▼
               Flask Application
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Authentication   Business Logic    REST API
      │               │
      ▼               ▼
   SQLAlchemy      Services Layer
      │               │
      └──────► SQLite / PostgreSQL
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      Docker SDK              AWS (Boto3)
```
---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CloudShield.git

cd CloudShield
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///cloudshield.db

FLASK_ENV=development

AWS_REGION=ap-south-1

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=
```

---

## 5. Initialize the Database

```bash
flask db init

flask db migrate

flask db upgrade
```

If migrations already exist, run only:

```bash
flask db upgrade
```

---

## 6. Start the Application

```bash
python run.py
```

Open:

```
http://127.0.0.1:5000
```

---

# ⚙ Configuration

CloudShield supports multiple configurations.

## Development

- SQLite
- Debug Mode
- Local Scanner
- Local Docker

---

## Production

Recommended:

- PostgreSQL
- Gunicorn
- Nginx
- Linux Server
- HTTPS
- Environment Variables

---

# 🐳 Docker Support

CloudShield can communicate with Docker Desktop.

Requirements:

- Docker Desktop Installed
- Docker Engine Running
- Docker Python SDK

Install SDK:

```bash
pip install docker
```

Verify Docker:

```bash
docker version
```

---

# ☁ AWS Integration

AWS integration is optional.

Supported Services:

- EC2
- S3
- IAM
- Security Groups
- CloudTrail
- GuardDuty
- Inspector

Before connecting AWS:

1. Create an IAM User.
2. Generate Access Keys.
3. Configure credentials in `.env`.
4. Restart CloudShield.

CloudShield continues to function normally even if AWS credentials are not configured.

---

# 📦 Project Requirements

Minimum:

- Python 3.12+
- 8 GB RAM
- 2 GB Free Disk Space
- Windows 10 / 11 or Linux

Recommended:

- 16 GB RAM
- PostgreSQL
- Docker Desktop
- AWS Account (optional)

---

# 📋 Requirements

Python Packages:

- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-Migrate
- SQLAlchemy
- WTForms
- boto3
- docker
- reportlab
- requests
- python-dotenv

Install all packages:

```bash
pip install -r requirements.txt
```
---

# 📖 Usage Guide

After logging into CloudShield Enterprise, the sidebar provides access to all available modules.

## Dashboard

The Dashboard provides a real-time overview of the platform.

Features:

- Security Statistics
- Recent Activity
- Overall Security Score
- Quick Navigation
- Executive Summary

---

## Security Scanner

Use the Scanner module to perform vulnerability assessments.

Workflow:

1. Select Scan Mode
2. Enter Target
3. Choose Scanner
4. Start Scan
5. View Findings
6. Export Report

---

## Asset Management

The Asset module helps manage infrastructure assets.

Functions:

- Add Assets
- Edit Assets
- Delete Assets
- Categorize Assets
- Track Asset Status

---

## Findings

Security findings generated by scans are stored here.

Features:

- Severity Levels
- Search
- Filters
- Status Tracking
- Report Generation

---

## Analytics

The Analytics Dashboard provides security insights.

Includes:

- Scan Statistics
- Severity Distribution
- Scanner Usage
- Trend Analysis
- Top Vulnerabilities

---

## Reports

Generate professional reports in multiple formats.

Supported Formats:

- PDF
- CSV
- JSON

---

## Notifications

Receive alerts for important security events.

Examples:

- Scan Completed
- High-Risk Findings
- Docker Alerts
- Cloud Alerts

---

## Docker

Manage Docker resources directly within CloudShield.

Available Features:

- Dashboard
- Containers
- Images
- Networks
- Volumes
- Logs
- Container Details

---

## Cloud

Monitor AWS cloud infrastructure.

Available Services:

- EC2
- Amazon S3
- IAM
- Security Groups
- CloudTrail
- GuardDuty
- Inspector

---

# 📸 Screenshots

Add screenshots after completing deployment.

Recommended screenshots:

```
Login Page

Dashboard

Scanner

Scan Results

Findings

Analytics

Reports

Docker Dashboard

Cloud Dashboard

Settings
```

Create a folder:

```
screenshots/
```

Example:

```
screenshots/

login.png

dashboard.png

scanner.png

reports.png

docker.png

cloud.png
```

---

# 🔒 Security Features

CloudShield includes multiple security mechanisms.

Authentication

- Password Hashing
- Session Management
- Login Protection

Application Security

- CSRF Protection
- Input Validation
- Secure Routing

Infrastructure Security

- Docker Integration
- AWS Integration
- Vulnerability Assessment

Reporting

- PDF Reports
- CSV Export
- JSON Export

---

# 🚀 Future Roadmap

CloudShield Enterprise v2 will introduce:

- AI Threat Detection
- SIEM Integration
- XDR Dashboard
- Kubernetes Security
- Azure Integration
- Google Cloud Integration
- Compliance Dashboard
- Threat Intelligence
- CVE Feed Integration
- Real-Time Monitoring
- WebSocket Live Dashboard
- AI Security Assistant

---

# 🤝 Contributing

Contributions are welcome.

Workflow:

1. Fork Repository
2. Create Feature Branch
3. Commit Changes
4. Submit Pull Request

Please follow the project's coding standards and documentation guidelines.

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for additional details.

---

# 👨‍💻 Author

**Sahil Samyal**

B.Tech Student

Cybersecurity Enthusiast

Cloud & Infrastructure Security

Enterprise Security Platform Developer

---

# ⭐ Acknowledgements

Special thanks to the open-source community and the developers of:

- Flask
- SQLAlchemy
- Bootstrap
- Docker SDK
- boto3
- ReportLab
- Python Community

---

# 📌 Project Status

Current Version

```
CloudShield Enterprise v1.0
```

Development Status

```
Production Ready (Educational Project)
```

Current Completion

```
≈ 98%
```

---

# 🌟 Support

If you found this project helpful:

⭐ Star the repository

🐛 Report bugs

💡 Suggest new features

🤝 Contribute improvements