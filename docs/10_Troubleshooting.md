# Troubleshooting

## Installation Issues

### ModuleNotFoundError

Cause

Missing Python package.

Solution

```bash
pip install -r requirements.txt
```

---

### Database Errors

Cause

Database not migrated.

Solution

```bash
flask db upgrade
```

---

### Docker Connection Failed

Cause

Docker Desktop not running.

Solution

Start Docker Desktop.

Verify:

```bash
docker version
```

---

### AWS Connection Failed

Cause

Missing or invalid AWS credentials.

Solution

Check:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION

---

### Template Not Found

Cause

Incorrect template path.

Solution

Verify the template exists in:

```
app/templates/
```

---

### BuildError

Cause

Incorrect route name.

Solution

Check:

```python
url_for(...)
```

matches the registered route.

---

### Permission Denied

Cause

Insufficient privileges.

Solution

Run terminal as Administrator (Windows) or use appropriate permissions on Linux.

---

### Report Generation Failed

Verify:

- ReportLab installed
- Output directory writable
- Scan data available

---

### Scanner Errors

Check:

- Target validity
- Internet connectivity
- Scanner configuration