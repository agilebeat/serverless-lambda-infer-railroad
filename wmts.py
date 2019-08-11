try:
  import unzip_requirements
except ImportError:
  pass


import json
import boto3
import base64
import string
import random
        
def select_server():
    servers = 'abc'
    return random.choice(servers)

def wmtsHandler(event, context):
    z = event['pathParameters']['z']
    x = event['pathParameters']['x']
    y = event['pathParameters']['y']
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












