from CalculateClass import Calculator

weather_instance = Calculator(
    file_path='SOLID/weather.dat', length=12, column_1=1, column_2=2, resultant_column=0)
min_diff = weather_instance.calculate_min_difference()
print(min_diff)
