import json
def handler(event, context):
    body = {
        "message": "You are authorized to access this resource!"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
