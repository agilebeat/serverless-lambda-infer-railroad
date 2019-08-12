try:
  import unzip_requirements
except ImportError:
  pass


import json
import boto3 


import tensorflow as tf
from tensorflow.python.platform import gfile
#from tensorflow.python.keras.preprocessing import image
from PIL import Image

import numpy as np
import base64
import io

    
    
def run_classify_image(img):
    
    f = gfile.FastGFile("tf-models/tf_model.pb", 'rb')
    graph_def = tf.GraphDef()
   # Parses a serialized binary message into the current message.
    graph_def.ParseFromString(f.read())
    f.close()

    sess = tf.Graph()
    with sess.as_default() as graph:
        tf.import_graph_def(graph_def)
        softmax_tensor = sess.get_tensor_by_name('import/activation_15_2/Softmax:0')

    with tf.Session(graph=graph) as sess:
        predictions = sess.run(softmax_tensor, {'import/conv2d_6_input_2:0': img})
         
    return predictions    
        


def inferHandler(event, context):
    body_txt = event['body']
    body_json = json.loads(body_txt)
    z = body_json['z'] 
    x = body_json['x']
    y = body_json['y']
    tile_base64 = body_json['tile_base64'] 
    

    img = base64.urlsafe_b64decode(tile_base64)
    img = io.BytesIO(img)
    img = Image.open(img)

    rgb_im = img.convert('RGB')
    img = np.asarray(rgb_im)/255.
    img = np.expand_dims(img, axis=0)

    predictions = run_classify_image(img)

    AWS_BUCKET_NAME_rail = 'wmts-maprover'
    AWS_BUCKET_NAME_other = 'wmts-maprover' 

    if predictions[0][0] > predictions[0][1]:
        dic = False
        AWS_BUCKET_NAME = AWS_BUCKET_NAME_other
    else:
        dic = True
        AWS_BUCKET_NAME = AWS_BUCKET_NAME_rail

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
        "body": json.dumps({'RailClass': dic})
    }
    
    return response
