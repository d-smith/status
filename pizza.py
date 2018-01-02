# This function is used to implement the pizza status tracking
# application. It takes correlated events and an assumed progression to
# maintain a simple model

def lambda_handler(event, context):
    print 'pizza function called with {}'.format(event)
