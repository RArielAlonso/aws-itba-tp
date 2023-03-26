import json
from geopy.distance import geodesic

def lambda_handler(event, context):
    
    
    distance=geodesic((-34.5986,-58.373062),(-34.598771,-58.374068)).m
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'+str(distance))
    }