try:
  import unzip_requirements
except ImportError:
  pass


import json
import boto3
import base64
        


def wmtsHandler(event, context):
    z = event['pathParameters']['z']
    x = event['pathParameters']['x']
    y = event['pathParameters']['y']
    response = {
        "statusCode": 302,
        "headers": {'Location': 'https://a.tile.openstreetmap.org/'
                                + z + '/' +
                                x + '/' +
                                y}
    }
    
    return response












