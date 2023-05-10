import json
from urllib.request import urlopen
from geopy.distance import geodesic,Point
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import os
import matplotlib.path as mplPath
import geojson

def get_stations_data():
    POSTGRES_USER=os.getenv('POSTGRES_USER')
    POSTGRES_PASS=os.getenv('POSTGRES_PASS')
    POSTGRES_HOST=os.getenv('POSTGRES_HOST')
    POSTGRES_DB=os.getenv('POSTGRES_DB')
    POSTGRES_PORT=os.getenv('POSTGRES_PORT')

    DB_STR=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    engine=create_engine(DB_STR,
                    connect_args={'options': '-csearch_path=eco_bikes' }
                    )
    conn = engine.connect()

    max_reload_id=pd.read_sql('select max(reload_id) from metadata_load',con=conn).values[0][0]

    data_station=pd.read_sql(f"""select ss.station_id,
                ss.num_bikes_available,
                si.lat,
                si.lon,
                si.address
                from eco_bikes.station_status ss 
                left join eco_bikes.station_info si on ss.station_id=si.station_id and ss.reload_id=si.reload_id 
                where ss.reload_id={max_reload_id}
                and ss.num_bikes_available>0""",conn)[['station_id','lat','lon','num_bikes_available','address']]
    return data_station

def verify_point_inside_polygon(user_latitude,user_longitude):
    urL_geojson='https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/perimetro/perimetro.geojson'
    response = urlopen(urL_geojson)
    data_json = geojson.loads(response.read())
    polygon_caba=mplPath.Path(data_json['features'][0]['geometry']['coordinates'][0][0])
    punto_usuario=(user_longitude,user_latitude)

    var_bool=None

    if polygon_caba.contains_point((user_longitude,user_latitude)):
        var_bool=True
    else:
        var_bool=False

    return var_bool  

def lambda_handler(event, context):
    
    data_station=get_stations_data()
    print(data_station)

    try:

        # Get values from API Gateway
        data_station['user_lat']=float(event['queryStringParameters']['user_lat'])
        data_station['user_lon']=float(event['queryStringParameters']['user_lon'])
        user_lat=float(event['queryStringParameters']['user_lat'])
        user_lon=float(event['queryStringParameters']['user_lon'])

        if verify_point_inside_polygon(user_lat,
                                       user_lon):

            data_station['station_point']=data_station.apply(lambda row: Point(latitude=row['lat'],
                                                                                longitude=row['lon']),
                                                                                axis=1)
            data_station['user_distance_meters']=data_station.apply(lambda row: geodesic(row[['lat','lon']],
                                                                                row[['user_lat','user_lon']]).m,axis=1)

            station1=data_station.sort_values(by='user_distance_meters').iloc[0,:]
            station2=data_station.sort_values(by='user_distance_meters').iloc[1,:]
            
            body =f"""<html><head><title>Su estacion de ecobici mas cercana</title></head><body><h1>Estacion mas cercana</h1><p>A continuacion encontrara los datos:<ul><li>Direcccion: {station1['address']}</li><li>Cantidad de bicicletas disponibles: {station1['num_bikes_available']}</li></ul></p><h1>Segunda alternativa</h1><p>Como segunda alternativa: <ul><li>Direcccion: {station2['address']}</li><li>Cantidad de bicicletas disponibles: {station2['num_bikes_available']}</li></ul></p></body></html>"""

        else:
            body ='<html><head><title>Su estacion de ecobici mas cercana</title></head><body><h1>Su punto esta fuera de la Ciudad Autonoma de Buenos Aires</h1><a href="http://itba-geolocalizacion-bucket.s3-website-us-east-1.amazonaws.com/">Para retornar a la pagina principal</a><p>Recorda ingresar con el formato correcto: ##.## (por ejemplo: 58.16)</p></body></html>'

    except:
        body = '<html><head><title>Su estacion de ecobici mas cercana</title></head><body><h1>Por favor ingresa nuevamente la latitud y longitud</h1><a href="http://itba-geolocalizacion-bucket.s3-website-us-east-1.amazonaws.com/">Para retornar a la pagina principal</a><h2>Recorda ingresar con el formato correcto: ##.## (por ejemplo: 58.16)</h2></body></html>'
    
    return {
        'statusCode': 200,
        'body': body,
        'headers': {"content-type": "text/html"},
         }