import unittest

from botocore.exceptions import ClientError, NoCredentialsError

from app.cloud.aws.connection import AWSConnection
from app.cloud.aws.scanner import AWSReadOnlyScanner


class FakeClient:
    def __init__(self, service, sts_mode="connected", denied=None):
        self.service = service
        self.sts_mode = sts_mode
        self.denied = denied or set()

    def get_caller_identity(self):
        if self.sts_mode == "missing":
            raise NoCredentialsError()
        if self.sts_mode == "invalid":
            raise ClientError({"Error": {"Code": "InvalidClientTokenId"}}, "GetCallerIdentity")
        if self.sts_mode == "denied":
            raise ClientError({"Error": {"Code": "AccessDenied"}}, "GetCallerIdentity")
        return {"Account": "123456789012", "Arn": "arn:aws:iam::123456789012:role/test"}

    def describe_instances(self):
        return {"Reservations": []}

    def describe_security_groups(self):
        return {"SecurityGroups": []}

    def describe_volumes(self):
        return {"Volumes": []}

    def describe_addresses(self):
        return {"Addresses": []}

    def list_buckets(self):
        return {"Buckets": []}

    def list_users(self):
        if "iam" in self.denied:
            raise ClientError({"Error": {"Code": "AccessDenied"}}, "ListUsers")
        return {"Users": []}


class FakeFactory:
    def __init__(self, sts_mode="connected", denied=None):
        self.sts_mode = sts_mode
        self.denied = denied or set()

    def client(self, service):
        return FakeClient(service, self.sts_mode, self.denied)


class AWSFlowTests(unittest.TestCase):
    def test_missing_credentials(self):
        result = AWSConnection(client_factory=FakeFactory("missing")).check()
        self.assertEqual(result["status"], "NOT_CONFIGURED")

    def test_invalid_credentials(self):
        result = AWSConnection(client_factory=FakeFactory("invalid")).check()
        self.assertEqual(result["status"], "INVALID_CREDENTIALS")

    def test_connected_scan_and_account(self):
        result = AWSReadOnlyScanner(region="us-east-1", client_factory=FakeFactory()).scan()
        self.assertEqual(result["connection"]["status"], "CONNECTED")
        self.assertEqual(result["account_id"], "123456789012")
        self.assertEqual(result["scan_status"], "SCAN_COMPLETED")

    def test_service_permission_failure_does_not_stop_scan(self):
        result = AWSReadOnlyScanner(client_factory=FakeFactory(denied={"iam"})).scan()
        self.assertTrue(result["services"]["ec2"]["success"])
        self.assertEqual(result["services"]["iam"]["status"], "PERMISSION_LIMITED")
        self.assertEqual(result["scan_status"], "SCAN_COMPLETED_WITH_WARNINGS")

    def test_dashboard_contract_contains_all_service_status_keys(self):
        scanner = AWSReadOnlyScanner(client_factory=FakeFactory("missing"))
        result = scanner.dashboard()
        for name in ("ec2", "s3", "iam", "security_groups", "ebs", "elastic_ips"):
            self.assertIn(name, result["service_status"])
            self.assertIn("status", result["service_status"][name])
            self.assertIn("color", result["service_status"][name])
            self.assertIn("message", result["service_status"][name])

    def test_credentials_are_not_returned(self):
        result = AWSReadOnlyScanner(client_factory=FakeFactory()).scan()
        self.assertNotIn("AWS_ACCESS_KEY_ID", repr(result))
        self.assertNotIn("AWS_SECRET_ACCESS_KEY", repr(result))
        self.assertNotIn("AWS_SESSION_TOKEN", repr(result))


if __name__ == "__main__":
    unittest.main()
