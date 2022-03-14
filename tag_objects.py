import json

import boto3
from botocore.client import Config

s3 = boto3.resource('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id='admin',
                    aws_secret_access_key='password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')


buck = s3.Bucket('exchange-rate-to-usd')
for obj in buck.objects.all():
    json_obj = json.loads(obj.get()['Body'].read())
    s3.meta.client.put_object_tagging(
        Bucket=obj.bucket_name,
        Key=obj.key,
        Tagging={
            'TagSet': [
                {
                    'Key': 'date',
                    'Value': json_obj['date']
                }
            ]
        }
    )
