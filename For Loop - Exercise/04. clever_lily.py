age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

count_toys = 0
money = 0
count_money = 10
brother_total = 0
total_sum = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys = count_toys + 1
    else:
        money = money + 10
        brother_total = brother_total + 1
        total_sum = money + total_sum

result = total_sum + (count_toys * toy_price) - brother_total
diff = abs(result - price_washing_machine)
if result >= price_washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')


