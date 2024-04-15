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
