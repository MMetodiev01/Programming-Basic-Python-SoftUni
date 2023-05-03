name_actor = input()
points_from_academy = float(input())
count_referees = int(input())
for count_referees in range(1, count_referees + 1):
    name_referee = input()
    points_referee = float(input())

    points_from_name = len(name_referee) * points_referee / 2
    points_from_academy += points_from_name
    if points_from_academy > 1250.5:
        break
if points_from_academy < 1250.5:
    diff = abs(points_from_academy - 1250.5)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")