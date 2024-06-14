import json


class FileHandler:
    def __init__(self, file_with_history_path, file_with_balance_path, file_with_warehouse_path):
        self.file_with_history = file_with_history_path
        self.file_with_balance = file_with_balance_path
        self.file_with_warehouse = file_with_warehouse_path

    def odczyt_danych_z_file_with_balance(self):
        with open(self.file_with_balance) as file:
            dane = file.read()
            return dane

    def odczyt_danych_z_file_with_warehouse(self):
        with open(self.file_with_warehouse) as file:
            dane = json.loads(file.read())
            return dane.get("stan_magazynu")

    def odczyt_danych_file_with_history_path(self):
        with open(self.file_with_history) as file:
            dane = json.loads(file.read())
            return dane

    def zapis_do_plikow_balance_warehouse(self, budzet, stan_magazynu):
        with open(self.file_with_balance, mode="w") as file:
            file.write(budzet)

        with open(self.file_with_warehouse, mode="w") as file:
            file.write(json.dumps({
                "stan_magazynu" : stan_magazynu
            }))

    def zapis_historii(self, historia):
        with open (self.file_with_history, mode="w") as file:
            file.write(json.dumps(historia))
