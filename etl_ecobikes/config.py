from constants import ROOT_DIR
from dotenv import load_dotenv
import os

load_dotenv()

API_CLIENT_ID=os.getenv('api_client_id')
API_CLIENT_SECRET=os.getenv('api_client_secret')

URL_SYSTEM_INFORMATION=os.getenv('url_system_information')
URL_STATION_STATUS=os.getenv('url_station_status')
URL_STATION_INFO=os.getenv('urL_stations_info')

POSTGRES_SCHEMA=os.getenv('POSTGRES_SCHEMA')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASS=os.getenv('POSTGRES_PASS')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')

DB_STR=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"