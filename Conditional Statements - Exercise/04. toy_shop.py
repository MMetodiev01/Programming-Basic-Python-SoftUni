trip_price = float(input())
puzzle = int(input())
talking_doll = int(input())
puff_bears = int(input())
minions = int(input())
toy_truck = int(input())

price = puzzle * 2.60 + talking_doll * 3 + puff_bears * 4.10 + minions * 8.20 + toy_truck * 2
total_num = puzzle + talking_doll + puff_bears + minions + toy_truck

if total_num >= 50:
    price = price * 0.75

price = price * 0.90
diff = abs(price - trip_price)
if price >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')


