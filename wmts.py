try:
  import unzip_requirements
  import json
  import boto3
  from botocore.errorfactory import ClientError
  import base64
  import string
  import random
  from io import BytesIO
except ImportError:
  pass



        
def select_server():
    servers = 'abc'
    return random.choice(servers)

def get_redirect(z, x, y):
    response = {
        "statusCode": 302,
        "headers": {'Location': 'https://' +
                                select_server() +
                                '.tile.openstreetmap.org/' +
                                z + '/' +
                                x + '/' +
                                y}
    }
    return response

def construct_debug_response(z, x, y, e):
    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps({'Exception': str(e), 'key': str(z) +'/'+ str(x) + '/' + str(y)})
    }
    return response

def read_tile(z, x, y):
    tile_64 = 'Initial String'
    response = None
    try:
        client = boto3.client('s3')
        tile = client.get_object(Bucket='wmts-maprover', Key=str(z) +'/'+ str(x) + '/' + str(y))
        tile_64 = base64.b64encode(BytesIO(tile['Body'].read()).read()).decode('UTF-8')
    except Exception as e:
        response = get_redirect(z, x, y)
    else:
        response = {
            "isBase64Encoded": True,
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png",
            },
            "body": tile_64
        }
    return response

def get_tile(z, x, y):
    body = "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAADYklEQVR4nO3UMWrDUBBAQZ/bKXUD3UKVA+q+DiPfRKlcxIFg3BjxpphmYWGbfZf7vh9A0+XTBwCfIwAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgAQJgBwctsYb+8KAJzUNsYxTdMxz/Ov+bIsx9f1+lIYBABO6vHgzwHYxjjWdRUAKHgOwH3fBQAqBADCBADCBADCvm+3P7NtDAEA/icAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAECYAEPYDw8wlgMsU1kgAAAAASUVORK5CYII="

    response =  {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png",
        },
        "body": body
    }
    return response

def wmtsHandler(event, context):
    z = event['pathParameters']['z']
    x = event['pathParameters']['x']
    y = event['pathParameters']['y']

    response = read_tile(z, x, y)
    return response












