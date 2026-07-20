"""
CloudShield Enterprise
AWS Client Factory
"""

import boto3
from botocore.config import Config


AWS_REGION = "ap-south-1"


class AWSClient:

    def __init__(self):

        self.config = Config(

            retries={

                "max_attempts": 5,

                "mode": "standard"

            }

        )

    def client(self, service):

        return boto3.client(

            service,

            region_name=AWS_REGION,

            config=self.config

        )