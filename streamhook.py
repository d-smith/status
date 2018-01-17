import boto3

# Note: sender and recipient email addresses must be verified in the 
# SES sandbox
import json

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    print event
    records = event['Records']
    
    
    for r in records:
        notify = ''
        
        ddbCtx = r['dynamodb']
        newImg = ddbCtx['NewImage']
        
        if 'notify' in newImg:
            notify = newImg['notify']
            
            if notify != '' and len(notify.split('a') == 2:
            
                print 'send mail to {}'.format(notify)
                
                body = json.dumps(newImg)
                
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
                                'Data': body,
                            },
                        },
                        'Subject': {
                            'Charset': 'UTF-8',
                            'Data': 'Status Update',
                        },
                    },
                    Source='a045103@fmr.com')    