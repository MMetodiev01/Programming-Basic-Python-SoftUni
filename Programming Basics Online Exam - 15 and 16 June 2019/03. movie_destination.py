budget_of_film = float(input())
destination = input()
season = input()
count_days = float(input())
price = 0
total_amount = 0
percents = 0
if destination != "Sofia" and destination != "London":
    if season != "Summer":
        price = 45000
        total_amount = count_days * price
    else:
        price = 40000
        total_amount = count_days * price
    percents = total_amount * 0.30
    total_amount -= percents
elif destination != "Dubai" and destination != "London":
    if season != "Summer":
        price = 17000
        total_amount = count_days * price
        percents = total_amount * 0.25
        total_amount += percents
    else:
        price = 12500
        total_amount = count_days * price
        percents = total_amount * 0.25
        total_amount += percents
else:
    if season != "Summer":
        price = 24000
        total_amount = count_days * price
    else:
        price = 20250
        total_amount = count_days * price
diff = abs(budget_of_film - total_amount)
if budget_of_film >= total_amount:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")



