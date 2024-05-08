import requests
from datetime import datetime, timedelta
import geopy.geocoders
from geopy.geocoders import Nominatim
import certifi
import ssl
import sys


ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="weather_forecast app")


def find_lat_and_lon_for_city(input_city):
    location = geolocator.geocode(input_city)
    return (location.latitude, location.longitude)


def ask_for_city():
    input_city = input("Dla jakiego miasta chcesz sprawdzić pogodę?: ")
    return input_city


def ask_for_date():
    today = datetime.now().date()
    input_date = input("Podaj datę w formacie YYYY-mm-dd aby sprawdzić, czy będzie tego dnia padać: ")
    if input_date == "":
        input_date = today + timedelta(days=1)
    return input_date


def get_data_from_file(data, city, date):
    for key, values in data.items():
        if key == city:
            for city_keys, value in values.items():
                if city_keys == date:
                    return values
    return None


def retrieve_data_from_api(latitude, longitude, searched_date):
    url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
                   f"&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}"
                   f"&end_date={searched_date}")
    response = requests.get(url_address)

    if response.status_code == 200:
        return load_data_from_api_response_to_dict(response.json())
    else:
        print("Niestety takie miasto/data są nieosiągalne, lub pobranie danych się nie powiodło.")
        sys.exit()


def load_data_from_api_response_to_dict(data_from_api):
    date = data_from_api.get("daily").get("time")
    rain =  data_from_api.get("daily").get("rain_sum")
    dict = {
        date[0]: rain[0],
    }
    return dict


def will_it_rain(data, date):
    for key, value in data.items():
        if key == date:
            if value == 0.0:
                return "nie będzie padać"
            elif value > 0.0:
                return "będzie padać"
            else:
                return "co będzie, to będzie"
        else:
            continue

