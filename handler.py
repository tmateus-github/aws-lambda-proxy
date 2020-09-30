import json


def hello(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "lambda proxy",
            "Http verb": event['httpMethod']
        }),
    }
