import base64
import boto3
import json
import os

ddb_client = boto3.client('dynamodb')
table_name = os.environ['STM_TABLE_NAME']

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

        txn_id = parsed['txnId']
        model_id = parsed['modelId']

        print 'processing status for transaction {} model {}'.format(
            txn_id, model_id
        )

        response = ddb_client.get_item(
            TableName=table_name,
            Key={
                'modelId': {'S': model_id}
            }
        )

        if not 'Item' in response:
            print 'Model {} not present in {}'.format(model_id, table_name)
            return
        
        item = response['Item']
        fn_name = item['functionName']['S']
        print fn_name
