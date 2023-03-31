import pandas as pd
import requests
from config import API_CLIENT_ID,API_CLIENT_SECRET,URL_SYSTEM_INFORMATION,URL_STATION_STATUS,URL_STATION_INFO
from constants import SQL_DIR
import datetime as dt

def get_request(url):
	"""Function to get request from API
	Args:
	url: str to connect to the API
	"""
	return requests.get(url=url,
						params={'client_id':API_CLIENT_ID,
								'client_secret':API_CLIENT_SECRET})

def api_to_dataframe_system(request):
    return pd.json_normalize(request.json()['data'])

def api_to_dataframe_station(request):
    return pd.json_normalize(request.json()['data']['stations'])

def extract():
	
	data_system_info=api_to_dataframe_system(get_request(URL_SYSTEM_INFORMATION))
	data_stations_status=api_to_dataframe_station(get_request(URL_STATION_STATUS))
	data_stations_info=api_to_dataframe_station(get_request(URL_STATION_INFO))
	data_stations_status['station_id']=data_stations_status['station_id'].astype(int)
	data_stations_info['station_id']=data_stations_info['station_id'].astype(int)

	return data_system_info,data_stations_info,data_stations_status

if __name__=="__main__":
	print("Initialing the extract")
	print(dt.datetime.now())

	extract()
	
	print("Finished")
	print(dt.datetime.now())

