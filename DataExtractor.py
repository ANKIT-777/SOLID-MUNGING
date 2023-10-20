class DataExtractor:
    def __init__(self):
        self.min_value = 999999999999
        self.data = []

    def read_file(self, file_path, length):
        data = []
        min_value = 999999999999

        with open(file_path) as file:
            next(file)
            for row in file:
                line = row.split()
                if len(line) > length:
                    data.append(line)

        return [data, min_value]

