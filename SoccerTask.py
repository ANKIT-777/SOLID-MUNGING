min_goal_difference = 999999999
best_team = ''

with open('SOLID/football.dat') as file:
    next(file)
    for row in file:
        data = row.split()
        if len(data) > 1:
            goals_for = int(data[6])
            goals_against = int(data[8])
            goal_difference = abs(goals_for - goals_against)

            if goal_difference < min_goal_difference:
                min_goal_difference = goal_difference
                best_team = data[1]

print(best_team)
