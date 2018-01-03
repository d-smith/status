# This function is used to implement the pizza status tracking
# application. It takes correlated events and an assumed progression to
# maintain a simple model.

# This model will be completely simple minded - no attempts to deal with out
# of order messages, skipped states, etc - it will simple persist the state in
# the model table

import os
import boto3

table_name = os.environ['MODEL_INSTANCE_TABLE_NAME']

ddb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    print 'pizza function called with {}'.format(event)
    txn_id = event['txnId']
    instance_id = event['instanceId']
    state = event['state']

    response = ddb_client.put_item(
        TableName=table_name,
        Item={
            'instanceId':{'S': instance_id},
            'txnId':{'S': txn_id},
            'state':{'S' : state}
        }
    )

    print response



