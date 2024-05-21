import sys
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def list_resources(service_name, region_name, user_profile):
    # Create session and auth the service
    try:
        session = boto3.Session(region_name=region_name,profile_name=user_profile)
        service = session.resource(service_name)
    except ClientError as e:
        print(f"Error: {e}")
        return

    # List resources as per service
    try:
        if service_name == "ec2":
            #ec2 = session.client(service_name)
            #response = ec2.describe_instances()
            instances = service.instances.all()
            print("EC2 Instances:")
            for instance in instances:
                print(f"- Instance ID: {instance.id}, State: {instance.state['Name']}")

        elif service_name == "s3":
            buckets = service.buckets.all()
            print("S3 Buckets:")
            for bucket in buckets:
                print(f"- Bucket Name: {bucket.name}")

        elif service_name == "dynamodb":
            tables = service.tables.all()
            print("DynamoDB Tables:")
            for table in tables:
                print(f"- Table Name: {table.name}")

        else:
            print(f"Unsupported service: {service_name}. Currently supports options are ec2, s3 and dynamodb")

    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 aws_list_services.py <service> <region> <user_profile>")
        sys.exit(1)

    # Assign arguments to variables
    service_name = sys.argv[1]
    region_name = sys.argv[2]
    user_profile = sys.argv[3]

    # Error if no creds are found
    try:
        list_resources(service_name, region_name, user_profile)
    except NoCredentialsError:
        print("Error: AWS credentials not found. Please configure your AWS credentials.")
