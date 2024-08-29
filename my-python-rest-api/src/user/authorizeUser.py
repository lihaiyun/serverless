import json
import boto3
from botocore.exceptions import ClientError
import os

def get_secret():
    stage = os.getenv('STAGE')
    secret_name = f"{stage}-my-secret"
    region_name = "ap-southeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e
    
    secret = json.loads(response['SecretString'])
    return secret

def handler(event, context):
    # Get secret from Secrets Manager
    secret = get_secret()
    my_secret = secret['MySecret']
    print(f"My Secret: {my_secret}")

    body = {
        "message": "You are authorized to access this resource!"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
