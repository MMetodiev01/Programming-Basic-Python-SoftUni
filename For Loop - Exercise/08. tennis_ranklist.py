import math

count_tournament = int(input())
innit_points = int(input())
win_count = 0
total_sum = innit_points
for i in range(1, count_tournament + 1):
    level = input()

    if level == "W":
        win_count += 1
        total_sum = total_sum + 2000
    elif level == "F":
        total_sum = total_sum + 1200
    elif level == "SF":
        total_sum = total_sum + 720
print(f"Final points: {total_sum}")
points_without_innit = total_sum - innit_points
avg_points = math.floor(points_without_innit / count_tournament)
print(f"Average Points: {avg_points}")
percent_win = win_count / count_tournament * 100
print(f"{percent_win:.2f}%")
