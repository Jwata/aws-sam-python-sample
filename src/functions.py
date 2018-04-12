import json
import numpy as np

def search(request, context):
    nparr = np.array([1,2,3])
    return create_response(200, {
        'nparr': nparr.tolist()
    })

def create_response(status_code, body):
    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }
