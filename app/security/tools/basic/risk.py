"""
CloudShield Enterprise
Risk Scoring Engine
"""


def calculate_risk(report):

    score = 100

    findings = []

    # --------------------------
    # Website
    # --------------------------

    if not report.get("website", {}).get("success"):

        score -= 50
        findings.append("Website is not reachable.")

    # --------------------------
    # SSL
    # --------------------------

    ssl = report.get("ssl", {})

    if not ssl.get("success", True):

        score -= 20
        findings.append("SSL certificate problem.")

    # --------------------------
    # Security Headers
    # --------------------------

    headers = report.get("headers", {})

    missing = headers.get("missing", [])

    score -= len(missing) * 5

    if missing:

<<<<<<< HEAD
        findings.append(f"{len(missing)} security headers missing.")
=======
        findings.append(
            f"{len(missing)} security headers missing."
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # --------------------------
    # Open Ports
    # --------------------------

    ports = report.get("ports", [])

    dangerous = [21, 23, 3389]

    for port in ports:

        if port["port"] in dangerous:

            score -= 10

<<<<<<< HEAD
            findings.append(f"Dangerous port {port['port']} open.")
=======
            findings.append(

                f"Dangerous port {port['port']} open."

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    if score < 0:

        score = 0

    if score >= 90:

        risk = "Low"

    elif score >= 70:

        risk = "Medium"

    elif score >= 40:

        risk = "High"

    else:

        risk = "Critical"

<<<<<<< HEAD
    return {"score": score, "risk": risk, "findings": findings}
=======
    return {

        "score": score,

        "risk": risk,

        "findings": findings

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
