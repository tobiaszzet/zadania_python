import sys
import os
from file_handler import CSVFileHandler, PickleFileHandler, JsonFileHandler, TXTFileHandler


def load_sys_args():
    if len(sys.argv) >= 3:
        return sys.argv[1], sys.argv[2], sys.argv[3:]
    else:
        print("Error. Wymagane są 3 arguementy systemowe")


input_file, output_file, changes = load_sys_args()

if not os.path.exists(input_file):
    print("Plik wejściowy nie istnieje.")
if not os.path.exists(output_file):
    print("Plik wyjściowy nie istnieje. Zmiany nie zostały zapisane do pliku")

input_file_handler = None
output_file_handler = None

if input_file.endswith(".txt"):
    input_file_handler = TXTFileHandler(input_file, output_file, changes)
elif input_file.endswith(".pkl"):
    input_file_handler = PickleFileHandler(input_file, output_file, changes)
elif input_file.endswith("json"):
    input_file_handler = JsonFileHandler(input_file, output_file, changes)
elif input_file.endswith("csv"):
    input_file_handler = CSVFileHandler(input_file, output_file, changes)
else:
    print("nie mamy takiego pliku")


if output_file.endswith(".txt"):
    output_file_handler = TXTFileHandler(input_file, output_file, changes)
elif output_file.endswith(".pkl"):
    output_file_handler = PickleFileHandler(input_file, output_file, changes)
elif output_file.endswith("json"):
    output_file_handler = JsonFileHandler(input_file, output_file, changes)
elif output_file.endswith("csv"):
    output_file_handler = CSVFileHandler(input_file, output_file, changes)
else:
    print("nie mamy takiego pliku")

input_file_handler.read_input_file()
print(f"input: {input_file_handler.data}")
input_file_handler.transform()
output_file_handler.data = input_file_handler.data
print(f"output: {output_file_handler.data}")
output_file_handler.save_to_file()
