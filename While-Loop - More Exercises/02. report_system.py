needed_sum = int(input())
command = input()
cash_pay_count = 0
amount_cash_total = 0
card_pay_count = 0
amount_card_total = 0
count_pays = 0
total_sold_products = 0
is_all_money = False
while command != "End":
    price_of_products = int(command)
    count_pays += 1

    if price_of_products <= 100 and count_pays % 2 != 0:
        cash_pay_count += 1
        amount_cash_total += price_of_products
        total_sold_products += price_of_products
        print("Product sold!")
    elif price_of_products >= 10 and count_pays % 2 == 0:
        card_pay_count += 1
        amount_card_total += price_of_products
        total_sold_products += price_of_products
        print("Product sold!")
    else:
        print("Error in transaction!")
    if total_sold_products >= needed_sum:
        average_cash = amount_cash_total / cash_pay_count
        average_card = amount_card_total / card_pay_count
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break

    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break



