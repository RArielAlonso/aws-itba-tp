from extract import extract
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s',
                  level=logging.INFO,
                  datefmt='%d-%b-%y %H:%M:%S')

if __name__=='__main__':
   logging.info('ETL Process has started')
   data_system_info,data_stations_info,data_stations_status=extract()
   print(data_system_info)
   print(data_stations_status)
   print(data_stations_info)
   logging.info('ETL Process has ended succesfully')
   

   