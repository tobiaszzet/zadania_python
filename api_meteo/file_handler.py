from utils import will_it_rain
import json


class FileHandler:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.path_to_file) as file:
            try:
                data = json.loads(file.read())
            except json.decoder.JSONDecodeError:
                data = {}
                json.dumps(data)
            return data

    def save_data_to_file(self):
        with open(self.path_to_file, mode="w") as file:
            file.write(json.dumps(self.data))

    def upload_request_to_data(self, city, date, data_api):
        if self.data == {}:
            self.data[city] = data_api
        else:
            rain = data_api.get(date)
            for key, values in self.data.items():
                if key == city:
                    self.data[key] |= {date: rain}
                    break
            else:
                self.data[city] = data_api

    def __setitem__(self, key, value):
        city, date = key
        city_data = self.data.get("city")
        if city_data:
            self.data[city][date] = value
        else:
            self.data[city] = {}
            self.data[city][date] = value

    def __getitem__(self, item):
        city_get, date_get = item
        selected_city = self.data.get(city_get)
        if selected_city:
            for city_date, info in selected_city.items():
                if city_date == date_get:
                    forecast = will_it_rain(selected_city, date_get)
                    return f'w mieście {city_get} dnia {date_get} {forecast}'
        return None

    def items(self):
        for city_key, city_data in self.data.items():
            for city_date, rain_amount in city_data.items():
                forecast = will_it_rain(city_data, city_date)
                yield f"({city_date}: {forecast})"

    def __iter__(self):
        return iter(self.data)
