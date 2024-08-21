import json
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

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
    if body is None:
        return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Request is invalid'})
            }

    # Extracting name from body
    name = body.get('name')
    print(f"Name: {name} ")
    if name is None:
        return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Name is required'})
            }
    
    # Prepare item with updated time
    item = body
    item['updatedAt'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
    
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # DynamoDB table
    table_name = "TestSettings"
    table = dynamodb.Table(table_name)
    
    try:
        # Put item into DynamoDB table
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Technical error'})
        }
