try:
  import unzip_requirements
except ImportError:
  pass


import json
import boto3
import base64
        


def inferHandler(event, context):
    body_txt = event['body']
    body_json = json.loads(body_txt)
    z = body_json['z'] 
    x = body_json['x']
    y = body_json['y']
    tile_base64 = body_json['tile_base64'] 


    AWS_BUCKET_NAME = 'wmts-maprover'

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    path = z + '/' + x + '/' + y
    data = base64.b64decode(tile_base64)
    

    bucket.put_object(
        ContentType='image/png',
        Key=path,
        Body=data,
        ACL='public-read'
    )


    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps({'Persist': 'Completed'})
    }
    
    return response












