import os
from sys import exit, stdout
from time import sleep
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("aws_access_key")
aws_secret_access_key = os.getenv("aws_secret_access_key")
frontend_instance_id = os.getenv("frontend_instance_id")
backend_instance_id = os.getenv("backend_instance_id")

ec2 = boto3.client(
    "ec2",
    "eu-west-2",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key,
)

response = ec2.stop_instances(InstanceIds=[backend_instance_id])
response = ec2.stop_instances(InstanceIds=[frontend_instance_id])
