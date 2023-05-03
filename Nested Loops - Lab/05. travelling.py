destination = input()
while destination != 'End':
    needed_money = float(input())
    money_in_hand = 0

    while money_in_hand < needed_money:
        current_num = float(input())
        money_in_hand += current_num
    print(f'Going to {destination}!')


    destination = input()


# Greece
# 1000.00
# 200.00
# 200.00
# 300.00
# 100.00
# 150.00
# 240.00
# Spain
# 1200.00
# 300.00
# 500.00
# 193.00
# 423.00
# End