# REST API Documentation

## Overview

CloudShield Enterprise provides REST APIs for integration with external applications.

---

# Authentication

All API endpoints require authenticated access unless otherwise specified.

---

# Dashboard

GET /api/dashboard

Returns dashboard statistics.

---

# Scanner

POST /api/scanner/start

Starts a new security scan.

GET /api/scanner/history

Returns scan history.

---

# Assets

GET /api/assets

Returns all assets.

POST /api/assets

Creates a new asset.

DELETE /api/assets/<id>

Deletes an asset.

---

# Reports

GET /api/reports

Returns available reports.

GET /api/reports/pdf/<id>

Downloads a PDF report.

GET /api/reports/csv/<id>

Downloads a CSV report.

GET /api/reports/json/<id>

Downloads a JSON report.

---

# Notifications

GET /api/notifications

Returns notifications.

POST /api/notifications/read

Marks a notification as read.