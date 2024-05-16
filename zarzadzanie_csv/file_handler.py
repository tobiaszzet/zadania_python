from abc import ABC, abstractmethod
import pickle
import csv
import json


class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = None

    @abstractmethod
    def read_input_file(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            column = int(transformation_list[0])
            row = int(transformation_list[1])
            change = transformation_list[2]
            self.data[row][column] = change


class CSVFileHandler(FileHandler):
    def read_input_file(self):
        temporary = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_line = []
                for value in line:
                    temp_line.append(value)
                temporary.append(temp_line)
        print(f"temporary {temporary}")
        self.data = temporary

    def save_to_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.data:
                writer.writerow(line)


class PickleFileHandler(FileHandler):
    def read_input_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def save_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.data, file)


class JsonFileHandler(FileHandler):
    def read_input_file(self):
        with open(self.input_file) as file:
            data = json.load(file)
            temporary = []
            for key, values in data.items():
                temporary.append(values)
            self.data = temporary

    def save_to_file(self):
        with open(self.output_file, mode="w") as file:
            temp = {}
            for key, value in enumerate(self.data):
                temp[key] = value
            json.dump(temp, file)


class TXTFileHandler(FileHandler):
    def read_input_file(self):
        temporary = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_line = []
                for value in line:
                    temp_line.append(value)
                temporary.append(temp_line)
        self.data = temporary

    def save_to_file(self):
        with open(self.output_file, mode="w") as file:
            file.write(str(self.data))
