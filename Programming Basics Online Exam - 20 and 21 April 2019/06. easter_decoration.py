count_clients = int(input())
average_bill = 0
for i in range(1, count_clients + 1):
    command = input()
    count_products = 0
    total = 0
    while command != "Finish":
        if command == "basket":
            count_products += 1
            price_basket = 1.50
            total += price_basket
        elif command == "wreath":
            count_products += 1
            price_wreath = 3.80
            total += price_wreath
        elif command == "chocolate bunny":
            count_products += 1
            price_chocolate = 7
            total += price_chocolate
        command = input()
        if command == "Finish":
            if count_products % 2 == 0:
                discount = total * 0.20
                total -= discount
            print(f"You purchased {count_products} items for {total:.2f} leva.")
            break
    average_bill += total
average_bill = average_bill / count_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")




