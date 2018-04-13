import json

def search(request, context):
    from services.location import search
    return create_response(200, {
        'results': search()
    })

def detail(request, context):
    from services.location import detail
    return create_response(200, detail())

def create_response(status_code, body):
    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }

def error_response(status_code, error):
    return {
        'statusCode': status_code,
        'error': json.dumps(body)
    }
