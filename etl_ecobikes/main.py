from extract import extract


if __name__=='__main__':
   data_system_info,data_stations_info,data_stations_status=extract()
   print(data_system_info)
   print(data_stations_status)
   print(data_stations_info)
   

   