"""
CloudShield Enterprise
Universal Finding Parser
"""

from app.findings.engine import FindingEngine

from app.findings.header_rules import HEADER_RULES
from app.findings.port_rules import PORT_RULES
from app.findings.ssl_rules import SSL_RULES
from app.findings.technology_rules import TECHNOLOGY_RULES
from app.findings.dns_rules import DNS_RULES
from app.findings.whois_rules import WHOIS_RULES
from app.findings.cloud_rules import CLOUD_RULES
from app.findings.threat_rules import THREAT_RULES


class FindingParser:
    """
    Enterprise Finding Parser

    Converts structured scanner output
    into standardized Findings.
    """

    @staticmethod
    def parse(scan, report):

        findings = 0

        # =====================================================
        # HEADER FINDINGS
        # =====================================================

        headers = report.get("headers", {})

        for item in headers.get("analysis", []):

            if item.get("status") != "Missing":
                continue

            rule = HEADER_RULES.get(item["header"])

            if not rule:
                continue

            FindingEngine.create(
<<<<<<< HEAD
                scan=scan,
                title=rule["title"],
                severity=rule["severity"],
                description=rule["description"],
                recommendation=rule["recommendation"],
                category=rule["category"],
                cvss=rule["cvss"],
                evidence=item["header"],
=======

                scan=scan,

                title=rule["title"],

                severity=rule["severity"],

                description=rule["description"],

                recommendation=rule["recommendation"],

                category=rule["category"],

                cvss=rule["cvss"],

                evidence=item["header"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            findings += 1

        # =====================================================
        # PORT FINDINGS
        # =====================================================

        ports = report.get("ports", [])

        for port in ports:

            if port.get("status") != "Open":
                continue

            rule = PORT_RULES.get(port["port"])

            if not rule:
                continue

            FindingEngine.create(
<<<<<<< HEAD
                scan=scan,
                title=rule["title"],
                severity=rule["severity"],
                description=f"{port['service']} service is exposed.",
                recommendation=rule["recommendation"],
                category="Network",
                cvss=rule["cvss"],
                evidence=str(port),
=======

                scan=scan,

                title=rule["title"],

                severity=rule["severity"],

                description=f"{port['service']} service is exposed.",

                recommendation=rule["recommendation"],

                category="Network",

                cvss=rule["cvss"],

                evidence=str(port)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            findings += 1

<<<<<<< HEAD
            # =====================================================
=======
                # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        # SSL FINDINGS
        # =====================================================

        ssl = report.get("ssl", {})

        if ssl:

            # Invalid Certificate

            if ssl.get("valid") is False:

                rule = SSL_RULES["invalid"]

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description="SSL certificate validation failed.",
                    recommendation=rule["recommendation"],
                    category="SSL",
                    cvss=rule["cvss"],
                    evidence=str(ssl),
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description="SSL certificate validation failed.",

                    recommendation=rule["recommendation"],

                    category="SSL",

                    cvss=rule["cvss"],

                    evidence=str(ssl)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1

            # Expired Certificate

            elif ssl.get("days_left", 99999) <= 0:

                rule = SSL_RULES["expired"]

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description="SSL certificate has expired.",
                    recommendation=rule["recommendation"],
                    category="SSL",
                    cvss=rule["cvss"],
                    evidence=str(ssl),
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description="SSL certificate has expired.",

                    recommendation=rule["recommendation"],

                    category="SSL",

                    cvss=rule["cvss"],

                    evidence=str(ssl)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1

            # Expiring Soon

            elif ssl.get("days_left", 99999) <= 30:

                rule = SSL_RULES["expiring"]

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description=f"Certificate expires in {ssl.get('days_left')} days.",
                    recommendation=rule["recommendation"],
                    category="SSL",
                    cvss=rule["cvss"],
                    evidence=str(ssl),
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description=f"Certificate expires in {ssl.get('days_left')} days.",

                    recommendation=rule["recommendation"],

                    category="SSL",

                    cvss=rule["cvss"],

                    evidence=str(ssl)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1

        # =====================================================
        # TECHNOLOGY FINDINGS
        # =====================================================

        technologies = report.get("technology", [])

        if isinstance(technologies, dict):

            technologies = technologies.get("technologies", [])

        for tech in technologies:

            if isinstance(tech, dict):

                name = tech.get("name", "")

            else:

                name = str(tech)

            rule = TECHNOLOGY_RULES.get(name)

            if not rule:
                continue

            FindingEngine.create(
<<<<<<< HEAD
                scan=scan,
                title=rule["title"],
                severity=rule["severity"],
                description=rule["description"],
                recommendation=rule["recommendation"],
                category="Technology",
                cvss=rule["cvss"],
                evidence=name,
            )

            findings += 1

            # =====================================================
=======

                scan=scan,

                title=rule["title"],

                severity=rule["severity"],

                description=rule["description"],

                recommendation=rule["recommendation"],

                category="Technology",

                cvss=rule["cvss"],

                evidence=name

            )

            findings += 1    

                # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        # DNS FINDINGS
        # =====================================================

        dns = report.get("dns", {})

        if dns:

            for key, rule in DNS_RULES.items():

                if key not in dns:

                    continue

                value = dns.get(key)

                if value in (None, "", [], False):

                    FindingEngine.create(
<<<<<<< HEAD
                        scan=scan,
                        title=rule["title"],
                        severity=rule["severity"],
                        description=rule["description"],
                        recommendation=rule["recommendation"],
                        category="DNS",
                        cvss=rule["cvss"],
                        evidence=f"{key}: {value}",
=======

                        scan=scan,

                        title=rule["title"],

                        severity=rule["severity"],

                        description=rule["description"],

                        recommendation=rule["recommendation"],

                        category="DNS",

                        cvss=rule["cvss"],

                        evidence=f"{key}: {value}"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                    )

                    findings += 1

        # =====================================================
        # WHOIS FINDINGS
        # =====================================================

        whois = report.get("whois", {})

        if whois:

            registrar = whois.get("registrar")

            if not registrar:

                rule = WHOIS_RULES["registrar"]

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description=rule["description"],
                    recommendation=rule["recommendation"],
                    category="WHOIS",
                    cvss=rule["cvss"],
                    evidence="Registrar Missing",
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description=rule["description"],

                    recommendation=rule["recommendation"],

                    category="WHOIS",

                    cvss=rule["cvss"],

                    evidence="Registrar Missing"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1

            expiry = whois.get("expiration_date")

            if expiry:

                try:

                    from datetime import datetime

                    if isinstance(expiry, list):

                        expiry = expiry[0]

                    if isinstance(expiry, str):

                        expiry = datetime.fromisoformat(expiry)

                    days = (expiry - datetime.utcnow()).days

                    if days <= 30:

                        rule = WHOIS_RULES["expiry"]

                        FindingEngine.create(
<<<<<<< HEAD
                            scan=scan,
                            title=rule["title"],
                            severity=rule["severity"],
                            description=f"Domain expires in {days} days.",
                            recommendation=rule["recommendation"],
                            category="WHOIS",
                            cvss=rule["cvss"],
                            evidence=str(expiry),
=======

                            scan=scan,

                            title=rule["title"],

                            severity=rule["severity"],

                            description=f"Domain expires in {days} days.",

                            recommendation=rule["recommendation"],

                            category="WHOIS",

                            cvss=rule["cvss"],

                            evidence=str(expiry)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                        )

                        findings += 1

                except Exception:

<<<<<<< HEAD
                    pass

                # =====================================================
=======
                    pass    

                 # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        # CLOUD FINDINGS
        # =====================================================

        cloud = report.get("cloud", {})

        for key, rule in CLOUD_RULES.items():

            if cloud.get(key):

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description=rule["description"],
                    recommendation=rule["recommendation"],
                    category=rule["category"],
                    cvss=rule["cvss"],
                    evidence=str(cloud.get(key)),
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description=rule["description"],

                    recommendation=rule["recommendation"],

                    category=rule["category"],

                    cvss=rule["cvss"],

                    evidence=str(cloud.get(key))

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1

<<<<<<< HEAD
            # =====================================================
=======
               # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        # THREAT INTELLIGENCE FINDINGS
        # =====================================================

        threat = report.get("threat", {})

        for key, rule in THREAT_RULES.items():

            if threat.get(key):

                FindingEngine.create(
<<<<<<< HEAD
                    scan=scan,
                    title=rule["title"],
                    severity=rule["severity"],
                    description=rule["description"],
                    recommendation=rule["recommendation"],
                    category=rule["category"],
                    cvss=rule["cvss"],
                    evidence=str(threat.get(key)),
=======

                    scan=scan,

                    title=rule["title"],

                    severity=rule["severity"],

                    description=rule["description"],

                    recommendation=rule["recommendation"],

                    category=rule["category"],

                    cvss=rule["cvss"],

                    evidence=str(threat.get(key))

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

                findings += 1
        # =====================================================
        # FUTURE AI ANALYZER
        # =====================================================

        ai = report.get("ai")

        if ai:
            pass

<<<<<<< HEAD
        return findings
=======
        return findings        
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
