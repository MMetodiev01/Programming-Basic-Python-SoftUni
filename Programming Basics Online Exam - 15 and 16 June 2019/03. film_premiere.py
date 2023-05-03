film = input()
snacks = input()
tickets_count = int(input())
total_sum = 0
discounts = 0
if film == "John Wick":
    if snacks == "Drink":
        snacks = 12
        total_sum = snacks * tickets_count
    elif snacks == "Popcorn":
        snacks = 15
        total_sum = snacks * tickets_count
    elif snacks == "Menu":
        snacks = 19
        total_sum = snacks * tickets_count
if film == "Star Wars":
    if snacks == "Drink":
      snacks = 18
      total_sum = snacks * tickets_count
    elif snacks == "Popcorn":
      snacks = 25
      total_sum = snacks * tickets_count
    elif snacks == "Menu":
      snacks = 30
      total_sum = snacks * tickets_count
    if tickets_count >= 4:
        discounts = total_sum * 0.30
        total_sum -= discounts

if film == "Jumanji":
    if snacks == "Drink":
        snacks = 9
        total_sum = snacks * tickets_count
    elif snacks == "Popcorn":
        snacks = 11
        total_sum = snacks * tickets_count
    elif snacks == "Menu":
        snacks = 14
        total_sum = snacks * tickets_count
    if tickets_count == 2:
        discounts = total_sum * 0.15
        total_sum -= discounts
print(f"Your bill is {total_sum:.2f} leva.")

