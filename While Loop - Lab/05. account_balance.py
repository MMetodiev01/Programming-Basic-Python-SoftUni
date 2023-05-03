total = 0
while True:
    price = input()
    if price == "NoMoreMoney":
        break
    current_price = float(price)

    if current_price > 0:
        total += current_price
        print(f"Increase: {current_price:.2f}")

    if current_price < 0:
        print("Invalid operation!")
        break
print(f"Total: {total:.2f}")

# 5.51
# 69.42
# 100
# NoMoreMoney