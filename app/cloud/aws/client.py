"""
CloudShield Enterprise
AWS Client Factory
"""

import boto3
from botocore.config import Config

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
AWS_REGION = "ap-south-1"


class AWSClient:

    def __init__(self):

<<<<<<< HEAD
        self.config = Config(retries={"max_attempts": 5, "mode": "standard"})

    def client(self, service):

        return boto3.client(service, region_name=AWS_REGION, config=self.config)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
