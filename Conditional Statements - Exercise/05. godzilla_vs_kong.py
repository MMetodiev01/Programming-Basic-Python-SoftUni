

film_budget = float(input())
statist = int(input())
clothing_per_statist = float(input())

decor_price = film_budget * 0.10
clothes_price = statist * clothing_per_statist

if statist > 150:
    clothes_price = clothes_price * 0.90

total_expenses = decor_price + clothes_price
diff = abs(total_expenses - film_budget)
if film_budget >= total_expenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")