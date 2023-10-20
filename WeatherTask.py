min_temp = float('inf')
day = ''
file_path = 'SOLID/weather.dat'
with open(file_path) as file:
    next(file)
    for row in file:
        line = row.split()
        if len(line) > 12:
            temp_diff = abs(float(line[1][:2]) - float(line[2][:2]))
            if temp_diff < min_temp:
                min_temp = temp_diff
                day = line[0]

print(day)
