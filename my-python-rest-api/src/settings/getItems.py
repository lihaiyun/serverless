import json
import boto3
from boto3.dynamodb.conditions import Key

def handler(event, context):
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # DynamoDB table
    table_name = "TestSettings"
    table = dynamodb.Table(table_name)
    
    try:
        # Get items from DynamoDB table
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Technical error'})
        }
