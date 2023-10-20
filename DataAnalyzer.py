from DataExtractor import DataExtractor

class DataAnalyzer:
    def get_data(self, file_path, length):
        data_extractor = DataExtractor()
        data, min_value = data_extractor.read_file(file_path, length)
        return data, min_value

    def min_diff(self, column1, column2, resultant_column, file_path, length):
        data, min_value = self.get_data(file_path, length)
        result_value = None

        for row in data:
            val1 = float(row[column1].split('*')[0])
            val2 = float(row[column2].split('*')[0])
            diff = abs(val1 - val2)

            if diff < min_value:
                min_value = diff
                result_value = row[resultant_column]

        return result_value
