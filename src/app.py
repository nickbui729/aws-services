def lambda_handler(event, context):
    print('IMAGE RECIEVED')
    return {"statusCode": 200, "body": "Helloooooooo, world"}
