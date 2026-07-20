# Installation Guide

## Overview

This guide explains how to install and configure CloudShield Enterprise on a local development environment.

---

# System Requirements

## Minimum

- Python 3.12+
- 8 GB RAM
- 2 GB Free Storage
- Windows 10/11 or Linux
- Git

---

## Recommended

- Python 3.13+
- 16 GB RAM
- Docker Desktop
- PostgreSQL
- Visual Studio Code

---

# Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/CloudShield.git

cd CloudShield
```

---

# Step 2 — Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 — Configure Environment

Create a `.env` file.

Example:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///cloudshield.db

AWS_REGION=ap-south-1

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=
```

---

# Step 5 — Database Migration

```bash
flask db upgrade
```

---

# Step 6 — Run Application

```bash
python run.py
```

Open:

```
http://127.0.0.1:5000
```

---

# Optional Components

## Docker

Install Docker Desktop.

Verify:

```bash
docker version
```

---

## AWS

Configure credentials only when cloud integration is required.

CloudShield functions normally without AWS credentials.

---

# Troubleshooting

Common Issues:

- Missing Python packages
- Docker Engine not running
- Database migration errors
- Incorrect AWS credentials

Refer to `10_Troubleshooting.md` for detailed solutions.