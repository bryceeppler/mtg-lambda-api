from lambda_function import lambda_handler

event = {'queryStringParameters': {'name': 'Dockside Extortionist'}}

print(lambda_handler(event, None))