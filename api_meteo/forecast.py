from file_handler import FileHandler
from utils import (get_data_from_file, find_lat_and_lon_for_city, ask_for_city, ask_for_date,
                   retrieve_data_from_api, will_it_rain)

file_handler = FileHandler("history.json")

city = ask_for_city()
date = str(ask_for_date())
latitude, longitude = find_lat_and_lon_for_city(city)

date_from_history = get_data_from_file(file_handler.data, city, date)

if not date_from_history:
    data_from_api = retrieve_data_from_api(latitude, longitude, date)
    file_handler.upload_request_to_data(city, date, data_from_api)
    file_handler.save_data_to_file()

data_for_forecast = get_data_from_file(file_handler.data, city, date)
will_it_rain(data_for_forecast, city, date)
