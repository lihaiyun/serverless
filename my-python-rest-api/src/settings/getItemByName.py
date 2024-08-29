import json
import boto3
from boto3.dynamodb.conditions import Key

def handler(event, context):
    # Get name from path parameters
    name = event.get('pathParameters', {}).get('name')
    print(f"Name: {name} ")
    if name is None:
        return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Name is required'})
            }

    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # DynamoDB table
    table_name = "TestSettings"
    table = dynamodb.Table(table_name)
    
    try:
        # Get item from DynamoDB table
        response = table.get_item(Key={'name': name})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Technical error'})
        }
