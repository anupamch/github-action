def handler(event, context):
    # Get input values from the event object
    print("Event received:", event)
    
    # Access specific values from the event
    body = event.get('body')
    print("Body:", body)
    
    # Example: if event is JSON string, parse it
    if isinstance(body, str):
        import json
        try:
            data = json.loads(body)
            print("Parsed data:", data)
        except:
            print("Could not parse JSON from body")
    
    # Get other event properties
    path = event.get('path')
    method = event.get('httpMethod')
    headers = event.get('headers')
    query_params = event.get('queryStringParameters')
    
    print(f"Path: {path}, Method: {method}")
    print(f"Headers: {headers}")
    print(f"Query Parameters: {query_params}")
    
    return {
        "statusCode": 200,
        "body": "Hello from GitHub Actions Deployment!"
    }