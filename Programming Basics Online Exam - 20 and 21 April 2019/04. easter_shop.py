available_eggs = int(input())
input_line = input()

sold_eggs_count = 0
while input_line != "Close":
    wanted_eggs = int(input())
    if input_line != "Buy":
        available_eggs += wanted_eggs
    else:
        if input_line == "Buy" and available_eggs < wanted_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {available_eggs}.")
            break
        available_eggs -= wanted_eggs
        sold_eggs_count += wanted_eggs
    input_line = input()
if input_line == "Close":
    print(f"Store is closed!")
    print(f"{sold_eggs_count} eggs sold.")