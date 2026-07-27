"""
CloudShield Enterprise
Cloud Findings Engine
"""


class CloudFindingsEngine:
    """
    Generate cloud security findings
    from AWS scanner results.
    """

    def generate(self, results):

        findings = []

        # ---------- EC2 ----------

        ec2 = results.get("ec2", {})

        if not ec2.get("success"):

            findings.append({

                "severity": "High",

                "title": "EC2 Scan Failed",

                "service": "EC2",

                "status": "Open"

            })

        # ---------- S3 ----------

        s3 = results.get("s3", {})

        if not s3.get("success"):

            findings.append({

                "severity": "High",

                "title": "S3 Scan Failed",

                "service": "S3",

                "status": "Open"

            })

        # ---------- IAM ----------

        iam = results.get("iam", {})

        if not iam.get("success"):

            findings.append({

                "severity": "Medium",

                "title": "IAM Configuration Issue",

                "service": "IAM",

                "status": "Open"

            })

        # ---------- Security Groups ----------

        sg = results.get("security_groups", {})

        if not sg.get("success"):

            findings.append({

                "severity": "Medium",

                "title": "Security Groups Unavailable",

                "service": "Security Groups",

                "status": "Open"

            })

        # ---------- CloudTrail ----------

        ct = results.get("cloudtrail", {})

        if not ct.get("success"):

            findings.append({

                "severity": "High",

                "title": "CloudTrail Not Available",

                "service": "CloudTrail",

                "status": "Open"

            })

        # ---------- GuardDuty ----------

        gd = results.get("guardduty", {})

        if not gd.get("success"):

            findings.append({

                "severity": "High",

                "title": "GuardDuty Not Enabled",

                "service": "GuardDuty",

                "status": "Open"

            })

        # ---------- Inspector ----------

        inspector = results.get("inspector", {})

        if not inspector.get("success"):

            findings.append({

                "severity": "Medium",

                "title": "Inspector Scan Failed",

                "service": "Inspector",

                "status": "Open"

            })

        return findings