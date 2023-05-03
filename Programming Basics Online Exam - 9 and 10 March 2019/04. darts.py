player_name = input()

command = input()
started_points = 301
successful_shots = 0
unsuccessful_shots = 0

while command != "Retire":
    points = int(input())
    zone = command
    if zone == "Single":
        points = points
        if points <= started_points:
            successful_shots += 1
            started_points -= points
        else:
            unsuccessful_shots += 1
    elif zone == "Double":
        points = points * 2
        if points <= started_points:
            successful_shots += 1
            started_points -= points
        else:
            unsuccessful_shots += 1
    elif zone == "Triple":
        points = points * 3
        if points <= started_points:
            successful_shots += 1
            started_points -= points
        else:
            unsuccessful_shots += 1
    if started_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
    command = input()
    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
