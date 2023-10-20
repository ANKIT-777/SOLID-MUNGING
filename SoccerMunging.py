
from CalculateClass import Calculator

soccer_instance = Calculator( file_path='SOLID/football.dat', length=1, column_1=6, column_2=8, resultant_column=1)

result = soccer_instance.calculate_min_difference()
print(result)
