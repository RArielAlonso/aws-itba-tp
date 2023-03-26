from decouple import AutoConfig
from etl_ecobikes.constants import ROOT_DIR

config=AutoConfig(search_path=ROOT_DIR)

API_CLIENT_ID=config('api_client_id')
API_CLIENT_SECRET=config('api_client_secret')

URL_SYSTEM_INFORMATION=config('url_system_information')
URL_STATION_STATUS=config('url_station_status')
URL_STATION_INFO=config('urL_stations_info')

DB_STR=config('db_str')
POSTGRES_SCHEMA=config('POSTGRES_SCHEMA')