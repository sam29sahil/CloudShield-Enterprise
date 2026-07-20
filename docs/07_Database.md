# Database Documentation

## Database Engine

Development

- SQLite

Production

- PostgreSQL

---

# Main Tables

User

Stores user accounts.

Fields

- id
- username
- email
- password_hash
- created_at

---

SecurityScan

Stores completed scans.

Fields

- id
- target
- scanner
- score
- duration
- started_at

---

Finding

Stores scan findings.

Fields

- id
- scan_id
- severity
- title
- description

---

Asset

Stores infrastructure assets.

Fields

- id
- name
- target
- category

---

Notification

Stores user notifications.

Fields

- id
- title
- message
- severity
- is_read

---

Relationships

User

↓

SecurityScan

↓

Finding

Reports are generated from SecurityScan and Finding data.