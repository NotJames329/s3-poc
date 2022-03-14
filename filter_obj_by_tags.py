import boto3
from botocore.config import Config

s3 = boto3.resource('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id='admin',
                    aws_secret_access_key='password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

filtered_objects = []

buck = s3.Bucket('exchange-rate-to-usd')
for obj in buck.objects.all():
    tags = s3.meta.client.get_object_tagging(
        Bucket=obj.bucket_name,
        Key=obj.key,
    )['TagSet']
    for tag in tags:
        if tag['Key'] == 'date':
            if tag['Value'].startswith('2014'):
                filtered_objects.append(obj)
            break

print(filtered_objects)
