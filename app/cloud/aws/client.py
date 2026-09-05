"""
CloudShield Enterprise
AWS Client Factory
"""

import os

import boto3
from botocore.config import Config

DEFAULT_AWS_REGION = "ap-south-1"


class AWSClient:

    def __init__(self, region=None):

        self.config = Config(retries={"max_attempts": 5, "mode": "standard"})
        self.region = region or os.getenv("AWS_DEFAULT_REGION", DEFAULT_AWS_REGION)

    def client(self, service):

        return boto3.client(service, region_name=self.region, config=self.config)


def aws_region(region=None):
    return region or os.getenv("AWS_DEFAULT_REGION", DEFAULT_AWS_REGION)
