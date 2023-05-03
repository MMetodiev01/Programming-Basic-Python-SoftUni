coins_amount = float(input())
coins_change = round(coins_amount * 100)
counter_coins = 0

while coins_change > 0:
    if coins_change >= 200:
        counter_coins += 1
        coins_change -= 200
    elif coins_change >= 100:
        counter_coins += 1
        coins_change -= 100
    elif coins_change >= 50:
        counter_coins += 1
        coins_change -= 50
    elif coins_change >= 20:
        counter_coins += 1
        coins_change -= 20
    elif coins_change >= 10:
        counter_coins += 1
        coins_change -= 10
    elif coins_change >= 5:
        counter_coins += 1
        coins_change -= 5
    elif coins_change >= 2:
        counter_coins += 1
        coins_change -= 2
    elif coins_change >= 1:
        counter_coins += 1
        coins_change -= 1
print(counter_coins)


