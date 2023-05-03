capacity_of_cinema = int(input())
data = input()
total_sum = 0
cur_price = 0
while data != "Movie time!":
    data = int(data)
    capacity_of_cinema -= data
    ticket_price = 5
    if capacity_of_cinema < 0:
        print(f"The cinema is full.")
        break
    else:
        if data % 3 != 0:
            cur_price = data * ticket_price
            total_sum += cur_price
        else:
            cur_price = (data * ticket_price) - ticket_price
            total_sum += cur_price
    data = input()
    if data == "Movie time!":
        print(f"There are {capacity_of_cinema} seats left in the cinema.")
print(f"Cinema income - {total_sum} lv.")
