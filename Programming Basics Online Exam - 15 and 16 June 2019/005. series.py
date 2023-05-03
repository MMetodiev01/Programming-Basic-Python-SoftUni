budget = float(input())
count_series = int(input())
total_sum = 0
for count_series in range(1, count_series + 1):
    name_of_series = input()
    price_for_series = float(input())

    if name_of_series == "Thrones":
        discount = price_for_series * 0.50
        price_for_series -= discount
        total_sum += price_for_series
    elif name_of_series == "Lucifer":
        discount = price_for_series * 0.40
        price_for_series -= discount
        total_sum += price_for_series
    elif name_of_series == "Protector":
        discount = price_for_series * 0.30
        price_for_series -= discount
        total_sum += price_for_series
    elif name_of_series == "TotalDrama":
        discount = price_for_series * 0.20
        price_for_series -= discount
        total_sum += price_for_series
    elif name_of_series == "Area":
        discount = price_for_series * 0.10
        price_for_series -= discount
        total_sum += price_for_series
    else:
        total_sum += price_for_series
diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")





