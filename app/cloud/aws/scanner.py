"""Canonical read-only AWS scan orchestration."""

from botocore.exceptions import BotoCoreError, ClientError

from app.cloud.aws.client import AWSClient, aws_region
from app.cloud.aws.connection import AWSConnection
from app.cloud.aws.ec2 import EC2Scanner
from app.cloud.aws.security_groups import SecurityGroupScanner
from app.cloud.aws.ebs import EBSScanner
from app.cloud.aws.elastic_ips import ElasticIPScanner
from app.cloud.aws.s3 import S3Scanner
from app.cloud.aws.iam import IAMScanner


class AWSReadOnlyScanner:
    scanner_types = {
        "ec2": EC2Scanner,
        "security_groups": SecurityGroupScanner,
        "ebs": EBSScanner,
        "elastic_ips": ElasticIPScanner,
        "s3": S3Scanner,
        "iam": IAMScanner,
    }

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)

    def connection_status(self):
        return AWSConnection(self.region, self._client_factory).check()

    def dashboard(self):
        connection = self.connection_status()
        service_names = ("ec2", "s3", "iam", "security_groups", "ebs", "elastic_ips")
        checks = {
            "ec2": ("ec2", "describe_instances", {"MaxResults": 5}, "total_instances"),
            "s3": ("s3", "list_buckets", {}, "total_buckets"),
            "iam": ("iam", "list_users", {"MaxItems": 1}, "total_users"),
            "security_groups": ("ec2", "describe_security_groups", {"MaxResults": 5}, "total_groups"),
            "ebs": ("ec2", "describe_volumes", {"MaxResults": 5}, "total_volumes"),
            "elastic_ips": ("ec2", "describe_addresses", {}, "total_addresses"),
        }
        services = {}
        service_status = {}
        for name in service_names:
            print(f"[AWS DEBUG] Starting service check: {name}", flush=True)
            if connection["status"] != "CONNECTED":
                result = {"success": False, "status": connection["status"], "error": connection["message"], "findings": []}
            else:
                client_name, operation, parameters, count_key = checks[name]
                try:
                    print(
                        f"[AWS DEBUG] Calling {client_name}.{operation} {parameters}",
                        flush=True
                    )
                    response = getattr(self._client_factory.client(client_name), operation)(**parameters)
                    print(
                        f"[AWS DEBUG] Completed {name}",
                        flush=True
                    )
                    collection_key = {
                        "total_instances": "Reservations",
                        "total_buckets": "Buckets",
                        "total_users": "Users",
                        "total_groups": "SecurityGroups",
                        "total_volumes": "Volumes",
                        "total_addresses": "Addresses",
                    }[count_key]
                    collection = response.get(collection_key, [])
                    if name == "ec2":
                        count = sum(len(item.get("Instances", [])) for item in collection)
                    else:
                        count = len(collection)
                    result = {"success": True, "status": "AVAILABLE", count_key: count, "findings": []}
                except Exception as error:
                    result = self._service_error(error)
            services[name] = result
            service_status[name] = self._status_object(result, connection)

        for name in ("cloudtrail", "guardduty", "inspector", "config"):
            service_status[name] = {
                "status": "NOT_CHECKED",
                "label": "Not checked",
                "color": "secondary",
                "message": "This service is not part of the dashboard health check.",
            }
        return {
            "provider": "AWS",
            "success": connection["status"] == "CONNECTED",
            "connection": connection,
            "account_id": connection.get("account_id"),
            "region": self.region,
            "scan_status": "NOT_STARTED",
            "services": services,
            "service_status": service_status,
            "findings": [],
            "summary": {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0},
            "security_score": 0,
        }

    def scan(self):
        connection = self.connection_status()
        services = {}
        findings = []
        for name, scanner_type in self.scanner_types.items():
            try:
                result = scanner_type(region=self.region, client_factory=self._client_factory).scan()
            except Exception as error:
                result = {"success": False, "error": str(error), "findings": []}
            if result.get("success"):
                result["status"] = "COMPLETED"
            else:
                result["status"] = "PERMISSION_LIMITED" if connection["status"] == "CONNECTED" else connection["status"]
            services[name] = result
            findings.extend(result.get("findings", []))

        summary = {key.lower(): 0 for key in ("Critical", "High", "Medium", "Low", "Info")}
        for finding in findings:
            severity = finding.get("severity", "Info").lower()
            if severity in summary:
                summary[severity] += 1
        score = max(0, 100 - summary["critical"] * 10 - summary["high"] * 7 - summary["medium"] * 4 - summary["low"])
        limited = [name for name, result in services.items() if result["status"] == "PERMISSION_LIMITED"]
        failed = [name for name, result in services.items() if result["status"] not in {"COMPLETED", "PERMISSION_LIMITED"}]
        if connection["status"] != "CONNECTED":
            scan_status = "SCAN_FAILED"
        elif limited or failed:
            scan_status = "SCAN_COMPLETED_WITH_WARNINGS"
        else:
            scan_status = "SCAN_COMPLETED"
        return {
            "provider": "AWS",
            "success": connection["status"] == "CONNECTED" and bool([item for item in services.values() if item.get("success")]),
            "connection": connection,
            "account_id": connection.get("account_id"),
            "region": self.region,
            "scan_status": scan_status,
            "services": services,
            "service_status": {name: self._status_object(result, connection) for name, result in services.items()},
            "findings": findings,
            "summary": summary,
            "security_score": score,
            "permission_limited_services": limited,
            "failed_services": failed,
        }

    @staticmethod
    def _status_object(result, connection):
        status = result.get("status", "FAILED")
        labels = {
            "AVAILABLE": ("Available", "success"),
            "COMPLETED": ("Completed", "success"),
            "PERMISSION_LIMITED": ("Permission Limited", "warning"),
            "NOT_CONFIGURED": ("Not Connected", "secondary"),
            "INVALID_CREDENTIALS": ("Invalid Credentials", "danger"),
            "UNAVAILABLE": ("Unavailable", "danger"),
        }
        label, color = labels.get(status, ("Failed", "danger"))
        return {"status": status, "label": label, "color": color, "message": result.get("error") or connection.get("message")}

    @staticmethod
    def _service_error(error):
        text = str(error).lower()
        if "credential" in text:
            status = "NOT_CONFIGURED"
            message = "AWS credentials are not configured."
        elif "accessdenied" in text or "permission" in text:
            status = "PERMISSION_LIMITED"
            message = "AWS service permission is unavailable."
        else:
            status = "UNAVAILABLE"
            message = "AWS service is temporarily unavailable."
        return {"success": False, "status": status, "error": message, "findings": []}