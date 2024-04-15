# def upload_request_to_data(self, city, date, data_api):
#     for key, values in self.data.items():
#         if key == city:
#             for city_keys, value in values.items():
#                 if city_keys == "date" and value != date:
#                     values[city_keys].append(date)
#         else:
#             self.data[city] = data_api
#
#
#     data_str = json.dumps(dict)
#     data_str = data_str.replace("[", "").replace("]", "")
#     data_new = json.loads(data_str)


dict = {"City":{'2024-04-16': 0.0}}


dict['City'] |= {'2024-04-17': 0.4}
# values[date] = rain
print(dict)