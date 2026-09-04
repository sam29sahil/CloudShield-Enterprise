import os
import unittest
from unittest.mock import patch

from app import create_app
from app.cloud.azure.client import (
    AZURE_CONFIGURATION_ERROR,
    AzureClient,
    AzureConfigurationError,
)
from app.cloud.azure.services import AzureService


class AzureOptionalTestCase(unittest.TestCase):

    def setUp(self):
        self.azure_keys = (
            "AZURE_SUBSCRIPTION_ID",
            "AZURE_TENANT_ID",
            "AZURE_CLIENT_ID",
            "AZURE_CLIENT_SECRET",
        )
        self.saved_environment = {
            key: os.environ.get(key) for key in self.azure_keys
        }

    def tearDown(self):
        for key, value in self.saved_environment.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value

    def test_application_starts_without_azure_credentials(self):
        with patch.dict(os.environ, {}, clear=False):
            for key in self.azure_keys:
                os.environ.pop(key, None)

            app = create_app()
            self.assertIsNotNone(app)

    def test_health_endpoint_does_not_require_azure(self):
        app = create_app()

        response = app.test_client().get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_client_reads_subscription_id_from_environment(self):
        with patch.dict(
            os.environ,
            {
                "AZURE_SUBSCRIPTION_ID": "subscription-from-env",
                "AZURE_TENANT_ID": "tenant",
                "AZURE_CLIENT_ID": "client",
                "AZURE_CLIENT_SECRET": "secret",
            },
        ):
            client = AzureClient()

            self.assertEqual(client.subscription(), "subscription-from-env")
            self.assertIsNone(client.configuration_error)

    def test_missing_configuration_is_graceful(self):
        with patch.dict(os.environ, {}, clear=False):
            for key in self.azure_keys:
                os.environ.pop(key, None)

            with patch.object(AzureClient, "_cli_subscription_id", return_value=None):
                client = AzureClient()
                service = AzureService()

            self.assertFalse(client.test_connection())
            self.assertEqual(
                service.summary()["error"],
                "Azure credentials are not configured.",
            )
            with self.assertRaisesRegex(AzureConfigurationError, AZURE_CONFIGURATION_ERROR):
                client.resource_client()

    def test_authentication_and_basic_scanner_routes_remain_available(self):
        app = create_app()
        client = app.test_client()

        self.assertLess(client.get("/auth/login").status_code, 500)
        self.assertLess(client.get("/scanner/").status_code, 500)


if __name__ == "__main__":
    unittest.main()
