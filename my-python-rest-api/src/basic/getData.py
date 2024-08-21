import json

def handler(event, context):
    # Extracting query string parameters
    query_string_parameters = event.get('queryStringParameters', {})
    print(f"Query String Parameters: {query_string_parameters}")
    
    # Check if query string parameters are not None
    if query_string_parameters:
        greeting = query_string_parameters.get('greeting')
        print(f"Greeting: {greeting} ")
    
    return {
        'statusCode': 200,
        'body': json.dumps(query_string_parameters)
    }
