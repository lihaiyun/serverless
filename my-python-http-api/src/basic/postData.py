import json

def handler(event, context):
    # Extracting request body
    body = event.get('body', '')
    
    # If the body is JSON, parse it
    try:
        body = json.loads(body)
    except json.JSONDecodeError:
        # If body is not a valid JSON, leave it as a string
        pass
    print(f"Request Body: {body}")
    
    if body:
        name = body.get('name')
        print(f"Name: {name}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
