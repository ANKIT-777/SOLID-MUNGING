from DataAnalyzer import DataAnalyzer

class Calculator:
    def __init__(self, file_path, length, column_1, column_2, resultant_column):
        self.file_path = file_path
        self.length = length
        self.column_1 = column_1
        self.column_2 = column_2
        self.resultant_column = resultant_column

    def calculate_min_difference(self):
        data_analyzer_instance = DataAnalyzer()
        min_difference = data_analyzer_instance.min_diff(
            self.column_1, self.column_2, self.resultant_column, self.file_path, self.length)
        return min_difference

