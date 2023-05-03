budget_for_the_film = float(input())
count_people = int(input())
price_for_clothe_for_person = float(input())

price_for_decor = budget_for_the_film * 0.10
price_for_clothes = price_for_clothe_for_person * count_people
if count_people > 150:
    discount = price_for_clothes * 0.10
    price_for_clothes -= discount
total_for_film = price_for_decor + price_for_clothes
final = budget_for_the_film - total_for_film
if total_for_film > budget_for_the_film:
    diff = abs(budget_for_the_film - total_for_film)
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {final:.2f} leva left.")
