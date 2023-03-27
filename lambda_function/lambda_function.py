import json
from geopy.distance import geodesic

def lambda_handler(event, context):
    if 'queryStringParameters' in event:
        distance=geodesic((event['queryStringParameters']['user_lat'],
                           event['queryStringParameters']['user_lon']),
                           (-34.598771,-58.374068)).m
        body = 'The distance is {}'.format(distance)
        
    else:    # If no parameters
        print('No parameters!')
        body = 'Please retry your parameters'
    
    return {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {"content-type": "text/html"},
         }
