# Deployment Guide

## Overview

CloudShield Enterprise can be deployed in development or production environments.

Supported platforms:

- Windows
- Linux
- Docker
- AWS EC2
- DigitalOcean
- Render
- Railway

---

# Development Deployment

Clone the repository.

```bash
git clone https://github.com/yourusername/CloudShield.git

cd CloudShield
```

Create a virtual environment.

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python run.py
```

---

# Production Deployment

Recommended Stack

- Ubuntu 24.04 LTS
- Python 3.12+
- Gunicorn
- Nginx
- PostgreSQL
- Docker Desktop (optional)

---

# Environment Variables

Example:

```env
SECRET_KEY=change_this_secret

DATABASE_URL=postgresql://user:password@localhost/cloudshield

AWS_REGION=ap-south-1

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=
```

---

# Gunicorn

Example:

```bash
gunicorn -w 4 run:app
```

---

# Nginx

Configure Nginx as a reverse proxy.

Enable HTTPS using Let's Encrypt for production deployments.

---

# Docker

Docker support is optional.

Install Docker Desktop.

Verify:

```bash
docker version
```

---

# PostgreSQL

Recommended for production.

Run migrations:

```bash
flask db upgrade
```

---

# Verification

After deployment verify:

- Login
- Dashboard
- Scanner
- Reports
- Docker
- Cloud
- API