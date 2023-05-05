import json
from geopy.distance import geodesic

def lambda_handler(event, context):
    
    if 'queryStringParameters' in event:
        distance=geodesic((event['queryStringParameters']['user_lat'],
                            event['queryStringParameters']['user_lon']),
                            (-34.598771,-58.374068)).m
        body = '<html><head><title>Su estacion de ecobici mas cercana</title></head><body><h1>La distancia a tu ecobici mas cercana es  {} metros</h1></body></html>'.format(round(distance))
        
    else:    # If no parameters
        print('No parameters!')
        body = 'Por favor ingresa nuevamente la latitud y longitud'
    
    return {
        'statusCode': 200,
        'body': body,
        'headers': {"content-type": "text/html"},
         }