import base64
import boto3
import json


def lambda_handler(event, context):
        
    print 'event: {}'.format(event)
    records = event['Records']
    for rec in records:
        data = rec['kinesis']['data']
        decoded = base64.b64decode(data)
        print 'decoded record data: {}'.format(decoded)
        
        print 'parse data'
        parsed = json.loads(decoded)
        print parsed
