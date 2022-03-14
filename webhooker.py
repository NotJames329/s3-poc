import json

from fastapi import FastAPI, Request
import boto3
from botocore.client import Config


app = FastAPI()
s3 = boto3.resource('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id='admin',
                    aws_secret_access_key='password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')


@app.post("/")
async def root(request: Request):
    """
    webhook to minio and download file
    """
    event: dict = await request.json()
    with open('event.json', 'w') as file:
        json.dump(event, file, indent=4)
    bucket = event['Records'][0]['s3']['bucket']['name']
    obj = event['Records'][0]['s3']['object']['key']
    s3.Bucket(bucket).download_file(obj, f'downloads/{obj}')

