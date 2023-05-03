clients_count = int(input())
exercise_list = ["Back", "Chest", "Legs", "Abs"]
exercise = exercise_list
items_bought_list = ["Protein shake", "Protein bar"]
items = items_bought_list
percent_people_exercise = 0
percent_people_bought_items = 0

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0
workout_count = 0
bought_item_count = 0
for i in range(1, clients_count + 1):
    activity_in_gym = input()

    if activity_in_gym == exercise[0]:
        back_count += 1
        workout_count += 1
    elif activity_in_gym == exercise[1]:
        chest_count += 1
        workout_count += 1
    elif activity_in_gym == exercise[2]:
        legs_count += 1
        workout_count += 1
    elif activity_in_gym == exercise[3]:
        abs_count += 1
        workout_count += 1
    elif activity_in_gym == items[0]:
        protein_shake_count += 1
        bought_item_count += 1
    elif activity_in_gym == items[1]:
        protein_bar_count += 1
        bought_item_count += 1
percent_people_exercise = (workout_count / clients_count) * 100
percent_people_bought_items = (bought_item_count / clients_count) * 100
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{percent_people_exercise:.2f}% - work out")
print(f"{percent_people_bought_items:.2f}% - protein")
