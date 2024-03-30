import sys
import csv
from file_handler import FileHandler


def load_sys_args():
    return sys.argv[1], sys.argv[2], sys.argv[3:]


input_file, output_file, changes = load_sys_args()

file_handler = FileHandler(input_file, output_file, changes)
print(f"input: {file_handler.manager}")
file_handler.transform()
print(f"output: {file_handler.manager}")
file_handler.save_data_to_csv()
