import boto3
from botocore.config import Config

s3 = boto3.client('s3',
                  endpoint_url='http://minio:9000',
                  aws_access_key_id='admin',
                  aws_secret_access_key='password',
                  config=Config(signature_version='s3v4'),
                  region_name='us-east-1')

bucket_name = 'exchange-rate-to-usd'
resp = s3.select_object_content(
    Bucket=bucket_name,
    Key='exchanges/row-2807.json',
    Expression='select * from s3object[*] s where s.euro_to_usd > 0.6',
    ExpressionType='SQL',
    InputSerialization={'JSON': {'Type': 'Document'}},
    OutputSerialization={
        'JSON': {}
    })
for event in resp['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode('utf-8'))
    elif 'Stats' in event:
        print(event['Stats'])
