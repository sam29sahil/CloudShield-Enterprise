"""
CloudShield Enterprise
AWS Service
"""

import boto3


class AWSService:

<<<<<<< HEAD
    def __init__(self, region="ap-south-1"):
=======
    def __init__(

        self,

        region="ap-south-1"

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        self.region = region

    def session(self):

<<<<<<< HEAD
        return boto3.Session(region_name=self.region)

    def ec2(self):

        return self.session().client("ec2")

    def s3(self):

        return self.session().client("s3")

    def iam(self):

        return self.session().client("iam")
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
