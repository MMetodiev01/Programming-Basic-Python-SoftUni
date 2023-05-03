import math

tournaments_count = int(input())
started_points = int(input())

wins_count = 0
points_count = 0
for i in range(1, tournaments_count + 1):
    stage_of_the_tournament = input()

    if stage_of_the_tournament == "F":
        points = 1200
        points_count += points
        started_points += points
    elif stage_of_the_tournament == "SF":
        points = 720
        points_count += points
        started_points += points
    elif stage_of_the_tournament == "W":
        points = 2000
        points_count += points
        wins_count += 1
        started_points += points
final_points = points_count / tournaments_count
diff_percent = (wins_count / tournaments_count) * 100
print(f"Final points: {started_points}")
print(f"Average points: {math.floor(final_points)}")
print(f"{diff_percent:.2f}%")