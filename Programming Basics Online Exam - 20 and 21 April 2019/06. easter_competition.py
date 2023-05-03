count_easter_bread = int(input())

most_points = 0
best_chef = ""

for i in range(1, count_easter_bread + 1):
    input_line = input()
    points_count = 0
    while input_line != "Stop":
        command = input()
        if command == 'Stop':
            if most_points < points_count:
                most_points = points_count
                best_chef = input_line
                print(f"{input_line} has {points_count} points.")
                print(f"{input_line} is the new number 1!")
                break
            else:
                print(f"{input_line} has {points_count} points.")
                break
        else:
            command = int(command)
            points_count += command
print(f"{best_chef} won competition with {most_points} points!")



# 3
# Chef Manchev
# 10
# 10
# 10
# 10
# Stop
# Natalie
# 8
# 2
# 9
# Stop
# George
# 9
# 2
# 4
# 2
# Stop