import json
import boto3
from boto3.dynamodb.conditions import Key

def handler(event, context):
    # Extracting query string parameters
    query_string_parameters = event.get('queryStringParameters', {})
    print(f"Query String Parameters: {query_string_parameters}")
    if query_string_parameters is None:
        return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Request is invalid'})
            }
    
    # Extracting name from query string parameters
    name = query_string_parameters.get('name')
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
