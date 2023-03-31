from extract import extract
from config import DB_STR,POSTGRES_SCHEMA
from sqlalchemy import create_engine
import logging
import datetime as dt
import pandas as pd


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s',
                  level=logging.INFO,
                  datefmt='%d-%b-%y %H:%M:%S')


def create_connection():
   engine=create_engine(DB_STR,
                    connect_args={'options': '-csearch_path=eco_bikes' }
                    )
   conn = engine.connect()

   return conn

def get_max_reload():
   if pd.read_sql('select max(reload_id) from metadata_load',con=conn).values[0][0]==None:
      reload_id=1
   else:
      reload_id=pd.read_sql('select max(reload_id) from metadata_load',con=conn).values[0][0]+1
   return reload_id
	

if __name__=='__main__':
   logging.info('ETL Process has started')
   conn=create_connection()
   reload_id=get_max_reload()
   date_reaload=dt.datetime.now().strftime("%Y-%m-%d %H:%M")
   
   pd.DataFrame([[reload_id,date_reaload]],
             columns=['reload_id','date_reload']).to_sql('metadata_load',
                                                con=conn,
                                                index=False,
                                                if_exists='append')

   
   data_system_info,data_stations_info,data_stations_status=extract()
   data_system_info['reload_id']=reload_id
   data_stations_info['reload_id']=reload_id
   data_stations_status['reload_id']=reload_id

   print(data_system_info)
   print(data_stations_status)
   print(data_stations_info)
   logging.info('Extract finished') 

   data_system_info.to_sql('general_info',
        	                  conn,
        	                  index=False,
        	                  if_exists='append'
                           )
   data_stations_info.to_sql('station_info',
        	                  conn,
        	                  index=False,
        	                  if_exists='append'
                           )
   data_stations_status.to_sql('station_status',
        	                  conn,
        	                  index=False,
        	                  if_exists='append'
                           )
   
   logging.info('Load finished')

   logging.info('ETL Process has ended succesfully')
   
