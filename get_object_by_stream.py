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
obj = buck.Object('exchanges/row-2807.json')
obj_stream = obj.get()['Body']
json_obj = json.loads(obj_stream.read())
print(json_obj)
