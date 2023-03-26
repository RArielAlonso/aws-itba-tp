from extract import extract
from config import DB_STR,POSTGRES_SCHEMA
from sqlalchemy import create_engine
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s',
                  level=logging.INFO,
                  datefmt='%d-%b-%y %H:%M:%S')

engine=create_engine(DB_STR,
                    connect_args={'options': '-csearch_path=eco_bikes' }
                    )
conn = engine.connect() 

if __name__=='__main__':
   logging.info('ETL Process has started')
   
   data_system_info,data_stations_info,data_stations_status=extract()
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
   
