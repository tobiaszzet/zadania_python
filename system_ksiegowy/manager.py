from file_handler import FileHandler


class Manager:
    def __init__(self):

        self.instancja_file_handlera = FileHandler(file_with_balance_path="saldo_konta.txt",
                                                   file_with_warehouse_path="stan_magazynu.json",
                                                   file_with_history_path="historia.txt")
        self.saldo = float(self.instancja_file_handlera.odczyt_danych_z_file_with_balance())
        self.stan_magazynu = self.instancja_file_handlera.odczyt_danych_z_file_with_warehouse()
        self.przeglad = self.instancja_file_handlera.odczyt_danych_file_with_history()
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Actions not defined")
        else:
            self.actions[name](self)


manager = Manager()


