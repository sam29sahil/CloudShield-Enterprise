"""
CloudShield Enterprise
DNS Scanner
"""

import dns.resolver

from app.scanner.constants import DNS_RECORDS


def dns_scan(hostname):
    """
    Collect common DNS records.
    """

    results = {}

    for record in DNS_RECORDS:

        try:

            answers = dns.resolver.resolve(
                hostname,
                record
            )

            results[record] = [

                answer.to_text()

                for answer in answers

            ]

        except Exception:

            results[record] = []

    return results