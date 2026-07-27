"""
CloudShield Enterprise
AWS Service
"""

import boto3


class AWSService:

    def __init__(

        self,

        region="ap-south-1"

    ):

        self.region = region

    def session(self):

        return boto3.Session(

            region_name=self.region

        )

    def ec2(self):

        return self.session().client(

            "ec2"

        )

    def s3(self):

        return self.session().client(

            "s3"

        )

    def iam(self):

        return self.session().client(

            "iam"

        )