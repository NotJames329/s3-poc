import json

import boto3
from botocore.client import Config
import pandas as pd
import numpy as np


s3 = boto3.client('s3',
                    endpoint_url='http://minio:9000',
                    aws_access_key_id='admin',
                    aws_secret_access_key='password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')


filename = 'exchange-rate-to-usd'

df = pd.read_csv(f'dataset/{filename}.csv').replace({np.nan: None})
rows = df.to_dict(orient='records')

# s3.create_bucket(Bucket=filename)

for index, row in enumerate(rows):
    row_json = json.dumps(row).encode('utf-8')
    s3.put_object(Body=row_json, Bucket=filename, Key=f'exchanges/row-{index}.json')

print("Uploaded csv")
