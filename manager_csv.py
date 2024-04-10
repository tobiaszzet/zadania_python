import sys
import os
from file_handler import FileHandler



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


file_handler = FileHandler(input_file, output_file, changes)
print(f"input: {file_handler.manager}")
file_handler.transform()
print(f"output: {file_handler.manager}")
file_handler.save_data_to_csv()
