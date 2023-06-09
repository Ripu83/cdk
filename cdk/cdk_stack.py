from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_rds as rds,
    aws_ec2 as ec2,
)


from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #S3
        my_bucket =  s3.Bucket(self,"mybucket",bucket_name="ripu-bucket08012")
        #VPC
        vpc = ec2.Vpc.from_lookup(self, "default_vpc", is_default=True)  
        #RDS
        instance = rds.DatabaseInstance(self, "Instance",
        engine=rds.DatabaseInstanceEngine.MYSQL,
        instance_type = ec2.InstanceType("t2.micro"),
        vpc = vpc,
        vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC),
        port=3306,
        database_name = "db1")
