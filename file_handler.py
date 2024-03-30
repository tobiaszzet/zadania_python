import csv


class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.manager = self.load_data_from_csv()

    def load_data_from_csv(self):
        temporary = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_line = []
                for value in line:
                    temp_line.append(value)
                temporary.append(temp_line)
        return temporary

    def save_data_to_csv(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.manager:
                writer.writerow(line)

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            column = int(transformation_list[0])
            row = int(transformation_list[1])
            change = transformation_list[2]
            self.manager[row][column] = change
