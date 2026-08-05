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

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "High",
                    "title": "EC2 Scan Failed",
                    "service": "EC2",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "High",

                "title": "EC2 Scan Failed",

                "service": "EC2",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- S3 ----------

        s3 = results.get("s3", {})

        if not s3.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "High",
                    "title": "S3 Scan Failed",
                    "service": "S3",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "High",

                "title": "S3 Scan Failed",

                "service": "S3",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- IAM ----------

        iam = results.get("iam", {})

        if not iam.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "Medium",
                    "title": "IAM Configuration Issue",
                    "service": "IAM",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "Medium",

                "title": "IAM Configuration Issue",

                "service": "IAM",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- Security Groups ----------

        sg = results.get("security_groups", {})

        if not sg.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "Medium",
                    "title": "Security Groups Unavailable",
                    "service": "Security Groups",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "Medium",

                "title": "Security Groups Unavailable",

                "service": "Security Groups",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- CloudTrail ----------

        ct = results.get("cloudtrail", {})

        if not ct.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "High",
                    "title": "CloudTrail Not Available",
                    "service": "CloudTrail",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "High",

                "title": "CloudTrail Not Available",

                "service": "CloudTrail",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- GuardDuty ----------

        gd = results.get("guardduty", {})

        if not gd.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "High",
                    "title": "GuardDuty Not Enabled",
                    "service": "GuardDuty",
                    "status": "Open",
                }
            )
=======
            findings.append({

                "severity": "High",

                "title": "GuardDuty Not Enabled",

                "service": "GuardDuty",

                "status": "Open"

            })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ---------- Inspector ----------

        inspector = results.get("inspector", {})

        if not inspector.get("success"):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "Medium",
                    "title": "Inspector Scan Failed",
                    "service": "Inspector",
                    "status": "Open",
                }
            )

        return findings
=======
            findings.append({

                "severity": "Medium",

                "title": "Inspector Scan Failed",

                "service": "Inspector",

                "status": "Open"

            })

        return findings
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
