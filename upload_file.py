import boto3
from botocore.client import Config


s3 = boto3.resource('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id='admin',
                    aws_secret_access_key='password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')




s3.Bucket('hello').upload_file('files/try.txt','try2.txt')


print("Uploaded files/try.txt")
