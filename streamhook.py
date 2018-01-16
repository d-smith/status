import boto3

# Note: sender and recipient email addresses must be verified in the 
# SES sandbox
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    print event
    records = event['Records']
    for r in records:
        ddbCtx = r['dynamodb']
        print ddbCtx
        newImg = ddbCtx['NewImage']
        print newImg
        
    ses_client.send_email(
        Destination={
            'ToAddresses': [
                'doug.smith@fmr.com',
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': "Hey there",
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Status Update',
            },
        },
        Source='a045103@fmr.com'

    )    