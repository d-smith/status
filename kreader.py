import base64
import boto3
import json


def lambda_handler(event, context):
        
    records = event['Records']
    for rec in records:
        data = rec['kinesis']['data']
        decoded = base64.b64decode(data)
        print decoded
        
        parsed = json.loads(data)
        print parsed
