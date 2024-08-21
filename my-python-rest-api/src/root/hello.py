import json
import os

def handler(event, context):
    stage = os.environ.get('STAGE', 'dev')
    my_env_var = os.getenv('MY_ENV_VAR')
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
        "stage": stage,
        "my_env_var": my_env_var
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
