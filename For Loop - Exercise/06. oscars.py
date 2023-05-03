name_of_actor = input()
points_from_academy = float(input())
number_of_assessors = int(input())


for i in range(1, number_of_assessors + 1):
    name_of_assessor = input()
    points_of_assessor = float(input())
    length_of_assessor = len(name_of_assessor)
    receive_points = (length_of_assessor * points_of_assessor) / 2

    points_from_academy += receive_points
    if points_from_academy > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break

    if i == number_of_assessors:
        diff = abs(points_from_academy - 1250.5)
        print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")




